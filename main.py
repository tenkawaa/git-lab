def main():
    print("hi")
    try:
        num1 = int(input("введите первое число: "))
        num2 = int(input("введите второе число: "))
    except:
        print("вы ввели не число")
        return


if __name__ == "__main__":
    main()
