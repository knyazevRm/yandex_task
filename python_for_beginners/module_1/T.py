def get_two_price(N, M, K_1, K_2):
    num_k_1 = (N * (M - K_2)) // (K_1 - K_2)
    num_k_2 = N - num_k_1

    return num_k_1, num_k_2


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    K_1 = int(input())
    K_2 = int(input())

    print(*get_two_price(N, M, K_1, K_2))