def ins_decode(instruction):
    temp1=instruction.replace(',','%')
    temp2=temp1.replace('(','%')
    temp3=temp2.replace(')','%')
    temp4=temp3.replace(' ','%')
    temp5=temp4.split('%')
    while '' in temp5:
        temp5.remove('')
    return temp5
