#RangeSearch_faiss
import faiss
import numpy as np
# example data

xb = np.random.rand(200000, 32).astype('float32')
xq = np.random.rand(500, 32).astype('float32')

# get reference result with index
index = faiss.IndexFlatL2(xb.shape[1])
index.add(xb)
lims, D, I = index.range_search(xq, 1.5)

def search_from_matrix(xq, xb, thresh):
    nq, d = xq.shape
    nb, d2 = xb.shape
    assert d == d2
    res = faiss.RangeSearchResult(nq)
    faiss.range_search_L2sqr(
        faiss.swig_ptr(xq), 
        faiss.swig_ptr(xb), 
        d, nq, nb, 
        thresh, res)
    
    # get pointers and copy them
    lims = faiss.rev_swig_ptr(res.lims, nq + 1).copy()
    nd = int(lims[-1])
    D = faiss.rev_swig_ptr(res.distances, nd).copy()
    I = faiss.rev_swig_ptr(res.labels, nd).copy()
    return lims, D, I

# test
lims2, D2, I2 = search_from_matrix(xq, xb, 1.5)

# check output 
assert np.all(lims2 == lims) 
assert np.all(D == D2)
assert np.all(I == I2)