"""
Disassembles the binary into a human-readable format.
"""
import op

op.read_binary()

addr = 0
out = False

def format_arg(arg):
    """
    Format instruction arguments for human-readability.
    """
    if arg >= 32768:
        arg = 'reg' + str(arg - 32768)
    return '{:>6}'.format(arg)

def write_inst(f):
    """
    Write the instruction at the current addr to f with nice formatting.
    """
    global addr
    global out

    opcode = op.mem[addr]

    # not every memory address contains an instruction
    if opcode > 21:
        addr += 1
        return

    name = op.OP[opcode]['name']

    # if we are no longer printing chars, write a new line
    if opcode != 19 and out == True:
        f.write('\n')
        out = False
    # write the inst name if we are not printing chars
    if out == False:
        f.write('{:4}'.format(addr) + ':\t' + '{:<5}'.format(name))
    # if we are printing chars
    if opcode == 19:
        out = True

    addr += 1

    for i in range(op.OP[opcode]['args']):
        if out == True:
            f.write(chr(op.mem[addr]))
        else:
            f.write(format_arg(op.mem[addr]))

        addr += 1

    if out == False:
        f.write('\n')

with open('disassembly.txt', 'w') as f:
    while addr < len(op.mem):
        write_inst(f)
