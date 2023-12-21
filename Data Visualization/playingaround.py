
import pandas as pd 
import warnings
warnings.simplefilter("ignore")
ED = pd.read_excel("ManHourData.xlsx", engine = "openpyxl")
print(ED)
effort = (ED.loc[:, "ManHour"])

import matplotlib.pyplot as plt 
# effort.plot.box()
# plt.show()
effort.plot.bar()
plt.xticks()
plt.show()