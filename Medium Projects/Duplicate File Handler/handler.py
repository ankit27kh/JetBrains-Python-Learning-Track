import os
import argparse
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str, help='Enter directory', default=False, nargs='?')
args = parser.parse_args()

if not args.dir:
    print('Directory is not specified')
else:
    result = {}

    file_type = input('Enter file format:\n')
    print()

    print("""Size sorting options:
    1. Descending
    2. Ascending""")

    while True:
        print()
        print("Enter a sorting option:")
        option = input()
        if option in ['1', '2']:
            break
        else:
            print('Wrong option')

    if option == '1':
        option = True
    else:
        option = False

    for root, dirs, files in os.walk(args.dir):
        for name in files:
            file_name, file_ext = os.path.splitext(os.path.join(root, name))
            if file_ext == f'.{file_type}' or file_type == '':
                size = os.path.getsize(os.path.join(root, name))
                if size in result.keys():
                    result[size].append(os.path.join(root, name))
                else:
                    result[size] = [os.path.join(root, name)]
    print()
    sizes = result.keys()
    sizes = list(sizes)
    sizes.sort(reverse=option)

    for size in sizes:
        paths = result[size]
        print(size, 'bytes')
        for path in paths:
            print(path)
        print()

    while True:
        print('Check for duplicates?')
        command = input()
        if command in ['yes', 'no']:
            break
        else:
            print('Wrong option')
            print()
    if command == 'no':
        pass
    else:
        hash_table = {}
        duplicate_files = {}
        for size in sizes:
            hash_table[size] = {}
            paths = result[size]
            for path in paths:
                with open(path, 'rb') as file:
                    bytes_ = file.readlines()[0]
                    if (hashlib.md5(bytes_)).hexdigest() in hash_table[size]:
                        hash_table[size][(hashlib.md5(bytes_)).hexdigest()].append(path)
                    else:
                        hash_table[size][(hashlib.md5(bytes_)).hexdigest()] = [path]
        i = 1
        for size, hash_dict in hash_table.items():
            temp = True
            print()
            for hashes, paths in hash_dict.items():
                if len(paths) > 1:
                    if temp:
                        print(f"{size} bytes")
                        temp = False
                    print(f"Hash: {hashes}")
                    for path in paths:
                        print(f"{i}. {path}")
                        duplicate_files[i] = [path, size]
                        i = i + 1
        while True:
            print()
            print("Delete files?")
            command = input()
            if command in ['yes', 'no']:
                break
            else:
                print('Wrong option')
        if command == 'no':
            pass
        else:
            total = 0
            while True:
                print()
                print("Enter file numbers to delete:")
                numbers = input()
                if numbers == '':
                    print("Wrong format")
                    continue
                else:
                    numbers = numbers.split()
                    try:
                        numbers_new = [int(n) for n in numbers if int(n) in list(duplicate_files.keys())]
                        if len(numbers) == len(numbers_new):
                            break
                        else:
                            print("Wrong format")
                            continue
                    except Exception:
                        print("Wrong format")
                        continue
            for n in numbers_new:
                os.remove(duplicate_files[n][0])
                total = total + duplicate_files[n][1]
            print(f"Total freed up space: {total} bytes")
