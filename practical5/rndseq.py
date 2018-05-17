#! /usr/bin/env python
"prints first argument aa sequences of length second argument to screen"
import random
import sys

def gene_order_parser(file_handle):
    integer_list = []
    with open (file_handle) as f:
        for line in f:
            i = line.split(" ")
            for ii in i:
                #print(ii)
                integer_list.append(ii.strip("\n"))
            
    return integer_list

def AA_generator (num1, num2, integer_list):
    number=int(num1)
    length=int(num2)
    aas="ARNDCEQGHILKMFPSTWYV"
    def r20():
        return random.randrange(20)
    db={}
    #print(integer_list)
    for i in integer_list:
        #print(i)
        for ii in range(int(i)):
            s=""
            for j in range(length):
                s+=aas[r20()]
                db[i] = s

    print (db)
    


    
    
if __name__ == "__main__":
    integer_list = gene_order_parser(sys.argv[3])
    AA_generator(sys.argv[1], sys.argv[2], integer_list)
    
