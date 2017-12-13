"""
Synacor Challenge
"""
import sys

addr = 0

def op(opcode):
    def halt():
        sys.exit()
    def out():
        global addr
        addr += 1
        print(chr(mem[addr]), end='')
    def nop():
        pass

    return {
        0: halt,
        1: halt,
        2: halt,
        3: halt,
        4: halt,
        5: halt,
        6: halt,
        7: halt,
        8: halt,
        9: halt,
        10: halt,
        11: halt,
        12: halt,
        13: halt,
        14: halt,
        15: halt,
        16: halt,
        17: halt,
        18: halt,
        19: out,
        20: halt,
        21: nop
    }[opcode]

# read and store the binary as 16-bit values in the mem array
bin_raw = open('challenge.bin', 'r', encoding='latin1').read()

# 15-bit address space
num_inst = int(len(bin_raw)/2)
mem = [0] * num_inst

# convert each little-endian pair to a 16-bit value
for i in range(num_inst):
    low = ord(bin_raw[i*2])
    high = ord(bin_raw[i*2 + 1])
    mem[i] = (high << 8) + low

# execute the binary
while True:
    opcode = mem[addr]
    #print(code, end='')
    op(opcode)()
    addr += 1

# TODO: the code currently breaks on a jump (opcode=6) instruction