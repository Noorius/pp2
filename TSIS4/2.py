import re

if __name__ == '__main__':
    s=str(input())
    pattern = re.compile(r"([a-zA-z0-9])\1+")
    m = re.findall(pattern,s)
    if m:
        print(m[0])
    else:
        print(-1)