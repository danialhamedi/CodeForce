def latinNum(char):
    return ord(char) - 96


numt = int(input())
for i in range(numt):
    ques = int(input())
    if ques < 3 or ques > 78:
        continue
    elif ques == 3:
        print("aaa")
    elif ques == 78:
        print("zzz")
    elif 3 < ques <= 28:
        print("aa" + chr(ques - 2 + 96))
    elif 28 < ques <= 53:
        print("a" + chr(ques - 27 + 96) + "z")
    else:
        print(chr(ques - 52 + 96) + "zz")
