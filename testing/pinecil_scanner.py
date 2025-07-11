# Import BLE module and async functions module
from bleak import BleakScanner, BleakClient
import asyncio
import sys

# Scan all BLE devices and append devices with pinecil service UUID to found devices list
found_devices = []
async def scan_device(found_devices):

    pinecil_service_UUID = "['9eae1000-9d0d-48c5-aa55-33e27f9bc533']"
    devices = await BleakScanner.discover(5.0, return_adv=True)

    for device in devices:
        if str(devices[device][1].service_uuids) == pinecil_service_UUID:
            found_devices.append(device)

# Select which pinecil to connect to, automatic if 1 device, user choice if > 1 device, throw error if 0
def select_device(found_devices):

    if len(found_devices) == 1:
        print("Found 1 Pinecil: ", (found_devices[0]))
        return found_devices[0]
    
    elif len(found_devices) == 0:
        sys.exit('No pinecils found, please check that Bluetooth is enabled under "Advanced Settings" on your pinecil')
    
    else:
        while True:

            i = 1
            for device in found_devices:
                print("Device ", i, ": ", str(found_devices[device][0]))
                i = i+1

            choice = int(input(print("Please enter the number of the device you want to pair with")))
            if choice > len(found_devices):
                print('That number is out of range, please try again')
                continue
            else:
                return found_devices[(choice - 1)]

# Get users Pinecil
asyncio.run(scan_device(found_devices))
pinecil = select_device(found_devices)

# Open connection with Pinecil
async def connect_device(pinecil):

    # Characteristic UUIDs for the individual services required
    UUID_time_since_last_movement = "d85ef009-168e-4a71-aa55-33e27f9bc533"
    UUID_temperature = "d85ef001-168e-4a71-aa55-33e27f9bc533"

    async with BleakClient(pinecil) as client:

        # Fetch services
        services = client.services

        # Fetch data from characteristic UUID, then convert from little endian byte array to integer
        temperature_raw = await client.read_gatt_char(UUID_temperature)
        temperature = int.from_bytes(temperature_raw, byteorder='little', signed = False)

        time_since_last_movement_raw = await client.read_gatt_char(UUID_time_since_last_movement)
        time_since_last_movement = int.from_bytes(time_since_last_movement_raw, byteorder='little', signed = False)

        print(temperature)
        print(time_since_last_movement)


# Connect with pinecil
asyncio.run(connect_device(pinecil))

# TODO - connect with hackatime
