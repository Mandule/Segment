def getChineseDict():
    with open('dict.txt', 'r', encoding='utf-8') as file:
        with open('dict_ch.txt', 'w', encoding='utf-8') as output:
            for line in file.readlines():
                chineseWord = line.split(',')[0].strip()
                output.write(chineseWord + '\n')

def loadDict(path):
    Dict = set()
    maxLen = 0
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip()
            Dict.add(line)
            if maxLen < len(line):
                maxLen = len(line)
    return Dict, maxLen

def singleCount(tokens):
    count = 0
    for token in tokens:
        if len(token) == 1:
            count += 1
    return count

def FMM(s, dic, maxLen):
    left = 0
    tokens = []
    while left < len(s):
        if left + maxLen <= len(s):
            lenght = maxLen
        else:
            lenght = len(s) - left
        for l in range(lenght, 0, -1):
            right = left + l
            if l == 1:
                tokens.append(s[left])
                left = right
            else:
                target = s[left:right]
                if target in dic:
                    tokens.append(target)
                    left = right
                    break
    return tokens

def RMM(s, dic, maxLen):
    right = len(s) - 1
    tokens = []
    while right > -1:
        if right - maxLen >= -1:
            lenght = maxLen
        else:
            lenght = right + 1
        for l in range(lenght, 0, -1):
            left = right - l
            if l == 1:
                tokens.append(s[right])
                right = left
            else:
                target = s[left+1:right+1]
                if target in dic:
                    tokens.append(target)
                    right = left
                    break
    return tokens[::-1]

def BMM(s, dic, maxLen):
    tokens_fmm = FMM(s, dic, maxLen)
    tokens_rmm = RMM(s, dic, maxLen)
    if tokens_fmm == tokens_rmm:
        return tokens_fmm
    else:
        if len(tokens_fmm) < len(tokens_rmm):
            return tokens_fmm
        elif len(tokens_fmm) > len(tokens_rmm):
            return tokens_rmm
        else:
            count_fmm = singleCount(tokens_fmm)
            count_rmm = singleCount(tokens_rmm)
            if count_fmm < count_rmm:
                return tokens_fmm
            else:
                return tokens_rmm

def main():
    dic, maxLen = loadDict('dict_ch.txt')
    while(1):
        sentence = input("please input a chinses sentence : ")
        segments = BMM(sentence, dic, maxLen)
        for token in segments:
            print(token, end=' ')
        print()

if __name__ == "__main__":
    main()
