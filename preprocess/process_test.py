import pickle

test_texts = []
with open("../corpus/Ind_test.txt", 'r', encoding='utf-8') as f:
    seq = []
    for line in f.readlines():
        if line.strip() == "":
            test_texts.append(seq[1:])
            seq = []
            continue
        seq.append(line.strip())

pickle.dump(test_texts, open("../corpus/Ind_test.pkl", 'wb'))

with open("../corpus/Lao_test.txt", 'r', encoding='utf-8') as f:
    print(f.readline().strip().split(" "))