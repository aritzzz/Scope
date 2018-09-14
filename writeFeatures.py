"""
To make a csv file of features Auth_listed_KW, Title_KW, bibtitle_KW, rake_bibvenue_KW, rake_KW

"""


import pandas as pd 
import os

path2 = '/home/rajeev/Desktop/work/workplace/KDDwork/Features/Artint_test_acc/'

dirs = os.listdir(path2)
print dirs



df1 = pd.read_csv(path2 + dirs[1], sep = '\t', header = None)
df1.columns = ['idd', 'authKW']
#print df1.head() 
df2 = pd.read_csv(path2 + dirs[2], sep = '\t', header = None)
df2.columns = ['idd', 'titleKW']
df3 = pd.read_csv(path2 + dirs[3], sep = '\t', header = None)
df3.columns = ['idd', 'bibtitleKW']
df4 = pd.read_csv(path2 + dirs[0], sep = '\t', header = None)
df4.columns = ['idd', 'rkbibvenueKW']
# df5 = pd.read_csv(path2 + dirs[4], sep = '\t', header = None)
# df5.columns = ['idd', 'hKW']
df6 = pd.read_csv(path2 + dirs[4], sep = '\t', header = None)
df6.columns = ['idd', 'rakeKW']

df = pd.merge(df1, df2, on = 'idd')
df = pd.merge(df, df3, on = 'idd')
df = pd.merge(df, df4, on = 'idd')
df = pd.merge(df, df6, on = 'idd')
df.to_csv('Artint_acc.csv')
print(len(df))
