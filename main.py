from Carry import carry_ins, init, get_pc, RegData, RomData, init_data
from Instruction_Translate import ins_decode
from Predict import init_global
import OnebitPredict
import TwobitPredict
import LocalPredict
import GlobalPredict
import MergePredict


def Fetch_Increase(method):
    if method == 0:
        res = OnebitPredict.Fetch_Increase()
    elif method == 1:
        res = TwobitPredict.Fetch_Increase()
    elif method == 2:
        res = LocalPredict.Fetch_Increase()
    elif method == 3:
        res = GlobalPredict.Fetch_Increase()
    elif method == 4:
        res = MergePredict.Fetch_Increase()
    else:
        raise ValueError()


def Predict_Increase(method):
    if method == 0:
        res = OnebitPredict.Predict_Increase()
    elif method == 1:
        res = TwobitPredict.Predict_Increase()
    elif method == 2:
        res = LocalPredict.Predict_Increase()
    elif method == 3:
        res = GlobalPredict.Predict_Increase()
    elif method == 4:
        res = MergePredict.Predict_Increase()
    else:
        raise ValueError()


def get_acu(method):
    if method == 0:
        res = OnebitPredict.get_acu()
    elif method == 1:
        res = TwobitPredict.get_acu()
    elif method == 2:
        res = LocalPredict.get_acu()
    elif method == 3:
        res = GlobalPredict.get_acu()
    elif method == 4:
        res = MergePredict.get_acu()
    else:
        raise ValueError()
    return res


def test(method, predict, pc=0):
    if method == 0:
        res = OnebitPredict.UpdateOnebitPredict(predict)
    elif method == 1:
        res = TwobitPredict.UpdateTwobitPredict(predict)
    elif method == 2:
        res = LocalPredict.UpdateLocalPredict(predict, pc)
    elif method == 3:
        res = GlobalPredict.UpdateGlobalPredict(predict)
    elif method == 4:
        res = MergePredict.UpdateMergePredict(predict, pc)
    else:
        raise ValueError()
    if res:
        Fetch_Increase(method)
    Predict_Increase(method)


FileData = []
init()
f = open("""C:\\Users\谢江钊\Desktop\\v.txt""", 'r')
'''
testpar=0
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
    testpar = i
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
                test(testpar, 0, now_pc)
            else:
                test(testpar, 1, now_pc)
    # print(RegData['$2'])
    print(get_acu(testpar))
# '''
f.close()
# ReadFile("""C:\\Users\谢江钊\Desktop\\f.txt""")
