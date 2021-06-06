#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# Creating Plain Black Image
art = np.zeros((1300,1300,3))


# In[3]:


# Variable used in creating image inside plain black Image
a = 50
t = 15
x,y,z = 590,570,820
q,w,e,r = 320,790,550,820
n,m,o = 160,110,170
c,d,v,f = 120,150,140,170


# In[4]:


# drawing Peacock Feather using some manipulations
for i in range(1,100,5):
    art[120+i:240,140:140+i] = [0,204,0]
    art[240:240+i,140+i:240] = [0,255,0]
for i in range(1,200,5):
    art[880:880, 630:1000] = [0,255,0]
for i in range(1,200,5):
    art[800:800+i, 500+i:800] = [0,255,0]
for i in range(1,200,5):
    art[800:800+i, 550+i:950] = [0,0,0]


# In[5]:


for i in range(50):
    cv2.circle(art,(220,290),i,(0,255,0),3)
    cv2.circle(art,(210,240),i,(0,255,0),3)
    cv2.circle(art,(190,230),i,(0,255,0),3)
    cv2.circle(art,(220,290+a),i,(0,255,0),3)
    cv2.circle(art,(220,290+(a*2)),i,(0,255,0),3)
    cv2.circle(art,(220,290+(a*3)),i,(0,255,0),3)
    cv2.circle(art,(190,290),i,(0,255,0),3)
    cv2.circle(art,(170+(a*2),290),i,(0,255,0),3)
    cv2.circle(art,(170+(a*2),290+a),i,(0,255,0),3)
    cv2.circle(art,(170+(a*3),290+a),i,(0,255,0),3)
    cv2.circle(art,(170+(a*2),290+(a*2)),i,(0,255,0),3)
    cv2.circle(art,(170+(a*3),290+(a*2)),i,(0,255,0),3)
    cv2.circle(art,(170+(a*4),290+(a*2)),i,(0,255,0),3)
    cv2.circle(art,(170+(a*5),290+(a*3)),i,(0,255,0),3)
    cv2.circle(art,(190,290+a),i,(0,255,0),3)
    cv2.circle(art,(190,290+(a*2)),i,(0,255,0),3)
    cv2.circle(art,(200,290+(a*2)),i,(0,255,0),3)
    cv2.circle(art,(200,290+(a*3)),i,(0,255,0),3)
    cv2.circle(art,(200,290+(a*4)),i,(0,255,0),3)
    cv2.circle(art,(210,290+(a*5)),i,(0,255,0),3)
    cv2.circle(art,(230,290+(a*6)),i,(0,255,0),3) 
    cv2.circle(art,(400,760),i,(0,255,0),3)
    cv2.circle(art,(400+a,780),i,(0,255,0),3)
    cv2.circle(art,(400+(a*2),800),i,(0,255,0),3)
    cv2.circle(art,(400+(a*3),780),i,(0,255,0),3)
    cv2.circle(art,(400+(a*3),800-a),i,(0,255,0),3)
    cv2.circle(art,(400+(a*3),800-(a*2)),i,(0,255,0),3)
while True:
    if x >= 710 and y >= 700 and z >= 970:
        break
    else:
        cv2.line(art,(x+t,y+t),(y+t,z+t),(0,255,0),8)
        x,y,z = x+t,y+t,z+t 
        
while True:
    if q >= 430 and w >= 950 and e >= 670 and r >= 970:
        break
    else:
        cv2.line(art,(q+t,w+t),(e+t,r+t),(0,255,0),8)
        q,w,e,r = q+t,w+t,e+t,r+t 

while True:
    if n >= 480 and m >= 380 and o >= 430:
        break
    else:
        cv2.line(art,(n+t,m+t),(o+t,o+t),(0,255,0),8)
        n,m,o = n+t,m+t,o+t 

while True:
    if c >= 160 and d >= 480 and v >= 220 and f >= 500:
        break
    else:
        cv2.line(art,(130,d+t),(160,f+t),(0,255,0),8)
        c,d,v,f = c+t,d+t,v+t,f+t 

for i in range(150 , 200):
    cv2.circle(art,(400,600),i,(0,153,0),3)
for p in range(100 ,150):
    cv2.circle(art,(400,600),p,(0,255,255),3)
for t in range(100):
    cv2.circle(art,(400,600),t,(0,102,0),3)
for i in range(50):
    cv2.circle(art,(380,630),i,(255,0,0),3)
    cv2.circle(art,(430,600),i,(255,0,0),3)
    


# In[6]:


plt.imshow(art)


# In[7]:


cv2.imshow('My Drawing', art)
cv2.waitKey(10)
cv2.destroyAllWindows()


# In[ ]:




