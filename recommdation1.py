fp=open("u.item","r")
h1={}
for line in fp:
    line=line.replace("\n","")
    line=line.split("|")
    line[0]=line[0].replace(",","")
    line[0]=line[0].replace("  "," ")
    h1.setdefault(line[0], [])
    key=line[0]
    line=line[5:]
    for i in line:
        h1[key].append(i)
fp1=open("test101.csv","w")
l=[]
c=0
for key in h1:
    l=h1[key]
    li=str(l)
    li=li.replace(","," ")
    li=li.replace("'","")
    li=li.replace("[","")
    li=li.replace("]","")
    li=li.replace(" ",",")
    li=li.replace(",,",",")
    fp1.write(str(li)+'\n')
fp1.close()
c=0
fp=open("u.data","r")
wr=open("test102.csv","w")
wr.write("\n")
h={}
l=[]
test=[]
for i in range(0,19):
    test.append(int(0))
for line in fp:
    line=line.replace("\t"," ")
    line=line.replace("\n"," ")
    li=line.split()
    h.setdefault(li[0], [])
    h[li[0]].append(li[1])
for key in h:
    wr.write(key)
    wr.write(",")
    for t in range(0,19):
        test[t]=0
    for j in h[key]:
        k=0
        for i in h1[j]:
            t=int(i)
            if t==1:
                test[k]=test[k]+1
            k=k+1
    for i in test:
        wr.write(str(i))
        wr.write(",")
    wr.write("\n")
    c=c+1
wr.close()
fp=open("test102.csv","r")
fq=open("test103.csv","w")
for line in fp:
    line=line.replace("\n","")
    line=line.split(",")
    line=line[2:20]
    for i in line:
        fq.write(i)
        fq.write(",")
    fq.write("\n")
fq.close()
fp=open("test103.csv","r")
fq=open("test104.csv","w")
h={}
h[0]="Action"
h[1]="Adventure"
h[2]="Animation"
h[3]="Children's"
h[4]="Comedy"
h[5]="Crime"
h[6]="Documentary"
h[7]="Drama"
h[8]="Fantasy"
h[9]="Film-Noir"
h[10]="Horror"
h[11]="Musical"
h[12]="Mystery"
h[13]="Romance"
h[14]="Sci-Fi"
h[15]="Thriller"
h[16]="War"
h[17]="Western"
i=1
for line in fp:
    if i==1:
        i=i+1
        continue
    line=line.replace("\n","")
    line=line.split(",")
    line=line[:-1]
    for i in range(0,18):
        if int(line[i])>10:
            fq.write(h[i])
            fq.write(",")
    fq.write("\n")
fq.close()

