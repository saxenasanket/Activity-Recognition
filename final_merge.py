import pandas as pd
import numpy as np
from numpy import genfromtxt
res=np.zeros((102401,600), dtype='float128')
j=1;
for j in range (1,7):
			for k in range(0,100,1):
						      path='/home/sanket/kth/pre_processed_frames/'+str(j)+'/'+str(k+1)+'.csv' 
						      a = genfromtxt(path, delimiter=',')
						      res[0:102401,100*(j-1)+k]=a;
						      

np.savetxt('/home/sanket/kth/pre_processed_frames/final_merged.csv', np.array(res), delimiter="\t") 
