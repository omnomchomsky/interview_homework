import urllib.request, json
import time
import influxdb_interface


def main():
    url = 'https://hsbxpv9829.execute-api.us-east-1.amazonaws.com/dev/ec2/instances/total'
    for i in range(1,100):
        time.sleep(10)
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            print(data['message']['value'])
            influxdb_interface.add_datum('aws_instance_total', data['message']['value'])
    print("done")
    return


if __name__ == '__main__':
    main()
