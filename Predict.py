OnebitLastPredict = 0
TwoBitLastPredict = 1
Predict_Time = [0] * 5
Fetch_Time = [0] * 5
Global_History = 0


def init_global():
    OnebitLastPredict = 0
    TwoBitLastPredict = 1
    Predict_Time = [0] * 5
    Fetch_Time = [0] * 5
    Global_History = 0


class BPT:
    Predict_all = [None] * 16

    def __init__(self):
        for i in range(16):
            self.Predict_all[i] = 1

    def get_predict(self, history):
        return self.Predict_all[history]

    def update(self, history, change):
        self.Predict_all[history] += change
        if (self.Predict_all[history] < 0):
            self.Predict_all[history] = 0
        elif (self.Predict_all[history] > 3):
            self.Predict_all[history] = 3
        return


class BHT:
    History = [None] * 31
    BPT_all = [None] * 31

    def __init__(self):
        for i in range(31):
            self.History[i] = 0
        for i in range(31):
            self.BPT_all[i] = BPT()

    def clear(self):
        for i in range(31):
            self.History[i] = 0
        for i in range(31):
            BPT_all[i] = BPT()


class BPT_Global:
    Predict_all = [None] * 16

    def __init__(self):
        for i in range(16):
            self.Predict_all[i] = 1

    def clear(self):
        for i in range(16):
            self.Predict_all[i] = 1

    def get_predict(self, history):
        return self.Predict_all[history]

    def update(self, history, change):
        self.Predict_all[history] += change
        if (self.Predict_all[history] < 0):
            self.Predict_all[history] = 0
        elif (self.Predict_all[history] > 3):
            self.Predict_all[history] = 3
        return


LocalBranch = BHT()
GlobalBranch = BPT_Global()
MergeBranch = [1] * 35


def OnebitPredict():
    global OnebitLastPredict
    return OnebitPredict()


def UpdateOnebitPredict(Predict):
    global OnebitLastPredict, Predict_Time
    Fetch = False
    if Predict == OnebitLastPredict:
        Fetch = True
    OnebitLastPredict = Predict
    return Fetch


def UpdateTwobitPredict(Predict):
    global TwoBitLastPredict, Predict_Time, Fetch_Time
    Fetch = False
    if Predict == 0 & (TwoBitLastPredict < 2):
        Fetch = True
        TwoBitLastPredict = max(TwoBitLastPredict - 1, 0)
    if Predict == 1 & (TwoBitLastPredict > 1):
        Fetch = True
        TwoBitLastPredict = min(TwoBitLastPredict + 1, 3)
    if Predict == 0 & (TwoBitLastPredict > 1):
        TwoBitLastPredict = max(TwoBitLastPredict - 1, 0)
    if Predict == 1 & (TwoBitLastPredict < 2):
        TwoBitLastPredict = min(TwoBitLastPredict + 1, 3)
    return Fetch


def UpdateLocalPredict(Predict, PC):
    global LocalBranch
    Fetch = False
    PC %= 32
    PC_history = LocalBranch.History[PC]
    pre = LocalBranch.BPT_all[PC].get_predict(PC_history)
    if (Predict == 0) & (pre < 2):
        Fetch = True
        LocalBranch.BPT_all[PC].update(PC_history, -1)
    if (Predict == 1) & (pre > 1):
        Fetch = True
        LocalBranch.BPT_all[PC].update(PC_history, 1)
    if (Predict == 0) & (pre > 1):
        LocalBranch.BPT_all[PC].update(PC_history, -1)
    if (Predict == 1) & (pre < 2):
        LocalBranch.BPT_all[PC].update(PC_history, 1)
    LocalBranch.History[PC] = (LocalBranch.History[PC] << 1) % 4
    LocalBranch.History[PC] += Predict
    return Fetch


def UpdateGlobalPredict(Predict):
    global Global_History, GlobalBranch
    Fetch = False
    pre = GlobalBranch.get_predict(Global_History)
    if (Predict == 0) & (pre < 2):
        Fetch = True
        GlobalBranch.update(Global_History, -1)
    if (Predict == 1) & (pre > 1):
        Fetch = True
        GlobalBranch.update(Global_History, 1)
    if (Predict == 0) & (pre > 1):
        GlobalBranch.update(Global_History, -1)
    if (Predict == 1) & (pre < 2):
        GlobalBranch.update(Global_History, 1)
    Global_History = (Global_History << 1) % 16
    Global_History += Predict
    return Fetch


def UpdateMergePredict(Predict, PC):
    global MergeBranch
    GlobalPre = UpdateGlobalPredict(Predict)
    LocalPre = UpdateLocalPredict(Predict, PC)
    if MergeBranch[PC] > 1:
        pre = GlobalPre
    else:
        pre = LocalPre
    if LocalPre > GlobalPre:
        MergeBranch[PC] -= 1
    if GlobalPre > LocalPre:
        MergeBranch[PC] += 1
    if MergeBranch[PC] > 3:
        MergeBranch[PC] = 3
    if MergeBranch[PC] < 0:
        MergeBranch[PC] = 0
    return pre


def get_acu(method):
    global Predict_Time, Fetch_Time
    return Fetch_Time[method] / Predict_Time[method]


if __name__ == '__main__':
    for i in range(4):
        a = UpdateGlobalPredict(1)
        print(a)
    for i in range(4):
        a = UpdateGlobalPredict(0)
        print(a)


def Fetch_Increase(method):
    global Fetch_Time
    Fetch_Time[method] += 1


def Predict_Increase(method):
    global Predict_Time
    Predict_Time[method] += 1
