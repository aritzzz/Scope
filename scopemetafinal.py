#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 18:19:50 2018

@author: namanrungta
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:58:39 2018

@author: namanrungta
"""
import rake
import operator
import json
import re
import os 
filen = 'statpro_rej_json/'
#path = '/home/rajeev/Desktop/work/Elsevier/statpro/statpro_test/' + filen
path='/Users/namanrungta4721/Desktop/server110/Elsevier/'
z=0
input_dir= path+'csi/CSI_test/csi_acc_json/'
output_dir= path +'csi/test_acc/'
files=os.listdir(input_dir)
for f in files:
    if('fuse' not in f):
        print(str(z)+'\t'+f)
        with open(input_dir+f) as input_file:
           try:
                    data = json.load(input_file)
           except:
                    continue
        title= open(output_dir+'title.txt','a')
        title.write('\n'+f)
        if data['metadata']['title']:
            title.write('\n'+ str(data['metadata']['title'].encode("utf-8",errors='ignore')))
        title.write('\n...\n')
        #print('title')
        reftitle=open(output_dir+'bibtile.txt','a')
        reftitle.write('\n'+f)
        for j in range(len(data['metadata']['references'])):
            if data['metadata']['references'][j]['title']:      
                reftitle.write('\n'+str(data['metadata']['references'][j]['title'].encode("utf-8",errors='ignore')))
        reftitle.write('\n...\n')
        #print('reftitle')
        refvenue=open(output_dir+'bibvenue.txt','a')    
        refvenue.write('\n'+f)
        for j in range(len(data['metadata']['references'])):
            if data['metadata']['references'][j]['venue']:              
                refvenue.write('\n'+str(data['metadata']['references'][j]['venue'].encode("utf-8",errors='ignore')))
        refvenue.write('\n...\n')
        #print('refvenue')
        authkeyword=open(output_dir+'authkeywords.txt','a')
        authkeyword.write('\n'+f)
        keyref=list()
        if data['metadata']['sections']:
            keyref=re.split(r"\n",data['metadata']['sections'][0]['text'])    
            for i in range(len(keyref)):
                if(re.search(r"eyword",keyref[i])):
                    authkeyword.write('\n'+str(keyref[i].encode("utf-8",errors='ignore')))
        authkeyword.write('\n...\n')
        #print('authkwors')
        bodykword=open(output_dir+'rakekwords.txt','a')
        bodykword.write('\n'+f)
        if data['metadata']['sections']:
            text=["" for col in range(len(data['metadata']['sections']))]
            rake_object = rake.Rake("SmartStoplist.txt", 3, 3, 1)
            for i in range(len(data['metadata']['sections'])):
                text[i]= data['metadata']['sections'][i]['text']
            conctext=" ".join(text)
            keyword=rake_object.run(conctext)
            for i in range(len(keyword)):
                bodykword.write('\n'+str(keyword[i]))
        bodykword.write('\n...\n')
        #print('bodykeyword')
        z=z+1
