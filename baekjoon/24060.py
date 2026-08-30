# problem: 24060
# tier: silver
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0
result = -1


def merge_sort(p, r):
    if p < r:
        q = (p + r) // 2

        # 배열을 반으로 나눠 각각 정렬
        merge_sort(p, q)
        merge_sort(q + 1, r)

        # 정렬된 두 부분을 하나로 합침
        merge(p, q, r)


def merge(p, q, r):
    global count, result

    i = p
    j = q + 1
    tmp = []

    # 두 배열의 값을 비교하며 작은 값부터 저장
    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1

    # 남은 값들을 순서대로 추가
    while i <= q:
        tmp.append(a[i])
        i += 1

    while j <= r:
        tmp.append(a[j])
        j += 1

    # 병합한 값을 원래 배열에 저장하면서 K번째 값을 확인
    for i in range(p, r + 1):
        a[i] = tmp[i - p]
        count += 1

        if count == k:
            result = a[i]


merge_sort(0, n - 1)
print(result)