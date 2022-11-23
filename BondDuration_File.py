
def getBondDuration(y, face, couponRate, m, ppy = 1):
    t = m*ppy
    pvcft=0
    pvcf=0
    couponRate = couponRate/ppy
    y = y/ppy
    for i in range(1,t+1):
        pv = (1+y)**(-i)

        if i<t:
            cf = face*couponRate
        else:
            cf = face*couponRate+face
        pvcf+= pv*cf
        pvcft+= (pv*cf*i)

    bondDuration = pvcft/pvcf

    return(bondDuration)