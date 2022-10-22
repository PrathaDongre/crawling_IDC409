#pandas and SQL
#structured query language
#using sqldf, used SQLite under the convers, and it can treate pandas dataframes like they were tables
import pandas as pd
from pandasql import sqldf
from pandasql import load_births
import os

births = load_births()
#print(sqldf('SELECT * FROM births where births > 250000 limit 5;', locals()))

#multiple line query can bedone as below:
q = '''
select
    date(date) as DOB,
    sum(births) as 'Total Births'
    from
        births
    group by
        date
        limit 10;

'''

#print(sqldf(q, locals()))
#can even use global instead of locals()

def pysqldf(q):
    #makes calling of pysqldf a bit simpler:
    return sqldf(q,globals())

print(os.getcwd())
filepath = './Data/'

dfcustomer = pd.read_csv(filepath + 'DimCustomer.csv')
