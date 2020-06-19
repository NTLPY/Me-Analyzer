"""
    Text Helper

    This header is to get infomation from text file.

    Author:   NTLPY
    Creation: 0x01d645706986e470 (UTC)

"""

import wcuthlp;

# extract from txt
def get_from_txt(filename : str, words : dict):
    file = open(filename);
    wcuthlp.cut_words(file.read(), words);
    pass;

