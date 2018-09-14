from authR import *
import re

eop_pattern = re.compile("(\.\.\.)")


def match(line, pattern):
		m = pattern.match(line)
		return m.groups()[0] if m else None


def write_file(fp):
	f1 = open('auth_interestComnetacc.txt', 'a+')
	f2 = open('auth_venueComnetacc.txt', 'a+')
	fname = fp.readline().strip('\n')
	f1.write(fname + '\n')
	f2.write(fname + '\n')
	f3.write(fname + '\n')
	p = fp.tell()
	l = fp.readline().strip('\n')
	while match(l, eop_pattern) == None:
		fp.seek(p)
		auth_name = fp.readline().strip('\n')
		f1.write('' + auth_name + '\n')
		f2.write('' + auth_name + '\n')
		sr = search(auth_name)
		print(sr)
		if sr != None:

			f1.write('  ' + ','.join(str(i.encode('utf-8')) for i in sr.interests) + '\n')
		else:
			f1.write('  ' + 'None' + '\n')
		if sr != None:
			write_auth_venue(sr,f2)
		else:
			f2.write('  ' + 'None' + '\n')
		p = fp.tell()
		l = fp.readline()
		f1.write('--\n')
		f2.write('--\n')

	f1.write('...\n')
	f2.write('...\n')








fp = open('authors.txt')
fp.read()
pos = fp.tell()
with open('authors.txt', 'r') as fp:
	# po = fp.tell()
	# l = fp.readline().strip('\n')
	# while l != '493.pdf.json':
	# 	p = fp.tell()
	# 	print(1)
	# 	l = fp.readline().strip('\n')
	# 	if l == '493.pdf.json':
	# 		break
	#fp.seek(p)
	while fp.tell()<pos:
		write_file(fp)
