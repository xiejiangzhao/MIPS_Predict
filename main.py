from Carry import carry_ins, init, get_pc, RegData, RomData, init_data
from Instruction_Translate import ins_decode
from Predict import init_global
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
import OnebitPredict
import TwobitPredict
import LocalPredict
import GlobalPredict
import MergePredict

plotx_Local = []
ploty_Local = []
plotx_Onebit = []
ploty_Onebit = []
plotx_Twobit = []
ploty_Twobit = []
plotx_Global = []
ploty_Global = []
plotx_Merge = []
ploty_Merge = []


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
        res = OnebitPredict.UpdateOnebitPredict(predict,pc)
    elif method == 1:
        res = TwobitPredict.UpdateTwobitPredict(predict,pc)
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


def plotallx(i):
    plotx_Local.append(7 + i)
    plotx_Onebit.append(7 + i)
    plotx_Twobit.append(7 + i)
    plotx_Global.append(7 + i)
    plotx_Merge.append(7 + i)


FileData = []
init()
f = open("""C:\\Users\谢江钊\Desktop\\v.txt""", 'r')
sizeofsort = 3
for i in range(1, 120, 1):
    sizeofsort = i
    plotallx(i)
    testpar = 2
    init_global()
    init_data()
    init()
    for i in f:
        FileData.append(i.strip('\n'))
        # carry_ins(ins_decode(i.strip('\n')))
    while get_pc() < len(FileData):
        now_ins = ins_decode(FileData[get_pc()].strip('\n'))
        now_pc = get_pc()
        if now_ins[0] == 'addi' and (now_ins[1] == '$2' or now_ins[1] == '$3') and now_ins[2] == '$0': now_ins[3] = str(
            int(now_ins[3]) + sizeofsort)
        carry_ins(now_ins)
        if (now_ins[0] == 'beq') | (now_ins[0] == 'bne'):
            if now_pc + 1 == get_pc():
                test(2, 0, now_pc)
                test(0, 0, now_pc)
                test(1, 0, now_pc)
                test(3, 0, now_pc)
                test(4, 0, now_pc)
            else:
                test(2, 1, now_pc)
                test(0, 1, now_pc)
                test(1, 1, now_pc)
                test(3, 1, now_pc)
                test(4, 1, now_pc)
    # print(RegData['$2'])
    print(i)
    ploty_Local.append(get_acu(2))
    ploty_Onebit.append(get_acu(0))
    ploty_Twobit.append(get_acu(1))
    ploty_Global.append(get_acu(3))
    ploty_Merge.append(get_acu(4))
    LocalPredict.clear_data()
    OnebitPredict.clear_data()
    TwobitPredict.clear_data()
    GlobalPredict.clear_data()
    MergePredict.clear_data()


plt.plot(plotx_Global, ploty_Global, 'm-', label='Global_Predict')
plt.plot(plotx_Local, ploty_Local, 'r-', label='Local_Predict')
plt.plot(plotx_Onebit, ploty_Onebit, 'g-', label='Onebit_Predict')
plt.plot(plotx_Twobit, ploty_Twobit, 'b-', label='Twobit_Predict')
plt.plot(plotx_Merge, ploty_Merge, 'c-', label='Merge_Predict')
plt.legend()
plt.xlabel('Sort_Scale')
plt.ylabel('Accuracy')
plt.show()
f.close()
# ReadFile("""C:\\Users\谢江钊\Desktop\\f.txt""")
