"""
Contains useful functions for interpreting and executing the binary.
"""
import codes
import sys

# the code (4-8) that you would like to reach automatically
# set code to 0 to run the binary normally
code = 8

# global memory
mem = None

# eight registers
reg = [0] * 8

# start with an empty stack
stack = []

# user input stack
stdin = []
if code >= 9:
    sys.exit('Value of code was ' + str(code) + ' but should be between 4 and 7.')
elif code >= 4:
    stdin = codes.code_to_stdin(code)

# current address
addr = 0

def read_binary():
    """
    Interprets the data in the binary and stores it in the mem array.
    """
    global mem

    # read and store the binary as 16-bit values in the mem array
    bin_raw = open('challenge.bin', 'rb').read()

    # 15-bit address space
    num_inst = int(len(bin_raw)/2)
    mem = [0] * num_inst

    # convert each little-endian pair to a 16-bit value
    for i in range(num_inst):
        low = bin_raw[i*2]
        high = bin_raw[i*2 + 1]
        mem[i] = (high << 8) + low

def exec_inst():
    """
    Executes the next instruction based on the current value of addr.
    """
    global addr
    opcode = mem[addr]
    OP[opcode]['func']()
    addr += 1

def set_teleporter():
    """
    Modify the teleporter (function call to address 6027) to return 6.
    """

    if code >= 7:
        reg[7] = 25734

    mem[6027] = 1
    mem[6028] = 32768
    mem[6029] = 6
    mem[6030] = 18

    print('Teleporter energy level set.')

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

"""
All operations for the architecture are implemented below.
"""
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
    global addr
    a = mem_val(addr + 1)
    stack.append(a)
    addr += 1

def _pop():
    global addr
    a = mem[addr + 1]
    reg[num_to_reg(a)] = stack.pop()
    addr += 1

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
    global addr
    a = mem[addr + 1]
    b = mem_val(addr + 2)
    c = mem_val(addr + 3)
    if b > c:
        reg[num_to_reg(a)] = 1
    else:
        reg[num_to_reg(a)] = 0
    addr += 3

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
    global addr
    a = mem[addr + 1]
    b = mem_val(addr + 2)
    c = mem_val(addr + 3)
    r = (b * c) % 32768
    reg[num_to_reg(a)] = r
    addr += 3

def _mod():
    global addr
    a = mem[addr + 1]
    b = mem_val(addr + 2)
    c = mem_val(addr + 3)
    r = b % c
    reg[num_to_reg(a)] = r
    addr += 3

def _and():
    global addr
    a = mem[addr + 1]
    b = mem_val(addr + 2)
    c = mem_val(addr + 3)
    r = b & c
    reg[num_to_reg(a)] = r
    addr += 3

def _or():
    global addr
    a = mem[addr + 1]
    b = mem_val(addr + 2)
    c = mem_val(addr + 3)
    r = b | c
    reg[num_to_reg(a)] = r
    addr += 3

def _not():
    global addr
    a = mem[addr + 1]
    b = mem_val(addr + 2)
    mask = (1<<15) - 1
    r = b ^ mask
    reg[num_to_reg(a)] = r
    addr += 2

def _rmem():
    global addr
    a = mem[addr + 1]
    b = mem_val(addr + 2)
    reg[num_to_reg(a)] = mem[b]
    addr += 2

def _wmem():
    global addr
    a = mem_val(addr + 1)
    b = mem_val(addr + 2)
    mem[a] = b
    addr += 2

def _call():
    global addr
    stack.append(addr + 2)
    a = mem_val(addr + 1)
    addr = a - 1

def _ret():
    global addr
    try:
        addr = stack.pop() - 1
    except IndexError:
        _halt()

def _out():
    global addr
    a = mem_val(addr + 1)
    print(chr(a), end='')
    addr += 1

def _in():
    global addr
    a = mem[addr + 1]

    # get user input if there is none pending
    if not stdin:
        in_str = input()
        stdin.append(ord('\n'))

        if in_str == 'set teleporter':
            set_teleporter()

        for c in in_str[::-1]:
            stdin.append(ord(c))

    # check to see if the command 'set teleporter' has been automatically inputted
    if ''.join([chr(c) for c in stdin[-14:][::-1]]) == 'set teleporter':
        set_teleporter()

    reg[num_to_reg(a)] = stdin.pop()
    addr += 1

def _noop():
    pass

OP_NAME = ['halt', 'set', 'push', 'pop', 'eq', 'gt', 'jmp',
    'jt', 'jf', 'add', 'mult', 'mod', 'and', 'or', 'not',
    'rmem', 'wmem', 'call', 'ret', 'out', 'in', 'noop']

OP_FUNC = [_halt, _set, _push, _pop, _eq, _gt, _jmp,
    _jt, _jf, _add, _mult, _mod, _and, _or, _not,
    _rmem, _wmem, _call, _ret, _out, _in, _noop]

OP_ARGS = [0, 2, 1, 1, 3, 3, 1,
    2, 2, 3, 3, 3, 3, 3, 2,
    2, 2, 1, 0, 1, 1, 0]

OP = {}
for i in range(len(OP_NAME)):
    OP[i] = {
        'name': OP_NAME[i],
        'func': OP_FUNC[i],
        'args': OP_ARGS[i]
    }
