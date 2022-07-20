from annoy import AnnoyIndex
from scipy import spatial
from nltk import ngrams
import random, json, glob, os, codecs, random
import numpy as np

# data structures
file_index_to_file_name = {}
file_index_to_file_vector = {}
chart_image_positions = {}

# config
dims = 2048
n_nearest_neighbors = 30
trees = 10000
infiles = glob.glob('image_vectors/*.npz')

# build ann index
t = AnnoyIndex(dims)
for file_index, i in enumerate(infiles):
    file_vector = np.loadtxt(i)
    file_name = os.path.basename(i).split('.')[0]
    file_index_to_file_name[file_index] = file_name
    file_index_to_file_vector[file_index] = file_vector
    t.add_item(file_index, file_vector)
t.build(trees)
t.save('model.ann')
# building tree and getting dicts are just enough for now.
print("model saved successfully as model.ann")

