def getBondPrice(y, face, couponRate, m, ppy=1):
    pvsum=0
    couponRate = couponRate/ppy
    m=m*ppy
    pv=(1+y/ppy)
    for i in range(1,m+1):
        pvsum+= (1+y/ppy)**(-i)

    bondPrice = (pvsum*couponRate+(pv)**(-m))*face
    return(bondPrice)

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1
ppy = 2

getBondPrice(y,face,couponRate,m,ppy)
