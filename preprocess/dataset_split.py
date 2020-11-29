def build_dataset(path, language):
    test = []
    valid = []
    train = []
    length = len(open(path, 'r', encoding="utf-8").readlines())
    with open(path, 'r', encoding="utf-8") as f:
        for i, line in enumerate(f.readlines()):
            seq = line.strip()
            if i <= length*0.25:
                test.append(seq)
            if length*0.25 < i <= length*0.5:
                valid.append(seq)
            if i > length*0.5:
                train.append(seq)
    for entry in {"train": train, "valid": valid, "test": test}.items():
        with open("../corpus/"+language+"/"+language+"_"+entry[0]+".txt", 'w', encoding='utf-8') as f:
            for text in entry[1]:
                f.write(text+"\n")


def build_dataset_test(path, language):
    valid = []
    train = []
    length = len(open(path, 'r', encoding="utf-8").readlines())
    with open(path, 'r', encoding="utf-8") as f:
        for i, line in enumerate(f.readlines()):
            seq = line.strip()
            if i <= length*0.25:
                valid.append(seq)
            if i > length*0.25:
                train.append(seq)
    for entry in {"train": train, "valid": valid}.items():
        with open("../corpus/"+language+"/"+language+"_"+entry[0]+".txt", 'w', encoding='utf-8') as f:
            for text in entry[1]:
                f.write(text+"\n")


# build_dataset("../corpus/Lao_train.txt", "Lao")
build_dataset_test("../corpus/Lao_train.txt", "Lao")