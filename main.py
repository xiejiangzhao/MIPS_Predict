from Carry import carry_ins, init, get_pc, RegData,RomData,init_data
from Instruction_Translate import ins_decode
from Predict import OnebitPredict, UpdateOnebitPredict, get_acu, UpdateTwobitPredict, UpdateLocalPredict, \
    UpdateGlobalPredict, Fetch_Increase, Predict_Increase, UpdateMergePredict,init_global


def test(method, predict, pc=0):
    if method == 0:
        res = UpdateOnebitPredict(predict)
    elif method == 1:
        res = UpdateTwobitPredict(predict)
    elif method == 2:
        res = UpdateLocalPredict(predict, pc)
    elif method == 3:
        res = UpdateGlobalPredict(predict)
    elif method == 4:
        res = UpdateMergePredict(predict, pc)
    else:
        raise ValueError()
    if res:
        Fetch_Increase(method)
    Predict_Increase(method)


FileData = []
init()
f = open("""C:\\Users\谢江钊\Desktop\\v.txt""", 'r')
testpar=4
for i in f:
    FileData.append(i.strip('\n'))
    # carry_ins(ins_decode(i.strip('\n')))
while get_pc() < len(FileData):
    now_ins = ins_decode(FileData[get_pc()].strip('\n'))
    now_pc = get_pc()
    carry_ins(now_ins)
    if (now_ins[0] == 'beq') | (now_ins[0] == 'bne'):
        if now_pc + 1 == get_pc():
            test(testpar,0,now_pc)
        else:
            test(testpar,1,now_pc)
print("MergeBranch_Predict:",end='')
print(get_acu(testpar))
'''
for i in range(5):
    testpar=i
    init_global()
    init_data()
    init()
    for i in f:
        FileData.append(i.strip('\n'))
        # carry_ins(ins_decode(i.strip('\n')))
    while get_pc() < len(FileData):
        now_ins = ins_decode(FileData[get_pc()].strip('\n'))
        now_pc = get_pc()
        carry_ins(now_ins)
        if (now_ins[0] == 'beq') | (now_ins[0] == 'bne'):
            if now_pc + 1 == get_pc():
                test(testpar,0,now_pc)
            else:
                test(testpar,1,now_pc)
    #print(RegData['$2'])
    print(get_acu(testpar))
'''
f.close()
# ReadFile("""C:\\Users\谢江钊\Desktop\\f.txt""")
