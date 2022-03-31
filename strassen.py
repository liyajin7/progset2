import math, sys, time, gc
from typing import List
import numpy as np

def reg_mult (a: np, b: np):
    l = a.shape[0]

    r = np.zeros((l,l),dtype=int)

    for j in range(l):
        for k in range(l):
            for i in range(l):
                r[i][j] += a[i][k] * b[k][j]
    
    return r

def my_strassens (a: np, b: np):#, srow, scol):   # starting upper row/column
    # print("\nMY_STRASSENS CALLED")

    n = a.shape[0]

    # print("\na and b: \n")
    # print(a)
    # print(b)
    # print("lengths of a and b: ", n, "    ", b.shape[0])

    if n <= 14:    # CHANGE THIS VALUE
        # print("<<<<<<<<<<<<<<<<<<<<<<<<< reg_mult running >>>>>>>>>>>>>>>>>>>>>>>>>>")
        # print("reg_mult running")
        return reg_mult(a, b)
    
    elif n % 2 != 0: #math.log2(n).is_integer(): # just has to be a power of 2!
        # print(">>>>>>>>>>> RUNNING PADDER")
        return (my_strassens(np.pad(a, ((0,1),(0,1)), 'constant'), np.pad(b, ((0,1),(0,1)), 'constant')))[:n,:n]
    
    else:
        # print(">>>>>>>>>>> RUNNING REG STRASSENS")
        
        n = a.shape[0]
     
        mid = n // 2   # changed for odd number matrices

        result_mtx = np.zeros((n,n), dtype = int)     # could possibly do this in a global matrix??
        ######### MOST EXPANDED VERSION POSSIBLE 

        p_temp = np.zeros((mid,mid), dtype = int)
        # print("p_temp size: ", p_temp.shape[0])

        p_temp = my_strassens(a[:mid, :mid], np.subtract(b[:mid, mid:], b[mid:, mid:]))
        # top right
        result_mtx[:mid, mid:] = np.add(result_mtx[:mid, mid:], p_temp)
        # bottom right
        result_mtx[mid:, mid:] = np.add(result_mtx[mid:, mid:], p_temp)

        # p2
        p_temp = my_strassens(np.add(a[:mid, :mid], a[:mid, mid:]), b[mid:, mid:])
        # top left
        result_mtx[:mid, :mid] = np.subtract(result_mtx[:mid, :mid], p_temp)
        # top right
        result_mtx[:mid, mid:] = np.add(result_mtx[:mid, mid:], p_temp)

        # p3
        p_temp = my_strassens(np.add(a[mid:, :mid], a[mid:, mid:]), b[:mid, :mid])
        # bottom left
        result_mtx[mid:, :mid] = np.add(result_mtx[mid:, :mid], p_temp)
        # bottom right
        result_mtx[mid:, mid:] = np.subtract(result_mtx[mid:, mid:], p_temp)

        # p4
        p_temp = my_strassens(a[mid:, mid:], np.subtract(b[mid:, :mid], b[:mid, :mid]))
        # top left
        result_mtx[:mid, :mid] = np.add(result_mtx[:mid, :mid], p_temp)
        # bottom left
        result_mtx[mid:, :mid] = np.add(result_mtx[mid:, :mid], p_temp)

        # p5
        p_temp = my_strassens(np.add(a[:mid, :mid],a[mid:, mid:]), np.add(b[:mid, :mid],b[mid:, mid:]))
        # top left
        result_mtx[:mid, :mid] = np.add(result_mtx[:mid, :mid], p_temp)
        # bottom right
        result_mtx[mid:, mid:] = np.add(result_mtx[mid:, mid:], p_temp)

        # p6
        p_temp = my_strassens(np.subtract(a[:mid, mid:],a[mid:, mid:]), np.add(b[mid:, :mid],b[mid:, mid:]))
        # top left
        result_mtx[:mid, :mid] = np.add(result_mtx[:mid, :mid], p_temp)

        # p7
        p_temp = my_strassens(np.subtract(a[mid:, :mid],a[:mid, :mid]), np.add(b[:mid, :mid],b[:mid, mid:]))
        # bottom right
        result_mtx[mid:, mid:] = np.add(result_mtx[mid:, mid:], p_temp)

        del p_temp
        gc.collect()

        return result_mtx


# global matrix for final output, but would require figuring out how to store current index within final
# final = np.array([[]], dtype = int)

def main ():
    me, flag, dim, fname = sys.argv

    dim = int(dim)
    flag = int(flag)

    f = open(fname, "r")
    temp = []
    m1_temp = []
    m2_temp = []
    
    for line in f:
        line = int(line)
        if len(m1_temp) < dim:
            temp.append(line)
            
            if len(temp) == dim:
                m1_temp.append(temp)
                temp = []
        else:
            temp.append(line)

            if len(temp) == dim:
                m2_temp.append(temp)
                temp = []

    m1 = np.array(m1_temp)
    m2 = np.array(m2_temp)

    # print(m1)
    # print(m2)
    # print("\n len m1: ", m1.shape[0], "\n len m2: ", m2.shape[0])

    final = np.zeros((dim,dim), dtype = int)

    start = time.time()
    if (flag == 0):
        # run variant strassens
        final = my_strassens(m1, m2)
    elif (flag == 1):
        final = reg_mult(m1, m2)
    # elif (flag == 2):
    #     final = reg_strassens(m1, m2)
    elif (flag == 3):
        # print("m1: \n", m1)
        # print("m2: \n", m2)
        
        a = my_strassens(m1,m2)
        # print("first product: \n", a)
        final = my_strassens(a, m1)
    end = time.time()

    iter = 0
    if not math.log2(m1.shape[0]).is_integer():
        iter = m1.shape[0]
    else:
        iter = final.shape[0]

    if (flag != 3):
        print("\nfinal matrix: \n", final, "\n\ndiagonal: ")
    
        for i in range(iter):
            print(final[i][i])
    else:
        countup = 0
        for i in range(iter):
            countup += final[i][i]
        
        print("\nnum triangles = ",countup/6)

    print("\nruntime: ", end-start, "\n\n")

if __name__ == "__main__":
    main()