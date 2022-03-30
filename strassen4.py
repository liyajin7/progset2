import math, sys, time, gc
from typing import List
import numpy as np

def reg_mult (m1: np, m2: np):
    l = m1.shape[0]

    r = np.zeros((l,l),dtype=int)

    for i in range(l):
        for k in range(l):
            for j in range(l):
                r[i][j] += m1[i][k] * m2[k][j]
    
    return r

def reg_strassens (a: np, b: np):#, srow, scol):   # starting upper row/column
    # print("\nMY_STRASSENS CALLED")

    n = a.shape[0]
    # print("len: ",n)

    if n == 1:
        return np.array([a[[0]]*b[[0]]])        
    else:
        # print("strassens running")
        
        n = a.shape[0]

        mid = n // 2   # changed for odd number matrices

        # p1 = reg_strassens(a, m_sub(f,h))
        # p2 = reg_strassens(m_add(a,b),h)
        # p3 = reg_strassens(m_add(c,d),e)
        # p4 = reg_strassens(d, m_sub(g,e))
        # p5 = reg_strassens(m_add(a,d), m_add(e,h))
        # p6 = reg_strassens(m_sub(b,d), m_add(g,h))
        # p7 = reg_strassens(m_sub(c,a), m_add(e,f))


        new_matrix = np.zeros((n,n), dtype = int)     # could possibly do this in a global matrix??
        ######### MOST EXPANDED VERSION POSSIBLE 

        p_temp = np.zeros((mid,mid), dtype = int)
        # a_temp = np.zeros((mid,mid), dtype = int)
        # b_temp = np.zeros((mid,mid), dtype = int)

        # p1
        p_temp = reg_strassens(a[:mid, :mid], np.subtract(b[:mid, mid:], b[mid:, mid:]))
        # top right
        new_matrix[:mid, mid:] = np.add(new_matrix[:mid, mid:], p_temp)
        # bottom right
        new_matrix[mid:, mid:] = np.add(new_matrix[mid:, mid:], p_temp)

        # p2
        p_temp = reg_strassens(np.add(a[:mid, :mid], a[:mid, mid:]), b[mid:, mid:])
        # top left
        new_matrix[:mid, :mid] = np.subtract(new_matrix[:mid, :mid], p_temp)
        # top right
        new_matrix[:mid, mid:] = np.add(new_matrix[:mid, mid:], p_temp)

        # p3
        p_temp = reg_strassens(np.add(a[mid:, :mid], a[mid:, mid:]), b[:mid, :mid])
        # bottom left
        new_matrix[mid:, :mid] = np.add(new_matrix[mid:, :mid], p_temp)
        # bottom right
        new_matrix[mid:, mid:] = np.subtract(new_matrix[mid:, mid:], p_temp)

        # p4
        p_temp = reg_strassens(a[mid:, mid:], np.subtract(b[mid:, :mid], b[:mid, :mid]))
        # top left
        new_matrix[:mid, :mid] = np.add(new_matrix[:mid, :mid], p_temp)
        # bottom left
        new_matrix[mid:, :mid] = np.add(new_matrix[mid:, :mid], p_temp)

        # p5
        p_temp = reg_strassens(np.add(a[:mid, :mid],a[mid:, mid:]), np.add(b[:mid, :mid],b[mid:, mid:]))
        # top left
        new_matrix[:mid, :mid] = np.add(new_matrix[:mid, :mid], p_temp)
        # bottom right
        new_matrix[mid:, mid:] = np.add(new_matrix[mid:, mid:], p_temp)

        # p6
        p_temp = reg_strassens(np.subtract(a[:mid, mid:],a[mid:, mid:]), np.add(b[mid:, :mid],b[mid:, mid:]))
        # top left
        new_matrix[:mid, :mid] = np.add(new_matrix[:mid, :mid], p_temp)

        # p7
        p_temp = reg_strassens(np.subtract(a[mid:, :mid],a[:mid, :mid]), np.add(b[:mid, :mid],b[:mid, mid:]))
        # bottom right
        new_matrix[mid:, mid:] = np.add(new_matrix[mid:, mid:], p_temp)

        # a = a[:mid, :mid]
        # b = a[:mid, mid:]
        # c = a[mid:, :mid]
        # d = a[mid:, mid:]
        # e = b[:mid, :mid]
        # f = b[:mid, mid:]
        # g = b[mid:, :mid]
        # h = b[mid:, mid:]

        # # top left
        # new_matrix[:mid, :mid] = 

        # # top right
        # new_matrix[:mid, mid:] = 

        # # bottom left
        # new_matrix[mid:, :mid] = 

        # # bottom right
        # new_matrix[mid:, mid:] = 



        # # print("\n>>>> top left running")
        # new_matrix[:mid, :mid] = np.subtract(np.add(np.add(my_strassens(np.add(m1[:mid, :mid],m1[mid:, mid:]), np.add(m2[:mid, :mid],m2[mid:, mid:])),my_strassens(np.subtract(m1[:mid, mid:],m1[mid:, mid:]), np.add(m2[mid:, :mid],m2[mid:, mid:]))),my_strassens(m1[mid:, mid:], np.subtract(m2[mid:, :mid],m2[:mid, :mid]))),my_strassens(np.add(m1[:mid, :mid],m1[:mid, mid:]),m2[mid:, mid:]))

        # # print("\n>>>> top right running")
        # new_matrix[:mid, mid:] = np.add(my_strassens(m1[:mid, :mid], np.subtract(m2[:mid, mid:],m2[mid:, mid:])),my_strassens(np.add(m1[:mid, :mid],m1[:mid, mid:]),m2[mid:, mid:]))

        # # print("\n>>>> bottom left running")
        # new_matrix[mid:, :mid] = np.add(my_strassens(np.add(m1[mid:, :mid],m1[mid:, mid:]),m2[:mid, :mid]),my_strassens(m1[mid:, mid:], np.subtract(m2[mid:, :mid],m2[:mid, :mid])))

        # # print("\n>>>> bottom right running")
        # new_matrix[mid:, mid:] = np.subtract(np.add(np.add(my_strassens(np.add(m1[:mid, :mid],m1[mid:, mid:]), np.add(m2[:mid, :mid],m2[mid:, mid:])),my_strassens(np.subtract(m1[mid:, :mid],m1[:mid, :mid]), np.add(m2[:mid, :mid],m2[:mid, mid:]))),my_strassens(m1[:mid, :mid], np.subtract(m2[:mid, mid:],m2[mid:, mid:]))),my_strassens(np.add(m1[mid:, :mid],m1[mid:, mid:]),m2[:mid, :mid]))

        # del m1
        # del m2
        del p_temp
        gc.collect()

        return new_matrix

def my_strassens (a: np, b: np):#, srow, scol):   # starting upper row/column
    # print("\nMY_STRASSENS CALLED")

    n = a.shape[0]
    # print("len: ",n)

    if n <= 512:    # CHANGE THIS VALUE
        #print("<<<<<<<<<<<<<<<<<<<<<<<<<",n, ">>>>>>>>>>>>>>>>>>>>>>>>>>")
        # print("reg_mult running")
        return reg_mult(a, b)
        
    else:
        # print("strassens running")
        
        n = a.shape[0]

        mid = n // 2   # changed for odd number matrices

        # p1 = reg_strassens(a, m_sub(f,h))
        # p2 = reg_strassens(m_add(a,b),h)
        # p3 = reg_strassens(m_add(c,d),e)
        # p4 = reg_strassens(d, m_sub(g,e))
        # p5 = reg_strassens(m_add(a,d), m_add(e,h))
        # p6 = reg_strassens(m_sub(b,d), m_add(g,h))
        # p7 = reg_strassens(m_sub(c,a), m_add(e,f))


        new_matrix = np.zeros((n,n), dtype = int)     # could possibly do this in a global matrix??
        ######### MOST EXPANDED VERSION POSSIBLE 

        p_temp = np.zeros((mid,mid), dtype = int)
        # a_temp = np.zeros((mid,mid), dtype = int)
        # b_temp = np.zeros((mid,mid), dtype = int)

        # p1
        p_temp = my_strassens(a[:mid, :mid], np.subtract(b[:mid, mid:], b[mid:, mid:]))
        # top right
        new_matrix[:mid, mid:] = np.add(new_matrix[:mid, mid:], p_temp)
        # bottom right
        new_matrix[mid:, mid:] = np.add(new_matrix[mid:, mid:], p_temp)

        # p2
        p_temp = my_strassens(np.add(a[:mid, :mid], a[:mid, mid:]), b[mid:, mid:])
        # top left
        new_matrix[:mid, :mid] = np.subtract(new_matrix[:mid, :mid], p_temp)
        # top right
        new_matrix[:mid, mid:] = np.add(new_matrix[:mid, mid:], p_temp)

        # p3
        p_temp = my_strassens(np.add(a[mid:, :mid], a[mid:, mid:]), b[:mid, :mid])
        # bottom left
        new_matrix[mid:, :mid] = np.add(new_matrix[mid:, :mid], p_temp)
        # bottom right
        new_matrix[mid:, mid:] = np.subtract(new_matrix[mid:, mid:], p_temp)

        # p4
        p_temp = my_strassens(a[mid:, mid:], np.subtract(b[mid:, :mid], b[:mid, :mid]))
        # top left
        new_matrix[:mid, :mid] = np.add(new_matrix[:mid, :mid], p_temp)
        # bottom left
        new_matrix[mid:, :mid] = np.add(new_matrix[mid:, :mid], p_temp)

        # p5
        p_temp = my_strassens(np.add(a[:mid, :mid],a[mid:, mid:]), np.add(b[:mid, :mid],b[mid:, mid:]))
        # top left
        new_matrix[:mid, :mid] = np.add(new_matrix[:mid, :mid], p_temp)
        # bottom right
        new_matrix[mid:, mid:] = np.add(new_matrix[mid:, mid:], p_temp)

        # p6
        p_temp = my_strassens(np.subtract(a[:mid, mid:],a[mid:, mid:]), np.add(b[mid:, :mid],b[mid:, mid:]))
        # top left
        new_matrix[:mid, :mid] = np.add(new_matrix[:mid, :mid], p_temp)

        # p7
        p_temp = my_strassens(np.subtract(a[mid:, :mid],a[:mid, :mid]), np.add(b[:mid, :mid],b[:mid, mid:]))
        # bottom right
        new_matrix[mid:, mid:] = np.add(new_matrix[mid:, mid:], p_temp)

        # a = a[:mid, :mid]
        # b = a[:mid, mid:]
        # c = a[mid:, :mid]
        # d = a[mid:, mid:]
        # e = b[:mid, :mid]
        # f = b[:mid, mid:]
        # g = b[mid:, :mid]
        # h = b[mid:, mid:]

        # # top left
        # new_matrix[:mid, :mid] = 

        # # top right
        # new_matrix[:mid, mid:] = 

        # # bottom left
        # new_matrix[mid:, :mid] = 

        # # bottom right
        # new_matrix[mid:, mid:] = 



        # # print("\n>>>> top left running")
        # new_matrix[:mid, :mid] = np.subtract(np.add(np.add(my_strassens(np.add(m1[:mid, :mid],m1[mid:, mid:]), np.add(m2[:mid, :mid],m2[mid:, mid:])),my_strassens(np.subtract(m1[:mid, mid:],m1[mid:, mid:]), np.add(m2[mid:, :mid],m2[mid:, mid:]))),my_strassens(m1[mid:, mid:], np.subtract(m2[mid:, :mid],m2[:mid, :mid]))),my_strassens(np.add(m1[:mid, :mid],m1[:mid, mid:]),m2[mid:, mid:]))

        # # print("\n>>>> top right running")
        # new_matrix[:mid, mid:] = np.add(my_strassens(m1[:mid, :mid], np.subtract(m2[:mid, mid:],m2[mid:, mid:])),my_strassens(np.add(m1[:mid, :mid],m1[:mid, mid:]),m2[mid:, mid:]))

        # # print("\n>>>> bottom left running")
        # new_matrix[mid:, :mid] = np.add(my_strassens(np.add(m1[mid:, :mid],m1[mid:, mid:]),m2[:mid, :mid]),my_strassens(m1[mid:, mid:], np.subtract(m2[mid:, :mid],m2[:mid, :mid])))

        # # print("\n>>>> bottom right running")
        # new_matrix[mid:, mid:] = np.subtract(np.add(np.add(my_strassens(np.add(m1[:mid, :mid],m1[mid:, mid:]), np.add(m2[:mid, :mid],m2[mid:, mid:])),my_strassens(np.subtract(m1[mid:, :mid],m1[:mid, :mid]), np.add(m2[:mid, :mid],m2[:mid, mid:]))),my_strassens(m1[:mid, :mid], np.subtract(m2[:mid, mid:],m2[mid:, mid:]))),my_strassens(np.add(m1[mid:, :mid],m1[mid:, mid:]),m2[:mid, :mid]))

        # del m1
        # del m2
        del p_temp
        gc.collect()

        return new_matrix


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
    elif (flag == 2):
        final = reg_strassens(m1, m2)
    end = time.time()

    print("\nfinal matrix: \n", final, "\n\ndiagonal: ")
    
    for i in range(final.shape[0]):
        print(final[i][i])

    print("\nruntime: ", end-start, "\n\n")

if __name__ == "__main__":
    main()