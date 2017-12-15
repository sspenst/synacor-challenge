"""
Runs an optimized version of the function at address 6027 to find
the input that will allow the teleporter to reach the second location.
"""
import sys

mod = 32768

def check_r7_val(r7):
    """
    Checks if a specific value of reg7 would result in a successful
    outcome for the function call at address 6027.
    """
    cache = {}

    def f6027(r0, r1, r7):
        """
        Optimized implementation of the function found at address 6027.
        """
        if (r0, r1) in cache:
            return cache[(r0, r1)]
        elif r0 == 2:
            ret = (2*r7 + r1*(r7+1) + 1) % mod
        elif r0 == 3 and r1 == 0:
            ret = (r7*(r7+3) + 1) % mod
        elif r1 == 0:
            ret = f6027(r0 - 1, r7, r7)
        else:
            t1 = f6027(r0, r1 - 1, r7)
            ret = f6027(r0 - 1, t1, r7)
        # update cache
        cache[(r0, r1)] = ret
        return ret

    # initialize the cache
    for i in range(mod):
        f6027(3, i, r7)

    # if our return value is 6, then the teleporter works!
    if f6027(4, 1, r7) == 6:
        print('REG7 SHOULD BE SET TO ' + str(r7))
        sys.exit()

# search through all possible values of r7
for r7 in range(1, mod):
    check_r7_val(r7)