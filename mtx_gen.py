import sys, random

def main():
    me, dim = sys.argv
    
    dim = int(dim)

    for i in range(2*dim*dim):
        print(random.randrange(0, 3, 1))

if __name__ == "__main__":
    main()