## Sighthound

## ALPR
* https://www.sighthound.com/products/alpr/ & [manual](https://www.sighthound.com/docs/alpr/)
* Uses mongoDB backend?
* Node.js, Port 9000
* Login with registered email
* Docs on google drive
* Must allocate 4GB RAM
* Backend in C

Exported result:

```
{
  "lp": {
    "0": {
      "bestFrame": 0,
      "bestFrameScore": 0.999880611896515,
      "color": "",
      "colorScore": 0,
      "firstFrame": 0,
      "lastUpdate": 0,
      "lpScore": 0.999880611896515,
      "makeModel": "",
      "makeModelScore": 0,
      "region": "UK",
      "regionScore": 0.960166931152344,
      "scoreTotals": {},
      "string": "LR33TEE",
      "time": "1589256247.93"
    },
    "1": {
      "bestFrame": 4,
      "bestFrameScore": 0,
      "color": "red",
      "colorScore": 0.999740064144135,
      "firstFrame": 4,
      "lastUpdate": 4,
      "lpScore": 0,
      "makeModel": "",
      "makeModelScore": 0,
      "region": "",
      "regionScore": 0,
      "scoreTotals": {},
      "string": "",
      "time": "1589256247.93"
    },
    "2": {
      "bestFrame": 8,
      "bestFrameScore": 0,
      "color": "brown",
      "colorScore": 0.507356584072113,
      "firstFrame": 8,
      "lastUpdate": 8,
      "lpScore": 0,
      "makeModel": "",
      "makeModelScore": 0,
      "region": "",
      "regionScore": 0,
      "scoreTotals": {},
      "string": "",
      "time": "1589256247.93"
    }
  }
}```