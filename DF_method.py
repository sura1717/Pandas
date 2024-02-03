import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

students=pd.DataFrame({"name":["suraj","baby","akshay","salu","salini","nikesh","NaN"],"cgpa":[7.5,5.5,None,9,7.7,6,None],"branch":[None,"CSE","CE","EEE",None,"AIML","NaN"],"college":["ies","tit","lnct","ies",None,"lnct","NaN"],"package":[4,6,9,6,3,None,None]})
movies=pd.read_csv("movies.csv")
student=pd.DataFrame([[100,80,32],[80,90,43],[70,54,13],[70,60,14],[70,60,14]],columns=["iq","cgpa","package"])
batsman=pd.read_csv("batsman_runs_ipl.csv")
ipl=pd.read_csv("ipl-matches.csv")
print(ipl.to_string())          #print whole dataframe

#value_counts
print(students.value_counts())      #count value in row wise
#which player find most award in final and qualifire
bo=ipl[~ipl["MatchNumber"].str.isdigit()]                #filter all qualifire matches
print(bo["Player_of_Match"].value_counts())
#toss desigion plot
print(ipl["TossDecision"].value_counts())
#how many matches each team has played
print(ipl["Team1"].value_counts()+ipl["Team2"].value_counts())


#sort_values
print(movies.to_string())
print(ipl.to_string())

#sort the dataframe on the basic of stadium name wise
ans=ipl["Venue"].sort_values()
print(ans.value_counts())

#sort df movies name wise
print(movies["title_x"].sort_values())
print(movies.sort_values("title_x",ascending=False))

#sort dataframe in multiple column
#every year desioned movie in alphabetical order
print(movies.sort_values(["year_of_release","title_x"]))

#rank
print(batsman)
x=batsman["batsman_run"].rank(ascending=False)
batsman["batsman_rank"]=x
print(batsman.sort_values("batsman_rank"))
#batsman["ranking"]=x

#sort_index
print(students.sort_index(ascending=False))
print(ipl.sort_index(ascending=False))          #sorting with index wise

#set index      not change in original dataframe
print(students.set_index("name",inplace=True))
print(movies.set_index("title_x"))
print(students)

#reset index
#print(students.reset_index())
print(students)


#change index column
students.reset_index(inplace=True)
students.set_index("cgpa",inplace=True)
print(students)

#rename
students.reset_index(inplace=True)
students.rename(columns={"cgpa":"percentage"},inplace=True)         #rename of column
print(students)
print(students.rename(index={1:"about baby",4:'about salini'}))     #rename of rows

#unique
num=pd.Series([1,4,5,2,8,4,5,5,4,5,2,0,1,3,1])
print(num.unique())
print(ipl.to_string())
print(ipl["City"].unique())     #fatch all unique value in a particulor column

#nunique
print(ipl["City"].nunique())            #return number of unique keys

#isnull         missing value are present or not
print(students.isnull())
#notnull
print(students.notnull())

#dropna
students.dropna(how="all",inplace=True)
students["name"].dropna(how="any",inplace=True)       #remove all missing values
print(students)

print(ipl.to_string())
ipl.dropna(how="all",inplace=True)
ipl.dropna(how="any",inplace=True)
print(ipl.to_string())

#multiple column
print(ipl.to_string())
ipl.dropna(how="any",subset=["SuperOver","TossDecision"],inplace=True)
print(ipl.to_string())

