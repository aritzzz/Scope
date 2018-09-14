import pandas as pd 
import numpy as np
import os
import shutil
import re
pattern = re.compile(r'.xml')

loc = '/home/rajeev/Desktop/work/SOTW_Prashant/Data/'            #/DR-OOS/

path = '/home/rajeev/Desktop/work/workplace/KDDwork/test_data_ids/'

# data = pd.read_csv(path + 'COMnetAcc297.csv', usecols = ['index'])
# data = data['index'].values
data = np.load(path + 'comnet_oos_ids.npy')
print len(data)
#print data
#print 'S000437021000158X.pdf.xml' in data

# for file in data:
# 	print file

src_files = os.listdir(loc + 'DR-OOS/COMNET_OOS_XML/ALL')                #+ 'ARTINT_OOS_XML' )
print len(src_files)
for file in src_files:
	pathe = os.path.join(loc + 'DR-OOS/COMNET_OOS_XML/ALL', file)
	filee = pattern.sub('.json', file)
	if filee in data:
		print filee
		shutil.copy(pathe, loc + 'comnet_oos')
		print 1