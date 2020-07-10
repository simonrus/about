#!/bin/bash
echo "https://pawel.krupa.net.pl/2018/07/automate-your-grammar-checks/"
mdspell --ignore-acronyms --en-us --report notes/*/*/*.md
python3 notes/publish.py
