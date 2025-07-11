# Import modules for BLE and Async functions

from bleak import BleakScanner
import asyncio



print('Searching for BLE devices...')
async def main():

    devices = await BleakScanner.discover()
    for device in devices:
        print(device)
    
    # Handle no devices found
    if devices == []:
        print('No devices found, please check your Pinecil is powered on, then try again.')

asyncio.run(main())
