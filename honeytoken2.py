import boto3

# Replace these with your actual AWS access key and secret key

aws_access_key_id = 'AKIAZ7TBUSG3OHWZIQPF'
aws_secret_access_key = 'j764D+P1ewcGb+Qptjh2acUQtF8/JrLiGrTAzXjI'


# Initialize a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

# Initialize the S3 client
s3 = session.client('s3')

# Specify the name of your bucket
#bucket_name = 'nikggtestbucket'

bucket_name = 'nikggtestbucket'

# List the contents of the bucket
response = s3.list_objects_v2(Bucket=bucket_name)

# Print the contents of the bucket
if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print("Bucket is empty or does not exist")
