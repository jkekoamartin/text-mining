
# coding: utf-8

# In[1]:


import csv
from sklearn.decomposition import PCA
import numpy
import pylab as pl


# In[36]:


filename = 'telltale_sent_output.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)


# In[37]:


pca = PCA(n_components=2).fit(data)
pca_2d = pca.transform(data)


# In[38]:


for i in range(0, pca_2d.shape[0]):
    if data[i][6] == 0:
        c1 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='r',marker='.')
    elif data[i][6] == 1:
        c2 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='g',marker='.')
    elif data[i][6] == 2:
        c3 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='b',marker='.')
    elif data[i][6] == 3:
        c4 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='m',marker='.')
    #elif data[i][6] == 4:
        #c5 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='c',marker='.')
pl.legend([c1, c2, c3, c4], ['Cluster 1', 'Cluster 2','Cluster 3', 'Cluster 4'])
pl.title('"A Tell-Tale Heart" Sentence Clustering')
pl.show()

