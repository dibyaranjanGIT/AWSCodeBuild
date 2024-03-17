import boto3
import pandas as pd
from io import StringIO

def lambda_handler(event, context):
    # Specify your S3 bucket name and object key
    print(event)
    
    key = event['Records'][0]['s3']['object']['key']
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    
    print("Key:", key)
    print("Bucket Name:", bucket_name)
    


    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # Read the file from S3
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        data = response['Body'].read().decode('utf-8')
    except Exception as e:
        print(f"Error reading file from S3: {e}")
        return {
            'statusCode': 500,
            'body': str(e)
        }

    # Convert the data to a DataFrame
    try:
        df = pd.read_csv(StringIO(data))
    except Exception as e:
        print(f"Error creating DataFrame: {e}")
        return {
            'statusCode': 500,
            'body': str(e)
        }

    # Do further processing with the DataFrame if needed
    print("DataFrame loaded successfully!")
    print(df.head())

    # Return a response
    return {
        'statusCode': 200,
        'body': 'DataFrame loaded successfully!'
    }
    
    print("This is my local file")

    print("some new feature")