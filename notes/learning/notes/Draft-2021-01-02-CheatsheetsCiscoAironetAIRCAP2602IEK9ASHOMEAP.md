---
title: Draft-2021-01-02-CheatsheetsCiscoAironetAIRCAP2602IEK9ASHOMEAP
created: '2021-01-01T11:23:21.643Z'
modified: '2021-01-01T11:27:39.698Z'
---

# Draft-2021-01-02-Cheatsheets_Cisco_Aironet_AIR_CAP2602I_E_K9_AS_HOMEAP

---
layout: post
title: "Cheat sheets: configure Cisco Aironet AIR-CAP2602I-E-K9 as home access point"
author: "Sergei Semenov"
categories: cheatsheets
image: 2021-01-02-cap2602i.jpg
---
# Introduction

Goal: set Autonomous AP in AIR-CAP2602I-E-K9

# Required tools

1. Cisco Aironet AIR-CAP2602I-E-K9 Dual-Band 802.11n Wireless Access Point

# 
```
docker image ls
docker image rm
docker container ls
docker container rm <HASH>
```

# normal mode 
```
#echo can be -t option ...
docker run --name <name> 
docker stop <name>
docker rm <name>
```

# Problems ??
```
docker ps -a
docker exec -it <name> /bin/bash
```


