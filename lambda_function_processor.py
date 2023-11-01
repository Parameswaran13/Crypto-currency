import boto3
import json
from datetime import datetime


# Specify the AWS region and your SQS queue URL
access_key = 'access_key'
secret_key = 'secret_key'
region= 'region'
sqs_url ='sqs_url'

# Initialize a Boto3 SQS client
sqs = boto3.client('sqs', region_name=region,aws_access_key_id=access_key,aws_secret_access_key=secret_key)
dynamodb=boto3.client('dynamodb',region_name=region)
dynamodb_table= "Coingeko"

def lambda_handler(event, context):
    timestamp = str(datetime.now())
    
    # Receive messages from the queue (up to 10 messages at a time)
    response = sqs.receive_message(
        QueueUrl=sqs_url,
        AttributeNames=[
            'All'
        ],
        MaxNumberOfMessages=3,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=20
        )
    messages = response.get('Messages',[])
    #if messages:
    for message in messages:
        #message = messages[0]
        message_body = message['Body']
        
        attributes = message_body.split(',')
        _id = attributes[0].split(':')[1]
        _price = attributes[1].split(':')[1]
        
        dynamodb.put_item(
        TableName=dynamodb_table,
        Item={
            'id': {'S': _id},
            'price': {'N': _price},
            'timestamp':{'S':timestamp}
        }
    )
    
    
    return {
        'statusCode': 200,  
        'body': json.dumps({
            'processed_message':len(messages)})
         
     }
        
