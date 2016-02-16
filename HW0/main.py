__author__ = 'Jiaxiao Zheng'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('cs52.csv')
sdf = df.query("University == 'University of California - Berkeley' and Doctorate == 'University of California - Berkeley - USA'")
print('number of professors meeting the criteria is ' +  str(sdf.shape[0]))
#print(df.loc[df['University'] == 'University of California - Berkeley' & (df['Doctorate'] == 'University of California - Berkeley')])