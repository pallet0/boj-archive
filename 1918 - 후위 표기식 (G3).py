import sys
input = sys.stdin.readline

"""
expr, term, factor is nonterminal, n is terminal

expr -> term (('+'|'-')term)*
term -> factor (('*'|'/')term)*
factor -> int | '('expr')'
"""

ptr = 0
s = ""

def nextIt():
    global ptr
    ptr += 1

def currentToken():
    return s[ptr]

def parseExpr():
    res = ""
    res += parseTerm()
    while currentToken() in ['+', '-'] and currentToken() != "\n":
        op = currentToken()
        nextIt()
        res += parseTerm() + op
    
    return res

def parseTerm():
    res = ""
    res += parseFactor()
    while currentToken() in ['*', '/'] and currentToken() != "\n":
        op = currentToken()
        nextIt()
        res += parseFactor() + op
    
    return res

def parseFactor():
    res = ""
    if currentToken() == "(":
        nextIt()
        res += parseExpr()
        nextIt()
    else:
        res += currentToken()
        nextIt()
    return res

s = list(input())
print(parseExpr())
