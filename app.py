import pandas as pd
import boto3

bucket = 'irl-ml-dataset'
file_name = 'dataset/Churn_Modelling.csv'
s3 = boto3.client('s3')

obj = s3.get_object(Bucket=bucket, Key=file_name)

df = pd.read_csv(obj['Body'])
print(df.head())