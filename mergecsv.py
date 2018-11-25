import pandas as pd
import numpy as np
from numpy import genfromtxt
res=np.zeros(102400)
for j in range(1,7,1):
		      for k in range(1,101,1):
			                      p=0;
					      for i in range(1,101,1):
                                                                	path='/home/sanket/kth/pre_processed_frames/'+str(j)+'/'+str(k)+'/'+str(i)+'.csv'   
                                                                	a = genfromtxt(path, delimiter=',')
                                                                	res[p:p+1024]=a;
                                                                	p=p+1024
									p	
					      path2='/home/sanket/kth/pre_processed_frames/'+str(j)+'/'+str(k)+'.csv' 
					      np.savetxt(path2, np.array(res), delimiter="\t") 
