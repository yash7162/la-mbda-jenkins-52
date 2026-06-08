import boto3
lambda_Client = boto3.client('lambda', region_name='us-east-1')
response =lambda_Client.create_function(
          Code={
                'S3Bucket': 'cloudeng-buck',
                'S3Key': 'lambda.zip', #how can i create or fetch this S3Key
          },
          Description='Process image objects from Amazon S3.',
          FunctionName="check",
          Handler='lambda.lambda_handler',
          Publish=True,
          Role='arn:aws:iam::987075663466:role/lambda-boto3',
          Runtime='python3.12'
          )
