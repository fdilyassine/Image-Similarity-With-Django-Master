from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from vector_img.models import Image
from django.urls import reverse_lazy 
from .forms import PostForm
from vector_img.modelnn import Similarity_Model
from django.core.files.storage import FileSystemStorage
from .classify_images import vectorize
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
import os
import json
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView 
from vector_img.serializers import ImageSerializer
from vector_img.models import Image
import numpy as np
from app.views import upload_path
# Create your views here.
def upload(request):
    """
    If the form is submitted, get the uploaded file
    vectorize it, read and create the json then show the similiraty table
    with out.html
    """
    if request.method == 'POST':
        n_neigh=request.POST['number']
        model = Similarity_Model(n_neigh=int(n_neigh))
        up_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(up_file.name,up_file)
        model.vectorizeAndRun(up_file.name)
        model.readVectorized()
        img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'img')
        img_name = up_file.name.split('.')[0]
        with open(img_path+'\\'+img_name+'.json') as d:
            data = json.load(d)  
        return render(request,'app/out.html', {'d':data},content_type="text/html")
        
    return render(request, 'app/index.html')

class ImageAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Image.objects.get(pk=id)
            serializer = ImageSerializer(item)
            return Response(serializer.data)
        except Image.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Image.objects.get(pk=id)
        except Image.DoesNotExist:
            return Response(status=404)
        serializer = ImageSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Image.objects.get(pk=id)
        except Image.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ImageViewSet(APIView):

    def get(self, request, format=None):
        items = Image.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ImageSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        #n_neigh=request.data['text']
        #n_neigh=request.POST.get('n_neighbor')
        #print(n_neigh)
        model = Similarity_Model(n_neigh=10)
        up_file = request.data['image']
        #up_file = request.POST.get('image')
        print(up_file)
        image = Image.objects.create(image=up_file)
        fs = FileSystemStorage()
        fs.save(up_file.name,up_file)
        print(up_file.name+'.npz')
        model.vectorizeAndRun(imgName=up_file.name)
        #model.readVectorized()
        img_path = os.path.join(upload_path,'img')
        img_name = up_file.name.split('.')[0]
        #with open(img_path+'\\'+img_name+'.json') as d:
        #    data = json.load(d)
        with open(img_path + '\\' + up_file.name + '.npz') as d:
            vector = []
            vector1 = np.loadtxt(d)
            for i in range(0,2048):
                vector.append({"data "+ str(i) : vector1[i]})
        response_data = {}
        #response_data['results'] = data
        response_data['vector'] = vector
        #return HttpResponse(json.dumps({'message': str(up_file.name) +" uploaded and vectorized"}), status=200)
        #return HttpResponse(json.dumps(data), status=200)
        return HttpResponse(json.dumps(response_data), status=200)