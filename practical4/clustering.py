# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:39:47 2018

@author: u2362
"""

#cluster

import sys
import re
from Bio.Blast import NCBIXML

def parsing_output():
	

blastOutputXMLFile = sys.argv [1]
