import json
from http.client import responses
'''
for this task I have connect aws cli first 
for that i have created IAM user and create a access key
by using that access i am performing below operation
'''
import boto3

class Awsutilities:
#create client that refer everywhere in the class
    def __init__(self):
        self.s3=self.get_connection("s3")
        # self.ec2=self.get_connection("ec2")
#create client that call services
    def get_connection(self,service):
        return boto3.client(service) # creating a client for S3 so that it can call APIs
#show list of bucket that has been already created
    def show_bucket(self):
        try:
            response = self.s3.list_buckets()
        # write buckets name in file
            with open("bucketlist.txt", "w+") as files:
                for bucket in response["Buckets"]:
                    bucket_name=bucket["Name"]
                 #print on CMD
                    print(bucket_name)
                    files.write(bucket_name+"\n")
        except Exception as e:
            print("error occurd",e)
#create a bucket from scrach
    def create_bucket(self,bucketname):
        try:
            response = self.s3.create_bucket(
                Bucket=bucketname,
                CreateBucketConfiguration={
                    'LocationConstraint': 'us-west-2',
                }
            )
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                print("Bucket created successfully")
            else:
                print("Error occured while creating the bucket")

        except:
              pass
#upload file in existing bucket
    def upload_file_bucket(self):
        self.s3.upload_file('output_data.json', 'akshaykibucket201', 'heloo')



a1 = Awsutilities()
a1.create_bucket("akshaykibucket201")
a1.upload_file_bucket()
a1.show_bucket()


