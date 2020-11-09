import re


def word2sentence(path, output):
    texts = []
    with open(path, 'r', encoding='utf-8') as f:
        seq = []
        for line in f.readlines():
            if line.strip() == "":
                texts.append(seq)
                seq = []
                continue
            w, pos = line.strip().split("\t")
            seq.append(w+"\u200b"+pos)

    with open(output, 'w', encoding='utf-8') as f:
        for i, seq in enumerate(texts):
            f.write("\t".join(seq)+"\n")


def change_format(path, output):
    texts = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            s = ""
            data = line.strip().split("\t")[1].split("/")
            s += data[0]
            for sub in data[1:-1]:
                p = len(re.findall('[a-zA-Z]', sub))  # 找到词性与词语的分割点(因为词中也有空格所以这么找)
                s += "\u200b" + sub[0:p] + "\t" + sub[p+1:]
            s += "\u200b" + data[-1]
            texts.append(s)

    with open(output, 'w', encoding='utf-8') as f:
        for i, seq in enumerate(texts):
            f.write(seq + "\n")


word2sentence("../corpus/Ind_train-1.txt", "../corpus/Ind_train.txt")
change_format("../corpus/Lao_train-1.txt", "../corpus/Lao_train.txt")