"""
    Word Cut Helper

    This header is to cut word.

    Author:   NTLPY
    Creation: 0x01d645706986e470 (UTC)

"""

# import module
import jieba as _jieba;
import re as _re;

# initialization
print("[LOAD MODULE] Loading module `jieba`...");
_jieba.initialize();

# determine text is en
def is_en(text : str) -> bool:
    m_res = _re.match(r"[a-zA-Z]+", text);
    if (m_res == None):
        return False;
    if (m_res.span()[1] != len(text)):
        return False;
    return True;

# determine text is numeric
def is_num(text : str) -> bool:
    m_res = _re.match(r"[0-9]+", text);
    if (m_res == None):
        return False;
    if (m_res.span()[1] != len(text)):
        return False;
    return True;

# determine text is ch (simple)
def is_ch(text : str) -> bool:
    if (u'\u4e00' <= text[0] <= u'\u9fff') :
        return True;
    return False;

# cut words
def cut_words(text : str, words : dict):
    temp = _jieba.lcut(text);
    m_res = None;
    for w in temp:
        #en
        if (is_en(w)):
            words["en"][w.lower()] = words["en"].get(w.lower(), 0) + 1;
        #num
        elif (is_num(w)):
            words["num"][int(w)] = words["num"].get(int(w), 0) + 1;
        #ch
        elif (is_ch(w)):
            words["ch"][w] = words["ch"].get(w, 0) + 1;
        #space
        #elif (_re.match(r"\s+", w).span()[1] == len(w)):
        #    pass;