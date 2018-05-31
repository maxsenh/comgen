# -*- coding: utf-8 -*-
"""
Created on Fri May 25 14:41:18 2018

@author: u2359
"""
import sys


def ORF_Parse(file_handle):
    RF1 = []
    RF2 = []
    RF3 = []
    with open (file_handle) as f:
        for line in f:
            if not line.startswith(">."):
                #print(line)
                shortline = line.rstrip()
                #print(shortline)
                for i in range (len(shortline)):
                    #print(line[i:i+3])
                    RF1.append(shortline[i:i+3])
                    RF2.append(shortline[i+1:(i+1)+3])
                    RF3.append(shortline[i+2:(i+2)+3])
    
    RF1_short = []
    RF2_short = []
    RF3_short = []
    for codons in RF1:
        if len(codons) > 2:
            RF1_short.append(codons)
    for codons in RF2:
        if len(codons) > 2:
            RF2_short.append(codons)
    for codons in RF3:
        if len(codons) > 2:
            RF3_short.append(codons)
            

    
if __name__ == "__main__":
    ORF_Parse(sys.argv[1])