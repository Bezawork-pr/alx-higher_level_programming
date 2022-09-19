#!/usr/bin/python3
f = open('text.txt', 'r')
content = f.read()
print(content, end = "")
f.close()
