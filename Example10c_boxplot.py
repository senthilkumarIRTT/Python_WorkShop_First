import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data1 = pd.read_csv('diamond.csv')
sns.boxplot(x=data1['cut'], y=data1['price'],data=data1)
plt.show()
