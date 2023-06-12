"""### 1. Load the CSV File (using Python)."""
import pandas as pd
obj = pd.read_csv("../../FireBrigadeAndAmbulanceCallOuts.csv")


"""### 2. Output the total number of rows and columns."""
print("Output the total number of rows and columns.\n", obj.shape)


"""### 3. Output the number of non-null rows (by column)"""
print("\nOutput the number of non-null rows (by column)\n", obj.notna().sum())


"""### 4. Output the number of null values (by column)"""
print("\nOutput the number of null values (by column)\n",obj.isna().sum())


"""### 5. Output the number of null values for all columns"""
def calculateNullValues(dataFrame):
  sum, total_nulls = 0, 0
  for cols in dataFrame.columns:  # provide column names
    total_nulls = dataFrame.isna()[cols].sum()
    if total_nulls > 0: # check if null values exist
      sum += total_nulls # sum them up
  return sum

print("\nOutput the number of null values for all columns\n", calculateNullValues(obj)) # call to the function


"""### 6. Output the total number of call outs by Station Area."""
group1 = obj.groupby('Station Area')
print("\nOutput the total number of call outs by Station Area.\n",group1.size())

"""### 7. Output the total number of call outs by Date and Station Area."""
group2 = obj.groupby(['Date', 'Station Area'])
print("\nOutput the total number of call outs by Date and Station Area\n",group2.size())


"""### 8. Output the total number of call outs by Station Area and Date where the description is either Fire Car or Fire Alarm."""
group2 = obj[(obj['Description']=="Fire CAR") | (obj['Description']=="Fire ALARM")].groupby(['Date', 'Station Area'])
print("\nOutput the total number of call outs by Station Area and Date where the description is either Fire Car or Fire Alarm\n",group2.first())

"""### 9. Replace any instance of "," (in any column) with an empty string."""
print("\nReplace any instance of , (in any column) with an empty string\n")
print("Number of , are: ", len(obj[obj['MAV']==','])) # to check if , are present
obj['MAV'] = obj['MAV'].replace(',',"")
print("Number of , now: ", len(obj[obj['MAV']==','])) # to ensure there are no , left


"""### 10. Replace any instance of "-" (in any column) with an empty string."""
print("\nReplace any instance of - (in any column) with an empty string\n")
print("Number of - are: ", len(obj[obj['MAV']=='-'])) # to check if - are present
obj['MAV'] = obj['MAV'].replace('-',"")
print("Number of - now: ", len(obj[obj['MAV']=='-'])) # to ensure there are no - left


"""### 11. Drop rows for the columns (AH, MAV, CD) where at least one row value is NULL."""
print("\nDrop rows for the columns (AH, MAV, CD) where at least one row value is NULL.\n")
print("Rows and columns are: ",obj.shape)
obj = obj.dropna(subset=['MAV','CD','AH'])
print("Rows and columns now: ",obj.shape)


"""### 12. Drop any duplicate rows (except for the first occurrence)."""
print("\nDrop any duplicate rows (except for the first occurrence).\n")
print("Rows and columns are: ",obj.shape)
obj = obj.drop_duplicates(keep='first')
print("Rows and columns now: ",obj.shape) # 1 less row

"""### 13. Output the minimum time difference between TOC and ORD."""
print("\nOutput the minimum time difference between TOC and ORD.\n")
FMT = '%H:%M:%S'
column1 = obj['TOC']
column1 = pd.to_datetime(column1, format=FMT)
column2 = obj['ORD']
column2 = pd.to_datetime(column2, format=FMT)

difference = column2 - column1
print(min(difference))

"""### 14. Using the resulting data set, post implementing the previous cleansing steps, 
load the data into a table in SQL Server. (Note: you must create the physical table in SQL Server to 
complete this task. Use the same column names as the columns in the CSV File.)
"""
import pypyodbc
from datetime import datetime
# Creating a connection
connection = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-U2JVISP;Database=testdb')
cursor = connection.cursor()

# Insertion Process
obj = obj.rename(columns={'Station Area': 'StationArea'}) # renaming a spaced out column
obj = obj.fillna("") # filling NaN values with empty string

# Insert Dataframe into SQL Server:
for index,row in obj.iterrows(): 
    """ iterrows() is a generator but here it is serving us 
        a purpose of providing indices and rows """
    InsertCommand = ("Insert into Fire"
                 "(Date, StationArea, Description, TOC, ORD, MOB, IA, LS, AH, MAV, CD)"
                 "VALUES (?,?,?,?,?,?,?,?,?,?,?)")
    """ we have to type cast into date and time because 
        dates & times in dataframe are in string format.
        They produce error on insertion into SQL table. """
    date_column = datetime.strptime(row.Date, "%d/%m/%Y").date()
    toc_column = datetime.strptime(row.TOC, '%H:%M:%S').time()
    ord_column = datetime.strptime(row.ORD, '%H:%M:%S').time()
    if not row.IA == "":    # if cell doesn't have empty string
        ia_column = datetime.strptime(row.IA, '%H:%M:%S').time()
    if not row.MOB == "":   # if cell doesn't have empty string
        mob_column = datetime.strptime(row.MOB, '%H:%M:%S').time()
    ls_column = datetime.strptime(row.LS, '%H:%M:%S').time()
    if not row.AH == ",":   # if cell doesn't have ","
        ah_column = datetime.strptime(row.AH, '%H:%M:%S').time()
    mav_column = datetime.strptime(row.MAV, '%H:%M:%S').time()
    cd_column = datetime.strptime(row.CD, '%H:%M:%S').time()
    Values = [date_column,row.StationArea,row.Description,toc_column,ord_column,
              mob_column,ia_column,ls_column,ah_column,mav_column,cd_column]
    cursor.execute(InsertCommand, Values)

connection.commit() # save the data inside table
connection.close() # Closing connection in the end