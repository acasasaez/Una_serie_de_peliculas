
import pandas as pd 
import matplotlib.pyplot as plt
import numpy 
import seaborn as sb
df = pd.read_csv(r"C:/Users/andre/OneDrive/Escritorio/Programación/Una_serie_de_peliculas/resultados.csv.csv")
print(df)

data = numpy.random.randn(5)
print("The data is-",data)
sorted_random_data = numpy.sort(data)
p = 1. * numpy.arange(len(sorted_random_data)) / float(len(sorted_random_data) - 1)
print("The CDF result is-",p)

fig = plt.figure()
fig.suptitle('CDF of data points')
ax2 = fig.add_subplot(111)
ax2.plot(sorted_random_data, p)
ax2.set_xlabel('sorted_random_data')
ax2.set_ylabel('p')