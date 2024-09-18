def solve(A, B, C):
    dp = [0] * (A + 1)
    if B == 1 or B == A - 1:
        return A % C
    if B > A:
        return 0
    if B == A or B == 0:
        return 1

    dp[0] = 1
    dp[1] = 1
    dp[-1] = 1
    for i in range(1, A + 1):
        for j in range(i//2, 0, -1):
            print(i,j,dp)
            dp[j] = (dp[j] + dp[j - 1]) % C
            print(dp,'here')
            dp[i - j] = dp[j]
            print(i, j, dp)
    return dp[B]

print(solve(5,3,200))