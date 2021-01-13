#the work done here is to compare the life expectancy in more than 150 countrys with a GDP(Gross domestic product) higher than 2938, 
#and lower than it, by showing the data in graphics. it is importante to see, that we are only dividing the data in two parts
#we are doing that by calculating the median (the second quartile)
#in histograms i will draw some direct conclusions (the data set is in the file country_data.csv, wich you can download)

#el trabajo realizado aqui es para comparar la expectativa de vida en más de 150 países con un GDP(producto bruto doméstico) más alto que
#2938 y lo mismo para los países por debajo del mismo, mostrando los datos en gráficos. Es importante recalcar, que estamos solamente
#dividiendo los gráficos en dos partes, y lo hacemos calculando la mediana (el segundo cuartil)
#en histogramas extraeré algunas conclusiones directas(el set de datos está en el archivo country_data.csv, que puede descargar)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
y 
data = pd.read_csv("country_data.csv") #leo los datos /i read the files
print(data) #veo cómo está formada la tabla de datos/i take a look to the dataframe
life_expectancy = data['Life Expectancy'] #guardo la columna en la variable life_expectancy/i save the column in the variable

gdp = data.GDP #guardo los valores de gdp en la variable con el mismo nombre/i save the values of gdp in the same name variable
median_gdp = np.median(gdp) #obtengo la mediana de los valores de gdp, para poder separar los datos/i obtain the gdp median so i can
#know where to split the data
print(median_gdp)

high_gdp = data[data.GDP >= 2938].reset_index(drop = True) #separo los datos en los valores superiores a 2938/i split the values in the
#higher than 2938 gdp
low_gdp = data[data.GDP < 2938].reset_index(drop = True)#hago lo mismo para los valores menores/i do the same with lower values

low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'],[0.25,0.5,0.75]) #obtengo los cuartiles de valores bajos/i obtain the quartiles
#of lower values
high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'],[0.25,0.5,0.75])#lo mismo para valores altos/the same for higher values
print(high_gdp_quartiles)#veo como están dispuestos los cuartiles/i see the disposal of the quartiles
print(low_gdp_quartiles)
plt.hist(low_gdp['Life Expectancy'], range = (40,90) , bins = 20, edgecolor = 'black', label = 'Low GDP', alpha = 0.5)

plt.hist(high_gdp['Life Expectancy'], range =(40,90) , bins = 20, edgecolor = 'black', label = 'High GDP', alpha = 0.5)
plt.legend()
plt.show()
#junto los histogramas en uno solo, para poder realizar una mayor comparación/i put together both histograms in one, so i make
#a better comparison

#de los datos obtenidos lo más simple a ver, es que para una persona de 70 años, en los cuartiles de los países con gdp más bajos
#resulta estar entre los últimos cuartiles
#mientras que para una persona que vive en un país con gdp más alto, se encuentre en el primer cuartil teniendo 70 años
#lo que implica que para países con gdp bajo, la expectativa de vida es menor que para países con gdp alto

#from the data obtained, the most simple to watch, is that for a person of 70 years, in the lower gdp quart countries quartiles, 
#it turns out to be, in the las quartiles
#meanwhile a persona that lives in en country with a higher gdp, it is found to be in the first quartil while being 70 years old,
#that implies that for lower gdp countries, the expectancy of life is lower, than for countries with higher gdp
