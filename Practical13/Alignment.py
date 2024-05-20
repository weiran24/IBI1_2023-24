edit_distance1 = 0
edit_distance2 = 0
edit_distance3 = 0
with open('SLC6A4_RAT.txt','r') as file1:
    lines1 = file1.readlines()
    sequence1 = ''.join(lines1.strip() for lines1 in lines1 if lines1.strip())
with open('SLC6A4_HUMAN.txt','r') as file2:
    lines2 = file2.readlines()
    sequence2 = ''.join(lines2.strip() for lines2 in lines2 if lines2.strip())
with open('SLC6A4_MOUSE.txt','r') as file3:
    lines3 = file3.readlines()
    sequence3 = ''.join(lines3.strip() for lines3 in lines3 if lines3.strip())
for i in range(len(sequence1)):   #human and rat
        if sequence1[i]!=sequence2[i]:
            edit_distance1 += 1
            a = len(sequence1)
            k = 100*(a - edit_distance1)/a
for i in range(len(sequence3)):  #human and mouse
        if sequence3[i]!=sequence2[i]:
            edit_distance2 += 1
            b = len(sequence3)
            l = 100*(b - edit_distance2)/b
for i in range(len(sequence3)):  #rat and mouse
        if sequence3[i]!=sequence1[i]:
            edit_distance3 += 1
            c = len(sequence3)
            m = 100*(c - edit_distance3)/c
global S
global E
global MIN
global amino
global blosum 
S   = -11
E   = -1
MIN = -float("inf")
amino = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '*']
blosum = [
[ 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
[-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
[-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
[-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
[-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4],
[-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4],
[-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4],
[-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4],
[-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4],
[-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4],
[-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4],
[-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4],
[-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
[ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4],
[ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4],
[-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4],
[-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4],
[ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4],
[-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1, -4],
[-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,  1],
]
def _match(s, t, i, j):
    index1=amino.index(t[i-1])
    index2 = amino.index(s[j-1])
    return blosum[index1][index2]
def _init_x(i, j):
    if i > 0 and j == 0:
        return MIN
    else:
        if j > 0:
            return S + E * j
        else:
            return 0
def _init_y(i, j):
    if j > 0 and i == 0:
        return MIN
    else:
        if i > 0:
            return S + E * i
        else:
            return 0
def _init_m(i, j):
    if j == 0 and i == 0:
        return 0
    else:
        if j == 0 or i == 0:
            return MIN
        else:
            return 0
def distance_matrix(s, t):
    dim_i = len(t) + 1
    dim_j = len(s) + 1
    X = [[_init_x(i, j) for j in range(0, dim_j)] for i in range(0, dim_i)]
    Y = [[_init_y(i, j) for j in range(0, dim_j)] for i in range(0, dim_i)]
    M = [[_init_m(i, j) for j in range(0, dim_j)] for i in range(0, dim_i)]
    for j in range(1, dim_j):
        for i in range(1, dim_i):
            X[i][j] = max((S + E + M[i][j-1]), (E + X[i][j-1]))
            Y[i][j] = max((S + E + M[i-1][j]), (E + Y[i - 1][j]))
            M[i][j] = max(_match(s, t, i, j) + M[i - 1][j - 1], X[i][j],
                          Y[i][j])
    return [X, Y, M]
def backtrace(s, t, X, Y, M):

    sequ1 = ''
    sequ2 = ''
    i = len(t)
    j = len(s)
    while (i>0 or j>0):
        if (i>0 and j>0 and M[i][j] == M[i-1][j-1] + _match(s, t, i, j)):
            sequ1 += s[j-1]
            sequ2 += t[i-1]
            i -= 1
            j -= 1
        elif (i>0 and M[i][j] == Y[i][j]):

            sequ1 += '_'
            sequ2 += t[i-1]
            i -= 1

        elif (j>0 and M[i][j] == X[i][j]):
  
            sequ1 += s[j - 1]
            sequ2 += '_'
            j -= 1

    sequ1r = ' '.join([sequ1[j] for j in range(-1, -(len(sequ1)+1), -1)])
    sequ2r = ' '.join([sequ2[j] for j in range(-1, -(len(sequ2)+1), -1)])

    return [sequ1r, sequ2r]


#for example
#human and rat
seq1 = sequence2
seq2 = sequence1

[X, Y, M] = distance_matrix(seq1, seq2)

score=M[len(seq2)][len(seq1)]
print('huamn and rat')
print("Alignment Score:"+ str(score))
print('percentage is ',k)

#huamn and mouse
seq2 = sequence2
seq3 = sequence3

[X, Y, M] = distance_matrix(seq2, seq3)

score=M[len(seq3)][len(seq2)]
print('human and mouse')
print("Alignment Score:"+ str(score))
print('percentage is ',l)

#rat and mouse
seq1 = sequence1
seq3 = sequence3

[X, Y, M] = distance_matrix(seq1, seq3)

score=M[len(seq3)][len(seq1)]
print('rat and mouse')
print("Alignment Score:"+ str(score))
print('percentage is ',m)
