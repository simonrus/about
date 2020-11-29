---
title: Active-2020-11-29-Cheatsheets_Docker
created: '2020-11-29T09:35:28.799Z'
modified: '2020-11-29T09:47:15.691Z'
---

# Active-2020-11-29-Cheatsheets_Docker

---
layout: post
title: "Cheat sheets: Docker"
author: "Sergei Semenov"
categories: cheatsheets
image: Docker_Moby-logo.png
---

# Maintain images and containers
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


