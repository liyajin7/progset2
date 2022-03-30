import math, sys, time
from typing import List
import numpy as np

# possibly use list comprehension instead of for loop?
# result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

# def m_neg (m: np): # NEEDED?
#     return [
#         [-m[row][col] for col in range(len(m[row]))]
#         for row in range(len(m))
#     ]

def m_add (m1: np, m2: np):
    # print("\n\nM_ADD m1: ", m1, ", ")
    # print("M_ADD m2: ", m2, ", ")

    #return m1 + m2

    n = m1.shape[0]

    temp = np.zeros((n,n))

    for row in range(n):
        for col in range(n):
            temp[row][col] = m1[row][col] + m2[row][col]

    return temp

    ### DOESN'T WORK BC CAN'T MUTATE M1
    

    # for row in range(n):
    #     for col in range(n):
    #         m1[row][col] += m2[row][col]

    # print("M_ADD result: ", m1)
    # return m1
    # just MODIFY m1 based on m2, return m1?

def m_sub (m1: np, m2: np):
    # print("\n\nM_SUB m1: ", m1, ", ")
    # print("M_SUB m2: ", m2, ", ")
    
    #return m1 - m2

    n = m1.shape[0]

    temp = np.zeros((n,n))

    for row in range(n):
        for col in range(n):
            temp[row][col] = m1[row][col] - m2[row][col]

    return temp
    
    ### DOESN'T WORK BC CAN'T MUTATE M1
    # n = m1.shape[0]

    # for row in range(n):
    #     for col in range(n):
    #         m1[row][col] -= m2[row][col]
    
    # print("M_SUB result: ", m1)
    # return m1
    # just MODIFY m1 based on m2, return m1?

def reg_mult (m1: np, m2: np):
    l = m1.shape[0]

    r = np.zeros((l,l),dtype=int)
    for i in range(l):
        for j in range(l):
            for k in range(l):
                r[i][j] += m1[i][k] * m2[k][j]
    
    return r

def reg_strassens (m1: np, m2: np):
    
    if m1.shape[0] == 1:
        return np.array([m1[[0]]*m2[[0]]])   # need to check return value here
    else:
        n = m1.shape[0]

        mid = n // 2   # changed for odd number matrices

        # print("\n\nn: ", n, "\nmid: ", mid)

        # print("!! reg_strassens m1/m2: \n", m1, "\n\n", m2)

        new_matrix = np.zeros((n,n), dtype = int)     # could possibly do this in a global matrix??

        ########## MOST NAIVE VERSION POSSIBLE

        # a = m1[:mid, :mid]
        # b = m1[:mid, mid:]
        # c = m1[mid:, :mid]
        # d = m1[mid:, mid:]
        # e = m2[:mid, :mid]
        # f = m2[:mid, mid:]
        # g = m2[mid:, :mid]
        # h = m2[mid:, mid:]

        # p1 = reg_strassens(a, m_sub(f,h))
        # p2 = reg_strassens(m_add(a,b),h)
        # p3 = reg_strassens(m_add(c,d),e)
        # p4 = reg_strassens(d, m_sub(g,e))
        # p5 = reg_strassens(m_add(a,d), m_add(e,h))
        # p6 = reg_strassens(m_sub(b,d), m_add(g,h))
        # p7 = reg_strassens(m_sub(c,a), m_add(e,f))

        ######### MOST EXPANDED VERSION POSSIBLE 

        # print("\n>>>> top left running")
        new_matrix[:mid, :mid] = m_sub(m_add(m_add(reg_strassens(m_add(m1[:mid, :mid],m1[mid:, mid:]), m_add(m2[:mid, :mid],m2[mid:, mid:])),reg_strassens(m_sub(m1[:mid, mid:],m1[mid:, mid:]), m_add(m2[mid:, :mid],m2[mid:, mid:]))),reg_strassens(m1[mid:, mid:], m_sub(m2[mid:, :mid],m2[:mid, :mid]))),reg_strassens(m_add(m1[:mid, :mid],m1[:mid, mid:]),m2[mid:, mid:])) #m_add(m_add(m_sub(p4,p2),p5),p6)

        # print("\n>>>> top right running")
        new_matrix[:mid, mid:] = m_add(reg_strassens(m1[:mid, :mid], m_sub(m2[:mid, mid:],m2[mid:, mid:])),reg_strassens(m_add(m1[:mid, :mid],m1[:mid, mid:]),m2[mid:, mid:]))

        # print("\n>>>> bottom left running")
        new_matrix[mid:, :mid] = m_add(reg_strassens(m_add(m1[mid:, :mid],m1[mid:, mid:]),m2[:mid, :mid]),reg_strassens(m1[mid:, mid:], m_sub(m2[mid:, :mid],m2[:mid, :mid])))

        # print("\n>>>> bottom right running")
        new_matrix[mid:, mid:] = m_sub(m_add(m_add(reg_strassens(m_add(m1[:mid, :mid],m1[mid:, mid:]), m_add(m2[:mid, :mid],m2[mid:, mid:])),reg_strassens(m_sub(m1[mid:, :mid],m1[:mid, :mid]), m_add(m2[:mid, :mid],m2[:mid, mid:]))),reg_strassens(m1[:mid, :mid], m_sub(m2[:mid, mid:],m2[mid:, mid:]))),reg_strassens(m_add(m1[mid:, :mid],m1[mid:, mid:]),m2[:mid, :mid]))



        # print("\n>>>> top left running")
        # new_matrix[:mid, :mid] = m_sub(m_add(m_add(p5,p6),p4),p2) #m_add(m_add(m_sub(p4,p2),p5),p6)

        # print("\n>>>> top right running")
        # new_matrix[:mid, mid:] = m_add(p1,p2)

        # print("\n>>>> bottom left running")
        # new_matrix[mid:, :mid] = m_add(p3,p4)

        # print("\n>>>> bottom right running")
        # new_matrix[mid:, mid:] = m_sub(m_add(m_add(p5,p7),p1),p3)


        
        ######## SUPER LONG VERSION, ALL DONE IN ONE

        # # top left
        # print(">> top left running")
        # # P4 - P2 + P5 + P6
        # new_matrix[:mid, :mid] = m_add(m_add(m_sub(reg_strassens(d, m_sub(g,e)), reg_strassens(m_add(a,b), h)), reg_strassens(m_add(a,d), m_add(e,h))), reg_strassens(m_sub(b,d), m_add(g,h)))
        # # WIP new_matrix[:mid, :mid] = m_add(m_add(m_sub(reg_strassens(m1[mid:, mid:], m_sub(m2[mid:, :mid],m2[:mid, :mid])), reg_strassens(m_add(m1[:mid, :mid],b), h)), reg_strassens(m_add(m1[:mid, :mid],m1[mid:, mid:]), m_add(m2[:mid, :mid],h))), reg_strassens(m_sub(b,m1[mid:, mid:]), m_add(m2[mid:, :mid],h)))
        
        # print(">> top right running")
        # # P1 + P2
        # new_matrix[:mid, mid:] = m_add(reg_strassens(a,m_sub(f,h)), reg_strassens(m_add(a,b),h))
        # # WIP new_matrix[:mid, mid:] = m_add(reg_strassens(m1[:mid, :mid],m_sub(f,h)), reg_strassens(m_add(m1[:mid, :mid],b),h))
        
        # print(">> bottom left running")
        # new_matrix[mid:, :mid] = m_add(reg_strassens(m_add(c,d),e), reg_strassens(d,m_sub(g,e)))
        # # WIP new_matrix[mid:, :mid] = m_add(reg_strassens(m_add(c,m1[mid:, mid:]),m2[:mid, :mid]), reg_strassens(m1[mid:, mid:],m_sub(m2[mid:, :mid],m2[:mid, :mid])))
        
        # print(">> bottom right running")
        # # P1 - P3 + P5 + P7
        # new_matrix[mid:, mid:] = m_add(m_add(m_sub(reg_strassens(a, m_sub(f,h)), reg_strassens(m_add(c,d),e)), reg_strassens(m_add(a,d), m_add(e,h))), reg_strassens(m_sub(c,a), m_add(e,f)))
        # # WIP new_matrix[mid:, mid:] = m_add(m_add(m_sub(reg_strassens(m1[:mid, :mid], m_sub(f,h)), reg_strassens(m_add(c,m1[mid:, mid:]),m2[:mid, :mid])), reg_strassens(m_add(m1[:mid, :mid],m1[mid:, mid:]), m_add(m2[:mid, :mid],h))), reg_strassens(m_sub(c,m1[:mid, :mid]), m_add(m2[:mid, :mid],f)))
        
        # new_matrix[:mid, :mid] = m_add(
        #                 m_sub(
        #                     m_add(
        #                             reg_strassens (m_add(m1[:mid, :mid],m1[mid:, mid:]), m_add(m2[:mid, :mid],m2[mid:, mid:])), #t5
        #                                 reg_strassens (m1[mid:, mid:], m_sub(m2[mid:, :mid], m2[:mid, :mid])) ),   #t4
        #                                 reg_strassens (m_add(m1[:mid, :mid],m1[:mid, mid:]),m2[mid:, mid:])    #t2
                                        
        #                                 ),
        #                             reg_strassens (m_sub(m1[:mid, mid:],m1[mid:, mid:]),m_add(m2[mid:, :mid],m2[mid:, mid:]))     #t6
        #                             )

        # # top right
        # print(" >> top right running")
        # new_matrix[:mid, mid:] = m_add(
        #                 reg_strassens (m1[:mid, :mid], m_sub(m2[:mid, mid:],m2[mid:, mid:])),
        #                 reg_strassens (m_add(m1[:mid, :mid],m1[:mid, mid:]), m2[mid:, mid:])
        #                 )
        
        # # bottom left
        # print(" >> bottom left running")
        # new_matrix[mid:, :mid] = m_add (reg_strassens(m_add(m1[mid:, :mid],m1[mid:, mid:]),m2[:mid, :mid]), reg_strassens(m1[mid:, mid:], m_sub(m2[mid:, :mid],m2[:mid, :mid])))
        
        # # bottom right
        # print(" >> bottom right running")
        # new_matrix[mid:, mid:] = m_sub(
        #                     m_sub(
        #                             m_add  (reg_strassens(m1[:mid, :mid], m_sub(m2[:mid, mid:],m2[mid:, mid:])),    #t1
                                            
        #                                     reg_strassens(m_add(m1[:mid, :mid],m1[mid:, mid:]), m_add(m2[:mid, :mid],m2[mid:, mid:])),     #t5

        #                             reg_strassens(m_add(m1[mid:, :mid],m1[mid:, mid:]), m2[:mid, :mid])   # t3
        #                         ),
        #                     reg_strassens(m_sub(m1[:mid, :mid],m1[mid:, :mid]), m_add(m2[:mid, :mid],m2[:mid, mid:])) # t7

        #                 )
        #             )

        # ## wrong??
        # for i in range(len(top_right)):
        #     new_matrix.append(top_left[i] + top_right[i])
        # for i in range(len(bottom_right)):
        #     new_matrix.append(bottom_left[i] + bottom_right[i])

        return new_matrix

def my_strassens (m1: np, m2: np):#, srow, scol):   # starting upper row/column
    n = m1.shape[0]

    if n <= 1000:    # @LIYA NEED TO CHANGE THIS VALUE!
        reg_mult(m1, m2)
    else:
        n = m1.shape[0]

        mid = n // 2   # changed for odd number matrices

        new_matrix = np.zeros((n,n), dtype = int)     # could possibly do this in a global matrix??
        ######### MOST EXPANDED VERSION POSSIBLE 

        # print("\n>>>> top left running")
        new_matrix[:mid, :mid] = m_sub(m_add(m_add(my_strassens(m_add(m1[:mid, :mid],m1[mid:, mid:]), m_add(m2[:mid, :mid],m2[mid:, mid:])),my_strassens(m_sub(m1[:mid, mid:],m1[mid:, mid:]), m_add(m2[mid:, :mid],m2[mid:, mid:]))),my_strassens(m1[mid:, mid:], m_sub(m2[mid:, :mid],m2[:mid, :mid]))),my_strassens(m_add(m1[:mid, :mid],m1[:mid, mid:]),m2[mid:, mid:])) #m_add(m_add(m_sub(p4,p2),p5),p6)

        # print("\n>>>> top right running")
        new_matrix[:mid, mid:] = m_add(my_strassens(m1[:mid, :mid], m_sub(m2[:mid, mid:],m2[mid:, mid:])),my_strassens(m_add(m1[:mid, :mid],m1[:mid, mid:]),m2[mid:, mid:]))

        # print("\n>>>> bottom left running")
        new_matrix[mid:, :mid] = m_add(my_strassens(m_add(m1[mid:, :mid],m1[mid:, mid:]),m2[:mid, :mid]),my_strassens(m1[mid:, mid:], m_sub(m2[mid:, :mid],m2[:mid, :mid])))

        # print("\n>>>> bottom right running")
        new_matrix[mid:, mid:] = m_sub(m_add(m_add(my_strassens(m_add(m1[:mid, :mid],m1[mid:, mid:]), m_add(m2[:mid, :mid],m2[mid:, mid:])),my_strassens(m_sub(m1[mid:, :mid],m1[:mid, :mid]), m_add(m2[:mid, :mid],m2[:mid, mid:]))),my_strassens(m1[:mid, :mid], m_sub(m2[:mid, mid:],m2[mid:, mid:]))),my_strassens(m_add(m1[mid:, :mid],m1[mid:, mid:]),m2[:mid, :mid]))

        return new_matrix


# global matrix for final output, but @LIYA would require figuring out how to store current index within final
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
    
    # convert lists to numpy arrays!!!

    final = np.zeros((dim,dim), dtype = int)

    start = time.time()
    if (flag == 0):
        # run variant strassens
        final = my_strassens(m1, m2)
    elif (flag == 1):
        # run regular strassens
        final = reg_strassens(m1, m2)
    elif (flag == 2):
        # run regular matrix mult
        final = reg_mult(m1, m2)
    end = time.time()

    print("\nfinal matrix: \n", final, "\ndiagonal: \n")
    
    for i in range(final.shape[0]):
        print(final[i][i])

    print("\nruntime: ", end-start, "\n\n")

if __name__ == "__main__":  # runs when file is run in the terminal
    main()
    # put biggest command here!!