OnebitLastPredict = 0
TwoBitLastPredict = 1
Predict_Time = 0
Fetch_Time = 0
Global_History = 0


class BPT:
    Predict_all = [None] * 16
    for i in range(16):
        Predict_all[i] = 1

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
    for i in range(31):
        History[i] = 0
    BPT_all = []
    for i in range(31):
        BPT_all.append(BPT())


LocalBranch = BHT()
GlobalBranch = BPT()


def OnebitPredict():
    global OnebitLastPredict
    return OnebitPredict()


def UpdateOnebitPredict(Predict):
    global OnebitLastPredict, Predict_Time, Fetch_Time
    if Predict == OnebitLastPredict:
        Fetch_Time += 1
    Predict_Time += 1
    OnebitLastPredict = Predict


def UpdateTwobitPredict(Predict):
    global TwoBitLastPredict, Predict_Time, Fetch_Time
    if Predict == 0 & (TwoBitLastPredict < 2):
        Fetch_Time += 1
        TwoBitLastPredict = max(TwoBitLastPredict - 1, 0)
    if Predict == 1 & (TwoBitLastPredict > 1):
        Fetch_Time += 1
        TwoBitLastPredict = min(TwoBitLastPredict + 1, 3)
    if Predict == 0 & (TwoBitLastPredict > 1):
        TwoBitLastPredict = max(TwoBitLastPredict - 1, 0)
    if Predict == 1 & (TwoBitLastPredict < 2):
        TwoBitLastPredict = min(TwoBitLastPredict + 1, 3)
    Predict_Time += 1


def UpdateLocalPredict(Predict, PC):
    global Predict_Time, Fetch_Time
    PC_history = LocalBranch.History[PC]
    pre = LocalBranch.BPT_all[PC].get_predict(PC_history)
    if (Predict == 0) & (pre < 2):
        Fetch_Time += 1
        LocalBranch.BPT_all[PC].update(PC_history, -1)
    if (Predict == 1) & (pre > 1):
        Fetch_Time += 1
        LocalBranch.BPT_all[PC].update(PC_history, 1)
    if (Predict == 0) & (pre > 1):
        LocalBranch.BPT_all[PC].update(PC_history, -1)
    if (Predict == 1) & (pre < 2):
        LocalBranch.BPT_all[PC].update(PC_history, 1)
    LocalBranch.History[PC] = (LocalBranch.History[PC] << 1) % 4
    LocalBranch.History[PC] += Predict
    Predict_Time += 1
    return LocalBranch.History[PC]


def UpdateGlobalPredict(Predict):
    global Global_History,GlobalBranch,Predict_Time,Fetch_Time
    pre=GlobalBranch.get_predict(Global_History)
    if (Predict == 0) & (pre < 2):
        Fetch_Time += 1
        GlobalBranch.update(Global_History, -1)
    if (Predict == 1) & (pre > 1):
        Fetch_Time += 1
        GlobalBranch.update(Global_History, 1)
    if (Predict == 0) & (pre > 1):
        GlobalBranch.update(Global_History, -1)
    if (Predict == 1) & (pre < 2):
        GlobalBranch.update(Global_History, 1)
    Global_History = (Global_History << 1) % 16
    Global_History += Predict
    Predict_Time += 1
    return Global_History

def UpdateMergePredict(Predict):
    pass


def get_acu():
    global Predict_Time, Fetch_Time
    return Fetch_Time / Predict_Time


if __name__ == '__main__':
    for i in range(4):
        a =UpdateGlobalPredict(1)
        print(a)
    for i in range(4):
        a =UpdateGlobalPredict(0)
        print(a)
