import boto3
import os
import sys
import random
client = boto3.client('sts')
#the following line is to just give different role session name, just to verify the role is being refreshed
sessionname = "test"+str(random.randint(1, 100))

creds = client.assume_role(RoleArn='arn:aws:iam::1234567890:role/role-name', RoleSessionName=sessionname)
creds = dict(creds)
access_key=creds['Credentials']['AccessKeyId']
secret_key=creds['Credentials']['SecretAccessKey']
session_token=creds['Credentials']['SessionToken']
#print access_key
#print secret_key
#print session_token

with open('/home/ec2-user/.aws/credentials','w') as f:
    f.write("[default]")
    f.write("\n")
    f.write(''.join(("aws_access_key_id = ",access_key)))
    f.write("\n")
    f.write(''.join(("aws_secret_access_key = ",secret_key)))
    f.write("\n")
    f.write(''.join(('aws_session_token = ',session_token)))

