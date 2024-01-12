import cv2
import os
import numpy as np

x = os.listdir('trai_cay/oi')
dem=1
for file_name in x:
    name, ext = os.path.splitext(file_name)    
    full_name_1 = 'trai_cay/oi/' + file_name
    full_name_2 = 'trai_cay_chuan_hoa/oi_' + '%03d' % dem+ '.bmp'
    dem=dem+1
    imgin = cv2.imread(full_name_1, cv2.IMREAD_COLOR)
    M, N, P = imgin.shape
    if M < N:
        d = N - M
        pad = np.ones((d,N,3), np.uint8)*255
        imgout = np.vstack((imgin,pad))
    elif M > N:
        d = M - N
        pad = np.ones((M,d,3), np.uint8)*255
        imgout = np.hstack((imgin, pad))
    else:
        imgout = imgin
    imgout = cv2.resize(imgout,(320,320))
    cv2.imwrite(full_name_2, imgout)
print('Done')
