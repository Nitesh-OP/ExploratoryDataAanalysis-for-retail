Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... import pandas as pd
... import matplotlib.pyplot as plt 
... import seaborn as sns 
... import warnings
... warnings.filterwarnings("ignore")
... 
... 
... df = pd.read_csv("C:\\Users\\PNDMUME470\\Downloads\\SampleSuperstore.csv")
... 
... 
... df.head()
... 
... print("Rows: ",df.shape[0], "Columns: ",df.shape[1])
... 
... df.columns
... 
... df.info()
... 
... df.describe()
... 
... df.isnull().sum()
... 
... df.duplicated().sum()
... 
... # Droping Duplicates
... 
... df.drop_duplicates(inplace=True)
... 
... # Sanity Check
... 
... df.duplicated().sum()
... 
... df.nunique()
... 
... df["Country"].value_counts()
... 
... df["Region"].value_counts()
... 
# 3 regions

df["State"].nunique()

# 49 states

df['State'].value_counts()

df["City"].value_counts()

# 531 cities

df["Ship Mode"].value_counts()

# 3 modes of shippment

df["Category"].value_counts()

# 3 categories of products are available

# Dropping irrelevant features - Postal Code 

df.drop(columns="Postal Code",inplace=True)

df[["Sales","Quantity","Discount","Profit"]].plot.box(vert=False,grid=True)

df.corr()

# Evaluating the correaltion matrix 

sns.heatmap(df.corr(), annot=True)
plt.show()

plt.figure(figsize=(8,5))
sns.kdeplot(df["Sales"], color="red",label="Sales", shade=True,bw=25)
sns.kdeplot(df["Profit"], color="Blue",label="Profit", shade=True,bw=25)
plt.xlim([-100,1000])
plt.legend()

sns.pairplot(df,hue="Category")
plt.show()

sns.pairplot(df, hue="Region")
plt.show()

plt.figure(figsize=(8,8))
textprops={"fontsize":15}
plt.title("Category")
plt.pie(df["Category"].value_counts(),labels=df["Category"].value_counts().index,autopct="%1.1f%%",textprops=textprops)
plt.show()

plt.figure(figsize=(10,16))
df.groupby("Category")["Profit","Sales"].agg(["sum"]).plot.bar()
plt.ylabel("Profit")
plt.title("Category wise Profit & Sales")
plt.legend()
plt.show()

fig,axs=plt.subplots(nrows=2,ncols=2,figsize=(10,9));

sns.countplot(df["Category"], ax=axs[0][0])
sns.countplot(df["Segment"], ax=axs[0][1])
sns.countplot(df["Ship Mode"], ax=axs[1][0])
sns.countplot(df["Region"], ax=axs[1][1])

axs[0][0].set_title("Category",fontsize=15)
axs[0][1].set_title("Segment",fontsize=15)
axs[1][0].set_title("Ship Mode",fontsize=15)
axs[1][1].set_title("Region",fontsize=15)

fig,axs =plt.subplots(nrows=2,ncols=2,figsize=(10,10))
sns.distplot(df["Sales"],color="red", ax=axs[0][0])
sns.distplot(df["Profit"],color="green", ax=axs[0][1])
sns.distplot(df["Discount"],color="orange", ax=axs[1][0])
sns.distplot(df["Quantity"],color="blue", ax=axs[1][1])

axs[0][0].set_title("Sales Distribution", fontsize=15)
axs[0][1].set_title("Profit Distribution", fontsize=15)
axs[1][0].set_title("Discount Distribution", fontsize=15)
axs[1][1].set_title("Quantity Distribution", fontsize=15)

plt.show()

df.plot.scatter("Discount","Sales",color= "green", title="Discount vs Sales")
plt.show()

df.plot.scatter("Profit","Sales",color= "green", title="Profit vs Sales")
plt.show()

# There are negative values showing loss

# computing top categories in terms of Sales & Profit

profit = df.groupby("Category")["Profit"].sum().sort_values()
sale = df.groupby("Category")["Sales"].sum().sort_values(ascending=False) 

plt.style.use("seaborn")

sale.plot(kind='bar',figsize = (10,5), fontsize=15)
profit.plot(kind='bar',figsize = (10,5), fontsize=15, color="red")
plt.xlabel("Category", fontsize=15)
plt.ylabel("Total Profits/Sales", fontsize=15)
plt.title('Top Category Sales vs Profits', fontsize=15)
plt.show()

# Top Sub-Category in terms of Sales & Profit

profit = df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False)[:14]
sale = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False) 

plt.style.use("seaborn")

sale.plot(kind='bar',figsize = (10,5), fontsize=15)
profit.plot(kind='bar',figsize = (10,5), fontsize=15, color="red")
plt.xlabel("Sub-Category", fontsize=15)
plt.ylabel("Total Profits/Sales", fontsize=15)
plt.title('Top Category Sales vs Profits', fontsize=15)
plt.show()

low = df.groupby("State")["Profit"].sum().sort_values()
low1 = df.groupby("State")["Sales"].sum().sort_values()

plt.figure(figsize=(10,15))
plt.style.use("seaborn")

low1.plot(kind="barh",fontsize=14)
low.plot(kind="barh",fontsize=14, color="orange")
plt.show()

order = df.groupby(["State"])["Profit"].mean().sort_values()
plt.style.use("seaborn")

order.plot(kind='barh',figsize = (15,15),fontsize=20,color="orange")
plt.xlabel("Profit", fontsize=25)
plt.ylabel("States", fontsize=25)
plt.title('Average Sales Per State', fontsize=25)
plt.show()

quant = df.groupby("Category")["Quantity"].count().sort_values()

plt.style.use("seaborn")

quant.plot(kind='bar',figsize = (10,5), fontsize=15)
plt.xlabel("Categories", fontsize=15)
plt.ylabel("Total Quantities Sold", fontsize=15)
plt.title('Number of Quantities sold per Category', fontsize=15)
plt.show()

quant = df.groupby("Sub-Category")["Quantity"].count().sort_values()

plt.style.use("seaborn")

quant.plot(kind='bar',figsize = (10,5), fontsize=15)
plt.xlabel("Sub-Categories", fontsize=15)
plt.ylabel("Total Quantities Sold", fontsize=15)
plt.title('Number of Quantities sold per Sub-Category', fontsize=15)
plt.show()

quant1 = df.groupby("Sub-Category")["Sales"].count().sort_values()

plt.style.use("seaborn")

quant1.plot(kind='bar',figsize = (10,5), fontsize=15)
plt.xlabel("Sub-Categories", fontsize=15)
plt.ylabel("Total Sales", fontsize=15)
plt.title('', fontsize=15)
plt.show()

plt.figure(figsize=(6,6))
plt.title("Region")
plt.pie(df["Region"].value_counts(), labels=df["Region"].value_counts().index,autopct="%1.1f%%")
plt.show()

sns.catplot(x="Category",y="Profit",data=df,kind='bar',ci=None,col="Region")

sum1= df.groupby("State")["Quantity"].count().sort_values()
plt.style.use("seaborn")

sum1.plot(kind='barh',figsize = (15,15),fontsize=20,color="brown")
plt.xlabel("Total Quantities sold", fontsize=25)
plt.ylabel("States", fontsize=25)
plt.title('Number of Quantities sold Statewise', fontsize=25)
plt.show()

# Top cities with Quantities sold more than 100 

city = df.groupby("City")["Quantity"].count().sort_values(ascending=False)[:13]

plt.style.use("seaborn")

city.plot(kind='barh',figsize = (15,15),fontsize=23,color="violet")
plt.xlabel("Total Quantities sold", fontsize=25)
plt.ylabel("Cites", fontsize=25)
plt.title('Number of Quantities sold City wise', fontsize=25)
plt.show()

best = df.groupby("State")["Profit"].sum().sort_values(ascending=False).iloc[:9]

plt.style.use("seaborn")

best.plot(kind='barh',figsize = (15,15),fontsize=23,color="purple")
plt.xlabel("Total Profit", fontsize=25)
plt.ylabel("States", fontsize=25)
plt.title('Best Performing States', fontsize=25)
plt.show()

less = df.groupby("State")["Profit"].sum().sort_values().iloc[:10]

plt.style.use("seaborn")

less.plot(kind='barh',figsize = (15,15),fontsize=23,color="gray")
plt.xlabel("Total Loss", fontsize=25)
plt.ylabel("States", fontsize=25)
plt.title('Least Performing States', fontsize=25)
plt.show()

more = df.groupby("City")["Profit"].sum().sort_values(ascending=False).iloc[:6]

plt.style.use("seaborn")

more.plot(kind='barh',figsize = (15,15),fontsize=23,color="green")
plt.xlabel("Total Profit", fontsize=25)
plt.ylabel("Cites", fontsize=25)
plt.title('Best Performing Cities', fontsize=25)
plt.show()

least = df.groupby("City")["Profit"].sum().sort_values().iloc[:19]

plt.style.use("seaborn")

least.plot(kind='barh',figsize = (15,15),fontsize=23,color="blue")
plt.xlabel("Total Loss", fontsize=25)
plt.ylabel("Cites", fontsize=25)
plt.title('Least Performing Cities', fontsize=25)
plt.show()

df.groupby(["State","City","Profit"])["Sales"].sum().sort_values().iloc[:20]


# least performing States and their cities showing loss and sales per city

df.groupby("Ship Mode")["Sales"].sum().sort_values().plot.bar(color = "red", title = "Total Quantity Sold Per Category")
plt.show()

