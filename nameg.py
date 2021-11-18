cho = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
joo = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jon = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ',
       'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
dic = {'': 0, 'ㄱ': 2, 'ㄲ': 4, 'ㄴ': 2, 'ㄷ': 3, 'ㄸ': 6, 'ㄹ': 5, 'ㅁ': 4, 'ㅂ': 4, 'ㅃ': 8, 'ㅅ': 2, 'ㅆ': 4, 'ㅇ': 1, 'ㅈ': 3,
       'ㅉ': 6, 'ㅊ': 4, 'ㅋ': 3, 'ㅌ': 4, 'ㅍ': 4, 'ㅎ': 3, 'ㄳ': 4, 'ㄵ': 5, 'ㄶ': 5, 'ㄺ': 7, 'ㄻ': 9, 'ㄼ': 9, 'ㄽ': 7, 'ㄾ': 9,
       'ㄿ': 9, 'ㅀ': 8, 'ㅄ': 6, 'ㅏ': 2, 'ㅐ': 3, 'ㅑ': 3, 'ㅒ': 4, 'ㅓ': 2, 'ㅔ': 3, 'ㅕ': 3, 'ㅖ': 4, 'ㅗ': 2, 'ㅘ': 4, 'ㅙ': 5,
       'ㅚ': 3, 'ㅛ': 3, 'ㅜ': 2, 'ㅝ': 4, 'ㅞ': 5, 'ㅟ': 3, 'ㅠ': 3, 'ㅡ': 1, 'ㅢ': 2, 'ㅣ': 1}


def sum_namenum(nameNum) -> int:
    nameScore = []
    if len(nameNum) == 2:
        n = nameNum[0] * 10 + nameNum[1]
        return n

    for i in range(0, len(nameNum) - 1):
        nameScore.append((nameNum[i] + nameNum[i + 1]) % 10)
    return sum_namenum(nameScore)



def name_number(name):
    ordData = []
    for letter in name:
        ordData.append(ord(letter))

    cnt = 0
    nameNum = []
    for ordnum in ordData:
        chon = dic[cho[(ordnum - 44032) // 588]]
        joon = dic[joo[((ordnum - 44032) % 588) // 28]]
        jonn = dic[jon[((ordnum - 44032 % 588) % 28)]]
        nameNum.append(chon + joon + jonn)
        cnt += 1
    return nameNum


name1 = input()
name2 = input()
nameNum1 = name_number(name1)
nameNum2 = name_number(name2)
nameNum = []
for i in range(0, 3):
    nameNum.append(nameNum1[i])
    nameNum.append(nameNum2[i])

print(sum_namenum(nameNum))
