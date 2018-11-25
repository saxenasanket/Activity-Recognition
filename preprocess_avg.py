from os import listdir
from os.path import isfile, join
import numpy
import cv2
for tp in range (1,101):
	images = numpy.empty(301, dtype=object)
	for t in range (1,301):
				mypath='/home/sanket/kth/frames/boxing/'+str(tp)+'/frame'+str(t)+'.jpg'
				
				images[t] = cv2.imread(mypath)	
				
	I = numpy.empty(300, dtype=object)  
	for i in range(1,301,2):                 
				i1=images[i]
				i2=images[i+1]
				temp=i1+i2
				I[i]=temp/2
	for x in range(1,301,2):
				y=x/2 + 1               	       					
				cv2.imwrite('/home/sanket/kth/pre_processed_frames/boxing/'+str(tp)+'/avg'+str(y)+'.jpg', I[x])
						
			
