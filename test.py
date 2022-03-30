import numpy as np

####### testing add and subtract


def m_add (m1, m2):
    n = m1.shape[0]
    
    ### DOESN'T WORK BC CAN'T MUTATE M1
    # for row in range(n):
    #     for col in range(n):
    #         m1[row][col] += m2[row][col]
    # return m1
    # just MODIFY m1 based on m2, return m1?

def m_sub (m1, m2):

    ### DOESN'T WORK BC CAN'T MUTATE M1
    # n = m1.shape[0]
    # for row in range(n):
    #     for col in range(n):
    #         m1[row][col] -= m2[row][col]
    # return m1

#m1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [1, 1, 2, 2], [3, 3, 4, 4]])
# [[1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [1, 1, 2, 2],
#  [3, 3, 4, 4]]

# [[1,2],[3,4]]


#m2 = np.array([[1, 0,0,0], [0, 1,0,0], [0,0, 1, 0], [0,0,0, 1]])


p5 = np.array([[1, 2], [3, 4]])
p6 = np.array([[1, 2], [3, 4]])
p4 = np.array([[1, 2], [3, 4]])
p2 = np.array([[1, 2], [3, 4]])

#print("1: \n", m_sub(m_add(m_add(p5,p6),p4),p2))
print("1: \n", m_add(m_add(p5,p6),p4))

#p5+p6+p4-p2

#print("2: \n", m_add(m_add(p4,p5),p6))

print("\np5: \n", p5,"\np6: \n", p6,"\np4: \n", p2,"\np5: \n", p2)

#p4-p2+p5+p6

#print("1: \n", m_sub(m_add(m_add(p5,p6),p4),p2))

#print("1: \n", m_add(m_add(m_sub(p4,p2),p5),p6))

# print(m_sub(m1, m2))

# [[2, 0, 2], [3, 3, 3], [3, 2, 1]]

# [[0, 0, 4], [3, 4, 1], [3, 1, 4]]


###### PUTTING ARRAYS BACK TOGETHER 

# a1 = np.array([[1,2],[3,4]])
# a2 = np.array([[5,6],[7,8]])
# a3 = np.array([[3,4],[1,2]])
# a4 = np.array([[7,8],[5,6]])

# dim = 4
# m = 2

# result = np.zeros((dim,dim), dtype = int)

# result[:m, :m] = a1
# result[:m, m:] = a2
# result[m:, :m] = a3
# result[m:, m:] = a4

# print(result)

# for i in range(len(a1)):            UNUSED!!
#     new_matrix.append(a1[i]+a2[i])
# for i in range(len(a1)):
#     new_matrix.append(a3[i]+a4[i])

##### INPUT FILE CONVERSION TO NUMPY

# f = [1,2,3,4,5,6,7,8,1,1,2,2,3,3,4,4,1,1,2,2,3,3,4,4,1,2,3,4,5,6,7,8]

# temp = []
# m1 = []
# m2 = []

# dim = 4

# for line in f:
#     if len(m1) < dim:
#         temp.append(line)
#         if len(temp) == dim:
#             m1.append(temp)
#             temp = []
#     else:
#         temp.append(line)
#         if len(temp) == dim:
#             m2.append(temp)
#             temp = []
        
# print("\n\n", m1, "\n\n\n", m2)



####### TESTING REGULAR MATRIX MULT

# m1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [1, 1, 2, 2], [3, 3, 4, 4]])
# m2 = np.array([[1, 0,0,0], [0, 1,0,0], [0,0, 1, 0], [0,0,0, 1]])

# def reg_mult (m1, m2):
#     l = len(m1)
#     r = np.zeros((l,l),dtype=int)
#     for i in range(l):
#         for j in range(l):
#             for k in range(l):
#                 r[i][j] += m1[i][k] * m2[k][j]
    
#     return r


# print("printing! \n", reg_mult(m1, m2))