from ast import operator
from math_function import add

def main() :
    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))

    if operator =="+":
        result = add(data_1, data_2)
    print("{} {} {} = {}".format(data_1, operator, data_2, result))

if __name__=="__main__":
    print("Hello main !")
    main()