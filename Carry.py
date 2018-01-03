RegData = {}
PC = 0
RomData = [0] * 1024
Timesum = 0
Collect = 0


def init():
    global RegData
    for i in range(31):
        RegData['$' + str(i)] = 0


def carry_ins(instruction):
    global RegData, PC
    if instruction[0] == 'add':
        RegData[instruction[1]] = RegData[instruction[2]] + RegData[instruction[3]]
    elif instruction[0] == 'addu':
        RegData[instruction[1]] = RegData[instruction[2]] + RegData[instruction[3]]
    elif instruction[0] == 'addi':
        RegData[instruction[1]] = RegData[instruction[2]] + int(instruction[3].replace('$', ''))
    elif instruction[0] == 'sub':
        RegData[instruction[1]] = RegData[instruction[2]] - RegData[instruction[3]]
    elif instruction[0] == 'subu':
        RegData[instruction[1]] = RegData[instruction[2]] - RegData[instruction[3]]
    elif instruction[0] == 'and':
        RegData[instruction[1]] = RegData[instruction[2]] & RegData[instruction[3]]
    elif instruction[0] == 'or':
        RegData[instruction[1]] = RegData[instruction[2]] | RegData[instruction[3]]
    elif instruction[0] == 'xor':
        RegData[instruction[1]] = RegData[instruction[2]] ^ RegData[instruction[3]]
    elif instruction[0] == 'nor':
        RegData[instruction[1]] = ~(RegData[instruction[2]] | RegData[instruction[3]])
    elif instruction[0] == 'slt':
        if RegData[instruction[2]] < RegData[instruction[3]]:
            RegData[instruction[1]] = 1
        else:
            RegData[instruction[1]] = 0
    elif instruction[0] == 'sltu':
        if RegData[instruction[2]] < RegData[instruction[3]]:
            RegData[instruction[1]] = 1
        else:
            RegData[instruction[1]] = 0
    elif instruction[0] == 'bne':
        if RegData[instruction[1]] != RegData[instruction[2]]:
            PC = PC + 1 + int(instruction[3].replace('$', ''))
            return
    elif instruction[0] == 'beq':
        if RegData[instruction[1]] == RegData[instruction[2]]:
            PC = PC + 1 + int(instruction[3].replace('$', ''))
            return
    elif instruction[0] == 'j':
        PC = int(int(instruction[1].replace('0x', '')) / 4)
        return
    elif instruction[0] == 'jal':
        RegData['$31'] = PC + 1
        PC = int(int(instruction[1].replace('0x', '')) / 4)
        return
    elif instruction[0] == 'jr':
        PC = RegData[instruction[1]]
        return
    elif instruction[0] == 'lw':
        if len(instruction) == 4:
            RegData[instruction[1]] = RomData[int(instruction[2].replace('$', '')) + RegData[instruction[3]]]
        else:
            RegData[instruction[1]] = RomData[RegData[instruction[2]]]
    elif instruction[0] == 'sw':
        if len(instruction) == 4:
            RomData[int(instruction[2].replace('$', '')) + RegData[instruction[3]]] = RegData[instruction[1]]
        else:
            RomData[RegData[instruction[2]]] = RegData[instruction[1]]
    elif instruction[0] == 'halt':
        PC = 10000
        return
    PC = PC + 1


def get_pc():
    global PC
    return PC
