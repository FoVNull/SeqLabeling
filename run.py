import argparse
import pickle
from kashgari.tasks.labeling import BiLSTM_Model, BiGRU_Model, BiLSTM_CRF_Model, BiGRU_CRF_Model, CNN_LSTM_Model
from utils import *

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="build sentiment dictionary")
    parse.add_argument("--model", default="BiLSTM_CRF",
                       help="you can choose [BiLSTM, BiGRU, BiLSTM_CRF, BiGRU_CRF, CNN_LSTM]")
    parse.add_argument("--language", default='Ind', type=str,
                       help='corpus folder should be ./corpus/[Language]')
    parse.add_argument("--evaluate", help="use test dataset for evaluation? [T/F]")
    parse.add_argument("--train", help="T:train model, F:load model")
    args = parse.parse_args()

    train_x, train_y = data_load(args.language, "train")
    valid_x, valid_y = data_load(args.language, "valid")

    assert args.model in ['BiLSTM', 'BiGRU', 'BiLSTM_CRF', 'BiGRU_CRF', 'CNN_LSTM'], \
        """
        you should choose among 
        ['BiLSTM_Model', 'BiGRU_Model', 'BiLSTM_CRF', 'BiGRU_CRF', 'CNN_LSTM']
        """

    model = globals()[args.model + "_Model"]()
    assert args.train in ['T', 'F'] and args.evaluate in ['T', 'F'], "only need T or F"
    if args.train == 'T':
        model.fit(train_x, train_y, valid_x, valid_y, batch_size=64, epochs=15, callbacks=None, fit_kwargs=None)
    else:
        model = model.load_model("./output")
    if args.evaluate == "T":
        test_x, test_y = data_load(args.language, "test")
        report = model.evaluate(test_x, test_y, batch_size=64, digits=4, truncating=False)
        print(report)

    # 测试用例
    if args.language == 'Lao':
        predict_result = model.predict(
            [["ບ່ອນໃດ", "ສາວ", "ງາມ", "ຫລາຍ", "ລະ", "ຮຽນ", "ໂລດ", "ບໍ່", "ສົນ", "ກັບ", "ຫຍັງ", "ເລີຍ", "ອິໆໆໆ"]],
            batch_size=64, truncating=False, predict_kwargs=None)
        # 正解：ບ່ອນໃດ/CLF ສາວ/N ງາມ/V ຫລາຍ/N ລະ/ADV ຮຽນ/V ໂລດ/N ບໍ່/NEG ສົນ/ADJ ກັບ/PRE ຫຍັງ/NTR ເລີຍ/ADV ອິໆໆໆ/IAC
        print(predict_result)
    if args.language == 'Ind':
        predict_result = model.predict(
        [["Namun", "aparat", "yang", "berjaga", "langsung", "sigap", "dan", "menangkap", "kedua", "orang", "itu", "."]],
            batch_size=64, truncating=False, predict_kwargs=None)
        print(predict_result)
        # 正解 Namun/CC aparat/NN yang/PRL berjaga/VB
        # langsung/RB sigap/NN dan/CC menangkap/VB kedua/NN orang/NN itu/DT ./Z

    test_set = pickle.load(open("./corpus/" + args.language + "_test.pkl", "rb"))
    result = model.predict(test_set)
    generate_result(result, test_set, args.language)

    model.save("./output")
