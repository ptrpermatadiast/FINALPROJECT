import snowflake.connector

# Snowflake connection details
sf_account = 'eb85158.ap-southeast-1.aws'
sf_user = 'ptrpermatadiast'
sf_password = 'Permata18'
sf_warehouse = 'COMPUTE_WH'
sf_database = 'KURBI'
sf_schema = 'PUBLIC'

# Connect to Snowflake
conn = snowflake.connector.connect(
    account=sf_account,
    user=sf_user,
    password=sf_password,
    warehouse=sf_warehouse,
    database=sf_database,
    schema=sf_schema
)

# Create a cursor
cursor = conn.cursor()

# List of table names to truncate
table_names = ['Putri_DailyGrosRev', 
                'Putri_MonthlyGrossRevPerProduct', 
                'Putri_MonthlyTotalPerProduct',
                'Putri_MonthlyTotalPerCat',
                'Putri_MonthlyTotalPerCountry']

# Truncate each table
for table_name in table_names:
    query = f"DROP TABLE IF EXISTS {table_name}"
    #query = f"TRUNCATE TABLE {table_name}"
    cursor.execute(query)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()