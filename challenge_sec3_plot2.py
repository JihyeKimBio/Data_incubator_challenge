#2018 Alzheimer’s Disease Facts and Figures is a statistical resource for U.S. data related to Alzheimer’s disease, the most common cause of dementia. Background and
#context for interpretating the data are contained in the Overview. 


# U.S. Annual Alzheimer's Death Rates (per 100,000 People) by Age and Year 



import pandas as pd
import numpy as np
import math
import matplotlib
from scipy import stats
from matplotlib import pyplot as plt


Alz_num_2018 = pd.read_csv('Alzheimer_2018_statistics_2.csv')

x=Alz_num_2018['Age']
y1=Alz_num_2018['2000']
y2=Alz_num_2018['2001']
y3=Alz_num_2018['2002']
y4=Alz_num_2018['2003']
y5=Alz_num_2018['2004']
y6=Alz_num_2018['2005']
y7=Alz_num_2018['2006']
y8=Alz_num_2018['2007']
y9=Alz_num_2018['2008']
y10=Alz_num_2018['2009']
y11=Alz_num_2018['2010']
y12=Alz_num_2018['2011']
y13=Alz_num_2018['2012']
y14=Alz_num_2018['2013']
y15=Alz_num_2018['2014']
y16=Alz_num_2018['2015']
plt.figure(figsize=(20,20))
plt.yticks(np.arange(0, 1200, 100))
plt.plot(x,y1, color='blue', marker='o')
plt.plot(x,y2, color='gray', marker='o')
plt.plot(x,y3, color='aqua', marker='o')
plt.plot(x,y4, color='beige', marker='o')
plt.plot(x,y5, color='brown', marker='o')
plt.plot(x,y6, color='chocolate', marker='o')
plt.plot(x,y7, color='coral', marker='o')
plt.plot(x,y8, color='darkgreen', marker='o')
plt.plot(x,y9, color='fuchsia', marker='o')
plt.plot(x,y10, color='gold', marker='o')
plt.plot(x,y11, color='green', marker='o')
plt.plot(x,y12, color='indigo', marker='o')
plt.plot(x,y13, color='lavender', marker='o')
plt.plot(x,y14, color='lime', marker='o')
plt.plot(x,y15, color='navy', marker='o')
plt.plot(x,y16, color='plum', marker='o')
plt.title('U.S. Annual Alzheimer\'s Death Rates by Age and Year', fontsize=25)
plt.xlabel('Age', fontsize=23)
plt.ylabel('Death Rates per 100,000 People', fontsize=23)
plt.legend(('2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012','2013', '2014', '2015'), loc='upper left')
plt.show()
plt.savefig('section3_plot2.png')

