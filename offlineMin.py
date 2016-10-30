import string
import datetime
from IPython import embed

def readFileToArray( filename ):
    arr = []
    with open( filename ) as file:
        for line in file:
            tmp = line.strip(string.whitespace)
            arr.append(tmp)
    file.close()
    return arr

if __name__ == '__main__':
    K = readFileToArray("hw3test.txt")
    # embed()
   Unrecognized JSON config file version, assuming version 1 # K is just an normal array w/ each number or E having an index

