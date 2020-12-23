import os
import time
from iot.client import IoTClient

DISTRIBUTION_NAME = 'iot'
DEFAULT_URL = 'http://rest-api-0:8008'

def _get_keyfile(customerName):
    return '/project/dapp/iot/{}.priv'.format(customerName)

def _get_pubkeyfile(customerName):
    return '/project/dapp/iot/{}.pub'.format(customerName)

def store_sensor_data(data):
    key_file = _get_keyfile(DISTRIBUTION_NAME)
    iot_cli = IoTClient(baseUrl=DEFAULT_URL, keyFile=key_file)
    response = iot_cli.store_sensor_data(str(data))
    print("Response: {}".format(response))

def get_sensor_data():
    key_file = _get_keyfile(DISTRIBUTION_NAME)
    iot_cli = IoTClient(baseUrl=DEFAULT_URL, keyFile=key_file)
    data = iot_cli.get_sensor_data()

    if data is not None:
        print("\n{} have a state = {}\n".format(DISTRIBUTION_NAME, data.decode()))
    else:
        raise Exception("state not found: {}".format(DISTRIBUTION_NAME))

def get_sensor_history():
    key_file = _get_keyfile(DISTRIBUTION_NAME)
    iot_cli = IoTClient(baseUrl=DEFAULT_URL, keyFile=key_file)
    data = iot_cli.get_sensor_history()

    if data is not None:
        for i in data:
            try:
                print(i.decode())
            except:
                pass
    else:
        raise Exception("history not found: {}".format(client))


def main():
    op = "-1"
    while op != "4":
        print("\n1 - store sensor data\n2 - get sensor data\n3 - get sensor history\n4 - exit\n")
        op = input("Operation: ")
        if op == "1":
            data = input("Data to insert: ")
            store_sensor_data(data)
        elif op == "2":
            get_sensor_data()
        elif op == "3":
            get_sensor_history()