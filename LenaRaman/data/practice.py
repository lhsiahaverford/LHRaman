#scatter
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob

#for datafile 1
GSHPEG_file = '/Users/lenahsia/PycharmProjects/LenaRaman/data/RawData/10mM_GSH_PEG_1_580nm_30sec_150gg67112_1.txt'
GSHPEG_data = np.genfromtxt(fname=GSHPEG_file, delimiter = ',', dtype = 'unicode')

#displaying and printing the data frame GSHPEG_data
df = pd.DataFrame(GSHPEG_data)

#dropping
df_dropped_column = df.drop(columns= [1])

#add labels with rename function to dropped dataframe and convert pd to numeric rather than string
df_droppedrenamed = df_dropped_column.rename(columns={0: 'raman shift', 2:'intensity'})
df_droppedrenamed['raman shift'] = pd.to_numeric(df_droppedrenamed['raman shift'])
df_droppedrenamed['intensity'] = pd.to_numeric(df_droppedrenamed['intensity'])
print("\nRenamed dropped Dataframe 1 :")
print(df_droppedrenamed)



#plot

plt.scatter(df_droppedrenamed['raman shift'], df_droppedrenamed['intensity'], label='data 1',s=5)
plt.legend(fontsize=10)
plt.title("10 mM GSH in PEG 30Sec 150 ", fontsize=10)
plt.xlabel('Raman Shift', fontsize=10)
plt.ylabel('Intensity', fontsize=10)
plt.show()


