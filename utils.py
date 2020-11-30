

def data_load(language, datasets_type) -> tuple:
    data_x = []
    data_y = []
    with open("./corpus/" + language + "/" + language + "_" + datasets_type + ".txt", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            seq = line.strip().split("\t")

            data_x.append([e.split("\u200b")[0] for e in seq])
            data_y.append([e.split("\u200b")[1] for e in seq])

    return data_x, data_y


def generate_result(result, test_set, language):
    task_no = {"Ind": '1', "Lao": '2'}
    # 任务X-队名-prediction-Y.txt
    with open("./output/任务" + task_no[language] + "-DUFLER-prediction-2.txt", 'w', encoding='utf-8') as f:
        for i in range(len(result)):
            if language == "Ind":
                f.write("id:"+str(i)+"\n")
            for j in range(len(test_set[i])):
                f.write(test_set[i][j] + "\t" + result[i][j] + "\n")
            f.write("\n")


