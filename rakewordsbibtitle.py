import rake
import os 
import re
path='/Users/namanrungta4721/Desktop/server110/'
file='test_rej'
with open(path+'Elsevier/statpro/'+file+'/bibtile.txt','r') as f:
    lines=f.readlines()
bodykword=open(path +'Elsevier/statpro/'+file+'/rakebibtitle.txt','w')
rake_object = rake.Rake("SmartStoplist.txt", 3, 3, 1)
for line in lines:
    match1=re.search(r'json',line)
    match2=re.search(r'\.\.\.',line)
    if match1:
        bodykword.write(line+'\n')
    elif match2:
        bodykword.write(line+'\n')
    else:
        keyword=rake_object.run(line)
        for i in range(len(keyword)):
            bodykword.write('\n'+str(keyword[i]))
        bodykword.write('\n')
    #print('bodykeyword')