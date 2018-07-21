import boto3


def get_number_of_instances():
    boto3.setup_default_session(region_name='us-east-1')
    ec2 = boto3.resource('ec2')

    total = 0
    for i in ec2.instances.all():
        total += 1
    return total


print(get_number_of_instances())
