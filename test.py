def solve():
    rows, cols = map(int, input().split())
    
    M = []
    for _ in range(rows):
        M.append(list(map(int, input().split())))
    
    M_prime = []
    for _ in range(rows):
        M_prime.append(list(map(int, input().split())))
    
    operations = []
    max_operations = 100000  # Define a reasonable limit for operations
    
    for i in range(rows):
        for j in range(cols):
            if M[i][j] != M_prime[i][j]:
                diff = M_prime[i][j] - M[i][j]
                
                for k in range(cols):
                    if k != j:
                        if len(operations) >= max_operations:
                            print(-1)
                            return
                        operations.append((i + 1, j + 1, i + 1, k + 1, diff // 2))
                        M[i][j] += diff
                        M[i][k] -= diff
                        break
    
    if M == M_prime:
        print(len(operations))
        for op in operations:
            print(" ".join(map(str, op)))
    else:
        print(-1)

if __name__ == "__main__":
    solve()
