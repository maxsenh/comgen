##Grimm scaler

import numpy as np
from sklearn.preprocessing import normalize

with open ('gc_content_dist_matrix.grimm') as f:
    matrix = np.loadtxt(f)
    newarray = np.zeros((5, 5))
    print(matrix)
    #print (aa)
    #for i in aa:
    #    newarray[i] = i * 100
        #newarray[y] = y * 100
    #print(newarray)
    norm_matrix = normalize(matrix, axis=1, norm='l2')
    print(norm_matrix)

    newfile = open('gc_content_dist_matrix.grimm' + '_normed', 'w')
    np.savetxt(newfile, norm_matrix, fmt='%.5f')

