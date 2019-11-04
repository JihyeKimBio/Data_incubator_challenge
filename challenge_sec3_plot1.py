#2018 Alzheimer’s Disease Facts and Figures is a statistical resource for U.S. data related to Alzheimer’s disease, the most common cause of dementia. Background and
#context for interpretating the data are contained in the Overview. 


# Projections of Total Numbers of Americans Age 65 and Older with Alzheimer's Dementia by State


import pandas as pd
import numpy as np
import math
import matplotlib
from scipy import stats
from matplotlib import pyplot as plt


Alz_num_2018 = pd.read_csv('Alzheimer_2018_statistics_1.csv')
x=Alz_num_2018['State']
y1=Alz_num_2018['2018']
y2=Alz_num_2018['2025']
plt.plot(x,y1, color='pink', marker='o')
plt.plot(x,y2, color='gray', marker='v')
plt.title('Projections of Total Numbers of Americans Age 65 and Older with Alzheimer\'s Dementia by State')
plt.xlabel('State')
plt.ylabel('Projected Number with Alzheimer\'s (in thousands')
plt.show()
plt.savefig('section3_figure1.png')

