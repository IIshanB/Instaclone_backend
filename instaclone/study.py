def solve( A, B):
    i = 0

    n = len(A)
    Mod = 10 ** 9 + 7
    j = n - 1

    cnt = 0
    while (i < j):

        x, y = A[i], A[j]

        sumx = x + y

        if sumx == B:
            temp1 = 1
            temp2 = 1
            i+=1
            j-=1
            while (i <= j and A[i] == x):
                temp2 += 1
                print(i, j, x, y,A[i], 'j')
                i += 1
            while (i <=j and A[j] == y):
                temp1 += 1
                print(i,j,x,y,A[j],'i')
                j -= 1

            print(temp1,temp2,cnt)
            cnt += (temp1 * temp2) % Mod

            print(cnt)
        elif sumx> B:
            j -= 1
        else:
            i += 1

    return cnt

A=[2,2,3,4,4,5,6,7,10]
A2=[1,1,1,2,2,3,4,5,6,7,8,9]
B=2
B2=8
print(solve(A2
            ,B))