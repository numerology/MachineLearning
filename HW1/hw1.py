__author__ = 'Jiaxiao Zheng'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

result_array = np.zeros([1,8])


nips_data = pd.read_csv('nips-word-stream.csv', header = None)
nips_hash = pd.read_csv('f2-hash.csv', header = None)
word_dict = np.zeros(12420)



#Q1.a
for i in range(0,nips_data.shape[0]):
    current = (nips_data.iloc[i,0])
#    print(nips_data.iloc[i,0])
    word_dict[current] = word_dict[current] + 1

F0 = 0
for i in range(0,len(word_dict)):
    if(word_dict[i] > 0):
        F0 = F0 + 1

print(F0)
result_array[0,0] = F0

#Q1.b
M = 100003
a = 33212
b = 74895

mins = 65535

for i in range(0,nips_data.shape[0]):
    current = (nips_data.iloc[i,0])
    if mins > ((a*current + b) % M) and not ((a*current + b) % M) == 0:
        mins = ((a*current + b) % M)

F0hat = round(float(M)/mins)
print(F0hat)
result_array[0,1] = F0hat

#Q1.c
F2 = 0
for i in range(0, len(word_dict)):
    F2 = F2 + word_dict[i] * word_dict[i]

result_array[0,2] = F2

#Q1.d
Z = 0
for i in range(1,len(word_dict)):
    Z = Z + word_dict[i]*nips_hash.iloc[i-1,0]

F2hat = Z * Z
result_array[0,3] = F2hat


#Q1.e
ID = np.argmax(word_dict)
result_array[0,4] = ID

#Q1.f
counter = 0
current_id = None


for i in range(0,nips_data.shape[0]):
    current = nips_data.iloc[i,0]
    if counter == 0:
        counter = counter + 1
        current_id = current
    else:
        if(not current_id == current):
            counter = counter - 1

        else:
            counter = counter + 1

IDhat = current_id
result_array[0,5] = IDhat

#Q2
M = 600011
a = 134598
b = 542234

mins = 10**9

counterlist = []
idlist = []
for i in range(0,10):
    counterlist.append(0)
    idlist.append(0)

with open('pubmed-word-stream.csv','r') as input_file:
    print('start processing the big one!')
    for line in input_file:
        x = int(line)
        if mins > ((a*x + b) % M):
            mins = ((a*x + b) % M)

        if(0 in counterlist):
            index = counterlist.index(0)
            counterlist[index] += 1
            idlist[index] = x
        elif(x in idlist):
            index = idlist.index(x)
            counterlist[index] += 1
        else:
            for i in range(0,10):
                counterlist[i] -= 1

F0hat = round(float(M)/mins)
print(F0hat)
result_array[0,6] = F0hat
print(counterlist)
#finding the est of frequentest
max = 0
max_ind = None
for key in range(0,10):
    if counterlist[key] >= max:
        max = counterlist[key]
        max_ind = key

print(idlist[max_ind])
result_array[0,7] = idlist[max_ind]

result = pd.DataFrame(data = result_array, columns = ['1a','1b','1c','1d','1e','1f','2a','2b'])
result.to_csv('hw1.csv', index = False, header = ['1a','1b','1c','1d','1e','1f','2a','2b'])