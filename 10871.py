#10871
n, x = map(int, input().split())
n_list = list(map(int, input().split()))
    for i in range(n_list):
        if i < x :
            print(i, end = "")