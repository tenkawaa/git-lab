def main():
    print("hi")
    try:
        num1 = int(input("введите первое число: "))
        num2 = int(input("введите второе число: "))
    except ValueError:
        print("вы ввели не число")
        return

    result = num1 - num2
    print("результат:", result)


if __name__ == "__main__":
    main()
