import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')
# to avoide encoding error , use 'unicode_escape'

# print(df.shape)
# print(df.head(50))
# print(df.tail(10))


removeUnusedCloumn = df.drop(['Status','unnamed1'],axis=1, inplace= True)
print(removeUnusedCloumn)

print(df.info())


