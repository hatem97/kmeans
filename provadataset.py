# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:35:40 2019

@author: Contrader_0255
"""
import numpy as np 
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv (r'C:\Users\Contrader_0255\Desktop\Progetto SuperUltraSegreto\DatasetMaicol.csv')
A=df['t_risposta']
B=df['volte']
print(A)

inputs=DataFrame({'t_risposta':A,'volte':B})
kmn = KMeans(n_clusters=2) 
kmn.fit(inputs)
labels = kmn.predict(inputs)
print(labels)
api.add_resource(risultatoKMeans), '/risulatatoKMeans/<t_risposta>&<volte>') # Route_1
if __name__ == '__main__':
    app.run(port='5000')