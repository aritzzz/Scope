"""
Do check the structure of file for running this code.
Reads the frequency file for an attribute to write the 
respective feature to a different file(filename) indexed by paperid.
"""
from __future__ import division
import numpy as np 
import csv
import re
eop_pattern = re.compile(r'\.\.\.')
def match(line,pattern):
			 m = pattern.match(line)
			 return m.groups() if m else None


#Jour = 'Comnet'
#path = '/home/rajeev/Desktop/work/Elsevier/statpro/test_rej/freqFiles/'
path='/Users/namanrungta4721/Desktop/server161/Naman/DATA/Accepted_feature/SIMPAT/SIMPAT_TEST/'
#path = '/home/rajeev/Desktop/work/workplace/KDDwork/' + Jour + '/authors_oos/'
#path2 = '/home/rajeev/Desktop/work/workplace/KDDwork/Features/Statpro_test_oos/'
path2='/Users/namanrungta4721/Desktop/server161/Naman/DATA/Accepted_feature/SIMPAT/freq/'
class Paper():
		 def __init__ (self, paperid, feature):
					self.paperid = paperid
					self.feature = feature
					

def features(f):
			 paper = [] 
			 #f.readline().strip()
			 fname = f.readline().strip()
			 f.readline()
			 p = f.tell()
			 line = f.readline().strip()
			 while match(line,eop_pattern) == None:
					 f.seek(p)
					 l = f.readline().strip()
					 #print(l)
					 #try:
					 if len(l.split('\t'))>1:
					 	freq = int(l.split('\t')[1])
					 #print(freq)
					 #except:
							#freq = 0
					 paper.append(freq)
					 p = f.tell()
					 line = f.readline().strip()
			 f.readline().strip()		 	
			 try:
				 paper = np.array(paper)
				 paper = np.sum(paper/np.max(paper))
			 except:
				 paper = 0.0
			 return Paper(fname, paper)
					 
					 
			 
def iter_papers(fileobject):
			#with open(filename, 'r') as fileobject:
			 fileobject.read()
			 pos = fileobject.tell()
			 fileobject.seek(0)
			 while fileobject.tell() < pos:
							record = features(fileobject)
							yield record

def write_file(fileobject, filename):
			with open(path2 + filename + '.txt', 'a+') as f:
					 papers = iter_papers(fileobject)
					 for paper in papers:
							 if paper == None:
									continue
							 else:
									f.write(paper.paperid + '\t' + str(paper.feature) + '\n')
##change the filename to read features from.
filename = 'frakeabstract'
with open(path + 'frakeabstract.txt', 'r') as fo:
			write_file(fo, filename)
					
