from functools import reduce


def main():
    lst = [0, 1, 2, 3]
    
    l = list(map(lambda x: x * 2, lst))
    print(l)
    
    l = [x * 2 for x in lst]
    print(l)
    
    l = list(filter(lambda x: x % 2 == 0, lst))
    print(l)
    
    sum = reduce(lambda x, y: x + y, lst)
    print(sum)


if __name__ == "__main__":
    main()