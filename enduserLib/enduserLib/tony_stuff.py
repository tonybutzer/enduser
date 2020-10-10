import os
def tony_mkdir(directory):
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
