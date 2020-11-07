# SeqLabeling
Build a POS Tagger for Lao and Bahasa Indonesia

### 结构说明
>- corpus 语料文件夹
>- reference 词性对照表等 参考资料
>- output 模型输出
>- preprocess 语料预处理
>>- dataset_split.py 挑选训练/验证/测试集  
>>- format_process.py 调整语料格式
>- utils.py 工具包(与模型训练无直接关联的工作)
>- run.py 模型训练

### 框架修改
基于kashgari框架进行了一些修改，以便于适配词性识别
>- 更改 .../kashgari/metrics/sequence_labeling.py 中的get_entities()函数如下  
```python
def get_entities(seq: List[str], *, suffix: bool = False) -> List[Tuple[str, int, int]]:
    """Gets entities from sequence.
    Args:
        seq: sequence of labels.
        suffix:
    Returns:
        list: list of (chunk_type, chunk_start, chunk_end).
    Example:
        >>> from kashgari.metrics.sequence_labeling import get_entities
        >>> seq = ['B-PER', 'I-PER', 'O', 'B-LOC']
        >>> get_entities(seq)
        [('PER', 0, 1), ('LOC', 3, 3)]
    """
    prev_tag = 'O'
    prev_type = ''
    begin_offset = 0
    chunks = []
    for i, chunk in enumerate(seq + ['O']):
        # if suffix:
        #     tag = chunk[-1]
        #     type_ = chunk.split('-')[0]
        # else:
        #     tag = chunk[0]
        #     type_ = chunk.split('-')[-1]
        #
        # if end_of_chunk(prev_tag, tag, prev_type, type_):
        #     chunks.append((prev_type, begin_offset, i - 1))
        # if start_of_chunk(prev_tag, tag, prev_type, type_):
        #     begin_offset = i
        # prev_tag = tag
        # prev_type = type_
        chunks.append((chunk, i-1, i-1))

    return chunks
```

