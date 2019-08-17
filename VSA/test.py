import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description='vsLSTM', formatter_class=RawTextHelpFormatter)
parser.add_argument('-p', '--video_path', dest='video_path')
parser.add_argument('-id', '--id', dest='video_id')
parser.add_argument('-dir', '--sum_dir', dest='dest_dir')
args = parser.parse_args
print(args)