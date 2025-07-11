import asyncio
import time
import datetime
from pinecil import Pinecil

def get_filename():
    timestamp_raw = datetime.datetime.now()
    timestamp_pretty = timestamp_raw.strftime("%d-%m-%Y_%H-%M-%S")
    filename = timestamp_pretty + ".hackapine"
    return filename

# Create a Pinecil object and select device
my_Pinecil = Pinecil()
asyncio.run(my_Pinecil.scan())
asyncio.run(my_Pinecil.select())

# Generate a new file
filename = get_filename()
file = open(filename, "a")

i = 0
while True:
    motion = asyncio.run(my_Pinecil.read_motion())
    time.sleep(5)
    newMotion = asyncio.run(my_Pinecil.read_motion())
    if motion != asyncio.run(my_Pinecil.read_motion()):
        print('Motion value has changed from ', motion , "to", newMotion)
    if i >= 10:
        break
    i = i+1

file.close()