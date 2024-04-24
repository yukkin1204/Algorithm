'''
しゃくとり法
O(N^2)をO(N)にするテクニック
条件を満たす区間を考える問題で有効
繰り返しにおいて、スタート地点を引き継ぐのがミソ
題材は鉄則A13
'''
N, K = map(int, input().split())
A = list(map(int, input().split()))

R = [0] * N

for i in range(N - 1):
    # スタート地点を決める
    if i == 0:
        R[i] = 0
    else:
        R[i] = R[i - 1]
    # ギリギリまで増やしていく
    while R[i] < N - 1 and A[R[i] + 1] - A[i] <= K:
        R[i] += 1

ans = 0
for i in range(N - 1):
    ans += R[i] - i

print(ans)