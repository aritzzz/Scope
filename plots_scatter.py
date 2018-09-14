import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import seaborn as sns
import pandas as pd 
import numpy as np
import matplotlib as mpl
#print(plt.style.available)
mpl.style.use('seaborn-paper')

label = 'ARTINT'

pathe = '/home/rajeev/Desktop/work/workplace/KDDwork/'
path = pathe + 'plots/' + label.lower() + '_scatter/'
ACC = pd.read_csv(pathe + label.lower() + '_acc.csv').sample(400)
REJ = pd.read_csv(pathe + label.lower() + '_oos.csv').sample(400)
# new_columns = ACC.columns.values
# new_columns[10] = 'bibtitle'
# ACC.columns = new_columns
# REJ.columns = new_columns
#print ACC.columns.values
#data = list(REJ.columns)[9:-1]
#for artint 
cols = ['Unnamed: 0', 'idd', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'abstract', 'biblio_title', 'authors_title', 'authors_venue', 'authors_interests', 'authors_keywords', 'title', 'biblio_title_keywords', 'biblio_venue', 'body', 'tag']
#cols = ['Unnamed: 0', 'idd', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'biblio_title', 'abstract', 'authors_title', 'authors_venue', 'authors_interests', 'authors_keywords', 'title', 'biblio_title_keywords', 'biblio_venue', 'body', 'tag']
ACC.columns = cols
REJ.columns = cols
print(list(ACC.columns))
data = list(ACC.columns)[9:-1]
print data
# data[1] = 'bibtitle'
#print data
ACC = ACC.fillna(0)
REJ = REJ.fillna(0)

for i in range(len(data)):
	for j in range(len(data)):
		if i == j:
			continue
		else:
			# print len(ACC[data[i]])
			# print len(ACC[data[j]])
			a = 0.8
			fig,ax = plt.subplots(figsize = (3.2, 2.8), dpi = 140)
			ax.xaxis.grid(True, linestyle = '-', color = 'lightgrey', alpha = 0.2)
			ax.yaxis.grid(True, linestyle = '-', color = 'lightgrey', alpha = 0.2)
			ax.scatter(ACC[data[i]],ACC[data[j]], s = 10, c = 'blue', marker = 'o', alpha = a)
			ax.scatter(REJ[data[i]],REJ[data[j]], s = 10, c = 'red', marker = 'o', alpha = a)

			ax.set_xlabel(data[i], fontsize = 8, )
			ax.set_ylabel(data[j], fontsize = 8, )
			ax.spines['top'].set_visible(False)
			ax.spines['right'].set_visible(False)
			ax.spines['bottom'].set_visible(False)
			ax.spines['left'].set_visible(False)
			# ax.yaxis.set_ticks_position('left')
			# ax.xaxis.set_ticks_position('bottom')
			#plt.axis('off')
			plt.tick_params(axis = 'x', which = 'both', bottom = 'off', top = 'off')
			plt.tick_params(axis = 'y', which = 'both', left = 'off', right = 'off')

			ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
			ax.autoscale(enable=True, axis='x', tight=True)
			ax.xaxis.major.formatter._useMathText = True

			fig.text(0.69, 0.84, label,
						  color='black', weight='roman',
						  fontsize = 8)
			plt.tight_layout()
			plt.savefig(path + label.lower() + '_' + data[i] + '_' + data[j] + '.png')
			#plt.show()


