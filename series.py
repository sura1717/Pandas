import pandas as pd
#read a csv file
color=pd.read_csv('single-color-names.csv')         #not in a series

#print(color)

#create a series
runs=pd.Series([12,23,43,54,23,7,67,87,55,43,12],dtype=int)

#series using dictionary
subj=pd.Series({"math":78,"english":67,"physics":72,"chemistry":73,"hindi":56,"bme":76,"bce":66,"m2":0,"ed":56,"com":88},name="result hai bhai mera")

country=["india","USA","pakistan","russia","nepal"]
code=[45,67,32,43,89]
country_code=pd.Series(country,index=code,name="cuuntry name and its code")       #costum indexes

print(country_code)
print(runs)
print(subj)

#series attributes ---> stype/size/name/is_unique/index/value
print(country_code.size)            #return size of series
print(country_code.dtype)       #return datatype of series
print(country_code.name)        #return name of series
print(country_code.index)           #return a list of all indexes
print(country_code.values)          #return a list of all values
print(country_code.is_unique)   #return true if all calue is uinque


#series methods
print(runs.head(3))             #print top 3 rows in series
print(runs.tail(5))                 #print last 5 rows in a series
print(subj.sample(2))        #return 2 random rows
print(subj.value_counts())      #return friquency count of every value
print(subj.sort_values(ascending=False))       #sort all values in decending order


#method chaining
print(subj.sort_values().head(5).values[2])     #sort all value in ascending order and top 5 of 2nd index values
print(subj.sort_values(ascending=False).head(4).mean())
print(subj.sort_index(inplace=True))        #sorted by inddex

#math method of series
print(runs.mean())      #mean of series
print(runs.mode())      #mode of series
print(runs.median())            #median of series
print(runs.std())           #standard deviation of series
print(runs.var())       #varience of series
print(subj.min())       #minimium value in series
print(subj.max())           #maximium value in series
print(subj.describe())          #discribe summery of all series


#series indexing and slicing
print(subj[2])
print(subj[2])
print(subj[::2])
print(subj[-1::-1])
print(subj[[1,3,5,6]])      #fancy indexing

#editimg series

runs[2]=58
print(runs)
subj[2]=99      #this is a warning 2 is not an index
subj["bce"]=43
subj["dsa"]=44      #when index is not present then its add in last
print(subj)

runs[2:5]=[22,45,67]        #editing using slicing
print(runs)
subj[["m2","math","bme"]]=[56,88,43]        #editing using fancy index
print(subj)

#series with pythin function
print(len(subj))
print(sorted(runs))         #output in the form of list
print(dir(runs))
print(type(subj))
print(min(subj))
print(max(subj))


#type conversion
marks_list=list(subj)
marks_dic=dict(subj)
print(marks_list)
print(marks_dic)


#membership operator

print("math" in subj)
print("43" in runs)
print("bce" not in subj)

for i in subj:          #looping in series
    print(i)


#arithmatic operators
print(100-subj)             #iterate operation one by one
print(3*subj)
print(runs%10)

#relational opertors
print(runs[runs>=50])
print((subj[subj>=75]).size)
print(subj.value_counts())


#plotting graph
subj.plot()