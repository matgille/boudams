import random
from typing import List, Iterator, Tuple, Union
from torchtext.data import Field, ReversibleField, TabularDataset, Dataset, Iterator as TorchIterator, Example


# https://github.com/bentrevett/pytorch-seq2seq/blob/master/1%20-%20Sequence%20to%20Sequence%20Learning%20with%20Neural%20Networks.ipynb
CharacterField: ReversibleField = ReversibleField(tokenize=list, init_token="£", eos_token="$", lower=False)


def get_datasets(train, test, dev) -> Tuple[TabularDataset, TabularDataset, TabularDataset]:
    fields = [("src", CharacterField), ("trg", CharacterField)]
    return (
        TabularDataset(train, format="TSV", fields=fields, skip_header=True),
        TabularDataset(test, format="TSV", fields=fields, skip_header=True),
        TabularDataset(dev, format="TSV", fields=fields, skip_header=True)
    )


def build_vocab(field: ReversibleField, datasets: Iterator[TabularDataset]) -> ReversibleField:
    for dataset in datasets:
        field.build_vocab(dataset)
    return field


def SOS_TOKEN(device="cpu", field=CharacterField):
    inp = [field.init_token]
    return field.numericalize(inp, device=device)


class InputDataset(Dataset):
    def __init__(self, texts: List[str], vocabulary: Field):
        examples = [
            Example.fromdict({"src": list(line)}, fields={"src": [("src", vocabulary)]})
            for line in texts
        ]
        super(InputDataset, self).__init__(
            examples=examples, fields=[("src", vocabulary)]
        )

    def get_iterator(self, batch_size=256):
        return TorchIterator(self, batch_size=batch_size, device="cuda", train=False, sort=False)