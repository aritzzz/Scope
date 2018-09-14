import matplotlib.pyplot as plt 
from matplotlib.patches import Polygon
import seaborn as sns
import pandas as pd 
import numpy as np
import matplotlib as mpl
#print(plt.style.available)
mpl.style.use('seaborn-paper')


label = 'ARTINT'

path = '/home/rajeev/Desktop/work/workplace/KDDwork/'
#data = ['abstractKW']#,'cit_macx', 'c', 'avgImpactCit']#, 'b', 'c', 'd']#['cit_avg', 'cit_max']#['avg_h', 'max_h']# 'cit_avg', 'cit_max']#['avg_doc', 'max_affl_doc', 'avg_rc', 'max_affl_rc']#['avg_h', 'max_h','cit_avg', 'cit_max', ['avg_doc', 'max_affl_doc']
#rD = ['ADPF'] #, 'Affl-max-rs'] #'clustering', 'bibsum', 'bibtitle']
ACC = pd.read_csv(path + label.lower() + '_acc.csv')
REJ = pd.read_csv(path + label.lower() + '_oos.csv')
cols = ['Unnamed: 0', 'idd', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'abstract', 'biblio_title', 'authors_title', 'authors_venue', 'authors_interests', 'authors_keywords', 'title', 'biblio_title', 'biblio_venue', 'body', 'tag']
ACC.columns = cols
REJ.columns = cols
print(list(ACC.columns))
data = list(ACC.columns)[9:-1]
print data
# ACC = pd.read_csv('sampledACC.csv')
# REJ = pd.read_csv('qualityREJ.csv')
# ACC = pd.read_csv('STATqualityACC.csv')
# REJ = pd.read_csv('STATqualityREJ.csv')


ACC = ACC.fillna(0)
REJ = REJ.fillna(0)

for i in range(len(data)):
	a = 0.8
	fig, ax = plt.subplots(figsize = (3.2,2.8), dpi = 140)
	# #print len(axarr)
	# #sns.boxplot(data)
	# bp = ax1.boxplot(data)
	# plt.setp(bp['boxes'], color = 'black')
	# plt.setp(bp['whiskers'], color = 'black')
	# plt.setp(bp['fliers'], color = 'black', marker = '+')
	# ax1.set_axisbelow(True)
	# #ax1.set_title('')
	# #ax1.set_xlabel('Avg. h index')
	# #ax1.set_ylabel('CDF')
	# ax1.set_xticklabels(np.repeat(rD,2), rotation=45, fontsize=8)
	# ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
	# ax1.yaxis.major.formatter._useMathText = True
	# boxColors = ['gray', 'khaki']
	# numBoxes = len(data)
	# medians = list(range(numBoxes))
	# for i in range(numBoxes):
	# 	box = bp['boxes'][i]
	# 	boxX = []
	# 	boxY = []
	# 	for j in range(5):
	# 		boxX.append(box.get_xdata()[j])
	# 		boxY.append(box.get_ydata()[j])
	# 	boxCoords = list(zip(boxX,boxY))
	# 	k = i % 2
	# 	boxPolygon = Polygon(boxCoords, facecolor = boxColors[k])
	# 	ax1.add_patch(boxPolygon)
	# 	med = bp['medians'][i]
	# 	medianX = []
	# 	medianY = []
	# 	for j in range(2):
	# 		medianX.append(med.get_xdata()[j])
	# 		medianY.append(med.get_ydata()[j])
	# 		ax1.plot(medianX, medianY, 'k')
	# 		medians[i] = medianY[0]
	# 	# Finally, overplot the sample averages, with horizontal alignment
	# 	# in the center of each box
	# 	ax1.plot([np.average(med.get_xdata())], [np.average(data[i])],
	# 			 color='w', marker='*', markeredgecolor='k')
	# #sns.jointplot()
	# fig.text(0.16, 0.83, 'Accepted',
	#          backgroundcolor=boxColors[0], color='black', weight='roman',
	#          size='x-small')
	# fig.text(0.16, 0.78, ' Rejected',
	#          backgroundcolor=boxColors[1], color='black', weight='roman',
	#          size='x-small')
	# # n, bins, patches = ax1.hist(ACC['avg_h'], normed=1, histtype='step',
	# # 						   #cumulative=True)
	# # y = mlab.normpdf(bins, ACC['avg_h'].mean(), ACC['avg_h'].std()).cumsum()
	# # z = ACC['avg_h']/(ACC['avg_h'].sum())
	#for i in range(len(axarr)):
		#for j in range(2):
	ax.yaxis.grid(True, linestyle = '-', color = 'lightgrey', alpha = 0.5)
	hist,bin_edges = np.histogram(ACC[data[i]],bins = 'auto', normed = True)
	cdf = np.cumsum(hist*np.diff(bin_edges))
	ax.plot(bin_edges[1:], cdf, c = 'blue', alpha = a, linewidth = 1.5)
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')
	#ax.set_xlabel(data[0])
	hist,bin_edges = np.histogram(REJ[data[i]],bins = 'auto', normed = True)
	cdf = np.cumsum(hist*np.diff(bin_edges))
	ax.plot(bin_edges[1:], cdf, c = 'maroon', alpha = a, linewidth = 1.5)
	ax.set_ylim(0,1.1)
	#t = t + 1

	ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	ax.autoscale(enable=True, axis='x', tight=True)
	ax.xaxis.major.formatter._useMathText = True
	# axarr[0,1].ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	# axarr[0,1].autoscale(enable=True, axis='x', tight=True)
	# axarr[1,0].ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	# #axarr[1,0].xaxis.major.formatter._useMathText = True
	# axarr[1,0].autoscale(enable=True, axis='x', tight=True)

	# axarr[1,1].ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	# # #axarr[1,1].xaxis.major.formatter._useMathText = True
	# axarr[1,1].autoscale(enable=True, axis='x', tight=True)
	# # axarr[2,0].ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	# # #axarr[2,0].xaxis.major.formatter._useMathText = True
	# # axarr[2,0].autoscale(enable=True, axis='x', tight=True)
	# # axarr[2,1].ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	# # axarr[2,1].autoscale(enable=True, axis='x', tight=True)
	# axarr[0,0].xaxis.major.formatter._useMathText = True
	# axarr[0,1].xaxis.major.formatter._useMathText = True
	# axarr[1,0].xaxis.major.formatter._useMathText = True
	# axarr[1,1].xaxis.major.formatter._useMathText = True
	# # axarr[2,0].xaxis.major.formatter._useMathText = True
	# # axarr[2,1].xaxis.major.formatter._useMathText = True

	#ax.set_xlabel('Auth-max-h', fontsize = 10)
	ax.set_ylabel('CDF', fontsize = 8, )
	ax.set_xlabel(data[i], fontsize = 8, )

	#ax.set_xticks([0.002,0.008,0.014])
	plt.tight_layout()
	# axarr[0,1].set_xlabel('keyword match')
	# #axarr[2].set_yscale('log')
	# #axarr[3].set_yscale('log')
	# axarr[1,0].set_xlabel('ADPF')
	# axarr[1,1].set_xlabel('journal Scope')
	#fig.text(2,2, 'CDF',color = 'black',size = 'x-small', weight = 'roman', rotation = 'vertical')

	#fig.text(0.045, 0.5, 'CDF', va = 'center', rotation = 'vertical', fontsize = 18)
	# fig.text(0.08, 0.94,'Accepted', color = 'black',size = 'x-small' )
	# fig.text(0.18, 0.94,'Rejected', color = 'goldenrod', size = 10)
	# axarr[0].ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	# axarr[0].autoscale(enable=True, axis='x', tight=True)
	# axarr[0].xaxis.major.formatter._useMathText = True
	# axarr[1].ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	# axarr[1].autoscale(enable=True, axis='x', tight=True)
	# axarr[1].xaxis.major.formatter._useMathText = True
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.spines['bottom'].set_visible(False)
	ax.spines['left'].set_visible(False)



	fig.text(0.69, 0.89, label,
	          color='grey', weight='roman',
	          fontsize = 8)
	# y = np.cumsum(z)
	# print 1
	# plt.plot(ACC['avg_h'],y)
	#plt.tight_layout()
	plt.savefig(path + 'plots/' + label.lower() + '/' + label.lower() + '_' +  data[i] + '.png')

