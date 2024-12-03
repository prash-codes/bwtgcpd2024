import snowflake.connector 

class SnowflakeConnector:
    def __init__(self, account, user, password, warehouse, database, schema, role):
        self.account = account
        self.user = user
        self.password = password
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.role = role
    
    def connect(self):
        snowflake.connection = snowflake.connector.connect(
            user = self.user,
            password = self.password,
            account = self.account,
            warehouse = self.warehouse,
            database = self.database,
            schema = self.schema,
            role = self.role
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()


account = "MGNKVYR-JF04384"
user = "PRASHANTY"
password = "Prashant$00"
database = "SNOWFLAKE_SAMPLE_DATA"
schema = "TPCH_SF10"
warehouse = "COMPUTE_WH"
role = "ACCOUNTADMIN"

sf_connector = SnowflakeConnector(
    account=account,
    user=user,
    password=password,
    database=database,
    schema=schema,
    warehouse=warehouse,
    role=role
)

sf_connector.connect()

query = "select * from SNOWFLAKE_SAMPLE_DATA.TPCH_SF10.SUPPLIER limit 10"
result = sf_connector.execute_query(query)

print(result)

sf_connector.close_connection()
