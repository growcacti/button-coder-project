import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog, messagebox, Toplevel, Frame, Scrollbar

# import tkinter.scrolledtext
from tkinter import scrolledtext as st
from tkinter import *
import tkinter.colorchooser
import os, pathlib
import pyautogui as pg
import pyperclip as pc
import glob
import time


root = tk.Tk()

top = Toplevel()


class Snips:
    def main(self):

        root_frm2 = ttk.Frame(top, width=300, height=100)
        root_frm2.grid(row=0, column=0, rowspan=16, columnspan=2)
        labelframe = tk.LabelFrame(root_frm2, labelanchor="s")
        labelframe.grid(row=1, column=0, sticky="nesw")

        text = st.ScrolledText(labelframe, width=120, height=49, background="mint cream")
        text.grid(row=1, column=0, sticky="nsew")

        def rowcol(ev=None):
            r, c = text.index("insert").split(".")
            labelframe["text"] = f"{r } | {c }"

        text.event_add(
            "<<REACT>>", *("<Motion>", "<ButtonRelease>", "<KeyPress>", "<KeyRelease>")
        )
        b = text.bind("<<REACT>>", rowcol)
        rowcol()  # get the ball rolling
        text.focus()

        ecount = 1
        btncount = 1
        btncount2 = 1
        labelcount = 1
        canvascount = 1
        lboxcount = 1
        rowcount = 1
        columncount = 1
        combocount = 1
        spincount = 1
        textcount = 1
        slidercount = 1
        scrollcount = 1
        projectcount = 1

        number_of_rows = 45

        colors = [
            "AntiqueWhite1",
            "AntiqueWhite2",
            "AntiqueWhite3",
            "AntiqueWhite4",
            "CadetBlue1",
            "CadetBlue2",
            "CadetBlue3",
            "CadetBlue4",
            "DarkGoldenrod1",
            "DarkGoldenrod2",
            "DarkGoldenrod3",
            "DarkGoldenrod4",
            "DarkOliveGreen1",
            "DarkOliveGreen2",
            "DarkOliveGreen3",
            "DarkOliveGreen4",
            "DarkOrange1",
            "DarkOrange2",
            "DarkOrange3",
            "DarkOrange4",
            "DarkOrchid1",
            "DarkOrchid2",
            "DarkOrchid3",
            "DarkOrchid4",
            "DarkSeaGreen1",
            "DarkSeaGreen2",
            "DarkSeaGreen3",
            "DarkSeaGreen4",
            "DarkSlateGray1",
            "DarkSlateGray2",
            "DarkSlateGray3",
            "DarkSlateGray4",
            "DeepPink2",
            "DeepPink3",
            "DeepPink4",
            "DeepSkyBlue2",
            "DeepSkyBlue3",
            "DeepSkyBlue4",
            "DodgerBlue2",
            "DodgerBlue3",
            "DodgerBlue4",
            "HotPink1",
            "HotPink2",
            "HotPink3",
            "HotPink4",
            "IndianRed1",
            "IndianRed2",
            "IndianRed3",
            "IndianRed4",
            "LavenderBlush2",
            "LavenderBlush3",
            "LavenderBlush4",
            "LemonChiffon2",
            "LemonChiffon3",
            "LemonChiffon4",
            "LightBlue1",
            "LightBlue2",
            "LightBlue3",
            "LightBlue4",
            "LightCyan2",
            "LightCyan3",
            "LightCyan4",
            "LightGoldenrod1",
            "LightGoldenrod2",
            "LightGoldenrod3",
            "LightGoldenrod4",
            "LightPink1",
            "LightPink2",
            "LightPink3",
            "LightPink4",
            "LightSalmon2",
            "LightSalmon3",
            "LightSalmon4",
            "LightSkyBlue1",
            "LightSkyBlue2",
            "LightSkyBlue3",
            "LightSkyBlue4",
            "LightSteelBlue1",
            "LightSteelBlue2",
            "LightSteelBlue3",
            "LightSteelBlue4",
            "LightYellow2",
            "LightYellow3",
            "LightYellow4",
            "MediumOrchid1",
            "MediumOrchid2",
            "MediumOrchid3",
            "MediumOrchid4",
            "MediumPurple1",
            "MediumPurple2",
            "MediumPurple3",
            "MediumPurple4",
            "MistyRose2",
            "MistyRose3",
            "MistyRose4",
            "NavajoWhite2",
            "NavajoWhite3",
            "NavajoWhite4",
            "OliveDrab1",
            "OliveDrab2",
            "OliveDrab4",
            "OrangeRed2",
            "OrangeRed3",
            "OrangeRed4",
            "PaleGreen1",
            "PaleGreen2",
            "PaleGreen3",
            "PaleGreen4",
            "PaleTurquoise1",
            "PaleTurquoise2",
            "PaleTurquoise3",
            "PaleTurquoise4",
            "PaleVioletRed1",
            "PaleVioletRed2",
            "PaleVioletRed3",
            "PaleVioletRed4",
            "PeachPuff2",
            "PeachPuff3",
            "PeachPuff4",
            "RosyBrown1",
            "RosyBrown2",
            "RosyBrown3",
            "RosyBrown4",
            "RoyalBlue1",
            "RoyalBlue2",
            "RoyalBlue3",
            "RoyalBlue4",
            "SeaGreen1",
            "SeaGreen2",
            "SeaGreen3",
            "SkyBlue1",
            "SkyBlue2",
            "SkyBlue3",
            "SkyBlue4",
            "SlateBlue1",
            "SlateBlue2",
            "SlateBlue3",
            "SlateBlue4",
            "SlateGray1",
            "SlateGray2",
            "SlateGray3",
            "SlateGray4",
            "SpringGreen2",
            "SpringGreen3",
            "SpringGreen4",
            "SteelBlue1",
            "SteelBlue2",
            "SteelBlue3",
            "SteelBlue4",
            "VioletRed1",
            "VioletRed2",
            "VioletRed3",
            "VioletRed4",
            "alice blue",
            "antique white",
            "aquamarine",
            "aquamarine2",
            "aquamarine4",
            "azure",
            "azure2",
            "azure3",
            "azure4",
            "bisque",
            "bisque2",
            "bisque3",
            "bisque4",
            "blanched almond",
            "blue",
            "blue violet",
            "blue2",
            "blue4",
            "brown1",
            "brown2",
            "brown3",
            "brown4",
            "burlywood1",
            "burlywood2",
            "burlywood3",
            "burlywood4",
            "cadet blue",
            "chartreuse2",
            "chartreuse3",
            "chartreuse4",
            "chocolate1",
            "chocolate2",
            "chocolate3",
            "coral",
            "coral1",
            "coral2",
            "coral3",
            "coral4",
            "cornflower blue",
            "cornsilk2",
            "cornsilk3",
            "cornsilk4",
            "cyan",
            "cyan2",
            "cyan3",
            "cyan4",
            "dark goldenrod",
            "dark green",
            "dark khaki",
            "dark olive green",
            "dark orange",
            "dark orchid",
            "dark salmon",
            "dark sea green",
            "dark slate blue",
            "dark slate gray",
            "dark turquoise",
            "dark violet",
            "deep pink",
            "deep sky blue",
            "dim gray",
            "dodger blue",
            "firebrick1",
            "firebrick2",
            "firebrick3",
            "firebrick4",
            "floral white",
            "forest green",
            "gainsboro",
            "ghost white",
            "gold",
            "gold2",
            "gold3",
            "gold4",
            "goldenrod",
            "goldenrod1",
            "goldenrod2",
            "goldenrod3",
            "goldenrod4",
            "gray",
            "gray1",
            "gray10",
            "gray11",
            "gray12",
            "gray13",
            "gray14",
            "gray15",
            "gray16",
            "gray17",
            "gray18",
            "gray19",
            "gray2",
            "gray20",
            "gray21",
            "gray22",
            "gray23",
            "gray24",
            "gray25",
            "gray26",
            "gray27",
            "gray28",
            "gray29",
            "gray3",
            "gray30",
            "gray31",
            "gray32",
            "gray33",
            "gray34",
            "gray35",
            "gray36",
            "gray37",
            "gray38",
            "gray39",
            "gray4",
            "gray40",
            "gray42",
            "gray43",
            "gray44",
            "gray45",
            "gray46",
            "gray47",
            "gray48",
            "gray49",
            "gray5",
            "gray50",
            "gray51",
            "gray52",
            "gray53",
            "gray54",
            "gray55",
            "gray56",
            "gray57",
            "gray58",
            "gray59",
            "gray6",
            "gray60",
            "gray61",
            "gray62",
            "gray63",
            "gray64",
            "gray65",
            "gray66",
            "gray67",
            "gray68",
            "gray69",
            "gray7",
            "gray70",
            "gray71",
            "gray72",
            "gray73",
            "gray74",
            "gray75",
            "gray76",
            "gray77",
            "gray78",
            "gray79",
            "gray8",
            "gray80",
            "gray81",
            "gray82",
            "gray83",
            "gray84",
            "gray85",
            "gray86",
            "gray87",
            "gray88",
            "gray89",
            "gray9",
            "gray90",
            "gray91",
            "gray92",
            "gray93",
            "gray94",
            "gray95",
            "gray97",
            "gray98",
            "gray99",
            "green yellow",
            "green2",
            "green3",
            "green4",
            "honeydew2",
            "honeydew3",
            "honeydew4",
            "hot pink",
            "indian red",
            "ivory2",
            "ivory3",
            "ivory4",
            "khaki",
            "khaki1",
            "khaki2",
            "khaki3",
            "khaki4",
            "lavender",
            "lavender blush",
            "lawn green",
            "lemon chiffon",
            "light blue",
            "light coral",
            "light cyan",
            "light goldenrod",
            "light goldenrod yellow",
            "light grey",
            "light pink",
            "light salmon",
            "light sea green",
            "light sky blue",
            "light slate blue",
            "light slate gray",
            "light steel blue",
            "light yellow",
            "lime green",
            "linen",
            "magenta2",
            "magenta3",
            "magenta4",
            "maroon",
            "maroon1",
            "maroon2",
            "maroon3",
            "maroon4",
            "medium aquamarine",
            "medium blue",
            "medium orchid",
            "medium purple",
            "medium sea green",
            "medium slate blue",
            "medium spring green",
            "medium turquoise",
            "medium violet red",
            "midnight blue",
            "mint cream",
            "misty rose",
            "navajo white",
            "navy",
            "old lace",
            "olive drab",
            "orange",
            "orange red",
            "orange2",
            "orange3",
            "orange4",
            "orchid1",
            "orchid2",
            "orchid3",
            "orchid4",
            "pale goldenrod",
            "pale green",
            "pale turquoise",
            "pale violet red",
            "papaya whip",
            "peach puff",
            "pink",
            "pink1",
            "pink2",
            "pink3",
            "pink4",
            "plum1",
            "plum2",
            "plum3",
            "plum4",
            "powder blue",
            "purple",
            "purple1",
            "purple2",
            "purple3",
            "purple4",
            "red",
            "red2",
            "red3",
            "red4",
            "rosy brown",
            "royal blue",
            "saddle brown",
            "salmon",
            "salmon1",
            "salmon2",
            "salmon3",
            "salmon4",
            "sandy brown",
            "sea green",
            "seashell2",
            "seashell3",
            "seashell4",
            "sienna1",
            "sienna2",
            "sienna3",
            "sienna4",
            "sky blue",
            "slate blue",
            "slate gray",
            "snow",
            "snow2",
            "snow3",
            "snow4",
            "spring green",
            "steel blue",
            "tan1",
            "tan2",
            "tan4",
            "thistle",
            "thistle1",
            "thistle2",
            "thistle3",
            "thistle4",
            "tomato",
            "tomato2",
            "tomato3",
            "tomato4",
            "turquoise",
            "turquoise1",
            "turquoise2",
            "turquoise3",
            "turquoise4",
            "violet red",
            "wheat1",
            "wheat2",
            "wheat3",
            "wheat4",
            "white smoke",
            "yellow",
            "yellow green",
            "yellow2",
            "yellow3",
            "yellow4",
        ]

        fontlist = [
            "@Arial Unicode MS",
            "@MS Gothic",
            "@MS PGothic",
            "@MS UI Gothic",
            "@Malgun Gothic",
            "@Malgun Gothic Semilight",
            "@Microsoft JhengHei",
            "@Microsoft JhengHei Light",
            "@Microsoft JhengHei UI",
            "@Microsoft JhengHei UI Light",
            "@Microsoft YaHei",
            "@Microsoft YaHei Light",
            "@Microsoft YaHei UI",
            "@Microsoft YaHei UI Light",
            "@MingLiU-ExtB",
            "@MingLiU_HKSCS-ExtB",
            "@NSimSun",
            "@PMingLiU-ExtB",
            "@SimSun",
            "@SimSun-ExtB",
            "@Yu Gothic",
            "@Yu Gothic Light",
            "@Yu Gothic Medium",
            "@Yu Gothic UI",
            "@Yu Gothic UI Light",
            "@Yu Gothic UI Semibold",
            "@Yu Gothic UI Semilight",
            "Agency FB",
            "Algerian",
            "Arabic Transparent",
            "Arial",
            "Arial Baltic",
            "Arial Black",
            "Arial CE",
            "Arial CYR",
            "Arial Greek",
            "Arial Narrow",
            "Arial Rounded MT Bold",
            "Arial TUR",
            "Arial Unicode MS",
            "Bahnschrift",
            "Bahnschrift Condensed",
            "Bahnschrift Light",
            "Bahnschrift Light Condensed",
            "Bahnschrift Light SemiCondensed",
            "Bahnschrift SemiBold",
            "Bahnschrift SemiBold Condensed",
            "Bahnschrift SemiBold SemiConden",
            "Bahnschrift SemiCondensed",
            "Bahnschrift SemiLight",
            "Bahnschrift SemiLight Condensed",
            "Bahnschrift SemiLight SemiConde",
            "Baskerville Old Face",
            "Bauhaus 93",
            "Bell MT",
            "Berlin Sans FB",
            "Berlin Sans FB Demi",
            "Bernard MT Condensed",
            "Blackadder ITC",
            "Bodoni MT",
            "Bodoni MT Black",
            "Bodoni MT Condensed",
            "Bodoni MT Poster Compressed",
            "Book Antiqua",
            "Bookman Old Style",
            "Bookshelf Symbol 7",
            "Bradley Hand ITC",
            "Britannic Bold",
            "Broadway",
            "Brush Script MT",
            "Calibri",
            "Calibri Light",
            "Californian FB",
            "Calisto MT",
            "Cambria",
            "Cambria Math",
            "Candara",
            "Candara Light",
            "Castellar",
            "Centaur",
            "Century",
            "Century Gothic",
            "Century Schoolbook",
            "Chiller",
            "Colonna MT",
            "Comic Sans MS",
            "Consolas",
            "Constantia",
            "Cooper Black",
            "Copperplate Gothic Bold",
            "Copperplate Gothic Light",
            "Corbel",
            "Corbel Light",
            "Courier",
            "Courier New",
            "Courier New Baltic",
            "Courier New CE",
            "Courier New CYR",
            "Courier New Greek",
            "Courier New TUR",
            "Curlz MT",
            "Dubai",
            "Dubai Light",
            "Dubai Medium",
            "Ebrima",
            "Edwardian Script ITC",
            "Elephant",
            "Engravers MT",
            "Eras Bold ITC",
            "Eras Demi ITC",
            "Eras Light ITC",
            "Eras Medium ITC",
            "Felix Titling",
            "Fixedsys",
            "Footlight MT Light",
            "Forte",
            "Franklin Gothic Book",
            "Franklin Gothic Demi",
            "Franklin Gothic Demi Cond",
            "Franklin Gothic Heavy",
            "Franklin Gothic Medium",
            "Franklin Gothic Medium Cond",
            "Freestyle Script",
            "French Script MT",
            "Gabriola",
            "Gadugi",
            "Garamond",
            "Georgia",
            "Gigi",
            "Gill Sans MT",
            "Gill Sans MT Condensed",
            "Gill Sans MT Ext Condensed Bold",
            "Gill Sans Ultra Bold",
            "Gill Sans Ultra Bold Condensed",
            "Gloucester MT Extra Condensed",
            "Goudy Old Style",
            "Goudy Stout",
            "Haettenschweiler",
            "Harlow Solid Italic",
            "Harrington",
            "High Tower Text",
            "HoloLens MDL2 Assets",
            "Impact",
            "Imprint MT Shadow",
            "Informal Roman",
            "Ink Free",
            "Javanese Text",
            "Jokerman",
            "Juice ITC",
            "Kristen ITC",
            "Kunstler Script",
            "Leelawadee UI",
            "Leelawadee UI Semilight",
            "Lucida Bright",
            "Lucida Calligraphy",
            "Lucida Console",
            "Lucida Fax",
            "Lucida Handwriting",
            "Lucida Sans",
            "Lucida Sans Typewriter",
            "Lucida Sans Unicode",
            "MS Gothic",
            "MS Outlook",
            "MS PGothic",
            "MS Reference Sans Serif",
            "MS Reference Specialty",
            "MS Sans Serif",
            "MS Serif",
            "MS UI Gothic",
            "MV Boli",
            "Magneto",
            "Maiandra GD",
            "Malgun Gothic",
            "Malgun Gothic Semilight",
            "Marlett",
            "Matura MT Script Capitals",
            "Microsoft Himalaya",
            "Microsoft JhengHei",
            "Microsoft JhengHei Light",
            "Microsoft JhengHei UI",
            "Microsoft JhengHei UI Light",
            "Microsoft",
            "New Tai Lue",
            "Microsoft PhagsPa",
            "Microsoft Sans Serif",
            "Microsoft Tai Le",
            "Microsoft YaHei",
            "Microsoft YaHei Light",
            "Microsoft YaHei UI",
            "Microsoft YaHei UI Light",
            "Microsoft Yi Baiti",
            "MingLiU-ExtB",
            "MingLiU_HKSCS-ExtB",
            "Mistral",
            "Modern",
            "Modern No. 20",
            "Mongolian Baiti",
            "Monotype Corsiva",
            "Myanmar Text",
            "NSimSun",
            "Niagara Engraved",
            "Niagara Solid",
            "Nirmala UI",
            "Nirmala UI Semilight",
            "OCR A Extended",
            "Old English Text MT",
            "Onyx",
            "PMingLiU-ExtB",
            "Palace Script MT",
            "Palatino Linotype",
            "Papyrus",
            "Parchment",
            "Perpetua",
            "Perpetua Titling MT",
            "Playbill",
            "Poor Richard",
            "Pristina",
            "Rage Italic",
            "Ravie",
            "Rockwell",
            "Rockwell Condensed",
            "Rockwell Extra Bold",
            "Roman",
            "Script",
            "Script MT Bold",
            "Segoe MDL2 Assets",
            "Segoe Print",
            "Segoe Script",
            "Segoe UI",
            "Segoe UI Black",
            "Segoe UI Emoji",
            "Segoe UI Historic",
            "Segoe UI Light",
            "Segoe UI Semibold",
            "Segoe UI Semilight",
            "Segoe UI Symbol",
            "Showcard Gothic",
            "SimSun",
            "SimSun-ExtB",
            "Sitka Banner",
            "Sitka Display",
            "Sitka Heading",
            "Sitka Small",
            "Sitka Subheading",
            "Sitka Text",
            "Small Fonts",
            "Snap ITC",
            "Stencil",
            "Sylfaen",
            "Symbol",
            "System",
            "Tahoma",
            "Tempus Sans ITC",
            "Terminal",
            "Times New Roman",
            "Times New Roman Baltic",
            "Times New Roman CE",
            "Times New Roman CYR",
            "Times New Roman Greek",
            "Times New Roman TUR",
            "Trebuchet MS",
            "Tw Cen MT",
            "Tw Cen MT Condensed",
            "Tw Cen MT Condensed Extra Bold",
            "Univers LT Std 45 Light",
            "Univers LT Std 47 Cn Lt",
            "Univers LT Std 55",
            "Univers LT Std 57 Cn",
            "Verdana",
            "Viner Hand ITC",
            "Vivaldi",
            "Vladimir Script",
            "Webdings",
            "Wide Latin",
            "Wingdings",
            "Wingdings 2",
            "Wingdings 3",
            "Yu Gothic",
            "Yu Gothic Light",
            "Yu Gothic Medium",
            "Yu Gothic UI",
            "Yu Gothic UI Light",
            "Yu Gothic UI Semibold",
            "Yu Gothic UI Semilight",
            "URW Chancery L",
        ]

        def osscandir():
            for entry in os.scandir(sys.argv[1]):
                if entry.is_dir():
                    typ = "dir"
                elif entry.is_file():
                    typ = "file"
                elif entry.is_symlink():
                    typ = "link"
                else:
                    typ = "unknown"
                    tk.messagebox.askokcancel(
                        "{name} {typ}".format(
                            name=entry.name,
                            typ=typ,
                        )
                    )
                print(
                    "{name} {typ}".format(
                        name=entry.name,
                        typ=typ,
                    )
                )

        def runpyprg():
            import runpy

            file = lbox.get(ANCHOR)
            runpy.run_module(file)
            return

        def run():
            import runpy

            x = lbox.curselection()[0]

            runpy.run_module(lbox.get(x))

        def lbox_update():

            path = tk.filedialog.askdirectory()
            flist = os.listdir(path)

            lbox = tk.Listbox(top_frm, height=80, width=30, bd=20)
            lbox.grid(row=1, column=1, rowspan=10, sticky="nsew")

            # THE ITEMS INSERTED WITH A LOOP
            for item in flist:
                lbox.insert(tk.END, item)

            index = lbox.curselection()

            if index:  # if the tuple is not empty
                file = path + "/" + lbox.get(x)
            with open(file, "r", encoding="utf-8") as file:
                file = file.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, file)

        def dirpath():
            path = tk.filedialog.askdirectory()
            flist = os.listdir(path)

            for item in flist:
                lbox.insert(tk.END, item)

            index = lbox.curselection()

            if index:  # if the tuple is not empty
                file = path + "/" + lbox.get(x)
            with open(file, "r", encoding="utf-8") as file:
                file = file.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, file)

        def canvaseventcode():
            can_func_str = """
        def key(event):
            tk.Label(frm3, repr(event.char), text = "pressed".grid(row=0, column=3))

        def xypos(event):
            a=event.x
            b=event.y
            e1 = tk.Label(frm3, text=a , font=('URW Chancery L', 12))
            e1.grid(row=0,column=5)
            e2 = tk.Label(frm3, text=b, font=('URW Chancery L', 12))
            e2.grid(row=11,column=5)
            ttt.insert(tk.END, "X=",)
            ttt.insert(tk.END, a)
            ttt.insert(tk.END, "Y=")
            ttt.insert(tk.END, b)
            ttt.insert(tk.END, "\n")
            #print "clicked at", event.x, event.y"""
            text.insert(tk.END, can_func_str)

        def gencode1():
            genstr = """def num_generator(self,
n):
        num =1
        while True:
        yield num
        if num == n:
          return
        else:
          num += 1
        for i in num_generator(200000000000):
        print (i*i)"""
            text.insert(tk.END, genstr)

        def gencode2():
            genstr2 = """def infinite_sequence():
        num = 0
        while True:
            yield num
            num += 1"""

            text.insert(tk.END, genstr2)

        def cmd():
            pass

        def e_code():
            nonlocal ecount, rowcount
            w_str = (
                """display1 = tk.StringVar()
    entry1 = tk.Entry(root, textvariable=display1, bg='snow')
    entry1.grid(row=3, column=4)"""
                + "\n"
            )
            w_str2 = w_str.replace("display1", "display" + str(ecount))
            w_str3 = w_str2.replace("entry1", "entry" + str(ecount))
            w_str4 = w_str3.replace("row=3", "row=" + str(rowcount))
            text.insert(tk.END, w_str4)
            ecount += 1
            rowcount += 1

        def button_code1():
            nonlocal btncount, rowcount
            w_str = (
                """b1 = tk.Button(root,
                    #relief=tk.FLAT,
                    compound=tk.LEFT,
                    text="new",
                    #command=None,

                    )
    b1.grid(row=1, column=2)"""
                + "\n"
            )
            w_str2 = w_str.replace("b1", "b" + str(btncount))
            w_str3 = w_str2.replace("row=1", "row=" + str(rowcount))
            text.insert(tk.END, w_str3)
            btncount += 1
            rowcount += 1

        def button_code2():
            nonlocal btncount2, columncount
            w_str = (
                """btn1 = tk.Button(root,
                    #relief=tk.FLAT,
                    compound=tk.LEFT,
                    text="new",
                    #command=None,

                    )
    btn1.grid(row=2, column=1)"""
                + "\n"
            )
            w_str2 = w_str.replace("btn1", "btn" + str(btncount2))
            w_str3 = w_str2.replace("column=1", "column=" + str(columncount))
            text.insert(tk.END, w_str3)
            btncount2 += 1
            columncount += 1

        def btnset1():
            btn_str = """btn1=tk.Button(root, text='button 2', bg="light blue", bd=10, command=command)
    btn1.grid(column=1, row=1)
    btn2=tk.Button(root, text='button 2', bg="orange", bd=10, command=command)
    btn2.grid(column=1, row=2)
    btn3=tk.Button(root, text='button 3', bg="yellow", bd=10, command=command)
    btn3.grid(column=1, row=3)
    btn4=tk.Button(root, text='button 4', bg="light green", bd=10, command=command)
    btn4.grid(column=1, row=4)
    btn5=tk.Button(root, text='button 5', bg="pink", bd=10, command=command)
    btn5.grid(column=1, row=5)
    btn6=tk.Button(root, text='button 6', bg="violet", bd=10, command=command)
    btn6.grid(column=1, row=6)"""
            text.insert(tk.END, btn_str)

        def label_code1():
            nonlocal labelcount, rowcount
            label_str = (
                """label1 = tk.Label(root
                ft = tkFont.Font(family='Ariel Black',size=10)
                label1["font"] = ft
                label1["fg"] = "#333333",
                label1["justify"] = "center",
                label1["text"] = "label",
                width=100,height=25)
    label1.grid(row=4, column=2)"""
                + "\n"
            )
            label_str2 = label_str.replace("label1", "label" + str(labelcount))
            label_str3 = label_str2.replace("row=1", "row=" + str(rowcount))
            text.insert(tk.END, label_str3)
            labelcount += 1
            rowcount += 1

        def label_code2():
            nonlocal labelcount, columncount
            label_str = (
                """label1 = tk.Label(root
                ft = tkFont.Font(family='Ariel Black',size=10)
                label1["font"] = ft
                label1["fg"] = "#333333",
                label1["justify"] = "center",
                label1["text"] = "label",
                width=100,height=25)
    label1.grid(row=5, column=2)"""
                + "\n"
            )
            label_str2 = label_str.replace("label1", "label" + str(labelcount))
            label_str3 = label_str2.replace("column=1", "column=" + str(columncount))
            text.insert(tk.END, label_str3)
            labelcount += 1
            columncount += 1

        def listbox_code():
            nonlocal lboxcount
            lbox_str = (
                """lbox1=tk.Listbox(root, width=80, height=25)
            lbox1["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times',size=10)
            lbox1["font"] = ft
            lbox1["fg"] = "#333333"
            lbox1["justify"] = "center"
    lbox1.grid(row=9, coloumn=3)"""
                + "\n"
            )
            lbox_str2 = lbox_str.replace("lbox1", "lbox" + str(lboxcount))
            text.insert(tk.END, lbox_str2)
            lboxcount += 1

        def menu1_code():
            menu1_str = (
                """root.option_add('*tearOff',False)
            menubar = Menu(root)
            root.config(menu = menubar)
            File = Menu(menubar)
            Edit = Menu(menubar)
            Help_ = Menu(menubar)
            menubar.add_cascade( menu = File , label = 'File')
            menubar.add_cascade( menu = Edit , label = 'Edit')
            menubar.add_cascade( menu = Help_, label = 'Help')
            File.add_command( label = 'New', command = lambda: print(" New File"))
            File.add_separator()
            File.add_command( label = 'Open',command = lambda: print("Open File"))
            File.add_separator()
            save = Menu(File)
            File.add_cascade( menu = save , label ='Save')
            save.add_command(label ='Save_as', command = lambda: print(" Save as"))
            save.add_command(label ='Save_all',command = lambda: print(" Save all"))"""
                + "\n"
            )
            text.insert(tk.END, menu1_str)

        def menu2_code():
            menu2_str = (
                """menubar = Menu(root)

    filemenu = Menu(menubar)
    filemenu.add_command(label="Open File",command=open)
    filemenu.add_command(label="New File",command=nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Save",command=nothing)
    filemenu.add_command(label="Save As",command=nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Close",command=close)
    filemenu.add_command(label="Close Tab",command=nothing)
    filemenu.add_command(label="Close rootdow",command=nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=root.quit)

    menubar.add_cascade(label="File", menu = filemenu)

    editmenu = Menu(menubar)
    editmenu.add_command(label="Undo",command=nothing)
    editmenu.add_command(label="Redo",command=nothing)
    editmenu.add_separator()
    editmenu.add_command(label="Copy",command=nothing)
    editmenu.add_command(label="Paste",command=nothing)
    editmenu.add_separator()
    editmenu.add_command(label="Columns",command=nothing)
    editmenu.add_command(label="Lines",command=nothing)
    editmenu.add_command(label="Text",command=nothing)
    editmenu.add_separator()
    editmenu.add_command(label="Exit",command=root.quit)

    menubar.add_cascade(label="Edit", menu = editmenu)

    root.config(menu = menubar)"""
                + "\n"
            )
            text.insert(tk.END, menu2_str)

        def canvas_code1():
            nonlocal canvascount
            canvas_str = (
                """canvas1 = Canvas(root)
            canvas.grid(row=1, column=1)
            canvas.config(width = 700 , height = 800)

            line = canvas.create_line(40,70, 79,140 , fill ='red', width = 7)"""
                + "\n"
            )

            canvas_str2 = canvas_str.replace("canvas1", "canvas" + str(canvascount))
            text.insert(tk.END, canvas_str2)
            canvascount += 1

        def canvascol():
            nonlocal canvascount, columncount
            canvas_str = (
                """canvas1 = Canvas(root, height=300, width=800, background="cornsilk")
    #canvas1.configure( )
    canvas1.grid(row=1, column=1)
    #canvas1.create_line(x1, y1, x2, y2, fill="black" width=1)"""
                + "\n"
            )

            canvas_str2 = canvas_str.replace("canvas1", "canvas" + str(canvascount))

            canvas_str3 = canvas_str.replace("column=1", "column=" + str(columncount))
            canvascount += 1
            columncount += 1

        def canvasrow():
            nonlocal canvascount, rowcount

            canvas_str = (
                """canvas1 = Canvas(root, height=300, width=800, background="cornsilk")
    #canvas.configure( )
    canvase grid(row=1, column=1)"""
                + "\n"
            )

            canvas_str2 = canvas_str.replace("canvas1", "canvas" + str(canvascount))
            lineout1
            canvas_str3 = canvas_str2.replace("row=1", "row=" + str(rowcount))
            canvascount += 1
            rowcount += 1

        def combo_code():
            nonlocal combocount, rowcount
            combo_str = (
                """cb1 = ttk.Combobox(root, values=["Value1", "value2, "value3"])
    cb1.grid(column=0, row=1)"""
                + "\n"
            )
            combo_str2 = combo_str.replace("cb1", "cb" + str(combocount))
            combo_str3 = combo_str2.replace("row=1", "row=" + str(rowcount))
            text.insert(tk.END, combo_str2)
            combocount += 1
            rowcount += 1

        def combo_code2():
            nonlocal combocount, columncount
            combo_str = (
                """cb1 = ttk.Combobox(root, values=["Value1", "value2, "value3"])
    cb1.grid(column=1, row=1)"""
                + "\n"
            )
            combo_str2 = combo_str.replace("cb1", "cb" + str(combocount))
            combo_str3 = combo_str2.replace("column=1", "column=" + str(columncount))
            text.insert(tk.END, combo_str2)
            combocount += 1
            columncount += 1

        def spin_code():
            nonlocal spincount, rowcount
            spin_str = (
                """sp1 = tk.Spinbox(root, from_=1.0, to=1000.0, increment=0.1)
    sp1.grid(row=1, column=0)"""
                + "\n"
            )
            spin_str2 = spin_str.replace("sp1", "sp" + str(spincount))
            spin_str3 = spin_str2.replace("row=1", "row=" + str(rowcount))
            text.insert(tk.END, spin_str2)
            spincount += 1
            rowcount += 1

        def spin_code2():
            nonlocal spincount, columncount
            spin_str = (
                """sp1 = tk.Spinbox(root, from_=1.0, to=1000.0, increment=0.1)
    sp1.grid(row=1, column=0)"""
                + "\n"
            )
            spin_str2 = spin_str.replace("sp1", "sp" + str(spincount))
            spin_str3 = spin_str2.replace("column=1", "column=" + str(columncount))
            text.insert(tk.END, spin_str2)
            spincount += 1
            columncount += 1

        def text_code():
            nonlocal textcount, spincount
            txt_str = (
                """txt1 = tk.Text(root, height=60, width=150, bg='white')
    txt1.insert('1.0', tk.END)
    txt1.grid(row=02, column=3)"""
                + "\n"
            )
            txt_str2 = txt_str.replace("txt1", "txt" + str(textcount))
            text.insert(tk.END, txt_str2)
            textcount += 1

        def slider():
            sld_str = (
                """slider1 = ttk.Scale(slider_str2 = slidar_str.replace("slider1", "slider" + str(slidercount))
            text.insert(tk.END, slider_str2)
            slidercount += 1"""
                + "\n"
            )
            text.insert(tk.END, sld_str)

        def scrollbar():

            # scrollcount not goint to add counter for this yet
            scr_str1 = (
                """scrollbar = tk.Scrollbar(command=text.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    text['yscrollcommand'] = scrollbar.set"""
                + "\n"
            )
            text.insert(tk.END, scr_str1)

        def restartstr():
            text.insert(tk.END, start_string)

        def cleartext():
            text.delete("1.0", tk.END)

        def open_code():
            # file type
            filetypes = [
                ("Python files", "*.py"),
                ("text files", "*.txt"),
                ("All files", "*.*"),
            ]
            # show the open file dialog
            f = filedialog.askopenfile(filetypes=filetypes)
            # read the text file and show its content on the Text
            text.insert("1.0", f.readlines())

        def save_code():

            stop_str = """if __name__== '__main__':
        root.mainloop()"""
            text.insert(tk.END, stop_str)
            filetypes = [
                ("Python files", "*.py"),
                ("Text files", "*.txt"),
                ("All files", "*.*"),
            ]

            projectpy = tk.filedialog.asksaveasfilename(
                title="Open a file", initialdir="/home/jh/Desktop", filetypes=filetypes
            )

        def runcode():
            runpy.run_path(path_name="project.py")

        def rbcode1():
            rb_str = (
                """import tkinter as tk
        from tkinter import *
        root = Tk()
        root.title("App")
        root.geometry('450x400')
        root.configure(bg='light green')
        frame = tk.Frame(root)
        frame.grid(row=0, column=1, rowspan=4, columnspan=4)
        def reset():
        pass

        def execute():
        pass
        Label(root, text='to calculate 2 - 10').grid(row=0, column=0)
        rb1 = Radiobutton(frame, text="2", value=2).grid(row=1, column=1)
        rb2 = Radiobutton(frame, text="3", value=3).grid(row=2, column=1)
        rb3 = Radiobutton(frame, text="4", value=4).grid(row=3, column=1)
        rb4 = Radiobutton(frame, text="5", value=5).grid(row=4, column=1)
        rb5 = Radiobutton(frame, text="6", value=6).grid(row=5, column=1)
        rb6 = Radiobutton(frame, text="7", value=7).grid(row=6, column=1)
        rb7 = Radiobutton(frame, text="8", value=8).grid(row=7, column=1)
        rb8 = Radiobutton(frame, text="9", value=9).grid(row=8, column=1)
        rb9 = Radiobutton(frame, text="10", value=10).grid(row=9, column=1)
        none_Rb = Radiobutton(frame, text="None", value=0).grid(row=10, column=1)


        btn01 = Button(root, text='reset', command=reset, padx=20, pady=5).grid(row=19, column=1)
        btn02 = Button(root, text='execute', command=lambda: execute, padx=20, pady=5).grid(row=20, column=1)

        root.mainloop()"""
                + "\n"
            )
            text.insert(tk.END, rb_str)

        def code1():
            w = (
                """def hort():
    width = 1900
    height = 30
    canvas = Canvas(root, background='blue', width=width, height=height)
    for line in range(0, width, 10): # range(start, stop, step)
    canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w', width=1)

    for line in range(0, height, 10):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h', width=1)

    for line in range(1000, 40, 100): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='light blue', tags='grid_line_w', width=2)

    for list in range(100, 1900, 100): # range(start, stop, step)
        canvas.create_text(list, 20 , text=list, fill="orange",font=('Helvetica 12 bold'))    
            canvas.grid(row=0, column=0)"""
                + "\n"
            )
            text.insert(tk.END, w)

        def code2():
            o = (
                """frm1 = ttk.Frame(root, height=20, width=500)
        frm1.grid(row=0, column=0)
        frm1.columnconfigure(0, weight=6)
        frm1.columnconfigure(1, weight=1)
        frm4 = ttk.Frame(root,height=10, width=100)
        frm4.grid(row=4, column=0)
        root = ttk.Frame(root, height=600, width=1000)
        root.grid(row=6, column=0, columnspan=10, rowspan=3)
        root.columnconfigure(0, weight=20)
        root.columnconfigure(1, weight=8)

        frm3 = ttk.Frame(root, height=500, width=1800)
        frm3.grid(row=10, column=0, columnspan=3)

        frm3.columnconfigure(0, weight=10)
        frm3.columnconfigure(1, weight=10)"""
                + "\n"
            )
            text.insert(tk.END, o)

        def code3():
            t = (
                """tk.Label(frm3, text="Store Temp Values").grid(row=24, column=1)
        lb = tk.Listbox(frm3)
        lb.grid(row=25, column=0)
        lb2 = tk.Listbox(frm3)
        lb2.grid(row=25, column=1)
        lb3 = tk.Listbox(frm3)
        lb3.grid(row=25, column=2)"""
                + "\n"
            )

            text.insert(tk.END, t)

        def code4():
            d = (
                """e1 = tk.Entry(frm1, font=('arial',12,'bold'),bd=20,bg='seashell2', width=10,justify=RIGHT)
        e1.grid(row=1, column=0)"""
                + "\n"
            )

            text.insert(tk.END, d)

        def code5():
            f = """if len(e3.get()) == 0:""" + "\n"
            text.insert(tk.END, f)

        def code6():
            c = """e1.delete(0, END)""" + "\n"
            text.insert(tk.END, c)

        def filetypes():
            fity = (
                """def open_file():
            Open a file for editing.
            filepath = askopenfilename(
                filetypes=[("Python Scripts", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")]
            )"""
                + "\n"
            )

            text.insert(tk.END, fity)

        start_string = (
            """#! /usr/bin/python3
    # proj_str
    import pyautogui as pg
    import pyperclip as pc
    import tkinter as tk
    from tkinter import ttk
    from tkinter import*
    root = tk.Tk()
    root.title("widget helper")

    f1 = ttk.Frame(root, height=300, width=300)
    f1.grid(row=0, rowspan=10, column=5, columnspan=10)
    f2 = ttk.Frame(root, height=300, width=300)
    f2.grid(row=0, column=0, rowspan=5, columnspan=5)"""
            + "\n"
        )

        def save_as_funct1():
            savefilestr = (
                """try:
    filename = filedialog.asksaveasfilename(initialfile="Untitled.txt",
    defaultextension=".txt",
    filetypes=[("All Files", "*.*"),
               ("Text Files", "*.txt"),
               ("Python Scripts", "*.py"),
               ("Markdown Documents", "*.md"),
               ("JavaScript Files", "*.js"),
               ("HTML Documents", "*.html"),
               ("CSS Documents", "*.css")])
    content = text.get(1.0,END)
    with open(filename, "w") as f:
        f.write(content)
    except Exception as e:
        messagebox.showerror("error is ",e)"""
                + "\n"
            )
            text.insert(tk.END, savefilestr)

        def save_as_funct2():
            save_as_str = (
                """def save(event=None):
    file_name = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    def write_to_file(file_name):
                
    try:

        content = text.get(1.0, 'end')

        with open(file_name, 'w') as the_file:

            the_file.write(content)

    except IOError:

        pass
    write_to_file(file_name)"""
                + "\n"
            )
            text.insert(tk.END, save_as_str)

        def smliner():
            gridstr = """.grid(row=1, column=1)""" + "\n"
            text.insert(tk.END, gridstr)

        def smliner2():
            gstr = """. grid(row= , column= , columnspan= , rowspan= ,)""" + "\n"
            text.insert(tk.END, gstr)

        def qukimp():
            qpo = (
                """import tkinter as tk
        from tkinter import ttk
        from tkinter import font
        from tkinter import filedialog, messagebox, Toplevel, Frame
        from tkinter import *
        import os, pathlib
        import pyautogui as pg
        import pyperclip as pc
        import glob
        import time"""
                + "\n"
            )
            text.insert(tk.END, qpo)

        def fontline():
            ftl = """font=['URW Chancery L', 15]""" + "\n"
            text.insert(tk.END, ftl)

        def btngrid():
            forstr = (
                """for button in keys:
            btn = tk.Button(root, text=button, width=5, bg="light yellow", fg="black", highlightthickness=4, 
                               activebackground="cyan", highlightcolor='red', activeforeground="purple", relief="raised", padx=1,
                               pady=1, bd=8, command=lambda x=button, i=varRow-1, j=varColumn: select(x, i, j))
            btn.bind('<Return>', lambda event, x=button, i=varRow-1, j=varColumn: select(x, i, j))
            buttonL[varRow-1].append(btn)
            btn.grid(row=varRow, column=varColumn)
            varColumn += 1
            if varColumn > 20:
                varColumn = 0
                varRow += 1
                buttonL.append([])"""
                + "\n"
            )
            text.insert(tk.END, forstr)

        def grid_rule():
            grid_canvas = (
                """#!/usr/bin/env python3
    import tkinter as tk
    from tkinter import ttk
    from tkinter import Canvas, Frame
    from tkinter import *

    root=tk.Tk()
    notebook = ttk.Notebook(root)
    notebook.grid(row=0, column=0)

    f2 = ttk.Frame(notebook)
    f2.grid(row=0, column=0)

    notebook.add(f2, text="2")
    def checkered(canvas, line_distance):
       # vertical lines at an interval of "line_distance" pixel
       for x in range(line_distance,canvas_width,line_distance):
          canvas.create_line(x, 0, x, canvas_height, fill="#476042")
       # horizontal lines at an interval of "line_distance" pixel
       for y in range(line_distance,canvas_height,line_distance):
          canvas.create_line(0, y, canvas_width, y, fill="#476042")


        canvas_width = 1800
        canvas_height = 900 
        wow = Canvas(f2, 
                   width=canvas_width,
                   height=canvas_height)
        wow.grid(row=0, column=0)
        wow.create_line(10, 450, 1800, 450, fill="black", width=4)
        wow.create_line(900, 10, 900, 900, fill="black", width=4)
        ##########################################################

        wow.create_line(50, 440, 50, 460, fill="blue", width=4)
        wow.create_line(100, 440, 100, 460, fill="blue", width=4)
        wow.create_line(150, 440, 150, 460, fill="blue", width=4)
        wow.create_line(200, 440, 200, 460, fill="blue", width=4)
        wow.create_line(250, 440, 250, 460, fill="blue", width=4)
        wow.create_line(300, 440, 300, 460, fill="blue", width=4)
        wow.create_line(350, 440, 350, 460, fill="blue", width=4)
        wow.create_line(400, 440, 400, 460, fill="blue", width=4)
        wow.create_line(450, 440, 450, 460, fill="blue", width=4)
        wow.create_line(500, 440, 500, 460, fill="blue", width=4)
        wow.create_line(550, 440, 550, 460, fill="blue", width=4)
        wow.create_line(600, 440, 600, 460, fill="blue", width=4)
        wow.create_line(650, 440, 650, 460, fill="blue", width=4)
        wow.create_line(700, 440, 700, 460, fill="blue", width=4)
        wow.create_line(750, 440, 750, 460, fill="blue", width=4)
        wow.create_line(800, 440, 800, 460, fill="blue", width=4)
        wow.create_line(850, 440, 850, 460, fill="blue", width=4)
        wow.create_line(900, 440, 900, 460, fill="blue", width=4)
        wow.create_line(950, 440, 950, 460, fill="blue", width=4)
        wow.create_line(1000, 440, 1000, 460, fill="blue", width=4)
        wow.create_line(1050, 440, 1050, 460, fill="blue", width=4)
        wow.create_line(1100, 440, 1100, 460, fill="blue", width=4)
        wow.create_line(1150, 440, 1150, 460, fill="blue", width=4)
        wow.create_line(1200, 440, 1200, 460, fill="blue", width=4)
        wow.create_line(1250, 440, 1250, 460, fill="blue", width=4)
        wow.create_line(1300, 440, 1300, 460, fill="blue", width=4)
        wow.create_line(1350, 440, 1350, 460, fill="blue", width=4)
        wow.create_line(1400, 440, 1400, 460, fill="blue", width=4)
        wow.create_line(1450, 440, 1450, 460, fill="blue", width=4)
        wow.create_line(1500, 440, 1500, 460, fill="blue", width=4)
        wow.create_line(1550, 440, 1550, 460, fill="blue", width=4)
        wow.create_line(1600, 440, 1600, 460, fill="blue", width=4)
        wow.create_line(1650, 440, 1650, 460, fill="blue", width=4)
        wow.create_line(1700, 440, 1700, 460, fill="blue", width=4)
        wow.create_line(1750, 440, 1750, 460, fill="blue", width=4)
        wow.create_line(1800, 440, 1800, 460, fill="blue", width=4)

        ##########################################################
        wow.create_line(890, 20, 910, 20, fill="blue", width=4)
        wow.create_line(890, 30, 910, 30, fill="blue", width=4)
        wow.create_line(890, 50, 910, 50, fill="blue", width=4)
        wow.create_line(890, 100, 910, 100, fill="blue", width=4)
        wow.create_line(890, 150, 910, 150, fill="blue", width=4)
        wow.create_line(890, 200, 910, 200, fill="blue", width=4)
        wow.create_line(890, 250, 910, 250, fill="blue", width=4)
        wow.create_line(890, 300, 910, 300, fill="blue", width=4)
        wow.create_line(890, 350, 910, 350, fill="blue", width=4)
        wow.create_line(890, 400, 910, 400, fill="blue", width=4)
        wow.create_line(890, 450, 910, 450, fill="blue", width=4)
        wow.create_line(890, 500, 910, 500, fill="blue", width=4)
        wow.create_line(890, 550, 910, 550, fill="blue", width=4)
        wow.create_line(890, 600, 910, 600, fill="blue", width=4)
        wow.create_line(890, 650, 910, 650, fill="blue", width=4)
        wow.create_line(890, 700, 910, 700, fill="blue", width=4)
        wow.create_line(890, 750, 910, 750, fill="blue", width=4)
        wow.create_line(890, 800, 910, 800, fill="blue", width=4)
        wow.create_line(890, 850, 910, 850, fill="blue", width=4)
        wow.create_line(890, 900, 910, 900, fill="blue", width=4)
        wow.create_line(890, 950, 910, 950, fill="blue", width=4)
        wow.create_line(900, 1000, 910, 1000, fill="blue", width=4)

    if __name__ == '__main__':
        checkered(wow,10)
        root.mainloop()"""
                + "\n"
            )

        def mmenu():
            m_str = (
                """from tkinter import *

    root =Tk()
    root.option_add('*tearOff',False)
    menubar =Menu(root)
    root.config(menu = menubar)
    File = Menu(menubar)
    Edit = Menu(menubar)
    Help_ = Menu(menubar)
    menubar.add_cascade( menu = File , label = 'File')
    menubar.add_cascade( menu = Edit , label = 'Edit')
    menubar.add_cascade( menu = Help_, label = 'Help')
    File.add_command( label = 'New', command = lambda: print(" New File"))
    File.add_separator()
    File.add_command( label = 'Open',command = lambda: print("Open File"))
    File.add_separator()
    save = Menu(File)
    File.add_cascade( menu = save , label ='Save')
    save.add_command(label ='Save_as', command = lambda: print(" Save as"))
    save.add_command(label ='Save_all',command = lambda: print(" Save all"))

    root.mainloop()"""
                + "\n"
            )

            text.insert(tk.END, m_str)

        def cmd():
            pass

        def pg1():
            doc1_str = """pg.press("enter")
        """
            text.insert(tk.END, doc1_str)

        def pg015():
            doc1_str2 = (
                """pg.keyDown('alt')
            pg.press('tab')
            pg.press('tab')
            pg.press('tab')
            pg.press('tab')
            pg.press('tab')
            pg.keyUp('alt')
            #pg.hotkey('alt', 'tab', interval=0.25)"""
                + "\n"
            )

            text.insert(tk.END, doc1_str)

        def pg2():
            doc1_str = (
                """pg.hotkey('F4')
         pg.press('enter')
         pg.write('cd /media/jh/Python_Backup')
         pg.press('enter')
         pg.write('pwd')
         pg.press('enter')
         pg.write("find . -name '*.py' | xargs cp -t /home/jh/Desktop/folder")
         pg.press('enter')"""
                + "\n"
            )
            text.insert(tk.END, doc1_str)

        def pg3():
            doc1_str = """pg.click()
            """
            text.insert(tk.END, doc1_str)

        def pg2():
            doc1_str = (
                """pg.press(F4)
    pg.write('sudo dpkg --configure -a', interval=1)"""
                + "\n"
            )
            text.insert(tk.END, doc1_str)

        def pg4():
            doc1_str = """pg.hotkey('ctrl', 'alt', 't')""" + "\n"
            text.insert(tk.END, doc1_str)

        def pg5():
            doc1_str = """text.insert(tk.END, doc1_str)""" + "\n"

        def pg6():
            doc1_str = """pg.hotket('F3')""" + "\n"
            text.insert(tk.END, doc1_str)

        def pg7():
            doc1_str = """pg.hotket('alt', 'F4')""" + "\n"

            text.insert(tk.END, doc1_str)

        def pg8():
            doc1_str = """pg.moveTo(1201, 400, 1)""" + "\n"

            text.insert(tk.END, doc1_str)

        def pg9():
            doc1_str = (
                """pg.hotkey('F4')
                pg.press('enter')
                pg.typewrite('sudo apt install update')
                pg.press('enter', interval=1)
                
                pc.paste
                pg.press('enter')"""
                + "\n"
            )

            text.insert(tk.END, doc1_str)

        def pg10():
            doc1_str = (
                """pg.hotkey('ctrl', 'alt', 't')
            pg.write('ssudo apt-get update', interval=0.5)
            pg.press('enter', interval=1)
            pg.write('uname', interval=1)
            pg.press('enter', interval=1)
            pg.write('sudo dpkg --configure -a', interval=1)
            pg.press('enter', interval=1)
            pg.write('sudo nmap 192.168.5.115/24', interval=1)
            pg.press('enter', interval=1)
            pg.write('mount nfs', interval=1)
            pg.press('enter', interval=1)
            pg.write('pwd', interval=1)
            pg.presss('enter', interval=1)"""
                + "\n"
            )

            text.insert(tk.END, doc1_str)

        def pg11():
            doc1_str = """pg.hotkey("")"""
            text.insert(tk.END, doc1_str)

        def pg12():
            doc1_str = """pg.press("enter")"""
            text.insert(tk.END, doc1_str)

        ##    def pg13():
        ##        doc1_str = '''pg.press("enter")'''
        ##        text.insert(tk.END, doc1_str)
        ##    def pg14():
        ##        doc1_str = '''pg.press("enter")'''
        ##        text.insert(tk.END, doc1_str)
        ##    def pg15():
        ##        doc1_str = '''pg.press("enter")'''
        ##        text.insert(tk.END, doc1_str)
        ##    def pg16():
        ##        doc1_str = '''pg.press("enter")'''
        ##        text.insert(tk.END, doc1_str)
        ##    def pg17():
        ##        doc1_str = '''pg.press("enter")'''
        ##        text.insert(tk.END, doc1_str)
        ##    def pg18():
        ##        doc1_str = '''pg.press("enter")'''
        ##        text.insert(tk.END, doc1_str)
        ##    def pg19():
        ##        doc1_str = '''pg.press("enter")'''
        ##        text.insert(tk.END, doc1_str)
        ##    def pg20():
        ##        doc1_str = '''pg.press("enter")'''
        ##        text.insert(tk.END, doc1_str)
        ##    def pg21():
        ##        doc1_str = '''pg.press("enter")'''
        ##        text.insert(tk.END, doc1_str)
        ##    def pg22():
        ##        doc1_str = '''pg.press("enter")'''
        ##        text.insert(tk.END, doc1_str)
        ##    def pg23():
        ##        doc1_str = '''pg.press("enter")'''
        ##        text.insert(tk.END, doc1_str)
        ##    def pg24():
        ##        doc1_str = '''pg.press("enter")'''
        ##        text.insert(tk.END, doc1_str)
        ##    def pg25():
        ##        doc1_str = '''pg.press("enter")'''
        ##        text.insert(tk.END, doc1_str)
        ##    def pg26():
        ##        doc1_str = '''pg.press("enter")"""
        ##        text.insert(tk.END, doc1_str)"""
        ##
        ##

        btn1 = tk.Button(root, text="pg_Enter", bg="orange", command=pg1)
        btn1.grid(row=5, column=1)
        btn2 = tk.Button(root, text="codeblck alttab", bg="orange", command=pg015)
        btn2.grid(row=6, column=1)
        btn3 = tk.Button(root, text="search & dump code", bg="orange", command=pg2)
        btn3.grid(row=7, column=1)
        btn4 = tk.Button(root, text="mouse click", bg="orange", command=pg3)
        btn4.grid(row=8, column=1)
        btn5 = tk.Button(root, text="ctlr alt t", bg="violet", command=pg4)
        btn5.grid(row=9, column=1)
        btn6 = tk.Button(root, text="terminal", bg="orange", command=pg5)
        btn6.grid(row=10, column=1)
        btn7 = tk.Button(root, text="open app", bg="orange", command=pg6)
        btn7.grid(row=11, column=1)
        btn8 = tk.Button(root, text="alt F4 close", bg="orange", command=pg7)
        btn8.grid(row=12, column=1)
        btn9 = tk.Button(root, text="pg.moveTo", bg="light blue", command=pg8)
        btn9.grid(row=13, column=1)
        btn10 = tk.Button(root, text="apt udate", bg="orange", command=pg9)
        btn10.grid(row=14, column=1)
        btn11 = tk.Button(root, text="Btn1", bg="orange", command=pg10)
        btn11.grid(row=15, column=1)
        btn12 = tk.Button(root, text="Btn1", bg="orange", command=pg11)
        btn12.grid(row=16, column=1)
        btn13 = tk.Button(root, text="Btn1", bg="orange", command=pg12)
        btn13.grid(row=17, column=1)
        aa260 = tk.Button(root, text="CLEAR TEXT", bg="violet", bd=10, command=cleartext)
        aa260.grid(row=18, column=1)
        b2c62 = tk.Button(root, text="          ", bg="violet", command=cmd)
        b2c62.grid(row=19, column=1)
        b2c63 = tk.Button(root, text="       ", bg="violet", command=cmd)
        b2c63.grid(row=20, column=1)

        ##################################################################
        b1 = tk.Button(root, text="Entry Widget", command=e_code)
        b1.grid(row=2, column=2)
        b2 = tk.Button(root, text="Insert Button row", command=button_code1)
        b2.grid(row=3, column=2)
        b55 = tk.Button(root, text="Insert Button column", command=button_code2)
        b55.grid(row=4, column=2)
        b4 = tk.Button(root, text="Insert label row", command=label_code1)
        b4.grid(row=5, column=2)
        b5 = tk.Button(root, text="List Box", command=listbox_code)
        b5.grid(row=6, column=2)
        b6 = tk.Button(root, text="Menu1", command=menu1_code)
        b6.grid(row=7, column=2)
        b7 = tk.Button(root, text="Menu2", command=menu2_code)
        b7.grid(row=8, column=2)
        b8 = tk.Button(root, text="Canvas", command=canvas_code1)
        b8.grid(row=9, column=2)
        b9 = tk.Button(root, text="Combobox", command=combo_code)
        b9.grid(row=10, column=2)
        bba = tk.Button(root, text="Spinbox", command=spin_code)
        bba.grid(row=11, column=2)
        bb1 = tk.Button(root, text="Text Box", command=text_code)
        bb1.grid(row=12, column=2)
        b14 = tk.Button(root, text="insert label col", command=label_code2)
        b14.grid(row=14, column=2)
        b15 = tk.Button(root, text="Slider Widget", command=slider)
        b15.grid(row=15, column=2)
        b16 = tk.Button(root, text="Scroll Bar", command=scrollbar)
        b16.grid(row=16, column=2)
        b17 = tk.Button(root, text="Clear Code Box", command=cleartext)
        b17.grid(row=17, column=2)
        b18 = tk.Button(root, text="Restart 1st Code Block", command=restartstr)
        b18.grid(row=18, column=2)
        b19 = tk.Button(root, text="Finish & Save", command=save_code)
        b19.grid(row=19, column=2)
        b20 = tk.Button(root, text="Open File", command=open_code)
        b20.grid(row=20, column=2)

        b21 = tk.Button(root, text="Run project", command=runcode)
        b21.grid(row=21, column=2)

        #########################################################

        btn93 = tk.Button(root, text="Canvas grid", bg="light blue", command=code1)
        btn93.grid(row=5, column=3)
        btn94 = tk.Button(root, text="ADD 3 Frames", bg="light blue", command=code2)
        btn94.grid(row=6, column=3)
        btn95 = tk.Button(root, text="3 list boxes", bg="light blue", command=code3)
        btn95.grid(row=7, column=3)
        btn96 = tk.Button(root, text="Entry with Border", bg="light blue", command=code4)
        btn96.grid(row=8, column=3)
        btn97 = tk.Button(root, text="if entry empty", bg="light blue", command=code5)
        btn97.grid(row=9, column=3)
        btn98 = tk.Button(root, text="Clear Entry", bg="light blue", command=code6)
        btn98.grid(row=10, column=3)
        btn99 = tk.Button(
            root, text="Save file type code", bg="light blue", command=save_as_funct1
        )
        btn99.grid(row=11, column=3)
        btn100 = tk.Button(
            root, text="Save as Code", bg="light blue", command=save_as_funct2
        )
        btn100.grid(row=12, column=3)
        btn101 = tk.Button(
            root, text=".grid(row, column)", bg="light blue", command=smliner
        )
        btn101.grid(row=13, column=3)
        btn102 = tk.Button(
            root, text="grid(rowspan colspan)", bg="light blue", command=smliner2
        )
        btn102.grid(row=14, column=3)
        btn103 = tk.Button(
            root, text="Quick top line import", bg="light blue", command=qukimp
        )
        btn103.grid(row=15, column=3)
        btn104 = tk.Button(
            root, text="Open file with ftypes", bg="light blue", command=filetypes
        )
        btn104.grid(row=16, column=3)
        btn105 = tk.Button(
            root, text="for loop make button grid", bg="light blue", command=btngrid
        )
        btn105.grid(row=17, column=3)
        btn106 = tk.Button(
            root, text="URW Chancery Font insert", bg="light blue", command=fontline
        )
        btn106.grid(row=18, column=3)
        btn107 = tk.Button(
            root, text="Canvas graph paper", bg="light blue", command=grid_rule
        )
        btn107.grid(row=19, column=3)
        btn108 = tk.Button(root, text="Cascade Menu Code", bg="light blue", command=mmenu)
        btn108.grid(row=20, column=3)
        btn109 = tk.Button(
            root, text="radiobutton code block ", bg="light blue", command=rbcode1
        )
        btn109.grid(row=21, column=3)
        btn909 = tk.Button(root, text="Generator code1", bg="light green", command=gencode1)
        btn909.grid(row=22, column=3)
        ##########################################################################

        btn143 = tk.Button(
            root, text="2func bind xy canvas", bg="orange", command=canvaseventcode
        )
        btn143.grid(row=5, column=4)
        btn144 = tk.Button(root, text="Gen Code2", bg="orange", command=gencode2)
        btn144.grid(row=6, column=4)
        btn145 = tk.Button(root, text="6 button vert", bg="lavender", command=btnset1)
        btn145.grid(row=7, column=4)
        btn146 = tk.Button(root, text="Canvas col", bg="orange", command=canvascol)
        btn146.grid(row=8, column=4)
        btn147 = tk.Button(root, text="Canvas row", bg="orange", command=canvasrow)
        btn147.grid(row=9, column=4)
        btn150 = tk.Button(root, text="combo code2 col", bg="orange", command=combo_code2)
        btn150.grid(row=10, column=4)
        btn151 = tk.Button(root, text="spinbox code2 col", bg="orange", command=spin_code2)
        btn151.grid(row=11, column=4)
        btn152 = tk.Button(root, text="Btn1", bg="orange", command=code1)
        btn152.grid(row=12, column=4)
        btn153 = tk.Button(root, text="Btn1", bg="orange", command=code2)
        btn153.grid(row=13, column=4)
        btn154 = tk.Button(root, text="Btn1", bg="orange", command=code3)
        btn154.grid(row=14, column=4)
        btn155 = tk.Button(root, text="Btn1", bg="orange", command=code4)
        btn155.grid(row=15, column=4)
        btn156 = tk.Button(root, text="Btn1", bg="orange", command=code5)
        btn156.grid(row=16, column=4)
        btn157 = tk.Button(root, text="Btn1", bg="orange", command=code6)
        btn157.grid(row=17, column=4)
        btn158 = tk.Button(root, text="Btn1", bg="orange", command=filetypes)
        btn158.grid(row=18, column=4)
        btn159 = tk.Button(root, text="Btn1", bg="orange", command=cmd)
        btn159.grid(row=19, column=4)
        btn160 = tk.Button(root, text="Btn1", bg="orange", command=cmd)
        btn160.grid(row=20, column=4)
        btn161 = tk.Button(root, text="Btn1", bg="orange", command=cmd)
        btn161.grid(row=21, column=4)
        btn1777 = tk.Button(root, text="Btn1", bg="violet", command=cmd)
        btn1777.grid(row=22, column=4)
        ######################################################
        btn167 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn167.grid(row=5, column=5)
        btn168 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn168.grid(row=6, column=5)
        btn169 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn169.grid(row=7, column=5)
        btn170 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn170.grid(row=8, column=5)
        btn171 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn171.grid(row=9, column=5)
        btn172 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn172.grid(row=10, column=5)

        btn192 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn192.grid(row=11, column=5)
        btn193 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn193.grid(row=12, column=5)
        btn194 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn194.grid(row=13, column=5)
        btn195 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn195.grid(row=14, column=5)
        btn196 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn196.grid(row=15, column=5)
        btn197 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn197.grid(row=16, column=5)
        btn198 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn198.grid(row=17, column=5)
        btn199 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn199.grid(row=18, column=5)
        btn200 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn200.grid(row=19, column=5)

        btn109 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn109.grid(row=20, column=5)
        btn140 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn140.grid(row=21, column=5)
        btn1499 = tk.Button(root, text="Btn1", bg="cyan", command=cmd)
        btn1499.grid(row=22, column=5)


if __name__ == "__main__":
    app=Snips()
    app.main()
    root.mainloop()
