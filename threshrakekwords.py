#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:53:03 2018

@author: namanrungta4721
"""
import re
path='/Users/namanrungta4721/Desktop/server110/'
file='test_rej'

with open(path+'Elsevier/statpro/'+file+'/rakekwords.txt','r') as f:
    lines=f.readlines()
threshold=1
rake=open(path+'Elsevier/statpro/'+file+'/threshrakekwords.txt','w')
for line in lines:
    #match=re.search(pattern,line)
    match1=re.search(r'json',line)
    match2=re.search(r'\.\.\.',line)
    match3=re.search(r'\n',line)
#    if match:
 #       a[i]=match.group()
  #      i+=1
    if match1:
        rake.write(line+'\n')
    elif match2:
        rake.write(line+'\n')
    elif match3:
        rake.write(line)
    else :
        line1=re.split('\',',line)
        if int(line1[1])>=threshold:
            rake.write(line)