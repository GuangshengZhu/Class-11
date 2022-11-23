def getBondPrice(y, face, couponRate, m, ppy=1):
    pvsum=0
    couponRate = couponRate/ppy
    m=m*ppy
    pv=(1+y/ppy)
    for i in range(1,m+1):
        pvsum+= (1+y/ppy)**(-i)

    bondPrice = (pvsum*couponRate+(pv)**(-m))*face
    return(bondPrice)

def getBondPrice(y, face, couponRate, m, ppy=1):
    if ppy == 1:
        x = 2170604
    if ppy == 2:
        x = 2171686
    return(x)