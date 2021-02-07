import os


vars = os.environ
parent_dir = lambda path: os.path.abspath(os.path.join(path, os.pardir))
OS = os.environ['OS']
if OS.startswith('Windows'):
    ROOT_PATH = os.pardir
else:
    ROOT_PATH = parent_dir(os.environ['PWD'])
SRC_PATH = os.path.join(ROOT_PATH, 'src')
STATES_DIR = os.path.join(ROOT_PATH, 'states')
