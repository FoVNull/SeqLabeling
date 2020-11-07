import argparse
from kashgari.tasks.labeling import BiLSTM_Model, BiGRU_Model, BiLSTM_CRF_Model, BiGRU_CRF_Model, CNN_LSTM_Model
from utils import data_load

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="build sentiment dictionary")
    parse.add_argument("--model", default="BiGRU_CRF",
                       help="you can choose [BiLSTM, BiGRU, BiLSTM_CRF, BiGRU_CRF, CNN_LSTM]")
    parse.add_argument("--language", default='Lao', type=str,
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
    model.fit(train_x, train_y, valid_x, valid_y, batch_size=64, epochs=5, callbacks=None, fit_kwargs=None)
    report = model.evaluate(test_x, test_y, batch_size=32, digits=4, truncating=False)
    print(report)

    # 测试用例
    predict_result = model.predict([["ບ່ອນໃດ", "ສາວ", "ງາມ", "ຫລາຍ"]], batch_size=32, truncating=False, predict_kwargs=None)
    print(predict_result)
    model.save("./output")
