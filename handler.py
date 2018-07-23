from __future__ import print_function

import json

import aws_interface
import influxdb_interface


def get_instance_totals_event(event, context):
    influxdb_hostname = event.get("influxdb_hostname")
    tag_name = event.get("tag_name")
    tag_value = event.get("tag_value")
    instance_totals = aws_interface.get_number_of_instances(tag_name, tag_value)
    influxdb_interface.add_datum("Number of EC2 instances", instance_totals, {tag_name: tag_value}, influxdb_hostname)
    body = {
        "message": {"Name":  "Total number of instances", "value": instance_totals},
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
