import ast


def save_dict(dict_to_save: dict, file_name: str):
    with open(file_name, 'wb') as fp:
        fp.write(str(dict_to_save))
        fp.flush()


def load_dict(file_name: str) -> dict:
    with open(file_name, 'rb') as fp:
        lines = fp.readlines()
    dict_str = ''.join(lines)
    return ast.literal_eval(dict_str)


# commands used in solution video for reference
if __name__ == '__main__':
    test_dict = {1: 'a', 2: 'b', 3: 'c', 4: {'a': 1, 'b': 2}, 5: [{'c': 1, 'd': 2}, {'c': 3, 'd': 4}]}
    save_dict(test_dict, 'test_dict.pickle')
    recovered = load_dict('test_dict.pickle')
    print(recovered)  # {1: 'a', 2: 'b', 3: 'c', 4: {'a': 1, 'b': 2}, 5: [{'c': 1, 'd': 2}, {'c': 3, 'd': 4}]}
