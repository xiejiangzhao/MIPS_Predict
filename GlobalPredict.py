Predict_Time = 0
Fetch_Time = 0
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
    def clear(self):
        for i in range(16):
            self.Predict_all[i] = 1


GlobalBranch = BPT()


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


def Fetch_Increase():
    global Fetch_Time
    Fetch_Time += 1


def Predict_Increase():
    global Predict_Time
    Predict_Time += 1


def get_acu():
    global Predict_Time, Fetch_Time
    return Fetch_Time / Predict_Time

def clear_data():
    global Predict_Time,Fetch_Time,Global_History
    Predict_Time=Fetch_Time=Global_History=0
    GlobalBranch.clear()