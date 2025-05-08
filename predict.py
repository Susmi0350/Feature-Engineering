import joblib
model = joblib.load('customer_segments.pkl')
def predict_customer(customer_id):
    # Get features from store
    features = session.sql(f"""
        SELECT TOTAL_ORDERS, AVG_SPEND 
        FROM CUSTOMER_FEATURES 
        WHERE CUSTOMER_ID = {customer_id}
    """).to_pandas()
    return model.predict(features)[0]
print(predict_customer(00000)) #an example  
