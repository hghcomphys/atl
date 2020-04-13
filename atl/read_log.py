"""
Read lammps log file into an array or pandas data format
"""
import pandas


def read_log(filename='log.lammps', run=1,
            criteria_1='Per MPI rank memory allocation',
            criteria_2='Loop time'):
    """
    This function reads lammps log file for specified run and returns
    a tuple containing tags and numeric data.

    Example:

        data,tag = read_log(filename=path+"log.lammps",run=1)
        print data[:5],tag[:5]
    """

    fp = open(filename, 'r')
    data = []
    nline = 0
    tags = []
    nr = 0
    while 1:

        line = fp.readline()
        nline += 1
        if not line:
            break

        if not criteria_1 in line:
            continue
        else:
            nr += 1
            if nr < run:
                continue

        line = fp.readline()
        nline += 1
        tags = line.rstrip("/n").split()

        line = fp.readline()
        nline += 1
        prv = None
        while not criteria_2 in line:
            line = line.rstrip("/n").split()

            lng = len(line)
            if prv != None and prv != lng:
                break

            data.append([float(_) for _ in line])
            line = fp.readline()
            nline += 1
            prv = lng

        if nr == run:
            break
    fp.close()

    return data, tags

# ========================================================================================


def read_log_pandas(filename='log.lammps',
                   run=1,
                   criteria_1='Per MPI rank memory allocation',
                    criteria_2='Loop time'):
    """
    This function reads lammps log file for specified run and returns
    pandas data frame  that includes tags and numeric data.

    Example:

        log = read_log_pandas(filename=path+"log.lammps",run=1)
        log.head()
    """

    data, tags = read_log(filename, run, criteria_1, criteria_2)
    return pandas.DataFrame(data, columns=tags)
