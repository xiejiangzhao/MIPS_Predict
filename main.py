from Carry import carry_ins, init, get_pc, RegData
from Instruction_Translate import ins_decode
from Predict import OnebitPredict, UpdateOnebitPredict, get_acu, UpdateTwobitPredict, UpdateLocalPredict, \
    UpdateGlobalPredict, Fetch_Increase, Predict_Increase


def Test(method, predict, pc=0):
    if method == 0:
        Res = UpdateOnebitPredict(predict)
    elif method == 1:
        Res = UpdateTwobitPredict(predict)
    elif method == 2:
        Res = UpdateLocalPredict(predict, pc)
    elif method == 3:
        Res = UpdateGlobalPredict(predict)
    else:
        Res = False
    if Res:
        Fetch_Increase()
    Predict_Increase()


FileData = []
init()
f = open("""C:\\Users\谢江钊\Desktop\\f.txt""", 'r')
for i in f:
    FileData.append(i.strip('\n'))
    # carry_ins(ins_decode(i.strip('\n')))
while get_pc() < len(FileData):
    now_ins = ins_decode(FileData[get_pc()].strip('\n'))
    now_pc = get_pc()
    carry_ins(now_ins)
    if (now_ins[0] == 'beq') | (now_ins[0] == 'bne'):
        if now_pc + 1 == get_pc():
            Test(3, 0)
            # UpdateLocalPredict(0, now_pc)
            # UpdateOnebitPredict(0)
            # UpdateTwobitPredict(0)
        else:
            Test(3, 1)
            # UpdateLocalPredict(1, now_pc)
            # UpdateOnebitPredict(1)
            # UpdateTwobitPredict(1)
print(RegData['$2'])
print(get_acu())
f.close()
# ReadFile("""C:\\Users\谢江钊\Desktop\\f.txt""")
