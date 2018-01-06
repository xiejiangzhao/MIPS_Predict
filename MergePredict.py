Predict_Time = 0
Fetch_Time = 0
Global_History = 0
MergeBranch = [1] * 35


class BPT:
    Predict_all = [None] * 16

    def __init__(self):
        for i in range(16):
            self.Predict_all[i] = 1

    def get_predict(self, history):
        return self.Predict_all[history]

    def update(self, history, change):
        self.Predict_all[history] += change
        if self.Predict_all[history] < 0:
            self.Predict_all[history] = 0
        elif self.Predict_all[history] > 3:
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
            self.BPT_all[i] = BPT()


GlobalBranch = BPT()
LocalBranch = BHT()


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


def Fetch_Increase():
    global Fetch_Time
    Fetch_Time += 1


def Predict_Increase():
    global Predict_Time
    Predict_Time += 1


def get_acu():
    global Predict_Time, Fetch_Time
    return Fetch_Time / Predict_Time
