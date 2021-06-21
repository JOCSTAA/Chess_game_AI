
from random import *

def check(i,j,ccur,cn):
    conflict = 0

    #a
    if i != 0:
        if j != 0:
            ai = i - 1
            aj = j - 1

            while (ai >= 0 and aj >= 0):
                    if ccur[ai][aj] == 1:
                        conflict = conflict + 1
                    ai = ai - 1
                    aj = aj - 1

    # b
    if i != 0:
        if j != cn:
            bi = i - 1
            bj = j + 1

            while (bi >= 0 and bj <= cn):
                    if ccur[bi][bj] == 1:
                        conflict = conflict + 1
                    bi = bi - 1
                    bj = bj + 1

    # c
    if j != 0:
        cj = j - 1
        ci = i

        while cj >= 0:
                if ccur[ci][cj] == 1:
                    conflict = conflict + 1
                cj = cj - 1

    # d
    if j != cn:
        di = i
        dj = j + 1

        while dj <= cn:
                if ccur[di][dj] == 1:
                    conflict = conflict + 1
                dj = dj + 1

    # e
    if i != cn:
        if j != 0:
            ei = i + 1
            ej = j - 1

            while (ei <= cn and ej >= 0):
                    if ccur[ei][ej] == 1:
                        conflict = conflict + 1
                    ei = ei + 1
                    ej = ej - 1
    # f
    if i != cn:
        if j != cn:
            fi = i + 1
            fj = j + 1

            while (fi <= cn and fj <= cn):
                    if ccur[fi][fj] == 1:
                        conflict = conflict + 1
                    fi = fi + 1
                    fj = fj + 1

    return conflict

def pick(pcur,pn):
    explored = []

    pi = 0
    while pi <= pn:
        pj = 0
        while pj <= pn:
            if pcur[pi][pj]==1:
                pc = check(pi,pj,pcur,pn)
                if pc > 0:
                    explored.append(pj)
            pj = pj + 1
        pi= pi+1

    #print(explored,": columns with conflict")

    x = sample(explored,1)
    #print(x[0], ": column i choose")
    return x[0]

def evalmin(ej,ecur,en):
    err = []
    oldec = 1000

    # checks what is the minimum conflict of all rows
    ei = 0
    while ei <= en:
        ec=check(ei,ej,ecur,en)
        if ec < oldec:
            oldec = ec
        ei = ei + 1

    # checks which rows have the minimum conflict
    ei = 0
    while ei <= en:
        ec = check(ei,ej,ecur,en)
        if ec == oldec:
            err.append(ei)
        ei = ei + 1

    # initaializes all rows to 0
    ei = 0
    while ei <= en:
        ecur[ei][ej]=0
        ei = ei + 1

    # picks one of the min conflict row at random
    #print(err, ": rows with min conflict")
    y = sample(err, 1)
    errr= y[0]
    #print(errr, ": row chosen")

    # puts the queen in the selected row
    ecur[errr][ej]=1
    return ecur

def wholecheck(wcur,wn):
    w = 0
    wi = 0

    while wi <= wn:
        wj = 0
        while wj <= wn:
            if wcur[wi][wj] == 1:
                w = w + check(wi, wj, wcur, wn)
            wj = wj + 1
        wi = wi + 1

    return w

def minconflict(cur,max,mn):
    #print(cur, "\n\n")

    mi = 1
    while mi < max:
        #print(mi)
        p = wholecheck(cur,mn)

        if p == 0:
            return cur

        b = pick(cur,mn)
        cur = evalmin(b,cur,mn)
        #print(cur)

        mi= mi+1

    print("failure to detemine solution within given iteration")
    return 0

def printboard(brd,cbn):
    cbi=0
    while cbi <= cbn:
        cbj=0
        while cbj <= cbn:
            if brd[cbi][cbj]==0:
                print("o", end =" ")
            else:
                print("x", end =" ")
            cbj = cbj + 1
        print(" ")
        cbi = cbi + 1

print("=======================================================================================================================")
print("This is a code that sets queens that never attack each other "
        "on a chessboard(n*n: where n is any integar greater than 4)")
print("made by Chibuike Joshua Ogbonda")
endj = 0
while endj == 0:
    # make chessboard
    chessbj = 0
    while chessbj == 0:
        num = input("\n\n -Enter size of chessboard(any number higher than 3): ")
        n = int(num) - 1

        if n >= 3:
            csp = [[0 for x in range(n + 1)] for y in range(n + 1)]
            chessbj = 1
        else:
            print("incorrect chessboard size")

    # input queens to chessboard
    print("\n\n")
    nj = 0
    while nj <= n:
        num2 = input(" -Enter row number for the queen on the column(" + str(nj + 1) + "):")
        pasta = int(num2) - 1
        if pasta <= n and pasta >= 0 :
            csp[pasta][nj] = 1
            nj = nj + 1
        else:
            print("ROW is out of bounds, please enter a ROW number between 1 and " + str(n + 1))

    #print the initial chessboard config
    print("\n\nTHIS IS YOUR START BOARD CONFIGURATION:")
    printboard(csp,n)

    #solves
    new = minconflict(csp,3000,n)

    #print the final chessboard
    print("\n\nTHIS IS YOUR BOARD WITH NO QUEEN ATTACKING EACH OTHER:")
    printboard(new,n)

    #end the program
    nume = input("\n\nEnter R to redo or any other key to end the program:")
    print("============================================================================================================")
    if nume == 'r':
        endj = 0
    elif nume == 'R':
        endj = 0
    else:
        endj = 1