"""
Contains sequences of inputs required to find codes in the adventure game.
# 1: found by reading the arch-spec hints
# 2: found by implementing out and noop
# 3: found by implementing all instructions
# 4: found by inputting the commands in '4' (by using the tablet)
# 5: found by inputting the commands in '5' (by getting the twisty passages)
# 6: found by inputting the commands in '6' (by teleporting to the safe location)
# 7: found by solving the teleporter puzzle
# 8: found by solving the orb puzzle
"""
code = {
    4: ["take tablet",
    "use tablet"],
    5: ["go doorway",
    "go north",
    "go north",
    "go bridge",
    "go continue",
    "go down",
    "go east",
    "take empty lantern",
    "go west",
    "go west",
    "go passage",
    "go ladder",
    "go west",
    "go south",
    "go north"],
    6: ["take can",
    "use can",
    "go west",
    "go ladder",
    "go darkness",
    "use lantern",
    "go continue",
    "go west",
    "go west",
    "go west",
    "go west",
    "go north",
    "take red coin",
    "go north",
    "go west",
    "take blue coin",
    "go up",
    "take shiny coin",
    "go down",
    "go east",
    "go east",
    "take concave coin",
    "go down",
    "take corroded coin",
    "go up",
    "go west",
    "use blue coin",
    "use red coin",
    "use shiny coin",
    "use concave coin",
    "use corroded coin",
    "go north",
    "take teleporter",
    "set teleporter",
    "use teleporter"],
    7: [],
    8: ["go north",
    "go north",
    "go north",
    "go north",
    "go north",
    "go north",
    "go north",
    "go north",
    "go north",
    "take orb",
    "go north",
    "go east",
    "go east",
    "go north",
    "go west",
    "go south",
    "go east",
    "go east",
    "go west",
    "go north",
    "go north",
    "go east",
    "go vault",
    "take mirror",
    "use mirror"]
}

def code_to_stdin(n):
    """
    Combines strings to create a sequence of user-inputs to the binary.
    """
    codes = []
    for i in range(4,n+1):
        # skip empty lists
        if len(code[i]) == 0:
            continue
        codes.append('\n'.join(code[i]))
    cmds = '\n'.join(codes)

    stdin = []
    stdin.append(ord('\n'))
    for c in cmds[::-1]:
        stdin.append(ord(c))
    return stdin
