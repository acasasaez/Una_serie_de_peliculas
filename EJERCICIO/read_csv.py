from tkinter import W
import pandas as pd 
df = pd.read_csv(r"C:/Users/andre/OneDrive/Escritorio/Programación/Una_serie_de_peliculas/EJERCICIO/archivo.csv")
print(df)
mh = pd.ExcelWriter("C:/Users/andre/OneDrive/Escritorio/Programación/Una_serie_de_peliculas/EJERCICIO/archivo.csv")