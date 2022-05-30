import faiss
import numpy as np
dataSetI = [.1, .2, .3]
#dataSetII = [.4, .5, .6]
dataSetII = [.7, .76, .91]

x = np.array([dataSetI]).astype(np.float32)
q = np.array([dataSetII]).astype(np.float32)
print(x)
print(q)
index = faiss.index_factory(3, "Flat", faiss.METRIC_INNER_PRODUCT)
index.ntotal
faiss.normalize_L2(x)
index.add(x)
faiss.normalize_L2(q)
print(x)
print(q)
distance, index = index.search(q, 5)
print('Distance by FAISS:{}'.format(distance))


#Por coseno
from scipy import spatial
result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
print('\n \n ------------------------------------------------------- \n\n')
print('Distance con faiss por coseno: {}'.format(result))