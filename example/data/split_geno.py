# Function for splitting a single file by character index in each line
def main():
    filename = "French_Yoruba.geno" # file to split
    SPLIT_I = 21 # character index at which to split lines
    geno1 = open('Yoruba.geno', 'w') # output file 1
    geno2 = open('French.geno', 'w') # output file 2
    with open(filename) as f:
        for line in f:
            if line != None:
                line = line.strip()
                geno1.write(line[:SPLIT_I] + "\n")
                geno2.write(line[SPLIT_I + 1:] + "\n")
    geno1.close()
    geno2.close()

if __name__ == '__main__':
    main()