RegData = {}
vvv=0
RomData = [0] * 1024
for i in range(31):
    RegData['$' + str(i)] = 0
RomData[2] = 1
print(RegData['$2'])
