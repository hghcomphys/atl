
def read_data(filename='data.dat', start_line=0, end_line=10000000):
    """
    This function reads data file between specified lines
    and return a list of numeric data.
    """

    fp = open(filename, 'r')
    data = []
    nline = 0
    prv = None
    while nline < end_line:

        # ----------------------------
        line = fp.readline()
        nline += 1
        if not line:
            break
            # ----------------------------
        if nline < start_line:
            continue
        # ----------------------------
        line = line.rstrip("/n").split()
        data.append([float(_) for _ in line])
        # ----------------------------
        lng = len(line)
        if prv != None and prv != lng:
            break
        # ----------------------------
        prv = lng
        # ----------------------------

    fp.close()
    return data