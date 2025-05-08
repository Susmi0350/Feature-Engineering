from snowflake.ml.feature_store import FeatureStore
from snowflake.ml.feature_store import Entity
fs = FeatureStore(session)
customer_entity = Entity(name="CUSTOMER", join_keys=["CUSTOMER_ID"])
fs.register_entity(customer_entity)
feature_view = fs.create_feature_view(
    name="CUSTOMER_FEATURES_V1",
    entities=[customer_entity],
    feature_df=session.table("CUSTOMER_FEATURES")
)
fs.materialize(feature_view)
