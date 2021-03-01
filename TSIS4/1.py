import sys
import re

def rex(text):
    for i in re.findall(r'#[0-9A-Fa-f]{3,6}(?!\s{)',text):
        print(i)

if __name__ == '__main__':
    text=str(sys.stdin.read())
    rex(text)
