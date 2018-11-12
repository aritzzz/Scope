import rake
import re
import os 

Jour = 'Comnet'
file='test_rej'
#path = '/home/rajeev/Desktop/work/workplace/KDDwork/' + Jour 
path='/Users/namanrungta4721/Desktop/server110/'
with open(path+'Elsevier/statpro/'+file+'/title.txt' ,'r') as f:
    lines=f.readlines()
bodykword=open(path+'Elsevier/statpro/'+file+'/raketitle.txt','w')
rake_object = rake.Rake("SmartStoplist.txt", 3, 3, 1)
for line in lines:
	#print type(line)
	line = line.strip().split('\t')[0]
	match1=re.search(r'json',line)
	match2=re.search(r'\.\.\.',line)
	match3 = re.search(r'--', line)
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