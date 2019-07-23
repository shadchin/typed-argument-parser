from typing import List

from tap import Tap


class MyArgumentParser(Tap):
    """My way better argument parser.

    Attributes:
    :data_path: Path to data file.
        One that is very important!

        An unusually cool path.
    :embedding_path: Path to embedding file.
    :embedding_size: Embedding size.
    :hidden_size: Hidden size.
    """
    data_path: str
    embedding_path: str = '/home'
    embedding_size: int = 1
    hidden_size: int = 2

    def add_arguments(self) -> None:
        self.add_argument('-dp', '--data_path', required=True)
        self.add_argument('--embedding_path')
        self.add_argument('--embedding_size')
        self.add_argument('--hidden_size')

    def process_args(self) -> None:
        if self.embedding_size > self.hidden_size:
            raise ValueError('Embedding size must be greater than hidden size')


class MySimpleArgumentParser(Tap):
    """My even better super simple argument parser.

    Every argument you don't explicitly specify in
    add_arguments is automatically added as
    --variable_name with required specified
    based on whether there's a default value or not.

    Attributes:
    :data_path: Path to data file.
        One that is very important!

        An unusually cool path.
    :embedding_path: Path to embedding file.
    :embedding_size: Embedding size.
    :hidden_size: Hidden size.
    :small_data: Use less data.
    :depths: List of depths.
    """
    data_path: str
    embedding_path: str = '/home'
    embedding_size: int = 1
    hidden_size: int = 2
    small_data: bool = False
    depths: List[int]


if __name__ == '__main__':
    print('Regular argument parser')
    parser = MySimpleArgumentParser()
    args = parser.parse_args()

    print(args.data_path)
    print(args.embedding_path)
    print(args.embedding_size)
    print(args.hidden_size)
    print(args.small_data)
    print(args.depths)
    print()

    print(args.as_dict())
    args.save('args.json')

    print('-' * 30)
    print(args)

    # print('Simple argument parser')
    # parser = MySimpleArgumentParser()
    # args = parser.parse_args()

    # print(args.data_path)
    # print(args.embedding_path)
    # print(args.hidden_size)
    # print()
