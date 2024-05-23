import boto3

# Assuming your credentials are set up correctly (environment variables, ~/.aws/credentials, etc.)
# You don't explicitly provide the keys in the code
s3 = boto3.client('s3')  # Create an S3 client
dynamodb = boto3.client('dynamodb')  # Create a DynamoDB client

# S3 Example: List buckets
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

# DynamoDB Example: Get an item
response = dynamodb.get_item(
    TableName='your-table-name',
    Key={
        'AKIA34UWIKTBZPNF7UYJ': {'S': 'JQ+vg7j3Kjt2oUtlGOWMj8zmcsJ7FBtlmFSzOo3D'}
    }
)
item = response.get('Item')
if item:
    print(item)
