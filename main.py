"""
Runs the binary.
"""
import op

op.read_binary()

# execute each instruction in memory
while True:
    op.exec_inst()
