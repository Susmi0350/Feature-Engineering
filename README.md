# Feature Engineering
Overview
This project demonstrates an end-to-end machine learning workflow for customer segmentation using the Snowflake Feature Store. It covers data extraction from Snowflake, feature engineering, storing features in a feature store, model training, and making predictions-all with detailed, beginner-friendly instructions.
The connect.py connects the server session with the environment we want to connect.
The feature_store.py create and materialize the feature view for further use.
The train_model.py trains KMeans clustering model.
The predict.py loads the trained model and predicts the cutomer's segment.
