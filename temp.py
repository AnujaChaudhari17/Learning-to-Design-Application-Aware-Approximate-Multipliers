
def AND(A,B):
    A=int(A)
    B=int(B)
    return A&B
def nand(a, b):
    return 0 if (a == 1 and b == 1) else 1
def xnor(a,b):
    return 1 if a==b else 0
def nor(a, b):
    return 1 if (a == 0 and b == 0) else 0
def half_adder(A, B):
    A=int(A)
    B=int(B)
    sum_bit = A ^ B
    carry = A & B
    return [sum_bit, carry]

def full_adder(A,B,C):
    A=int(A)
    B=int(B)
    C=int(C)
    sum = A^B^C
    carry = (A&B) | (B&C) | (A&C)
    return [sum,carry]

# Basic compressors
def ahmad(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = nand(nor(A,B),nor(C,D))
    carry = nor(nor(A,B),nor(C,D))
    return [sum,carry]

def akbari(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = nand(xnor(A,B),xnor(C,D))
    carry = nand(nand(A,B),nand(C,D))
    return [sum,carry]

def meo(x1,x2,x3,x4):
    num_bi = [x4, x3, x2, x1]
    num_de = int(''.join(str(x) for x in num_bi), base=2)

    if num_de == 0:
        sum_a = 0
        carry_a = 0

    elif num_de == 1:
        sum_a = 1
        carry_a = 0

    elif num_de == 2:
        sum_a = 1
        carry_a = 0

    elif num_de ==3:
        sum_a = 0
        carry_a = 1

    elif num_de==4:
        sum_a = 1
        carry_a = 0

    elif num_de ==5:
        sum_a = 0
        carry_a = 1

    elif num_de ==6:
        sum_a = 0
        carry_a = 1

    elif num_de ==7:
        sum_a = 0
        carry_a = 1

    elif num_de ==8:
        sum_a = 1
        carry_a = 0

    elif num_de ==9:
        sum_a = 0
        carry_a = 1

    elif num_de ==10:
        sum_a = 0
        carry_a = 1

    elif num_de ==11:
        sum_a = 1
        carry_a = 1

    elif num_de ==12:
        sum_a = 0
        carry_a = 1

    elif num_de ==13:
        sum_a = 1
        carry_a = 1

    elif num_de ==14:
        sum_a = 1
        carry_a = 1

    else:
        sum_a = 1
        carry_a = 1


    return [sum_a,carry_a]


def venka(x1,x2,x3,x4):
    num_bi = [x4, x3, x2, x1]
    num_de = int(''.join(str(x) for x in num_bi), base=2)

    if num_de == 0:
        sum_a = 0
        carry_a = 0

    elif num_de == 1:
        sum_a = 1
        carry_a = 0

    elif num_de == 2:
        sum_a = 1
        carry_a = 0

    elif num_de ==3:
        sum_a = 0
        carry_a = 1

    elif num_de==4:
        sum_a = 1
        carry_a = 0

    elif num_de ==5:
        sum_a = 1
        carry_a = 0

    elif num_de ==6:
        sum_a = 1
        carry_a = 0

    elif num_de ==7:
        sum_a = 1
        carry_a = 1

    elif num_de ==8:
        sum_a = 1
        carry_a = 0

    elif num_de ==9:
        sum_a = 1
        carry_a = 0

    elif num_de ==10:
        sum_a = 1
        carry_a = 0

    elif num_de ==11:
        sum_a = 1
        carry_a = 1

    elif num_de ==12:
        sum_a = 0
        carry_a = 1

    elif num_de ==13:
        sum_a = 1
        carry_a = 1

    elif num_de ==14:
        sum_a = 1
        carry_a = 1
    else:
        sum_a = 1
        carry_a = 1


    return [sum_a,carry_a]

def yang(x1,x2,x3,x4):
    num_bi = [x4, x3, x2, x1]
    num_de = int(''.join(str(x) for x in num_bi), base=2)

    if num_de == 0:
        sum_a = 0
        carry_a = 0
    elif num_de == 1:
        sum_a = 1
        carry_a = 0
    elif num_de == 2:
        sum_a = 1
        carry_a = 0
    elif num_de ==3:
        sum_a = 0
        carry_a = 1
    elif num_de==4:
        sum_a = 1
        carry_a = 0
    elif num_de ==5:
        sum_a = 0
        carry_a = 1
    elif num_de ==6:
        sum_a = 0
        carry_a = 1
    elif num_de ==7:
        sum_a = 1
        carry_a = 1
    elif num_de ==8:
        sum_a = 1
        carry_a = 0
    elif num_de ==9:
        sum_a = 0
        carry_a = 1
    elif num_de ==10:
        sum_a = 0
        carry_a = 1
    elif num_de ==11:
        sum_a = 1
        carry_a = 1
    elif num_de ==12:
        sum_a = 1
        carry_a = 1
    elif num_de ==13:
        sum_a = 1
        carry_a = 1
    elif num_de ==14:
        sum_a = 1
        carry_a = 1
    else:
        sum_a = 1
        carry_a = 1

    return [sum_a,carry_a]

def momeni(x1,x2,x3,x4):
    num_bi = [x4, x3, x2, x1]
    num_de = int(''.join(str(x) for x in num_bi), base=2)

    if num_de == 0 :
        sum_a = 1
        carry_a = 0

    elif num_de == 1:
        sum_a = 1
        carry_a = 0

    elif num_de == 2:
        sum_a = 1
        carry_a = 0

    elif num_de ==3:
        sum_a = 1
        carry_a = 0

    elif num_de==4:
        sum_a = 1
        carry_a = 0

    elif num_de ==5:
        sum_a = 0
        carry_a = 1

    elif num_de ==6:
        sum_a = 0
        carry_a = 1

    elif num_de ==7:
        sum_a = 1
        carry_a = 1

    elif num_de ==8:
        sum_a = 1
        carry_a = 0

    elif num_de ==9:
        sum_a = 0
        carry_a = 1

    elif num_de ==10:
        sum_a = 0
        carry_a = 1

    elif num_de ==11:
        sum_a = 1
        carry_a = 1

    elif num_de ==12:
        sum_a = 1
        carry_a = 0

    elif num_de ==13:
        sum_a = 1
        carry_a = 1

    elif num_de ==14:
        sum_a = 1
        carry_a = 1

    else:
        sum_a = 1
        carry_a = 1


    return [sum_a,carry_a]
def mux(sel, data0, data1):
    if sel == 0:
        return data0
    elif sel == 1:
        return data1
    else:
        return None

def app_compressor(A,B,C,D):
  a = int(A)
  b = int(B)
  c = int(C)
  d = int(D)
  temp1 = a^b
  temp2 = nand(a,b)
  temp3 = c^d
  temp4 = nand(c,d)

  temp5 = nand(temp1,temp3)
  temp6 = 1^temp1
  temp7 = AND(temp2,temp4)

  #sum
  sum = mux(temp3,temp1,temp6)

  #carry
  carry = nand(temp7,temp5)

  return [sum,carry]

# AC6G compressors
def AC6G1(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|B)|(C|D))
    carry = (A&(C|D)|(B&C))
    return [sum,carry]

def AC6G2(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|B)|(C|D))
    carry = (A&(C|D)|(B&D))
    return [sum,carry]

def AC6G3(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|C)|(B|D))
    carry = (A&(C|D)|(D&C))
    return [sum,carry]

def AC6G4(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|C)|(B|D))
    carry = (B& (C|D)|(A&C))
    return [sum,carry]

def AC6G5(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|D)|(B|C))
    carry = (B&(C|D)|(A&D))
    return [sum,carry]

def AC6G6(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|D)|(B|C))
    carry = (B&(C|D)|(D&C))
    return [sum,carry]

def AC6G7(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|B)|(C|D))
    carry = ((C&(A|B))|(A&B))
    return [sum,carry]

def AC6G8(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|C)|(B|D))
    carry = ((D&(A|B))|(A&B))
    return [sum,carry]

def AC6G9(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|D)|(B|C))
    carry = ((A&(B|D))|(B&C))
    return [sum,carry]

def AC6G10(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|B)|(C|D))
    carry = ((A&(B|D))|(C&D))
    return [sum,carry]

def AC6G11(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|C)|(B|D))
    carry = ((C&(B|D))|(A&B))
    return [sum,carry]

def AC6G12(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = ((A|D)|(B|C))
    carry = ((C&(B|D))|(A&D))
    return [sum,carry]

# ACFGI compressors
def ACFGI1(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = 1
    carry = A
    return [sum,carry]

def ACFGII1(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = A
    carry = B
    return [sum,carry]

def ACFGII10(A,B,C,D):
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    sum = D
    carry = A
    return [sum,carry]

###############################MULTIPLIER##################
def multiply2(A,B):
    A=bin(A)[2:]
    B=bin(B)[2:]
    A=A.zfill(8)
    B=B.zfill(8)
    L=[]
    N=len(A)
    M=len(B)

    for i in range(M):
        k = []
        for j in range(N):
            k.append(AND(A[j],B[M-1-i]))
        L.append(k)

    ##column 5
    (x20,y20) = akbari(L[0][3],L[1][4],L[2][5],L[3][6])
    (x21,y21) = AC6G5(L[4][7],x20,0,0)

    ##column 6
    (x0,y0)   = AC6G5(L[0][2],L[1][3],L[2][4],L[3][5])
    (x19,y19) = AC6G11(L[4][6],L[5][7],x0,y20)
    (m5,c5)   = half_adder(x19,y21)

    ##column 7
    (x1,y1) = akbari(L[0][1],L[1][2],L[2][3],L[3][4])
    (x2,y2) = momeni(L[4][5],L[5][6],L[6][7],0)
    (x3,y3) = AC6G3(x1,x2,y0,0)
    (m6,c6) = full_adder(x3,y19,c5)

    ##column 8
    (x4,y4) = AC6G1(L[0][0],L[1][1],L[2][2],L[3][3])
    (x5,y5) = AC6G11(L[4][4],L[5][5],L[6][6],L[7][7])
    (x6,y6) = AC6G10(x4,x5,y1,y2)
    (m7,c7) = full_adder(x6,y3,c6)

    ##column 9
    (x7,y7) = AC6G1(L[1][0],L[2][1],L[3][2],L[4][3])
    (x8,y8) = AC6G1(L[5][4],L[6][5],L[7][6],0)
    (x9,y9) = AC6G3(x7,x8,y4,y5)
    (m8,c8) = full_adder(x9,y6,c7)

    ##column 10
    (x10,y10) = AC6G10(L[2][0],L[3][1],L[4][2],L[5][3])
    (x11,y11) = AC6G3(L[6][4],L[7][5],0,0)
    (x12,y12) = AC6G4(x10,x11,y7,y8)
    (m9,c9)   = full_adder(x12,y9,c8)

    ##column 11
    (x13,y13) = momeni(L[3][0],L[4][1],L[5][2],L[6][3])
    (x14,y14) = AC6G10(L[7][4],x13,y10,y11)
    (m10,c10) = full_adder(x14,y12,c9)

    ##column 12
    (x15,y15) = AC6G2(L[4][0],L[5][1],L[6][2],L[7][3])
    (x16,y16) = half_adder(x15,y13)
    (m11,c11) = full_adder(x16,y14,c10)

    ##column 13
    (x17,y17) = meo(L[5][0],L[6][1],L[7][2],y15)
    (m12,c12) = full_adder(x17,y16,c11)

    ##column 14
    (x18,y18) = half_adder(L[6][0],L[7][1])
    (m13,c13) = full_adder(x18,y17,c12)

    ##column 15
    (m14,c14) = full_adder(L[7][0],c13,y18)

    m15 = c14
    m0 = m1 = m2 = m3 = 0
    m4 = x21
    out=[m15,m14,m13,m12,m11,m10,m9,m8,m7,m6,m5,m4,m3,m2,m1,m0]
    result = ''.join(map(str, out))
    return(int(result,2))
