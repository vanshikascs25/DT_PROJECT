def add_sub(l): #addition and substration
    sum=0
    sub=0
    for i in range(len(l)):
        if l[i-1]=='+' or i==0 :
            sum+=l[i]
        elif l[i-1]=='-':
            sub+=l[i]
    return (sum-sub) # as - and +   have precedence so to ans is sum(term)-sub(term)
def mult(a,b): #multiplication 
    if b!=0:
        mu=a*b
        return mu 
def div(a,b): #divison
    if b!=0:
        di=a/b
        return di
    else:
        print("!!!!!!!!!ERRORERRORERRORERROR!!!!!!!!!!\nZERO CANNOT BE DENOMINATOR")#we know enominator cannot be zero 
def ins(i,n):#to insert output of any operator on two number on index of index - 1
    l[i-1]=n# i put the output in list
    l.pop(i) #i delete two number which output i get
    l.pop(i)
l=[]
print("CALCULATOR:------>")
exp=input()
la=l[::]
n=''
for i in range(len(exp)):# it help to separate the operator and number 
    if exp[i].isdigit():#number
        n=n+exp[i]
    else:#operator
        l.append(int(n))
        l.append(exp[i])
        n=''
if n!='':#to take last number
    l.append(int(n))
if '/' in l:#highest precedence i write it first
    i=0
    while i<len(l):
        if l[i]=='/':
            ins(i,div(l[i-1],l[i+1]))#call the div func to get output
            i-=1
        i+=1
if '*' in l:#multiplication
    i=0
    while i<len(l):
        if l[i]=='*':
            ins(i,mult(l[i-1],l[i+1]))   #call the multi func to get output
            i-=1
        i+=1
if '+' in l or '-' in l:  #add and sub output
    ans=add_sub(l)
    print("\n",ans) # if list have + or - then ans get by fun add_sub 
if '+' not in la or '-' not in la :# if list not contain + or-
    if '*' in l and '/' in l:
        print("\n\n\n",l[0])#ans is l[0]


