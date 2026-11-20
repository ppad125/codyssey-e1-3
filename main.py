import time
EPSILON = 1e-9   # 이 값보다 차이가 작으면 동점으로 본다 (부동소수점 오차 대비)
REPEAT = 10      # 성능 측정 반복 횟수 (미션 최소 기준 10회)

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

def read_matrix(name, n=3):
    """n줄을 입력받아 n×n 숫자 리스트로 돌려준다. 형식이 틀리면 그 줄만 다시 입력받는다."""
    print(f"{name} ({n}줄 입력, 공백 구분)")
    matrix = []
    while len(matrix) < n:
        parts = input().split()
        try:
            row = []
            for v in parts:
                row.append(float(v))
        except ValueError:
            print(f"입력 형식 오류: 각 줄에 {n}개의 숫자를 공백으로 구분해 입력하세요.")
            continue
        if len(row) != n:
            print(f"입력 형식 오류: 각 줄에 {n}개의 숫자를 공백으로 구분해 입력하세요.")
            continue
        matrix.append(row)
    return matrix

def measure_ms(pattern, filt):
    """MAC을 REPEAT번 반복해 평균 시간(ms)을 돌려준다. 입출력은 측정에서 제외."""
    start = time.perf_counter()
    for _ in range(REPEAT):
        mac(pattern, filt)
    return (time.perf_counter() - start) / REPEAT * 1000

def run_mode1():
    print("\n# [1] 필터 입력")
    filter_a = read_matrix("필터 A")
    filter_b = read_matrix("필터 B")
    print("✓ 필터 A, B 저장 완료")

    print("\n# [2] 패턴 입력")
    pattern = read_matrix("패턴")

    print("\n# [3] MAC 결과")
    score_a = mac(pattern, filter_a)
    score_b = mac(pattern, filter_b)
    print("A 점수:", score_a)
    print("B 점수:", score_b)
    result = judge(score_a, score_b)
    if result == "판정 불가":
        print(f"판정: 판정 불가 (|A-B| < {EPSILON})")
    else:
        print("판정:", result)

    print("\n# [4] 성능 분석 (3×3)")
    print(f"평균 연산 시간({REPEAT}회): {measure_ms(pattern, filter_a):.4f} ms / 연산 횟수: {3 * 3}")
    

if __name__ == "__main__":
    print("=== Mini NPU Simulator ===")
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")
    choice = input("선택: ").strip()
    if choice == "1":
        run_mode1()
    elif choice == "2":
        print("모드 2는 다음 단계에서 구현합니다.")
    else:
        print("1 또는 2를 입력하세요.")