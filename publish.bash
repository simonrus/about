#!/bin/bash
echo "https://pawel.krupa.net.pl/2018/07/automate-your-grammar-checks/"
git status --porcelain | awk 'match($2, ".md"){print $2}' | xargs -r mdspell --ignore-acronyms --en-us --report
python3 notes/publish.py
