import os
import textwrap
import os.path
import shutil
import sys

pac_path = "data.pac"
tbl_path = "data.tbl"

folder_extract_path = "DATA"

def tbl():
    try:
        tbl_file = open(tbl_path, "rb")
        tbl_file.close()
    except FileNotFoundError as x:
        print ()
        print ("///ERROR///: DATA.TBL file not found.")
        print ()
        a = input("///INPUT///: Press any key to exit...")
        if a:
            exit(0)
        else:
            exit(0)
    else:
        return tbl_file

def pac():
    try:
        pac_file = open(pac_path, "rb")
        pac_file.close()
    except FileNotFoundError as x:
        print ()
        print ("///ERROR///: DATA.PAC file not found.")
        print ()
        a = input("///INPUT///: Press any key to exit...")
        if a:
            exit(0)
        else:
            exit(0)
    else:
        return pac_file

def extraction(tbl_file, pac_file):
    val = 0
    f_n = 0
    f_offset = 8
    offset_list = []
    size_list = []
    tbl_file.seek(0, 0)
    tbl_nof = int.from_bytes(tbl_file.read(4), byteorder = "little")
    for f in range(tbl_nof):
        tbl_file.seek(f_offset, 0)
        offset_list.append(int.from_bytes(tbl_file.read(4), byteorder = "little"))
        f_offset = f_offset + 4
        tbl_file.seek(f_offset, 0)
        size_list.append(int.from_bytes(tbl_file.read(4), byteorder = "little"))
        f_offset = f_offset + 4
    for f in range(tbl_nof):
        fname = folder_extract_path + "\\" + str(f_n).zfill(4) + ".dat"
        file = open(fname, "wb")
        pac_file.seek(offset_list[val])
        data = pac_file.read(size_list[val])
        file.write(data)
        file.close()
        print ("file:", fname, "offset:", hex(offset_list[val]), "size:", size_list[val])
        val = val + 1
        f_n = f_n + 1

def get_paths(arg_list):
    # Gets .PAC, .TBL and Extract Folder paths from command line arguments
    global pac_path
    global tbl_path
    global folder_extract_path
    if len(arg_list) == 1: #If no arguments are passed...
        # Use standard values
        pac_path = "data.pac"
        tbl_path = "data.tbl"
        folder_extract_path = "DATA"

    elif len(arg_list) == 4: # If the right ammount of arguments is passed...
        #Get values from list
        pac_path = arg_list[1]
        tbl_path = arg_list[2]
        folder_extract_path = arg_list[3]
    
    else: #If none of those conditions are met
        exit(1) # Exit program with an error

    


print(textwrap.fill("Ace Combat 5/ZERO DATA.PAC content extractor by death_the_d0g", width = 80))
print(textwrap.fill("=============================================================", width = 80))
print()
print(textwrap.fill("Extracts the contents of the DATA.PAC file.", width = 80))
print()

get_paths(sys.argv)

if os.path.exists(folder_extract_path):
    shutil.rmtree(folder_extract_path)
    os.mkdir(folder_extract_path)
else:
    os.mkdir(folder_extract_path)

tbl_file = tbl()
pac_file = pac()
extraction(tbl_file, pac_file)