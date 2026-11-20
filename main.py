def mac(pattern, filt):
    """같은 위치끼리 곱해서(Multiply) 모두 더한다(Accumulate)."""
    n = len(pattern)
    total = 0.0
    for i in range(n):
        for j in range(n):
            total += pattern[i][j] * filt[i][j]
    return total

if __name__ == "__main__":
    cross = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    x     = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    print("십자가 x 십자가 =", mac(cross, cross))   # 기대값 5.0
    print("십자가 x X    =", mac(cross, x))       # 기대값 1.0

