##Grimm scaler

import numpy as np

with open ('gc_content_dist_matrix.grimm') as f:
    aa = np.loadtxt(f)
    newarray = np.zeros((5, 5))
    for i in aa:
        i = i * 100
        newarray = np.array(i)
    print(newarray)