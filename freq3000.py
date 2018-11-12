import re
import json

path = '/Users/namanrungta4721/Desktop/server110/' 
with open(path+'Elsevier/statpro/3000/threshrakebibvenue.txt','r') as f:
	lines=f.readlines()
	#filetext = f.read()
freqfile=open(path+'Elsevier/statpro/3000/f3000rakebibvenue.txt','w')
dict={}
pattern=re.compile(r'\'.+\'')
for line in lines:
	match=pattern.findall(line)
	print(match)
	if match:
		x=dict.get(match[0],1)
		dict[match[0]]=x+1
json.dump(dict,freqfile,indent=4)