import os
import json
file='test_rej/'
path='/Users/namanrungta4721/Desktop/server110/'
input_dir=path+'Elsevier/statpro/STATPRO_ACC_JSON/'
output_dir=path+'Elsevier/statpro/'+file
files=os.listdir(input_dir)
abstract=open(output_dir+'abstract.txt','w')
for f in files:
	#print(f)
	if('fuse' not in f):
		print(f)
		with open(input_dir+f) as input_file:
			data = json.load(input_file)
		abstract.write('\n'+f)
		if data['metadata']['sections']:
			#print (data['metadata']['sections'][0]['heading'])
			if data['metadata']['sections'][0]['heading'] == None:
				abstract.write('\n'+str(data['metadata']['sections'][0]['text']))#.encode("utf-8",errors='ignore'))
			else:
				print(data['metadata']['sections'][0]['heading'])
		abstract.write('\n...\n')