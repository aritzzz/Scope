import re
import json

path = '/Users/namanrungta4721/Desktop/server110/'
folder='test_acc'


with open(path+'Elsevier/statpro/3000/f3000bibvenue.txt','r') as json_file:
	#json_str=json_file.read()
	data_dict = json.load(json_file)#,strict=False)
with open(path+'Elsevier/statpro/'+folder+'/bibvenue.txt','r') as f:
	lines=f.readlines()
freqfile=open(path+'Elsevier/statpro/'+folder+'/fbibvenue.txt','w')
#pattern=re.compile('\n')
for line in lines:
	#match=pattern.findall(line)
	match1=re.search(r'json',line)
	match2=re.search(r'\.\.\.',line)
	if match1:
		freqfile.write('\n'+line)
	elif match2:
		freqfile.write('\n'+line)
	else:
		#print(data_dict.get(match[0],0))
		freqfile.write('\n'+line+str(data_dict.get(line,0)))
	#print('.'),