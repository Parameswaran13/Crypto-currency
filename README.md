# Crypto-currency

The project centers around developing a REST API that fetches cryptocurrency coin data from the "Coin Geko" trading website After we hit the api link every 1 sec with the Python script and send the data to AWS SQS Once 10 records accumulate in the SQS queue, a separate AWS Lambda function named "Processor" is triggered to process this data. The processed data, containing information exclusively about bitcoin,ethereum,ripple coins price, then inserted into a Dynamodb no-sql database.

