from influxdb import InfluxDBClient
import datetime


def connect_to_client(db_hostname="localhost"):
    return InfluxDBClient(host=db_hostname, port=8086)


def add_datum(measurement_name, datum, user_specified_tags={}, db_hostname="localhost"):
    """
    :param measurement_name: Name of the data table
    :param datum: Data value to be added to data table
    :param user_specified_tags: tags to track
    :param db_hostname: hostname of the database
    :return:
    """
    try:
        client = connect_to_client(db_hostname)
        json_body = [
            {
                "measurement": measurement_name,
                "tags": user_specified_tags,
                "time": datetime.datetime.now(),
                "fields": {
                    "value": datum
                }
            }
        ]
        client.write_points(json_body, database='aws_metrics')
        return "Data successfully written"
    except ConnectionError:
        return 'There was a connection error'
    finally:
        client.close()


def get_data(measurement_name):
    """
    :param measurement_name: Name of the data table
    :return:
    """
    client = connect_to_client()
    return client.query('select * from {}'.format(measurement_name), database='aws_metrics')


def main():
    client = connect_to_client()
    client.create_database(dbname='aws_metrics')
    client.create_retention_policy(name="aws_policy", duration='10d', replication='3', database='aws_metrics')
    # add_datum("some_bs", 10)
    # add_datum("some_bs", 11)
    # add_datum("some_bs", 12)
    print(get_data("aws_instance_total"))


if __name__ == '__main__':
    main()
