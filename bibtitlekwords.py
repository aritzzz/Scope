import rake
import re
import operator

with open('title.txt','r') as f:
    array = []
    for line in f:
        array.append(line)
bibtitlekword=open('titlekwords','w')
rake_object = rake.Rake("venuestoplist.txt", 3, 3, 1)
for j in range(len(array)):
    i=j
    if (re.search(r'json',array[i])):
        a=""
        b=""
        bibtitlekword.write('\n'+array[j])
        while (re.search(r'\.\.\.',array[i])==None):
            a=a+array[i]
            i+=1
        keyword=rake_object.run(a)
        for i in range(len(keyword)):
            bibtitlekword.write('\n'+str(keyword[i]))
        bibtitlekword.write('\n...\n')
    
