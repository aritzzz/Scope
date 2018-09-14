from D import *
import re

eop_pattern = re.compile("(\.\.\.)")
path = '/home/rajeev/Desktop/work/workplace/KDDwork/Artint/'
#path1 = path + 'authors_acc/'

def match(line, pattern):
		m = pattern.match(line)
		return m.groups()[0] if m else None


def write_file(fp):
	#f1 = open('auth_interestst.txt', 'a+')
	#f2 = open('auth_venuet.txt', 'a+')
	f3 = open(path + 'authors_acc/auth_titlet.txt', 'a+')
	fname = fp.readline().strip('\n')
	# f1.write(fname + '\n')
	# f2.write(fname + '\n')
	f3.write(fname + '\n')
	p = fp.tell()
	l = fp.readline().strip('\n')
	while match(l, eop_pattern) == None:
		fp.seek(p)
		auth_name = fp.readline().strip('\n')
		# f1.write('' + auth_name + '\n')
		# f2.write('' + auth_name + '\n')
		f3.write('' + auth_name + '\n')
		sr = search(auth_name)
		print sr
		# if sr != None:

		# 	f1.write('  ' + ','.join(i.encode('utf-8') for i in sr.interests) + '\n')
		# else:
		# 	f1.write('  ' + 'None' + '\n')
		if sr != None:
			write_auth_venue(sr,None,f3)
		else:
			#f2.write('  ' + 'None' + '\n')
			f3.write('  ' + 'None' + '\n')
		p = fp.tell()
		l = fp.readline()
		# f1.write('--\n')
		# f2.write('--\n')
		f3.write('--\n')

	# f1.write('...\n')
	# f2.write('...\n')
	f3.write('...\n')
	f3.close()
 #        f1.close()
	# f2.close()








fp = open(path + 'authors_acc.txt')
fp.read()
pos = fp.tell()
with open(path + 'authors_acc.txt', 'r') as fp:
	po = fp.tell()
	l = fp.readline().strip('\n')
	while l != 'S0004370210001761.pdf.json':
		p = fp.tell()
		print 1
		l = fp.readline().strip('\n')
		if l == 'S0004370210001761.pdf.json':
			break
	fp.seek(p)
	while fp.tell()<pos:
		write_file(fp)
