def calculate_power(base, exponent):
    """
    반복문을 사용하여 거듭제곱을 계산하는 함수
    """
    if exponent == 0:
        return 1
    
    result = 1
    abs_exponent = abs(exponent)
    
    for _ in range(abs_exponent):
        result *= base
    
    # 지수가 음수인 경우 1을 결과로 나눔
    if exponent < 0:
        result = 1 / result
    
    return result

def main():
    try:
        # 사용자로부터 숫자 입력받기
        number_input = input("Enter number: ")
        base = float(number_input)
    except ValueError:
        print("Invalid number input.")
        return
    
    try:
        # 사용자로부터 지수 입력받기
        exponent_input = input("Enter exponent: ")
        exponent = int(exponent_input)
    except ValueError:
        print("Invalid exponent input.")
        return
    
    # 거듭제곱 계산
    result = calculate_power(base, exponent)
    
    # 결과가 정수인 경우 정수로 출력, 아닌 경우 소수점 포함하여 출력
    if result == int(result):
        print(f"Result: {int(result)}")
    else:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
