"""
Synacor Challenge
"""
import sys

addr = 0

def op(opcode):
    def _halt():
        sys.exit()
    def _set():
        print('ERROR: set not implemented')
        sys.exit()
    def _push():
        print('ERROR: push not implemented')
        sys.exit()
    def _pop():
        print('ERROR: pop not implemented')
        sys.exit()
    def _eq():
        print('ERROR: eq not implemented')
        sys.exit()
    def _gt():
        print('ERROR: gt not implemented')
        sys.exit()
    def _jmp():
        global addr
        jmp_addr = mem[addr + 1]
        addr = jmp_addr - 1
    def _jt():
        print('ERROR: jt not implemented')
        sys.exit()
    def _jf():
        print('ERROR: jf not implemented')
        sys.exit()
    def _add():
        print('ERROR: add not implemented')
        sys.exit()
    def _mult():
        print('ERROR: mult not implemented')
        sys.exit()
    def _mod():
        print('ERROR: mod not implemented')
        sys.exit()
    def _and():
        print('ERROR: and not implemented')
        sys.exit()
    def _or():
        print('ERROR: or not implemented')
        sys.exit()
    def _not():
        print('ERROR: not not implemented')
        sys.exit()
    def _rmem():
        print('ERROR: rmem not implemented')
        sys.exit()
    def _wmem():
        print('ERROR: wmem not implemented')
        sys.exit()
    def _call():
        print('ERROR: call not implemented')
        sys.exit()
    def _ret():
        print('ERROR: ret not implemented')
        sys.exit()
    def _out():
        global addr
        addr += 1
        print(chr(mem[addr]), end='')
    def _in():
        print('ERROR: in not implemented')
        sys.exit()
    def _nop():
        pass

    return {
        0: _halt,
        1: _set,
        2: _push,
        3: _pop,
        4: _eq,
        5: _gt,
        6: _jmp,
        7: _jt,
        8: _jf,
        9: _add,
        10: _mult,
        11: _mod,
        12: _and,
        13: _or,
        14: _not,
        15: _rmem,
        16: _wmem,
        17: _call,
        18: _ret,
        19: _out,
        20: _in,
        21: _nop
    }[opcode]()

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
    op(opcode)
    addr += 1

# TODO: the code currently breaks on a jump (opcode=6) instruction