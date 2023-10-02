import pandas as pd
from sqlalchemy import create_engine








# Credentials to database connection
hostname="localhost"
dbname="mydb"
uname="root"
pwd="Wht1257891011"

# Create dataframe
df = pd.read_csv(r"C:\Users\willt\Documents\Datasets\Retail-Transaction-Dimension-Modeling\retail_cashier_d.csv")

print(df.head())

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table                                   
df.to_sql('retail_cashier_d', engine, index=False, if_exists='append')




