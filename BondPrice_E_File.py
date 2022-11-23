

def getBondPrice_E(face, couponRate, m, yc):
    l=[]
    for count,y in enumerate(yc):
        pv=(1+y)**-(count+1)
        l.append(pv)
    bondPrice = (sum(l)*couponRate+l[len(l)-1])*face
    return(bondPrice)

yc = [.010,.015,.020,.025,.030]
face = 2000000
couponRate = .04
m = 5

getBondPrice_E(face,couponRate,m,yc)
