"""
    File Header

    This header is to implement some basic file operation.

    Author:   NTLPY
    Creation: 0x01d6456045e809a0 (UTC)

"""

import os as _os;

# Retrieve all files' full path in a directory (include child directory)
def track_file(root : str) -> list:
    file_list = [];

    for path, dirs, files in _os.walk(root):
        for file in files:
            file_list.append((path + file) if (path[-1] == "\\") else (path + "\\" + file));

    return file_list;

# Retrieve all files' full path in directories (include child directory)
def track_file_ex(roots : list) -> list:
    file_list = [];

    for root in roots:
        for path, dirs, files in _os.walk(root):
            for file in files:
                file_list.append((path + file) if (path[-1] == "\\") else (path + "\\" + file));

    return file_list;

#get extend name
def get_extended_name(filename : str) -> str:
    ppoint = filename.rfind(".");
    plad = filename.rfind("\\");
    if (ppoint <= plad):
        return "";
    else:
        return filename[ppoint + 1:];