import pandas as pd
import numpy as np
from numpy import genfromtxt
res=np.zeros(102401)
for j in range(1,7,1):
		      		for k in range(1,101,1):
							      path='/home/sanket/kth/pre_processed_frames/'+str(j)+'/'+str(k)+'.csv' 
							      a = genfromtxt(path, delimiter=',')
							      res[0:102401]=a[0:102401];
							      res[102400]=j;
							      k
							      np.savetxt(path, np.array(res), delimiter="\t") 
