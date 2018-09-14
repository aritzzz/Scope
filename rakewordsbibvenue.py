import rake
import re
import os 
with open('/home/rajeev/Desktop/work/workplace/KDDwork/comnet/authors_oos/auth_venue_oos.txt','r') as f:
    lines=f.readlines()
bodykword=open('/home/rajeev/Desktop/work/workplace/KDDwork/comnet/auth_venue_oos.txt','w')
rake_object = rake.Rake("SmartStoplist.txt", 3, 3, 1)
for line in lines:
    line = line.strip()
    match1=re.search(r'json',line)
    match2=re.search(r'\.\.\.',line)
    match3=re.search(r'--')
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