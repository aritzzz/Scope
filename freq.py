import re
import json

path = '/Users/namanrungta4721/Desktop/server110/'
folder='test_rej'

with open(path + 'Elsevier/statpro/3000/f3000raketitle.txt','r') as json_file:

	data_dict = json.load(json_file)
with open(path + 'Elsevier/statpro/'+folder+'/threshraketitle.txt','r') as f:

	lines=f.readlines()
freqfile=open(path + 'Elsevier/statpro/'+folder+'/fraketitle.txt','w')
pattern=re.compile(r'\'.+\'')

for line in lines:
	match=pattern.findall(line)
	match1=re.search(r'json',line)
	match2=re.search(r'\.\.\.',line)

	if match1:
		freqfile.write('\n'+line)
	elif match2:
		freqfile.write('\n'+line)
	elif match:
		freqfile.write('\n'+match[0]+'	'+str(data_dict.get(match[0],0)))