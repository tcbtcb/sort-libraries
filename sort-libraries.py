import argparse
import os
import shutil

def get_file_extensions(file_space):
    # useful for debugging, not used in the main function
    exts = []
    for root, dirs, files in file_space:
        for name in files:
            if not name.lower().endswith(('.wav', '.aiff', '.aif', '.mid', '.alp', '.nki')):
                exts.append(name.split('.')[-1])
    exts = set(exts)
    print(exts)



def remove_files_by_type(file_space, source):
   for root, dirs, files in file_space:
      for name in files:
        if not name.lower().endswith(('.wav', '.aiff', '.aif', '.mid', '.alp', '.nki')):
            os.remove((os.path.join(source, name)))


def main(source, destination):
    file_space = os.walk(source)
    remove_files_by_type(file_space, source)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='sort through sample libaries')
    parser.add_argument('source', help='samples from ')
    parser.add_argument('destination', help='destination folder')
    args = parser.parse_args()
    print(args)

    main(args.source, args.destination)
