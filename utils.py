

def data_load(language, datasets_type) -> tuple:
    data_x = []
    data_y = []
    with open("./corpus/"+language+"/"+language+"_"+datasets_type+".txt", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            seq = line.strip().split("\t")

            data_x.append([e.split("\u200b")[0] for e in seq])
            data_y.append([e.split("\u200b")[1] for e in seq])

    return data_x, data_y
