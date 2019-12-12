#from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
#iris_dataset = load_iris()
#data1 = iris_dataset["data"]
data = pd.read_csv('carsdetails.csv')
plt.scatter(data['wt'],data['mpg'])
plt.title('Scatter plot of mpg vs weight of car')
plt.xlabel('weight of car')
plt.ylabel('miles per gallon')
plt.show()
