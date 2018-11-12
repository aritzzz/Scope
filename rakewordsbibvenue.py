import rake
import re
import os 

#path = '/home/rajeev/Desktop/work/workplace/KDDwork/Comnet/authors_oos/'
path='/Users/namanrungta4721/Desktop/server110/'
file='test_rej'
with open(path + 'Elsevier/statpro/'+file+'/bibvenue.txt','r') as f:
    lines=f.readlines()
bodykword=open(path + 'Elsevier/statpro/'+file+'/rakebibvenue.txt','w')
rake_object = rake.Rake("venuestoplist.txt", 3, 3, 1)
for line in lines:
    line = line.strip().split('\t')[0]
    match1=re.search(r'json',line)
    match2=re.search(r'\.\.\.',line)
    match3=re.search(r'--',line)
    if match1:
        bodykword.write(line+'\n')
    elif match2:
        bodykword.write(line+'\n')
    elif match3:
        continue
    else:
    	keyword=rake_object.run(line)
    	for i in range(len(keyword)):
    		bodykword.write('\n'+str(keyword[i]))
    	bodykword.write('\n')
    #print('bodykeyword')