__author__ = 'jxzheng'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import random
import glob
from sklearn.feature_extraction.text import HashingVectorizer

filelist=glob.glob("Gutenberg/text/*.txt")

hv=HashingVectorizer(input="filename", strip_accents="ascii", analyzer="word", ngram_range=(2,2), stop_words="english", n_features=2**18, binary=True)

smat=hv.transform(filelist) #This is the output mat

#b
p = 4294967311
n = 90
N = 3036

c1List = []
c2List = []
for i in range(n):
    c1List.append(random.randint(0,p))
    c2List.append(random.randint(0,p))

#compute minhash signature, for each article, minHash output the ID corresponding to smallest hash value
minHashMat = []
for i in range(0,N):
    cMinHashVec = np.zeros(n)
    cShingles = smat[i,:]
    for j in range(0,len(cShingles)):
        for k in range(n):
            cMinHashVec[k] = cShingles[j] if (c1List[k] * cShingles[j] + c2List[k]) % p < (c1List[k] * cMinHashVec[k] + c2List[k]) % p else cMinHashVec[k]
    '''TODO: Can be accelerated by storing the hashed value instead of shingle id'''
    minHashMat.append(cMinHashVec)

