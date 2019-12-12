#from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
#iris_dataset = load_iris()
#data1 = iris_dataset["data"]
data = pd.read_csv('carsdetails.csv')
plt.hist(data['mpg'],density=False)
plt.title('Histogram of miles per gallon')
plt.xlabel('miles per gallon')
plt.ylabel('Frequency')
plt.show()
