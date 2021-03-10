#!/bin/bash
wget -r -nv --spider https://simonrus.github.io/about/ 2>&1 | egrep -A 1 '(^---response end---$|^--[0-9]{4}-[0-9]{2}-[0-9]{2}|^[0-9]{4}-[0-9]{2}-[0-9]{2} ERROR|^Referer:|^Remote file does not)'
