def addNumber(fNo,lNo):
    sumNo = fNo+lNo
    return sumNo
def mulNumber(no1,no2):
    res=no1*no2
    return res

print(addNumber(4,10))

no = addNumber(1,3);
res = mulNumber(no,3);
print(res)


#NOTE:
#As python is interpreted you need to specify function defination prior
#to function call else python interpreter will display NameError 'function name'
#is not defined
