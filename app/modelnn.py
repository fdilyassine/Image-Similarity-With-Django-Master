from annoy import AnnoyIndex
from scipy import spatial
from nltk import ngrams
import os
import random, json, glob, os, codecs, random
import numpy as np
#from .classify_images import vectorize

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
class Similarity_Model():

    def __init__(self,n_neigh):
        """
        Initialization, n_neighbors is set by user.
        """
        n_neigh = 10
        self.dims = 2048
        self.trees = 10000
        infiles = glob.glob(str(BASE_DIR+'\image_vectors\*.npz')) 
        self.file_index_to_file_name = {}
        for file_index,i in enumerate(infiles):
            file_name = os.path.basename(i).split('.')[0]
            self.file_index_to_file_name[file_index] = file_name

        self.model = AnnoyIndex(self.dims)
        dir_path = os.path.join(BASE_DIR,'model.ann')

        self.model.load(dir_path)
    
    def getSimilarityForNew(self,vector,vecName):
        """
        Just functionized your code for new images.
        Saves the json into img folder
        """
        named_nearest_neighbors = []
        nearest_neighbors = self.model.get_nns_by_vector(vector, 10)
        for j in nearest_neighbors :
            neighbor_file_name = self.file_index_to_file_name[j]
            neighbor_file_vector = self.model.get_item_vector(j)

            similarity = 1 - spatial.distance.cosine(vector, neighbor_file_vector)
            rounded_similarity = int((similarity * 10000)) / 10000.0
            if (vecName.split('.')[0] != neighbor_file_name) and (rounded_similarity > 0.90):
                named_nearest_neighbors.append({
                'filename': neighbor_file_name,
                'similarity': rounded_similarity
                })
 
        if  named_nearest_neighbors != [] :
            print(vecName)
            with open('app/img/'+str(vecName)+'.json', 'w') as out:
                json.dump(named_nearest_neighbors, out)
        else:
            named_nearest_neighbors.append({
            'message': "no similar image above 90% similarity"
            })  
            with open('app/img/'+str(vecName)+'.json', 'w') as out:
                json.dump(named_nearest_neighbors, out)


    #def vectorizeAndRun(self,imgName):
        """
        Get the path of uploaded image, and vectorize
        save into img folder
        """

    #    pth = os.path.join('app/img/',str(imgName))
    #    print(pth)
    #    self.path = pth
    #    vectorize(str(pth),str(os.path.dirname(pth)))
       
    def readVectorized(self,vecName):
        """
        Load the vectorized form, get the similarities
        """
        pth = os.path.join('app/img/',str(vecName))
        print(pth)
        self.path = pth
        vector = np.loadtxt(str(pth))
        #vecName = os.path.basename(pth).split('.')[0]
        self.getSimilarityForNew(vector,vecName)
        