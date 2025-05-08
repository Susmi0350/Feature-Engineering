from snowflake.snowpark import Session
conn = {
    "account": "Susmitha_Guntuku",
    "user": "susmi",
    "password": "susmi123*",
    "warehouse": "ML_WH",
    "database": "CUSTOMER_DATA",
    "schema": "FEATURE_STORE"
}
session = Session.builder.configs(conn).create()
