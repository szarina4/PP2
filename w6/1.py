import os
WORKING_DIR = os.getcwd()

def align_left(depth):
  print('   ' * depth, end=' ')

def show_dir_content(path, depth = 1):
  for item in os.listdir(path):
    target_path = os.path.join(path, item)
    if os.path.isfile(target_path):
      align_left(depth)
      print(f'FILE: {item}')
    if os.path.isdir(target_path):
      align_left(depth)
      print(f'DIR: {item}')
      show_dir_content(target_path, depth + 2)

show_dir_content(WORKING_DIR)