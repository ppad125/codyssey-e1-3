EPSILON = 1e-9   # 이 값보다 차이가 작으면 동점으로 본다 (부동소수점 오차 대비)


def mac(pattern, filt):
    """같은 위치끼리 곱해서(Multiply) 모두 더한다(Accumulate)."""
    n = len(pattern)
    total = 0.0
    for i in range(n):
        for j in range(n):
            total += pattern[i][j] * filt[i][j]
    return total


def judge(score_a, score_b):
    """두 점수를 비교해 'A', 'B', '판정 불가' 중 하나를 돌려준다."""
    if abs(score_a - score_b) < EPSILON:   # 동점 검사를 가장 먼저
        return "판정 불가"
    elif score_a > score_b:
        return "A"
    else:
        return "B"


if __name__ == "__main__":
    cross = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    x     = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    print("십자가 x 십자가 =", mac(cross, cross))   # 기대값 5.0
    print("십자가 x X    =", mac(cross, x))       # 기대값 1.0
    print("판정(십자가 vs X 필터, 십자가 입력) =", judge(mac(cross, cross), mac(cross, x)))  # 기대: A

    s = 0.0
    for _ in range(9):
        s += 0.1
    print("0.9 vs 0.1x9 =", 0.9, s, "→", judge(0.9, s))   # 기대: 판정 불가