x=input()
string=""
cnt=0
while cnt<len(x):
    if(x[cnt]=="G"):
        string+='G'
        cnt+=1
    else:
        if(x[cnt+1]==')'):
            string+='o'
            cnt+=2
        else:
            string+='al'
            cnt+=4
print(string)