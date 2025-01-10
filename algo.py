n,m = map(int, input().split())
dic = {}
for _ in range(m):
    idd, Prob, score = map(str, input().split())
    idd=int(idd)
    score=int(score)
    if idd not in dic:
        dic[idd] = {Prob : score}
    else:
        if Prob not in dic[idd]:
            dic[idd][Prob] = score
        else:
            dic[idd][Prob] = max(dic[idd][Prob], score)

my_score = 0
ans = 0
for i in dic:
    # print(dic[i])
    k_keys = list(dic[i].values())
    k_keys.sort()
    # print(k_keys)
    if i == 1:
        my_score = sum(k_keys)
    else:
        check = 0
        sub_ans = 0
        for i in k_keys:
            check += i
            if check <= my_score:
                sub_ans += 1
            else:
                break
        ans += (len(k_keys)-sub_ans)
print(ans)