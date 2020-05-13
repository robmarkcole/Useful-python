## Sighthound

## ALPR
* https://www.sighthound.com/products/alpr/ & [manual](https://www.sighthound.com/docs/alpr/)
* Uses mongoDB backend?
* Browse containers with `docker exec -it sighthound-alpr_mongo_1 bash`
* Node.js, Port 9000
* Login with registered email
* Docs on google drive
* Must allocate 4GB RAM
* Backend in C
* Db `data` -> `frames` and `objects` collections. 

frames:
```
{ "_id" : ObjectId("5eba2061f57cd40007a7828c"), 
"analyticsId" : "61e46a9c13c2411896411d5284bd8782", 
"createdAt" : 1589256289893, 
"objects" : [ { "box" : { "x" : 417.807251, "y" : 305.074951, "width" : 249.13623, "height" : 64.6194 }, 

"objectId" : "c691b59412454086b57121e101b031a6" }, { "box" : { "x" : 145.974167, "y" : 2.350834, "width" : 790.251709, "height" : 613.433777 }, 

"objectId" : "92435336b6d642809052755023f35333" }, { "box" : { "x" : 805.638977, "y" : 1.227673, "width" : 68.630798, "height" : 34.151989 }, 

"objectId" : "d263b0053247434782e7a18426e195c2" } ], "sourceId" : "20cc218fda6ceb3919d3b7114ee79472", "startsAt" : 1589256247930, "timestamp" : 0 }
```

objects:
```
{ "_id" : ObjectId("5eba204414c87b5ac9b95a31"), 
"id" : "c691b59412454086b57121e101b031a6", 
"analyticsId" : "61e46a9c13c2411896411d5284bd8782", 
"attributes" : { 
"region" : "UK", 
"regionScore" : 0.960166931152344, 
"string" : "LR33TEE", 
"stringScore" : 0.999880611896515 }, 
"bestFrameTimestamp" : 0, 
"boxAtBestFrame" : { "height" : 64.6194, "width" : 249.13623, "x" : 417.807251, "y" : 305.074951 }, 
"createdAt" : 1589256260021, 
"detectionScore" : 0.957192301750183, 
"firstFrameTimestamp" : 0, 
"lastFrameTimestamp" : 0, 
"sourceId" : "20cc218fda6ceb3919d3b7114ee79472", 
"startsAt" : 1589256247930, 
"type" : "licenseplate", 
"updatedAt" : 1589256289882,
"links" : [ "92435336b6d642809052755023f35333" ] }

{ "_id" : ObjectId("5eba204414c87b5ac9b95a33"), "id" : "92435336b6d642809052755023f35333", "analyticsId" : "61e46a9c13c2411896411d5284bd8782", "attributes" : { "classes" : [ "car", "coupe", "hatchback" ], "color" : "red", "colorScore" : 0.999740064144135, "make" : "MINI", "makeScore" : 0.213310688734055, "model" : "Cooper", "modelScore" : 0.213310688734055 }, "bestFrameTimestamp" : 0, "boxAtBestFrame" : { "height" : 613.433777, "width" : 790.251709, "x" : 145.974167, "y" : 2.350834 }, "createdAt" : 1589256260086, "detectionScore" : 0.999394953250885, "firstFrameTimestamp" : 0, "lastFrameTimestamp" : 0, "sourceId" : "20cc218fda6ceb3919d3b7114ee79472", "startsAt" : 1589256247930, "type" : "car", "updatedAt" : 1589256289887, "links" : [ "c691b59412454086b57121e101b031a6" ] }

{ "_id" : ObjectId("5eba204414c87b5ac9b95a35"), "id" : "d263b0053247434782e7a18426e195c2", "analyticsId" : "61e46a9c13c2411896411d5284bd8782", "attributes" : { "classes" : [ "van" ], "color" : "brown", "colorScore" : 0.507356584072113, "make" : "Ford", "makeScore" : 0.0659083873033524, "model" : "E Series", "modelScore" : 0.0659083873033524 }, "bestFrameTimestamp" : 0, "boxAtBestFrame" : { "height" : 34.151989, "width" : 68.630798, "x" : 805.638977, "y" : 1.227673 }, "createdAt" : 1589256260101, "detectionScore" : 0.648538947105408, "firstFrameTimestamp" : 0, "lastFrameTimestamp" : 0, "sourceId" : "20cc218fda6ceb3919d3b7114ee79472", "startsAt" : 1589256247930, "type" : "car", "updatedAt" : 1589256289890 }
```