import re

if __name__ == '__main__':
    pattern=re.compile(r'#[0-9A-Fa-f]{3,6}(?!\s{)')
    n = int(input())
    for i in range(n):
        line=str(input())
        item=pattern.findall(line)
        if item:
            print(item[0])
