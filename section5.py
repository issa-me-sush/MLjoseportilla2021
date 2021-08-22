import pandas as pd
import numpy as np
#labeled indices - series
#help(pd.Series) -> gives complete documentation on it, rather look into pandas documentation on a browser
mylabels = ['USA',"Canada","Mexico"]
mydata  = [1776,1867,1821]
series1 = pd.Series(data = mydata, index = mylabels)#pd.Series(data,index/labels,datatype,name/main label)
print(series1)
print(series1[0])
print(series1['Canada'])
print(series1.index[0])
#series using dictionaries
dict1 = {'demonslayer':9.5,'AOT':9,'naruto':8.5,'bleach':9.5}
series2 = pd.Series(dict1)#same as series2 = pd.Series({'demonslayer':9.5,'AOT':9,'naruto':8.5,'bleach':9.5})
print(series2)
print(series2.keys())
#PAY ATTENTION
list1 = [1,2]
nplist1 = np.array(list1)
print(list1*2)
print(nplist1*2)#gets broadcasted - works in the same way with pandas
marks_sem1 = pd.Series({'sheldon':96,'Raj':94,'Howard':87})
marks_sem2 = pd.Series({'Raj':92,'sheldon':91,'Leonard':90})
print((marks_sem1+marks_sem2)/20)#prints the year's gpa
print((marks_sem1+marks_sem2)/2*10)#notice the difference
#if both the series dont have a specific label NaN (not a number) is printed
#to fill the NaN values
gpa = (marks_sem1.add(marks_sem2,fill_value = 50))/20
print(gpa)
#dataframes-most important part
np.random.seed(101);data1 = np.random.randint(0, 101,(4,3))
labels1= ['NY','CA','TX','GA']
columns1 = ['JAN','FEB','MARCH']
df1 = pd.DataFrame(data1,labels1,columns1)
print(df1)
print(df1.info())
dataset1 = pd.read_csv("tips.csv")
print(dataset1)
print(dataset1.info())
print(dataset1.columns)
print(dataset1.index)
print(dataset1.head(10))#default - first five
print(dataset1.tail())#default - last five
print(dataset1.describe())
print(dataset1.describe().transpose())#better readability - works just like a matrix transpose
print(dataset1['tip'])#accessing a column
print(dataset1[['tip','total_bill']])#accessing several columns with one command
#operations
dataset1['tip_percent'] = (dataset1['tip']/dataset1['total_bill'])*100#adding a column
print(dataset1)
print(dataset1['price_per_person'].head(5))
dataset1['price_per_person'] = np.round(dataset1['price_per_person'],1)
print(dataset1['price_per_person'].head(5))
dataset1 = dataset1.drop('price_per_person',1)# (column/row name,axis) -> row - axis = 0, column - axis = 1
#also remember drop returns the table with the specified column or row dropped, it doesnt update the dataframe
print(dataset1.head(5))#price_per_person column dropped/deleted
print(dataset1.shape)
print(dataset1.shape[0])#gives number of rows, whereas if given '1', then it gives number of columns
#working with rows
print(dataset1.index)
dataset1 = dataset1.set_index('Payment ID')# 'Payment ID' becomes the new index heading
print(dataset1.head())
print(dataset1.iloc[0])#to access data of specific rows 'iloc' is used to access based on integral indices, starting from 0
print(dataset1.loc['Sun4458'])#loc is used to access row data based on label name
#slicing
print(dataset1.iloc[12:14])# 12th and 13th row of data accessed
print(dataset1.loc[['Sun2959','Sun4458']])# specific labels accessed
#dropping rows
print(dataset1.head())
dataset1 = dataset1.drop('Sun2959',axis = 0)
print(dataset1.head())
#to drop using integer indices , we cant use drop(),just slicing can be used- and its not that flexible
dataset1 = dataset1.iloc[1:]
print(dataset1.head())
first_row = dataset1.iloc[0]
dataset1 = dataset1.append(first_row)
print(dataset1.head())
print(dataset1.tail())#the same row gets added in the end, duplication isnt denied
#conditional filtering
df = pd.read_csv('tips.csv')
print(df[df['total_bill']>40])
print(df[df['sex']=='Female'])#case sensitive
#multiple conditions , use '&' for and, '|' for or

print(df[(df['sex']=='Female') & (df['total_bill']>40)])
#for list of filters, use isin()
print(df[df['day'].isin(['Thur','Fri'])])#both thursday and friday data filtered

#useful methods
#apply()
def last_four(x):
    return str(x)[-4:]

df['lastfourcc']=df['CC Number'].apply(last_four)
print(df['lastfourcc'].head())
print(df['total_bill'].mean())
def price_rating(x):
    if x<15:
        return '$'
    elif x>15 and x<25:
        return '$$'
    else:
        return '$$$'

df['price_rating']= df['total_bill'].apply(price_rating)
print(df['price_rating'].head())

#using lambda expression instead of oen time functions
print(df['total_bill'].apply(lambda num:num*2))#can also be assigned or update
#multiple columns
def tip_quality(x,y):
    if y/x>0.15:
       return 'generous'
    else:
       return 'reasonable'
#using np.vectorize - suggested method
df['tip_quality'] = np.vectorize(tip_quality)(df['total_bill'],df['tip'])
print(df['tip_quality'].head(10))
#using lambda function
#df['tip_quality'] = df[['total_bill','tip']].apply(lambda df:tip_quality(df['total_bill'],df['tip']),axis=1)
#print(df['tip_quality'].head(10))
#look into timeit for run times - video #28
#statistical information and sorting
print(df.describe())
print(df.sort_values('tip'))#ascending by default
print(df.sort_values('tip',ascending = False))
print(df.sort_values(['tip','total_bill']))# multiple conditions,first one gets first priority
print(df['tip'].max())
print(df.iloc[df['tip'].idxmax()])#same concept for min
print(df.corr())#correlation co efficient ;range ->(1,1)
print(df['sex'].value_counts())
print(df['sex'].unique())
print(df['sex'].nunique())# same as len(print(df['sex'].unique()))
df['sex']=df['sex'].replace('Female','F')
print(df['sex'].head(10))
df['sex']=df['sex'].replace(['Female','Male'],['F','M'])
print(df['sex'].head(10))

#another method for multiple replacements
print(df['day'].unique())
map1 ={'Sun':'S','Sat':'Sa','Fri':'F','Thur':'T'}
print(df['day'].map(map1))#can be updated or assigned
#to check and remove duplication (in rows)
df = df.append(df.iloc[0])#appending a copy of the first row to the end
print(df.duplicated())
#to remove duplication
print(df.drop_duplicates())#must be updated, as it returns the data fram with the duplicates removed
print(df)
#between(v1,v2,inclusive = True or False)
print(df[df['total_bill'].between(35,40,inclusive = True)])
#nlargest/nsmallest
print(df['tip'].nlargest(2))
print(df.sort_values('tip',ascending = False).iloc[0:2])
print(df['total_bill'].nsmallest(2))
print(df.sort_values('total_bill').iloc[0:2])
#sampling
print(df.sample(2))
print(df.sample(frac = 0.1))#10% sampled
