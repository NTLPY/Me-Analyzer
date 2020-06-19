"""
    GUI Header

    This header is to implement gui operation.

    Author:   NTLPY
    Creation: 0x01d6456349a27230 (UTC)

"""

import tkinter as _tk;

# Retrieve a list of working directories from user
def get_working_dirs():
    def WM_CLICK():
        pass;
    dir_list = [];

    hwnd = _tk.Tk();
    hwnd.title("Me Analyzer");
    hwnd.resizable(width = False, height = False);

    lab1 = _tk.Label(hwnd, text = "Please enter your working directory(s), and then we could analyze it!", wraplength = 320, justify = _tk.LEFT);
    lab1.grid(row = 0, column = 0, padx = 8, pady = 8, columnspan = 2);

    edit = _tk.Entry(hwnd);
    edit.grid(row = 1, column = 0, padx = 8, pady = 8, sticky = _tk.E + _tk.W);

    btn_enter = _tk.Button(hwnd, text = "Add");
    btn_enter.grid(row = 1, column = 1, padx = 8, pady = 8);
    btn_enter.config(command = lambda : lst_dirs.insert(_tk.END, edit.get()));

    lst_dirs = _tk.Listbox(hwnd, );
    lst_dirs.grid(row = 2, column = 0, padx = 8, pady = 8, columnspan = 2, sticky = _tk.E + _tk.W);
    scroll = _tk.Scrollbar(lst_dirs);
    scroll.pack(side = _tk.RIGHT, fill = _tk.Y);
    scroll.config(command = lst_dirs.yview);
    lst_dirs.config(yscrollcommand = scroll.set);

    btn_ok = _tk.Button(hwnd, text = "Okay!");
    btn_ok.grid(row = 3, column = 1, padx = 8, pady = 8);
    btn_ok.config(command = lambda : (dir_list.extend(lst_dirs.get(0, lst_dirs.size())), hwnd.quit()));
    hwnd.mainloop();

    try:
        hwnd.destroy();
    except:
        return None;
    return dir_list;