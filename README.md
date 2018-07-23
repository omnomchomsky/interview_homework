# Interview Homework


## Problem 1

### Scenario
Due to data requirements, developers need to spin up application and database instances in a special AWS account to be able to test their code.  In order to contain costs, the SRE team needs to keep track of how many instances are running at any given time to make sure that we do not cross certain cost thresholds.

### Requirement
Create a Lambda function that can be run on a regular schedule (Cloudwatch Events) that get the number of EC2 Instances running in an account that have a specific tag and put the results in an InfluxDB.

### Instructions
Fork this repo to your personal GitHub account.  After you have completed your function, email a link to your repository for review (an address will be provided to you).  For convenience. , an InfluxDB Docker compose file is included to spin up the InfluxDB

## What You Will Need
1.  A GitHub account
2.  AWS Account
3.  Docker

# My Solution:

-Learned about the serverless framework to help do AWS Lambda in a very iterable way. https://serverless.com/
- Got a simple serverless Hello World working
  -  Created AWS Keypair
  -  Witnessed creation of AWS Lambda from using serverless framework
  -  Tested URL returned from serverless to verify correctness
- Created an aws_interface file to seperate function domains
- Added simple logic using boto3 to count all ec2 instances
- Verified it works locally
- Updated IAM permissions for the role associated with the lambda
- Verified that lambda now properly returns number of servers
- Added filter logic to aws_interface
- Added tag logic to influxdb_interface

#To Do:
- Still need to test filtering adequately(does influx behave the way that I think it does?)
- Still need to figure out how to package venv together so AWS Lambda can use it.
- Still need to automate a CloudWatch event that can call

