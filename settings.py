"""
    Settings Header

    This header is to store constant.

    Author:   NTLPY
    Creation: 0x01d645ea4bd4f640 (UTC)

"""

import cv2 as _cv2;

sets = {
    "analyze_region" : {},
    # analyze pdf
    "analyze_pdf" : "disabled",
    # types options
    "types" : {
        "except" : { },
        },

    # words options
    "words" : {
        "ch" : {
            "min_len" : 2,
            "min_freq" : 0,
            "max_count" : 64,
            "except" : { }},
        "en" : {
            "min_len" : 4,
            "min_freq" : 0,
            "max_count" : 64,
            "except" : { "about", "time", "have", "your", "their", "what", "that", "where", "more",
                        "witch", "than", "when", "with", "this", "from", "they", "them", "here",
                        "there", "which", "some", "much", "else"}},
        "num" : {
            "min_value" : 0,
            "min_freq" : 0,
            "max_count" : 64,
            "except" : { }},
        },

    # pics options
    "pics" : {
        "max_count" : 16
        },

    # caffe settings
    "caffe" : {
        "prototxt" :    r"caffe\bvlc_googlenet.prototxt",
        "caffeModel" :  r"caffe\bvlc_googlenet.caffemodel",
        "synset_word" : r"caffe\synset_words.txt",
        "total" :       1000,
        "confidence" :  0.2 },

    # output
    "output" : {
        "width" : 1080,
        "height" : 720,
        "background_color" : "white",
        "foreground_color" : { (0, 162, 232), (255, 127, 39) },
        "foreground_color_max_offset" : (20, 20, 20),
        "mask" : r"res\mask.bmp",
        "_mask_img" : None,
        "font_tp" : r"res\en.ttf",    #显示常用 文件类型 时，使用的字体
        "font_ch"   : r"res\ch.ttf",    #显示常用 中文分词 时，使用的字体
        "font_en" :   r"res\en.ttf",    #显示常用 英文分词 时，使用的字体
        "font_num" :  r"res\en.ttf",    #显示常用 数字 时，使用的字体
        "font_pt" : r"res\en.ttf",    #显示出现最多次 图片的类型 时，使用的字体
        },
    }

sets["output"]["_mask_img"] = _cv2.imread(sets["output"]["mask"]);