from sklearn.cluster import KMeans
import pandas as pd
import joblib
features = session.table("CUSTOMER_FEATURES").to_pandas()
model = KMeans(n_clusters=3)
model.fit(features[['TOTAL_ORDERS', 'AVG_SPEND']])
joblib.dump(model, 'customer_segments.pkl')
