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
            seq.append(w+"/"+pos)

    with open(output, 'w', encoding='utf-8') as f:
        for seq in texts:
            f.write(" ".join(seq)+"\n")


word2sentence("../corpus/Ind_train-1.txt", "../corpus/Ind_train.txt")