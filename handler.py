import json

import aws_interface

def hello(event, context):
    instances = aws_interface.get_number_of_instances()
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!"
                   " Number of ec2 instances are {}".format(instances),
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


hello("something","something_else")
