# Import dependencies
import asyncio
from bleak import BleakClient, BleakScanner
import sys

# Create class for discovering and fetching data from Pinecils in BLE 
class Pinecil():

    # Declare internal variables and structures for holding device objects and UUIDs
    device = None
    _found_devices = []
    

    _pinecil_service_UUID = "['9eae1000-9d0d-48c5-aa55-33e27f9bc533']"
    _pinecil_UUID_temperature_service = "d85ef001-168e-4a71-aa55-33e27f9bc533"
    _pinecil_UUID_movement_service = "d85ef009-168e-4a71-aa55-33e27f9bc533"
        
    # Scans for all BLE devices, and append devices matching Pinecil Service UUID to found_devices[]
    async def scan(self):
        
        devices = await BleakScanner.discover(5.0, return_adv=True)

        for d in devices:
            if str(devices[d][1].service_uuids) == self._pinecil_service_UUID:
                self._found_devices.append(d)
        
    # Selects desired Pinecil from found_devices[] and establishes a BLE connection
    async def connect(self):

        # Select Pinecil from available options
        num_devices_found = len(self._found_devices)
        match num_devices_found:
            case 0:
                raise Exception("No Pinecils were found, try scanning again or check if Bluetooth is enabled under your Pinecil's Advanced Settings")
            case 1:
                print("One Pinecil found, MAC Address: ", self._found_devices[0])
                return self._found_devices[0]
            case _:
                print(num_devices_found, " Pinecils found:")
                i = 1
                for d in self._found_devices:
                    print("[", num_devices_found, "]: ", str(self._found_devices[d][0]))
                    i = i + 1
                
                while True:
                    choice = int(input(print("Please enter the number of the device you wish to connect to:")))
                    if choice > num_devices_found:
                        print("Number out of range, please try again or type 0 to cancel")
                        continue
                    elif choice == 0:
                        print("Canceling connection...")
                        raise Exception("User cancelled operation")
                    else:
                        self.device = self._found_devices[(choice-1)]
            
            # Establish connection with Pinecil
        try:
            print("Attempting to connect to Pinecil ", device)
            await BleakClient(self.device).connect()
            print("Successfully connected!")
        except:
            raise Exception("Failed to connect, please try again later")

    # Disconnects from connected Pinecil
    async def disconnect(self):

        try:
            await BleakClient(self.device).disconnect()
            print("Sucessfully disconnected from Pinecil", self.device)
        except:
            raise Exception("Failed to disconnect, please try again later")

    # Fetches little endian byte array from Temperature Service and converts to integer
    async def read_temperature():
        print('TODO')
    
    # Fetches little endian byte array from Motion Service and converts to integer
    async def read_motion():
        print('TODO')