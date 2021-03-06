TwoBitLastPredict = [0]*32
Predict_Time = 0
Fetch_Time = 0

def UpdateTwobitPredict(Predict,PC):
    global TwoBitLastPredict, Predict_Time, Fetch_Time
    PC%=32
    Fetch = False
    if Predict == 0 & (TwoBitLastPredict[PC] < 2):
        Fetch = True
        TwoBitLastPredict[PC] = max(TwoBitLastPredict[PC] - 1, 0)
    if Predict == 1 & (TwoBitLastPredict[PC] > 1):
        Fetch = True
        TwoBitLastPredict[PC] = min(TwoBitLastPredict[PC] + 1, 3)
    if Predict == 0 & (TwoBitLastPredict[PC] > 1):
        TwoBitLastPredict[PC] = max(TwoBitLastPredict[PC] - 1, 0)
    if Predict == 1 & (TwoBitLastPredict[PC] < 2):
        TwoBitLastPredict[PC] = min(TwoBitLastPredict[PC] + 1, 3)
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
    global Fetch_Time,Predict_Time,TwoBitLastPredict
    Fetch_Time=0
    Predict_Time=0
    TwoBitLastPredict=[0]*32