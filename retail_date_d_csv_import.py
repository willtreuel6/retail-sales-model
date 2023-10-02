import pandas as pd
from sqlalchemy import create_engine
from datetime import date








# Credentials to database connection
hostname="localhost"
dbname="mydb"
uname="root"
pwd="Wht1257891011"

# Create dataframe
df = pd.read_csv(r"C:\Users\willt\Documents\Datasets\Retail-Transaction-Dimension-Modeling\retail_date_d.csv")



# Transformations

# Add day of week column

df['day_of_week'] = pd.to_datetime(df['date'])
df['day_of_week'] = df['day_of_week'].dt.day_name()



# Add Calendar Month

df['calendar_month'] = pd.to_datetime(df['date'])
df['calendar_month'] = df['calendar_month'].dt.month_name()

# Add calendar quarter

df['calendar_quarter'] = pd.to_datetime(df['date'])
df['calendar_quarter'] = df['calendar_quarter'].dt.quarter

# Add Calendar Year

df['calendar_year'] = pd.to_datetime(df['date'])
df['calendar_year'] = df['calendar_year'].dt.year

# Is Holiday?

#pip install holidays
import holidays
us_holidays = holidays.US()

date_column = df['date']

def new_date(x):
    return x.replace("/","-")

new_date_column = date_column.apply(new_date)

df['is_holiday'] = new_date_column

def is_holiday(x):
    if x in us_holidays:
        return "Y"
    else:
        return "N"

is_holiday_column = new_date_column.apply(is_holiday)

df['is_holiday'] = is_holiday_column

################Import to SQL################

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table                                   
df.to_sql('retail_date_d', engine, index=False, if_exists='append')

















# Create SQLAlchemy engine to connect to MySQL Database
#engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
#				.format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table                                   
#df.to_sql('retail_date_d', engine, index=False, if_exists='append')

