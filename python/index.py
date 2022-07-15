import json
import boto3

def lambda_handler(event, context):
    iam = boto3.client('iam')
    my_managed_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "logs:CreateLogGroup",
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "dynamodb:DeleteItem",
                    "dynamodb:GetItem",
                    "dynamodb:PutItem",
                    "dynamodb:Scan",
                    "dynamodb:UpdateItem"
                ],
                "Resource": "*"
            }
        ]
    }
    response = iam.create_policy(
            PolicyName='brotatoPolicy',
            PolicyDocument=json.dumps(my_managed_policy)
        )

   
    message = 'Hello {} !'.format(event['key1'])
    return {
       'message' : message
    }