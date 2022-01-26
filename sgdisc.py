#! /usr/bin/env python3

from datetime import datetime
import boto3
import json

client = boto3.client('ec2')

def date_time_convertor(inputs):
    if isinstance(inputs, datetime):
        return inputs.__str__()

response = client.describe_security_groups(
    GroupIds=[
        '',]
)

#print(response)
print(json.dumps(response, default=date_time_convertor, indent=4))
