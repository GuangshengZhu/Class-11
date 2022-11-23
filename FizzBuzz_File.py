def FizzBuzz(start, finish):
    outlist = []
    i=start
    while i<=finish:
        if i%3==0 and i%5 !=0:
            outlist.append('fizz')
        elif i%5==0 and i%3 !=0:
            outlist.append('buzz')
        elif i%3==0 and i%5==0:
            outlist.append('fizzbuzz')
        else:outlist.append(i)
        i+=1

    return(outlist)

start=40
finish=45

FizzBuzz(start,finish)