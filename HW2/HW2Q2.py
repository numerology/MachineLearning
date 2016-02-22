__author__ = 'jxzheng'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nltk import corpus
import binascii
import random



#a
shingleLen = 2

with open('articles-1000.txt') as file:
    content = file.readlines()

shinglesIDList = []
for art in content:
    rawlistOfWords = art.split()
    listOfWords = rawlistOfWords[1:]
    listOfWords = [word for word in listOfWords if word not in corpus.stopwords.words('english')]
    shingles = [listOfWords[i:i + shingleLen] for i in range(len(listOfWords) - shingleLen + 1)]
    shinglesID =[]

    for s in shingles:
       # print(s)
        cShingle = ' '.join(s)
        shinglesID.append(binascii.crc32(cShingle) & 0xffffffff)

    shinglesIDList.append(shinglesID)


#print(shinglesIDList[0])

#b
p = 4294967311
n = 10
c1List = []
c2List = []
for i in range(n):
    c1List.append(random.randint(0,p))
    c2List.append(random.randint(0,p))

#compute minhash signature, for each article, minHash output the ID corresponding to smallest hash value
minHashMat = []
for sids in shinglesIDList:
    cMinHashVec = np.zeros(n)
    for sid in sids:
        for i in range(n):
            cMinHashVec[i] = sid if (c1List[i] * sid + c2List[i]) % p < (c1List[i] * cMinHashVec[i] + c2List[i]) % p else cMinHashVec[i]

    minHashMat.append(cMinHashVec)

#find the most similar book to the 1st one
firstBook = minHashMat[0]
minBookID = 1001
maxJSim = 0
for i in range(1,1000):
    cBook = minHashMat[i]
    jSimilarity = np.count_nonzero(firstBook == cBook)/10 #TODO: chech what's the problem
    if jSimilarity > maxJSim:
        maxJSim = jSimilarity
        minBookID = i

#find actual Jsimilarity
set1 = set(shinglesIDList[0])
set2 = set(shinglesIDList[minBookID])
actualJSimilarity = len(set1.intersection(set2))/len(set1.union(set2))

#c
r = 2
t = 0.8
fpVec = []

for b in range(1,10,2):
    n = b * r #b: number of bands, r: number of rows of each band
    c1List = []
    c2List = []
    for i in range(n):
        c1List.append(random.randint(0,p))
        c2List.append(random.randint(0,p))

    #hash through all articles
    minHashMat = []
    for sids in shinglesIDList:
        cMinHashVec = np.zeros(n)
        for sid in sids:
            for i in range(n):
                cMinHashVec[i] = sid if (c1List[i] * sid + c2List[i]) % p < (c1List[i] * cMinHashVec[i] + c2List[i]) % p else cMinHashVec[i]

        minHashMat.append(cMinHashVec)

    #compare the min hash vector segment by segment, if >1 segment matches, two books match
    firstBook = minHashMat[0]
    firstBookBands = [(firstBook[i:i+r] for i in range(0,len(firstBook),r))]
    firstBookBandsSet = set(firstBookBands) #TODO: ndarray is not hashable

    similarSet = []
    fpNumber = 0
    for i in range(1,1000):
        cBook = minHashMat[i]
        cBookBands = [cBook[i:i + r] for i in range(0,len(cBook),r)] #hope this may work
        if len(set(cBookBands).intersection(firstBookBandsSet)) > 0:
            similarSet.append(i) #storing ids
            #compute actual Jsim
            set2 = set(shinglesIDList[i])
            actualJSimilarity = len(set1.intersection(set2))/len(set1.union(set2))
            if actualJSimilarity < t:
                fpNumber += 1

    fpVec[(b-1)/2] = fpNumber/len(similarSet)


plt.plot(range(1,10,2), fpVec)
plt.show()

b = 10
fpVec = []
for r in range(1,10,2):
    n = b * r
    c1List = []
    c2List = []
    for i in range(n):
        c1List.append(random.randint(0,p))
        c2List.append(random.randint(0,p))

    #hash through all articles
    minHashMat = []
    for sids in shinglesIDList:
        cMinHashVec = np.zeros(n)
        for sid in sids:
            for i in range(n):
                cMinHashVec[i] = sid if (c1List[i] * sid + c2List[i]) % p < (c1List[i] * cMinHashVec[i] + c2List[i]) % p else cMinHashVec[i]

        minHashMat.append(cMinHashVec)

    #compare the min hash vector segment by segment, if >1 segment matches, two books match
    firstBook = minHashMat[0]
    firstBookBands = [firstBook[i:i+r] for i in range(0,len(firstBook),r)]
    firstBookBandsSet = set(firstBookBands)

    similarSet = []
    fpNumber = 0
    for i in range(1,1000):
        cBook = minHashMat[i]
        cBookBands = [cBook[i:i + r] for i in range(0,len(cBook),r)] #hope this may work
        if len(set(cBookBands).intersection(firstBookBandsSet)) > 0:
            similarSet.append(i) #storing ids
            #compute actual Jsim
            set2 = set(shinglesIDList[i])
            actualJSimilarity = len(set1.intersection(set2))/len(set1.union(set2))
            if actualJSimilarity < t:
                fpNumber += 1

    fpVec[(b-1)/2] = fpNumber/len(similarSet)


plt.plot(range(1,10,2), fpVec)
plt.show()
