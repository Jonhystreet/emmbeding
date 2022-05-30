import ngtpy
import random


dim = 10
nb = 100
vectors = [[random.random() for _ in range(dim)] for _ in range(nb)]
query = vectors[0]
  
ngtpy.create(b"tmp", dim)
index = ngtpy.Index(b"tmp")
index.batch_insert(vectors)
index.save()
results = index.search(query, 3)
for i, (id, distance) in enumerate(results) :
  print(str(i) + ": " + str(id) + ", " + str(distance))
  object = index.get_object(id)
  print(object)