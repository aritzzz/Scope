import json

with open('/Users/namanrungta4721/Desktop/server110/Elsevier/statpro/3000/bibvenue.txt','r') as f:
	lines=f.readlines()
	filetext = f.read()
freqfile=open('/Users/namanrungta4721/Desktop/server110/Elsevier/statpro/3000/f3000bibvenue.txt','w')
dict={}
for line in lines:
	x=dict.get(line,1)
	dict[line]=x+1
json.dump(dict,freqfile,indent=4)