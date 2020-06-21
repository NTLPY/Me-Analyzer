"""
    Me Analyzer Application

    Author:   NTLPY
    Creation: 0x01d6456377c44a80 (UTC)
"""

#import modules
import sys;
import files;
import gui;
import wordcloud;
import random;
import cv2;

import filehlp.wordhlp;
import filehlp.ppthlp;
import filehlp.pdfhlp;
import filehlp.txthlp;
import filehlp.pichlp;

from settings import sets;

"""
    Part I:  Retrieve User's working directory
    Part II: Analyze file

"""

#define variables
file_types = {};
words = { "ch" : {}, "en" : {}, "num" : {}};
pic_types = [0 for i in range(0, filehlp.pichlp.total())];

#---------test region----------#

#------------------------------#

#Retrieve working dirs
work_dirs = gui.get_working_dirs();
if ((work_dirs == None) or (len(work_dirs) == 0)):
    sys.exit(0);

#Retrieve files in working dirs
work_files = files.track_file_ex(work_dirs);

#sort and analyze
i = 0;
for work_file in work_files:
    i += 1;

    ext_name = files.get_extended_name(work_file);
    #collect types of files
    file_types[ext_name.upper()] = file_types.get(ext_name.upper(), 0) + 1;

    print("({}/{}) In parsing: {}".format(i, len(work_files), work_file));
    try:
        # parse doc
        if (ext_name == "doc"):
            #filehlp.wordhlp.get_from_doc(work_file, words);
            pass;
            print("({}/{}) NO Parse DOC: {}".format(i, len(work_files), work_file));

        elif (ext_name == "docx"):
            filehlp.wordhlp.get_from_docx(work_file, words);
            print("({}/{}) Parsed DOCX: {}".format(i, len(work_files), work_file));

        elif (ext_name == "ppt"):
            #filehlp.wordhlp.get_from_doc(work_file, words);
            pass;
            print("({}/{}) NO Parse PPT: {}".format(i, len(work_files), work_file));

        elif (ext_name == "pptx"):
            filehlp.ppthlp.get_from_pptx(work_file, words);
            print("({}/{}) Parsed PPTX: {}".format(i, len(work_files), work_file));

        elif (ext_name == "pdf"):
            if (sets["analyze_pdf"] == "enabled"):
                filehlp.pdfhlp.get_from_pdf(work_file, words);
                print("({}/{}) Parsed PDF : {}".format(i, len(work_files), work_file));
            else:
                print("({}/{}) NO Parse PDF: {}".format(i, len(work_files), work_file));

        elif (ext_name == "txt"):
            filehlp.txthlp.get_from_txt(work_file, words);
            print("({}/{}) Parsed TXT: {}".format(i, len(work_files), work_file));

        elif ((ext_name == "jpg") or (ext_name == "jpeg") or 
              (ext_name == "png") or (ext_name == "bmp")):
            ana_res = filehlp.pichlp.analyze_pic(work_file);
            if (ana_res != None):
                pic_types[ana_res] += 1;
            print("({}/{}) Parsed Picture: {}".format(i, len(work_files), work_file));
            print("catch {}".format(filehlp.pichlp.object_name[ana_res]));

        else:
            print("({}/{}) Unknown file format: {}".format(i, len(work_files), work_file));

    except:
        print("({}/{}) Parse Error: {}".format(i, len(work_files), work_file));

"""
    Part III: analyze data

"""

#filter types
for t in sets["types"]["except"]:
    try:
        del file_types[t.upper()];
    except:
        pass;
if (len(file_types) == 0):
    file_types = { "Oh, we can't find anything in your folder!" : 1};

#filter words: filter, sort
for w in sets["words"]["ch"]["except"]:
    try:
        del words["ch"][w];
    except:
        pass;
words["ch"] = [(k, v) for (k, v) in words["ch"].items() if ((len(k) >= sets["words"]["ch"]["min_len"]) and (v >= sets["words"]["ch"]["min_freq"]))];
words["ch"].sort(key = lambda elem: elem[1], reverse = True);
words["ch"] = words["ch"][:sets["words"]["ch"]["max_count"]];
words["ch"] = dict(words["ch"]);
if (len(words["ch"]) == 0):
    words["ch"] = { "Oh, we can't find anything in your folder!" : 1};

for w in sets["words"]["en"]["except"]:
    try:
        del words["en"][w];
    except:
        pass;
words["en"] = [(k, v) for (k, v) in words["en"].items() if ((len(k) >= sets["words"]["en"]["min_len"]) and (v >= sets["words"]["en"]["min_freq"]))];
words["en"].sort(key = lambda elem: elem[1], reverse = True);
words["en"] = words["en"][:sets["words"]["en"]["max_count"]];
words["en"] = dict(words["en"]);
if (len(words["en"]) == 0):
    words["en"] = { "Oh, we can't find anything in your folder!" : 1};

for w in sets["words"]["num"]["except"]:
    try:
        del words["num"][w];
    except:
        pass;
words["num"] = [(str(k), v) for (k, v) in words["num"].items() if ((k > sets["words"]["num"]["min_value"]) and (v > sets["words"]["num"]["min_freq"]))];
words["num"].sort(key = lambda elem: elem[1], reverse = True);
words["num"] = words["num"][:sets["words"]["num"]["max_count"]];
words["num"] = dict(words["num"]);
if (len(words["num"]) == 0):
    words["num"] = { "Oh, we can't find anything in your folder!" : 1};

#filter pics
pic_types = [(filehlp.pichlp.object_name[i], pic_types[i]) for i in range(len(pic_types)) if (pic_types[i] >= 1)]
pic_types.sort(key = lambda elem: elem[1], reverse = True);
pic_types = pic_types[:sets["pics"]["max_count"]];
pic_types = dict(pic_types);
if (len(pic_types) == 0):
    pic_types = { "Oh, we can't find anything in your folder!" : 1};

"""
    Part IV: Output Result

"""
# generate foreground color in random
def random_color_func(word, font_size, position, orientation, font_path, random_state):
    main_color = random.choice(list(sets["output"]["foreground_color"]));
    return (random.randint(main_color[0] - sets["output"]["foreground_color_max_offset"][0],
                                main_color[0] + sets["output"]["foreground_color_max_offset"][0]),
                 random.randint(main_color[1] - sets["output"]["foreground_color_max_offset"][1],
                                main_color[1] + sets["output"]["foreground_color_max_offset"][1]),
                 random.randint(main_color[2] - sets["output"]["foreground_color_max_offset"][2],
                                main_color[2] + sets["output"]["foreground_color_max_offset"][2]));

# create an word cloud image from a dict
def create_wordcloud_from_freq(freq : dict, font_path : str):

    tmp_cloud = wordcloud.WordCloud(width = sets["output"]["width"],
                                   height = sets["output"]["height"],
                                   mask = sets["output"]["_mask_img"],
                                   color_func = random_color_func,
                                   font_path = font_path,
                                   background_color = sets["output"]["background_color"],
                                   ).generate_from_frequencies(freq);
    return tmp_cloud.to_array()

# show image in a model window
def show_image_model(winname, img):
    while True:
        cv2.imshow(winname, img);

        key = cv2.waitKey(1)
        if key & 0xFF == ord('s'):
            cv2.imwrite(winname + ".bmp", img);
        if key & 0xFF == 27:
            break;
    return cv2.destroyAllWindows();

# generate word cloud
cloud_img = { "tp" : create_wordcloud_from_freq(file_types, sets["output"]["font_tp"]),
              "ch" : create_wordcloud_from_freq(words["ch"], sets["output"]["font_ch"]),
              "en" : create_wordcloud_from_freq(words["en"], sets["output"]["font_en"]),
              "num": create_wordcloud_from_freq(words["num"], sets["output"]["font_num"]),
              "pt" : create_wordcloud_from_freq(pic_types, sets["output"]["font_pt"]),
             };

# show all
show_image_model("Types", cloud_img["tp"]);
show_image_model("Chinese Words", cloud_img["ch"]);
show_image_model("English Words", cloud_img["en"]);
show_image_model("Numeric", cloud_img["num"]);
show_image_model("Picture", cloud_img["pt"]);