import hashlib
import os.path
import sys

f_dict = dict()


def get_files(path_, file_format_="."):
    for root, dirs, files in os.walk(path_):
        for name in files:
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            file_hash = get_hash(file_path)
            if os.path.splitext(file_path)[-1] == file_format_ or file_format_ == ".":
                f_dict[file_path] = [file_size, file_hash]


def get_hash(path_):
    h_ = hashlib.md5()
    with open(path_, 'rb') as f:
        h_.update(f.read())
        f_hash = h_.hexdigest()
    return f_hash


def sort_files(files_dict):
    while (sort_order := input('Size sorting options:\n1. Descending\n2. Ascending\n')) not in '12':
        print('Wrong option')

    a = [[v[0], v[1], k] for k, v in files_dict.items()]
    a.sort() if sort_order == '2' else a.sort(reverse=True)
    return a


def show_files(_sorted_file):
    _size = None
    for [size, _, filename] in _sorted_file:
        print('', end='') if size == _size else print(f'\n{size} bytes')
        print(f'{filename}')
        _size = size


def check_dup_files(_sorted_file, numbers_to_delete=None):
    dup_files = list()
    _id = 1

    # Use set and remove, create a list of duplicate Hash
    _hash = [_[1] for _ in _sorted_file]
    for _ in set(_hash):
        _hash.remove(_)

    for h in _hash:
        for [size, filehash, filename] in _sorted_file:
            if filehash == h:
                dup_files.append([size, filehash, _id, filename])
                _id += 1
    if numbers_to_delete == None:
        _size = None
        for [size, filehash, _id, filename] in dup_files:
            print('', end='') if size == _size else print(f'\n{size} bytes')
            print(f'Hash: {filehash}')
            print(f'{_id}. {filename}')
            _size = size
    else:
        _size = 0
        for [size, filehash, _id, filename] in dup_files:
            for number in numbers_to_delete:
                if int(number) == _id:
                    os.remove(filename)
                    _size += size
        print(f'\nTotal freed up space: {_size} bytes')


def main():
    # check args
    args = sys.argv
    # args = [argv[0], "../../Duplicate File Handler"]
    if len(args) == 1:
        print('Directory is not specified')
        return

    file_format = '.' + input('Enter file format:')

    get_files(args[-1], file_format)
    sorted_files = sort_files(f_dict)
    show_files(sorted_files)

    while (check_dup := input('\nCheck for duplicates?\n')) not in ['yes', 'no']:
        print('Wrong option')

    if check_dup == 'yes':
        check_dup_files(sorted_files)
    else:
        return

    while (check_dup := input('\nDelete files?\n')) not in ['yes', 'no']:
        print('Wrong option')

    if check_dup == 'yes':
        while not (numbers_to_delete := ''.join(input('\nEnter file numbers to delete:\n').split(' '))).isdigit():
            print('Wrong option')

        check_dup_files(sorted_files, numbers_to_delete)
    else:
        return


if __name__ == '__main__':
    main()
