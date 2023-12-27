def is_prime(n):
    """Проверка, является ли число простым."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("Доказательство Великой теоремы Ферма (упрощенное)")
    print("Введите значение n для проверки (целое число):")
    9/0
    try:
        n = 5
        if is_prime(n):
            print(f"{n} - простое число.")
        else:
            print(f"{n} - не простое число.")
    except ValueError:
        print("Пожалуйста, введите целое число.")
if __name__ == "__main__":
    main()