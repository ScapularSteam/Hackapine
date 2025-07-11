# Import dependencies
import asyncio
import time
import datetime
from pinecil import Pinecil

# Generate file using formatted timestamp and .hackapine file extension
def get_filename():
    timestamp_raw = datetime.datetime.now()
    timestamp_pretty = timestamp_raw.strftime("%d-%m-%Y_%H-%M-%S")
    filename = timestamp_pretty + ".hackapine"
    return filename

# Adds a line to .hackapine file if motion1 and motion2 are not equal, aka the Pinecil has moved in the last 2 minutes
async def Main(filename):
    i = 0
    while True:
        print("Reading Motion1")
        motion1 = asyncio.run(my_Pinecil.read_motion())
        time.sleep(120)
        print("Reading Motion2")
        motion2 = asyncio.run(my_Pinecil.read_motion())

        if motion1 != motion2:
            print("Generating log entry for detected motion")
            with open(filename, "a") as file:
                file.write("TODO - Call log entry creation function here")
        else:
            with open(filename, "a") as file:
                file.write("No motion detected")

        # Limit number of iterations for testing purposes
        if i >= 10:
            break
        i = i+1

# Create a Pinecil object and select device
my_Pinecil = Pinecil()
asyncio.run(my_Pinecil.scan())
asyncio.run(my_Pinecil.select())

# Generate a new file and write MAC Address to file
filename = get_filename()
with open(filename, "a") as file:
    file.write("Begining testing")

asyncio.run(Main(filename))


