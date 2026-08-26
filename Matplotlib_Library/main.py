import matplotlib.pyplot as plt 
#line chart
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend('LinePlot')
plt.title('Line-Plot')
plt.show()

# customizing a plot 
plt.plot(x,y,color='blue',linestyle='-.',marker='o')
plt.show()

# grid plot
plt.grid(True) 
plt.show() 

x=[1,2,3,4,5]
y=[2,4,6,8,10]
y1=[1,2,3,4,5]
plt.figure(figsize=(5,9))
plt.subplot(2,2,1)
plt.plot(x,y,color='blue',marker='o')
plt.title('plot1')

plt.subplot(2,2,2)
plt.plot(y,x,color='green',marker='o')
plt.title('plot2')

plt.subplot(2,2,3)
plt.plot(x,y1,color='red',marker='o')
plt.title('plot3')

plt.subplot(2,2,4)
plt.plot(y1,x,color='black',marker='o')
plt.title('plot4')

plt.show() 

# bar plot
categories=['apples','grapes','banana','orange']
quantity=[5,2,3,7]
plt.figure(figsize=(5,5))
plt.bar(categories,quantity,color='purple')
plt.xlabel('Products')
plt.ylabel('Quantity in kgs ')
plt.title('Product Sales')
plt.show()

# histogram 
data=[1,2,2,3,3,3,4,4,4,5,5,5,5,5]
plt.hist(data,bins=5,color='green',edgecolor='red')
plt.show() 

# scatter plot
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.scatter(x,y,color='blue',marker='x')
plt.show() 

# pie chart
labels=['A','B','C','D']
data=[30,20,40,10]
colors=['pink','green','blue','purple']
explode=(0.2,0,0,0)
plt.pie(data,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%')
plt.show()  

import pandas as pd
df=pd.read_csv("Matplotlib_Library/sales_data.csv")
print(df.info())
#print(df)
x=df['Product']
y=df['Quantity']
plt.xlabel('Products')
plt.ylabel('Quantity')
plt.bar(x,y,color='yellow')
plt.show()

total_Sales_df=df.groupby('Product')['Total_Sales'].sum()
print(total_Sales_df)
total_Sales_df.plot(kind='bar',color='yellow')
plt.xticks(rotation=45)
plt.show()
