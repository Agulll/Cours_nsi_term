def search(s,t):
    n = len(t)//2
    print(n,t)
    if n == 1:
        if t[n]==s:
            print("yes")
        else:
            print("nope")
            return(t)
    if t[n]>s :
        search(s,t[:n])
    if t[n]<s :
        search(s,t[n:])
search(9,[1,2,3,4,5,6,7,8,9])
