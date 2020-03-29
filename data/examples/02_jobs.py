"""
jobs.py

Show a simple example of how to define a custom job and pass it to the ZdmClient.

"""
import json
import time

from zdm import ZDMClient

device_id = '*** PUT YOU DEVICE ID HERE ***'
password = '*** PUT YOUR PASSWORD HERE ***'


def set_temp(zdmclient, args):
    print("Executing job set_temp. Received args: {}".format(args))
    # DO SOMETHING
    # return the result of the job ad JSON
    return json.dumps({"msg": "Temperature set correctly."})


# A dictionary of jobs where the key is the name of the job and value if the function to execute.
my_jobs = {
    "set_temp": set_temp,
}

device = ZDMClient(device_id=device_id, jobs=my_jobs)
device.set_password(password)
device.connect()

while True:
    time.sleep(3)