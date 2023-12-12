# Crypto-currency

The project centers around developing a REST API that fetches cryptocurrency coin data from
the "Coin- Gecko" trading website After we hit the API link every 1 sec with the Python script 
and send the data to AWS SQS Once 10 records accumulate in the SQS queue, a separate 
AWS Lambda function named "Processor" is triggered to process this data. The processed 
data, containing information exclusively about bitcoin, Ethereum, ripple coins price, then 
inserted into a DynamoDB No-SQL database.


