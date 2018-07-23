import boto3


def get_number_of_instances(tag_key="", tag_value=""):
    """
    Given a set of tag_key names and values, return the number of ec2 instances that match
    :param tag_key: AWS Tag Name
    :param tag_value:  AWS Tag Value
    :return: Number of ec2 instances in the form of an integer
    """
    tag_filter=[{"".format(tag_key):"{}".format(tag_value)}]
    boto3.setup_default_session(region_name='us-east-1')
    ec2 = boto3.resource('ec2').filter(Filters=tag_filter)
    total = 0
    for i in ec2.instances.all():
        total += 1
    return total


def main():
    print(get_number_of_instances())


if __name__ == '__main__':
    main()