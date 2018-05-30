##Grimm scaler

import numpy as np

with open ('gc_content_dist_matrix.grimm') as f:
    aa = np.loadtxt(f)
    newarray = np.zeros((5, 5))
    print(newarray)
    print (aa)
    for i in aa:
        newarray[i] = i * 100
        #newarray[y] = y * 100
    print(newarray)