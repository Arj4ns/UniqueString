# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:57:32 2019

@author: Arjan
"""

class isUnique:
    def __init__(self, string):
        self.string = string
    
    def checkUnique(self):
        for i in range(0, len(self.string)):
            newString = self.string[:i] + self.string[i+1:]
            keptChar = self.string[i]
            for j in newString:
                if keptChar == j:
                    return False
        return True
    
stringChecker = isUnique("gundam")
print(stringChecker.checkUnique())