import argparse
from kashgari.tasks.labeling import BiLSTM_Model, BiGRU_Model, BiLSTM_CRF_Model, BiGRU_CRF_Model, CNN_LSTM_Model
from utils import data_load

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="build sentiment dictionary")
    parse.add_argument("--model", default="BiGRU_CRF",
                       help="you can choose [BiLSTM, BiGRU, BiLSTM_CRF, BiGRU_CRF, CNN_LSTM]")
    parse.add_argument("--language", default='Ind', type=str,
                       help='corpus folder should be ./corpus/[Language]')
    args = parse.parse_args()

    train_x, train_y = data_load(args.language, "train")
    valid_x, valid_y = data_load(args.language, "valid")
    test_x, test_y = data_load(args.language, "test")

    assert args.model in ['BiLSTM', 'BiGRU', 'BiLSTM_CRF', 'BiGRU_CRF', 'CNN_LSTM'], \
        """
        you should choose between in 
        ['BiLSTM_Model', 'BiGRU_Model', 'BiLSTM_CRF', 'BiGRU_CRF', 'CNN_LSTM']
        """

    model = globals()[args.model + "_Model"]()
    model.fit(train_x, train_y, valid_x, valid_y, batch_size=64, epochs=10, callbacks=None, fit_kwargs=None)
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
    model.save("./output")
