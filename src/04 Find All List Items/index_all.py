def index_all(search_list, item, indexes=None):
    if indexes is None:
        indexes = []

    for index, value in enumerate(search_list):
        if value == item:
            yield indexes + [index]
        elif isinstance(value, list):
            yield from index_all(value, item, indexes + [index])


# commands used in solution video for reference
if __name__ == '__main__':
    # Tests
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(list(index_all(example, None)))
    print(list(index_all(example, [])))
    print(list(index_all(example, 4)))
    print(list(index_all(example, [4])))
    print(list(index_all(example, [2])))
    
    example = [1, 2, 3]
    print(list(index_all(example, 2)))
    
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(list(index_all(example, 2)))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(list(index_all(example, [1, 2, 3])))  # [[0, 0], [1]]
