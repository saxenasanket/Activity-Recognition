import caffe as caffe
import cv2
import os
import numpy as np
model_file='/home/sanket/caffe/models/bvlc_googlenet/deploy.prototxt'
weight_file='/home/sanket/caffe/models/bvlc_googlenet/googlenet_quick_iter_1120.caffemodel'
net=caffe.Net(model_file, weight_file, caffe.TEST)
p=1
/home/sanket/kth/pre_processed_frames/2/2/avg2.jpg
for F in range (1,7):
for f in range (1,101):
for i in range (1,101):
                         path='/home/sanket/kth/pre_processed_frames/'+str(F)+'/'+str(f)+'/avg'+str(i)+'.jpg'
                         IMAGE=cv2.imread(path)
                       	 IMAGE=cv2.resize(IMAGE,(224,224))
                       	 image=np.random.rand(10,3,224,224)	        
                       	 print(i)
                       	 print('**********p*********')		
                         for x in range(1,10,1):
                         			for y in range(1,3,1):
                         					      image[x,y,:,:]=IMAGE[:,:,0]			
                         net.blobs['data'].data[...]=image
                         ft=net.forward()
                         ft_list=ft.values()
                         ft_array=np.asarray(ft_list)
                         ft_array=ft_array[0,0,:,:,:]
                         ft_vect=ft_array.flatten()
                         np.savetxt('/home/sanket/kth/pre_processed_frames/'+str(F)+'/'+str(f)+'/'+str(i)+'.csv', np.array(ft_vect), delimiter="\t")