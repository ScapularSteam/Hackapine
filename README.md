# Hackapine

A bridge to enable Hack Clubbers to log time spent soldering with the PinecilV2 on Hackatime

## Progress

[x] Make a Python module to connect to and gather data from the PinecilV2.

[WIP] Detect changes in motion and trigger relevant Wakatime functions

[ ] Handle Wakatime functions and send heartbeat to Hackatime.

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
