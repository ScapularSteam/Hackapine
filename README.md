# Hackapine

A bridge to enable Hack Clubbers to log time spent soldering with the PinecilV2 on Hackatime

## Progress

[x] Make a Python module to connect to and gather data from the PinecilV2.

[ ] Calculate activity based on differences in motion counter data from PinecilV2 over elapsed time.

[ ] Send heartbeat to Hackatime.

[ ] Send activity data to Hackatime and link to the desired project.

## Using the pinecil.py module

#### Install the dependencies:
```
pip install asyncio
pip install bleak
```

#### Import the module
```
from pinecil import Pinecil
```

*Note: the module pinecil.py should be placed in the same folder as the file you are importing it into*

#### Using the module

There are 4 methods: ```scan()```, ```select()```,```read_temperature()```, ```read_motion()```

These methods are asynchronous, so you will need to use the asyncio module to run these methods

#### Example:
```
from pinecil import Pinecil
import asyncio

myPinecil = Pinecil()
asyncio.run(myPinecil.scan())
