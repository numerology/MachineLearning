__authot__ = 'jxzheng'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from gensim import models

w = models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary = True)
#a
print(w['queen'])
# The first number of the vector is 0.00173332

#b

print(w.most_similar('man'))


#c
print(w.most_similar(positive = ['woman', 'king'], negative = ['man'], topn = 1))

#d
print(w.doesnt_match('breakfast cereal dinner lunch'.split()))

#e
listOfWords = ['man', 'woman', 'girl', 'tree', 'trees', 'pine_trees']
listOfVec = w[listOfWords]
X = np.vstack(listOfVec)

eigVal, eigVec = np.linalg.eigh(np.dot(X,X.transpose()))
eigVec = eigVec[:, :2]
#Projection

vecAfterPCA = np.inner(listOfVec.transpose(), eigVec.transpose())
plt.scatter(vecAfterPCA[:,0], vecAfterPCA[:,1])
plt.show()




