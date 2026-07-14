import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy, pymysql
df=pd.read_csv("Causesofdeath.csv")
def ExportData():
    engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@localhost/deaths?charset=utf8')
    mycon = engine.connect()
    df.to_sql("Number_of_deaths",mycon, if_exists = "replace",index_label = None)
    print("Exported successfully")
        
def DisplayData():
    print("""
          1.Get Rows
          2.Get Columns
          """)
    ch1=int(input("enter your choice:"))
    if ch1==1:
        print(df)
    elif ch1==2:
        print(df.columns)
        
def AnalyzeData():
    df=pd.read_csv("Causesofdeath.csv")
    edf=df.groupby('Entity')
    ydf=df.groupby('Year')
    print(df)
    print("""
          1.Get data of Minimum Death
          2.Get data of Maximum Death
          3.Get data country wise
          4.Get data year wise
          5.Get data of max. accidents year wise
          6.Get data of min. accidents year wise
          """)
    ch1=int(input("enter your choice:"))
    if ch1==1:
        print(df.iloc[:,7:].min())
    elif ch1==2:
        print(df.iloc[:,7:].max())
    elif ch1==3:
        country =input("enter country:")
        print(edf.get_group(country))
    elif ch1==4:
        year=int(input("enter year:"))
        print(ydf.get_group(year))
    elif ch1==5:
        year=int(input("enter year:"))
        print(ydf.get_group(year).max())
    elif ch1==6:
        year=int(input("enter year:"))
        print(ydf.get_group(year).min())

def VisualiseData():
    df=pd.read_csv("Causesofdeath.csv")
    print("""
          1.Bar Graph for Deaths caused by Meningitis
          2.Scatter graph for Deaths caused by Alzheimer's disease and other dementias
          3.Histogram for Deaths caused by Cardiovascular diseases
          4.Pie graph for Deaths caused by Lower respiratory infections
          5.Pie graph country wise
          6.Pie graph year wise
          7.Horizontal bar graph for Deaths caused by Cardiovascular diseases
          8.Scatter graph for Deaths caused by Neoplasms
          """)
    ch2=int(input("enter your choice:"))
    if ch2==1:
        gdf=df.groupby("Year").get_group(2000).sort_values("Deaths-Meningitis")
        mdf = df.groupby("Entity")
        x = df.Year
        y=df.iloc[:,7]
        plt.bar(x,y)
        plt.xlabel("Year")
        plt.ylabel("Death Cases")
        plt.show()
        press = int(input("press any key : "))
    elif ch2==2:
        gdf=df.groupby("Year").get_group(1990).sort_values("Deaths-Alzheimer'sdisease")
        coundf = gdf.groupby("Entity").get_group("India")
        print(coundf)
        x= coundf.columns[6:]
        y = coundf.iloc[0 , 6:]
        plt.scatter(x,y)
        plt.xticks(rotation = "vertical")
        plt.show()
    elif ch2==3:
        gdf=df.groupby("Year").get_group(2005).sort_values("Deaths-Cardiovasculardiseases")
        coundf = df.groupby("Entity")
        x = df.Year
        y=df.iloc[:,7]
        plt.hist([x,y])
        plt.xlabel("Year")
        plt.ylabel("Death Cases")
        plt.show()
    elif ch2==4:
        gdf=df.groupby("Year").get_group(1990).sort_values("Deaths-Lowerrespiratoryinfections")
        coundf = df.groupby("Entity")
        x = df.iloc[0,4:20]
        l = list(x)
        plt.pie(x,labels=l)
        plt.title("DEATH CASES OF LOW RESPIRATORY INFECTIONS")
        plt.show()
    elif ch2==5:
        country= input("Enter Country:")
        countdf = df.groupby("Entity").get_group(country)
        x = df.iloc[0,4:14]
        l = list(x)
        plt.pie(x,labels=l)
        plt.title("DATA OF THAT COUNTRY WHICH YOU WANT TO SEE")
        plt.show()
    elif ch2==6:
        year= int(input("Enter year:"))
        countdf = df.groupby("Year").get_group(year)
        x = df.iloc[0,20:27]
        l = list(x)
        plt.pie(x,labels=l)
        plt.title("DATA OF THAT YEAR WHICH YOU WANT TO SEE")
        plt.show()
    elif ch2==7:
        x= df.Year
        y= df.iloc[:,16]
        plt.barh(x,y)
        plt.xlabel("Year")
        plt.ylabel("Deaths - Cardiovascular diseases")
        plt.title("HORIZONTAL BAR GRAPH")
        plt.show()
    elif ch2==8:
        deathdf = df.groupby("Year").get_group(2015).sort_values("Deaths-Neoplasms")
        country = input("Enter Country : ")
        edf = deathdf.groupby("Entity").get_group(country)
        print(edf)
        x= edf.columns[6:]
        y = edf.iloc[0 , 6:]
        plt.scatter(x,y)
        plt.xlabel("Deaths by Neoplasms")
        plt.ylabel("countries")
        plt.xticks(rotation = "vertical")
        plt.show()
        
def main_menu():
  ch=0
  print("                     ==============================")
  print("                             Main Menu")
  print("                     ==============================")
  while ch!=5:
    print("""
          1.Display data
          2.Analyze data
          3.Visualize data
          4.Export data
          5.Exit from main menu
          """)
    ch=int(input("Enter your choice:"))
    if ch==1:
        DisplayData()
    elif ch==2:
        AnalyzeData()
    elif ch==3:
        VisualiseData()
    elif ch==4:
        ExportData()
    elif ch==5:
        print("thank you")

        break
main_menu()

