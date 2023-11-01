import boto3
import json
import requests



access_key = 'access_key'
secret_key = 'secret_key'
region= 'region'
sqs_url ='sqs_url'
api_url = 'api_url'


sqs = boto3.client('sqs',region_name=region,aws_access_key_id=access_key,aws_secret_access_key=secret_key)

response = requests.get(api_url)
data = response.text

data = json.loads(data)
#print(data)
#for _ in range(10):
    
bitcoin_id = None
bitcoin_price = None
ripple_id = None
ripple_price = None
ethereum_id = None
ethereum_price = None

for element in data.get("body", []):
    currency_id = element.get('id','').lower()
        
    if currency_id == "bitcoin":
        bitcoin_id = element['id']
        bitcoin_price = element.get("sparkline_in_7d",{}).get("price",[])[0]
        print("Bitcoin ID:", bitcoin_id)
        print("Bitcoin Price:", bitcoin_price)
        sqs.send_message(QueueUrl=sqs_url,MessageBody=f"bitcoin_id:{bitcoin_id},price:{bitcoin_price}")
        #sqs.send_message(QueueUrl=sqs_url,MessageBody=f"{bitcoin_price}")
        
        
                    
    if currency_id == "ripple":
        ripple_id = element['id']
        ripple_price = element.get("sparkline_in_7d",{}).get("price",[])[0]
        print("Ripple ID:", ripple_id)
        print("Ripple Price:", ripple_price)
        sqs.send_message(QueueUrl=sqs_url,MessageBody=f"ripple_id:{ripple_id},price:{ripple_price}")
        #sqs.send_message(QueueUrl=sqs_url,MessageBody=f"{ripple_price}")
                    
    if currency_id == "ethereum":
        ethereum_id = element['id']
        ethereum_price = element.get("sparkline_in_7d",{}).get("price",[])[0]
        print("Ethereum ID:", ethereum_id)
        print("Ethereum Price:", ethereum_price)
        sqs.send_message(QueueUrl=sqs_url,MessageBody=f"ethereum_id:{ethereum_id},price:{ethereum_price}")
        #sqs.send_message(QueueUrl=sqs_url,MessageBody=f"{ethereum_price}")
        


#-----------Old Approach--------------------------
'''
target_currencies = ['bitcoin','ethereum','ripple']
for i in range(10):
    for element in json_data["body"]:
        currency_id = element['id'].lower()
    if currency_id in target_currencies:
        currency_name = element['name']
        currency_price = element['sparkline_in_7d']['price'][0]
        print(f"{currency_name} id is :{currency_id} and {currency_name} price is:{currency_price}")
    else:
        print("Invalid element in object:",element)
'''
#--------Ends here----
