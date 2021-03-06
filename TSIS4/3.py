import re 

if __name__ == '__main__':
    m=re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]',input())
    #m=re.findall(r'[QWRTYPSDFGHJKLZXCVBNM]|[qwrtypsdfghjklzxcvbnm]([AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNM]|[qwrtypsdfghjklzxcvbnm]',input())
    if m:
        print("\n".join(m))
    else:
        print(-1)