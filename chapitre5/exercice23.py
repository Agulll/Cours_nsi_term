def mintab(u):
    n = len(u)
    if n == 1:
        return(u)
    else:
        m = mintab(u[0:n-1])
        if u[n-1]< m:
            return(u[n-1])
        else:
            return(m)

mintab([7,8,5,3,1,4,9,6,45,8])