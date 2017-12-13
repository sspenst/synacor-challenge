"""
Synacor Challenge
"""
import sys

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

# eight registers
reg = [0] * 8

# current address
addr = 0

def num_to_reg(num):
    """
    Convert a value to a register index.
    Fails if the value is not a valid register index.
    """
    reg_id = num - 32768
    assert reg_id >= 0 and reg_id < 8
    return reg_id

def mem_val(addr):
    """
    Get the value of memory address 'addr'. If the value
    corresponds to a register, the register's value is returned.
    """
    val = mem[addr]
    if val >= 0 and val < 32768:
        return val
    else:
        return reg[num_to_reg(val)]

def op(opcode):
    def _halt():
        print('HALT at addr ' + str(addr))
        sys.exit()

    def _set():
        global addr
        a = mem[addr + 1]
        b = mem_val(addr + 2)
        reg[num_to_reg(a)] = b
        addr += 2
    
    def _push():
        print('ERROR: push not implemented')
        sys.exit()
    
    def _pop():
        print('ERROR: pop not implemented')
        sys.exit()
    
    def _eq():
        global addr
        a = mem[addr + 1]
        b = mem_val(addr + 2)
        c = mem_val(addr + 3)
        if b == c:
            reg[num_to_reg(a)] = 1
        else:
            reg[num_to_reg(a)] = 0
        addr += 3
    
    def _gt():
        print('ERROR: gt not implemented')
        sys.exit()
    
    def _jmp():
        global addr
        a = mem_val(addr + 1)
        addr = a - 1
    
    def _jt():
        global addr
        a = mem_val(addr + 1)
        b = mem_val(addr + 2)
        if a != 0:
            addr = b - 1
        else:
            addr += 2
    
    def _jf():
        global addr
        a = mem_val(addr + 1)
        b = mem_val(addr + 2)
        if a == 0:
            addr = b - 1
        else:
            addr += 2
    
    def _add():
        global addr
        a = mem[addr + 1]
        b = mem_val(addr + 2)
        c = mem_val(addr + 3)
        r = (b + c) % 32768
        reg[num_to_reg(a)] = r
        addr += 3
    
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
        a = mem_val(addr + 1)
        print(chr(a), end='')
        addr += 1
    
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

# execute each instruction in memory
while True:
    opcode = mem[addr]
    op(opcode)
    addr += 1