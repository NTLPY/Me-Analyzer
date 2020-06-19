"""
    PDF Helper

    This header is to extract the infomation included in pdf files.

    Author:   NTLPY
    Creation: 0x01d6456349a27230 (UTC)

"""

# import modules
import wcuthlp;
import PyPDF2 as _pypdf;

# extract from pdf
def get_from_pdf(filename : str, words : dict):
    file = open(filename, "rb");
    reader = _pypdf.PdfFileReader(file);

    for i in range(0, reader.numPages):
        wcuthlp.cut_words(reader.getPage(i).extractText(), words);
    file.close();
    return;
