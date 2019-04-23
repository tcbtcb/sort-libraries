import argparse
import os
import shutil

def sort_samples(source, destination):
    print(os.listdir(source))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='sort through sample libaries')
    parser.add_argument('source', help='samples from ')
    parser.add_argument('destination', help='destination folder')
    args = parser.parse_args()
    print(args)

    sort_samples(args.source, args.destination)
