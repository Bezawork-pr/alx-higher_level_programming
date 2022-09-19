#!/usr/bin/python3
import sys
f = open("more_text.txt", "r")
content = f.read()
sys.stderr.write(content)
exit(1)

