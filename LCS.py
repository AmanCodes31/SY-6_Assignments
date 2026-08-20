def lcs(X, Y):
    m = len(X)
    n = len(Y)

    lcs_table = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    index = lcs_table[m][n]
    lcs_string = ""

    i = m
    j = n

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string = X[i - 1] + lcs_string
            i = i - 1
            j = j - 1
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i = i - 1
        else:
            j = j - 1

    return lcs_string


X = input("Enter first sequence: ")
Y = input("Enter second sequence: ")

result = lcs(X, Y)

print("Longest Common Subsequence:", result)
print("Length:", len(result))