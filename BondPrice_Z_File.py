def getBondPrice_Z(face, couponRate, times, yc):

    p = [(1+y)**(-t) for y, t in zip(yc, times)]
    bondPrice= (sum(p)*couponRate+p[len(p)-1])*face
    return(bondPrice)

yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = .04

getBondPrice_Z(face,couponRate,times,yc)

