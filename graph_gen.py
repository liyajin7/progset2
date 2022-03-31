import sys, random
import numpy as np

def main():
    me, prob = sys.argv

    dim = 256
    
    g = np.zeros((dim, dim), dtype = int)

    valid = []

    for i in range(int(prob)):
        valid.append(i+1)

    count = 0

    for i in range(dim):
        for j in range(i,dim):
            #print("i: ",i,"     j: ",j )
            if (random.randrange(1, 101, 1) in valid):
                
                g[i][j] = 1
                g[j][i] = 1
            #print(g[i][j])
            # count += 1
    
    for i in range(2):
        for i in range(dim):
            for j in range(dim):
                print(g[i][j])
        
    #print("\ncount: ", count)

if __name__ == "__main__":
    main()