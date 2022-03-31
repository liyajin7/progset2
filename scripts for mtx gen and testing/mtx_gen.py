import sys, random

def main():
    me, dim = sys.argv
    
    dim = int(dim)

    # print("dim: ", dim)
    # count = 0

    for i in range(2*dim*dim):
        print(random.randrange(0, 3, 1))
        #count += 1

    # print("count: ", count)

if __name__ == "__main__":
    main()