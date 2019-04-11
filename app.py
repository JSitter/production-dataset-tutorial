import pandas as pd
import boto3
from pymongo import MongoClient
from datetime import datetime

client = MongoClient()

db = client['tutorial']
coll = db['articles']
doc = {
  "title": "an article title",
  "author": "Marco",
  "publication_date": datetime.utcnow()
}

doc_id = coll.insert_one(doc).inserted_id

for doc in coll.find():
  print(doc)

bucket = 'irl-ml-dataset'
file_name = 'dataset/Churn_Modelling.csv'
s3 = boto3.client('s3')

obj = s3.get_object(Bucket=bucket, Key=file_name)

df = pd.read_csv(obj['Body'])
print(df.head())

# enc = Encoder()
# enc.fit(X-a, y_a)
# bin = pickle.dumps(enc)
# enc = pickle.loads(bin)
# X_b_transormed = enc.transform(X_b, y_b)

# label_encoder_X_1 = LabelEncoder()
# X[:, 1 ]= label_encoder_X_1.fit_transform(X[:, 1])
# label_encoder_X_2 = LabelEncoder()
# X[:, 2] = label_encoder_X_2.fit_transform(X[: 2])
