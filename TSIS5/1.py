n=int(input())
poem=""

with open("read.txt","rt",encoding="utf8") as f:
    while True:
        line=f.readline()
        if n<0:
            break
        poem+=line
        n-=1
    
with open("write.txt","wt",encoding="utf8") as wf:
    print("\tУ себя", file=wf)
    wf.write(poem)
    print("\n\t\t\t\tВладимир Соловьев", file=wf, sep="", end="")

with open("write.txt","at", encoding="utf8") as af:
    af.write("\nUploaded by Nur")

flow=open("write.txt",'rt',encoding="utf8")
print(flow.read())
flow.close()