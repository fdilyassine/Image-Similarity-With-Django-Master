from rest_framework.serializers import ModelSerializer
from vector_img.models import Image

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'