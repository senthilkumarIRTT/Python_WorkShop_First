cars=["Maruthi","Honda","TataIndica"]
x = cars[0]
print("x=\n",x)
cars[0]="Ford"
print("cars=\n",cars)
L = len(cars)
print("Length of cars=",L)
#Print each item in the car array
for y in cars:
    print(y)

cars.append("BMW")
print("cars=\n",cars)
#Delete the second element of the cars array
cars.pop(1)
print("cars=\n",cars)
#Delete the element that has the value "Honda"
cars.remove('TataIndica')
print("cars=\n",cars)

#Result
##x= Maruthi
##cars=  ['Ford', 'Honda', 'TataIndica']
##Length of cars= 3
##Ford
##Honda
##TataIndica
##cars=  ['Ford', 'Honda', 'TataIndica', 'BMW']
##cars=  ['Ford', 'TataIndica', 'BMW']
##cars=  ['Ford', 'BMW']


