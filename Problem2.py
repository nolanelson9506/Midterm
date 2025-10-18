#Midterm Exam
#Problem2.py
#Name:Nola Nelson
#Date:10/18/25


def countAEIOU(text):
    countA = 0
    countE = 0
    countI = 0
    countO = 0
    countU = 0

    for i in range(len(text)):
            letter = text[i]
            if letter == 'A' or letter == 'a':
                    countA = countA + 1
            elif letter == 'E' or letter == 'e':
                    countE = countE + 1
            elif letter == 'I' or letter == 'i':
                    countI = countI + 1
            elif letter == 'O' or letter == 'o':
                    countO = countO + 1
            elif letter == 'U' or letter == 'u':
                    countU = countU + 1
    return countA, countE, countI, countO, countU

def main():
        sentence = input("Enter a word or sentence: ")
        a, e, i, o, u = countAEIOU(sentence)
        print("A: ", a)
        print("E: ", e)
        print("I: ", i)
        print("O: ", o)
        print("U: ", u)


if __name__ == "__main__":
        main()
