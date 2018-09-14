#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:53:03 2018

@author: namanrungta4721
"""
import re

path = '/home/rajeev/Desktop/work/workplace/KDDwork/Comnet/authors_oos/'

with open(path + 'rake_auth_venue_oos.txt','r') as f:
    lines=f.readlines()
threshold=1
rake=open(path + 'clean_rake_auth_venue_oos.txt','w')
for line in lines:
    #match=re.search(pattern,line)
    match1=re.search(r'json',line)
    match2=re.search(r'\.\.\.',line)
    #match3=re.search(r'\n',line)
#    if match:
 #       a[i]=match.group()
  #      i+=1
    if match1:
        rake.write(line+'\n')
    elif match2:
        rake.write(line+'\n')
    else :
        line1=re.split('\', ',line)
        #print(line)
        if len(line1)>1:
            line2=re.sub(" \d+", "", line1[0])
            rake.write(line2+'\','+line1[1])
        else:
            rake.write(line)

                