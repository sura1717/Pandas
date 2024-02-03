import numpy as np
import pandas as pd

#creating DATAFRAME
student=pd.DataFrame([[85,70,7],[100,45,15],[55,90,10]])
students=pd.DataFrame({"name":["suraj","nikesh","satish","abhishek","akshay","amit"],"IQ":[90,84,75,97,23,45],"CGPA":[70,None,74,72,60,78],"LPA":[7,11,21,16,9,18]})
movies=pd.read_csv("movies.csv")
ipl=pd.read_csv("ipl-matches.csv")

print(ipl)
print(movies)
print(student)
print(students)

#methods and attributes in DataFrame
print(movies.shape)     #return shape of dataframe in the form of row and column
print(ipl.shape)

print(movies.dtypes)        #return datatype of every column
print(students.dtypes)
print(ipl.dtypes)

print(movies.index)         #return index in the form of range
print(students.index)

print(ipl.columns)          #return all column name
print(students.columns)

print(movies.values)            #return value in the form of 2D array
print(ipl.values)
print(student.values)


print(ipl.head(3))
print(ipl.tail(4))
print(students.head(8))


print(students.sample(2))       #fatched 2 random rows
print(movies.sample())

print(students.info())      #about information your dataframe
print(movies.info())

print(movies.describe())        #summery about all column and information about table
print(ipl.describe())

print(students.isnull())        #if null value in dataframe return true\
print(movies.isnull().sum(axis=1))        #sum of every null value row wise wise
print(students.isnull().sum())      #sum of all null value column wise

print(ipl.duplicated())        # row wise duplicate values

print(students.rename(columns={"CGPA":"percentile","name":"NAME"}))
print(ipl)
print(ipl.rename(columns={"ID":"ID","City":"TOWN"}))                #change name of table columns temproey
print(ipl)

#some mathmatical function
#print(movies.sum())     #sum all column(string concatination) working on only same datatype
print(students.sum())
print(students.min())
print(students.median())
print(students.max())     #working only same data type

#selecting column from a dataframe

print(ipl["City"])

print(ipl[["City","ID","Umpire1","Umpire2"]])       #fancy style order decided by given list

#selecting row in a dataframe
#iloc = Search using index position
#loc = Search using index level
print(ipl.iloc[3])
print(movies.iloc[6])
print(students.loc["suraj","nikesh","satish"])
print(students.loc["Suraj":"amit"])

#selecting rows and column both

print(ipl.iloc[0:3,0:3])                #using iloc
print(ipl.loc[0:7,"ID":"Date"])
print(ipl.loc[0:10,["ID","City","Date"]])         #in fancy style
