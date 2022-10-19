## Ace Combat Zero: The Belkan War DATA.PAC re-builder and DATA.TBL generator by death_the_d0g (death_the_d0g@Twitter)
##====================================================================================================================
## Repacks the contents found in the DATA folder into a new DATA.PAC file
## This is the first Python script I ever wrote as well my first baby steps in the world of programming.
## I'm aware that the code can be inefficient and that it can be further simplified and optimized.
## If you are interested in improving the code and want to share it please let me know.
## I will include it in future releases.


import os
import textwrap

print (textwrap.fill("DATA TBL & PAC rebuilder by death_the_d0g", width = 80))
print (textwrap.fill("=========================================", width = 80))
print (textwrap.fill("This script will process the files inside the DATA folder and create a new DATA.PAC file then generate a new DATA.TBL file with modified offsets/filesizes to accommodate the newly modded files.", width = 80))
print (textwrap.fill("This window will automatically close when the rebuilding process is done.", width = 80))
print ()
print ()
print (textwrap.fill("Rebuilding file, please wait..."))

##Set BASEDIR and variables
basedir = "DATA"
true_nof = 1563
pad = 0
true_nof_hex = true_nof.to_bytes(4, "little")
pad_hex = pad.to_bytes(4, "little")
val = 0
f_offset = 0

##Create empty LISTs and set new variables
filenames = []
f_size_table = []
f_offset_table = []
f_offset_table.append(0) ##Append extra 0 for F_OFFSET

##Create DATA.PAC and DATA.TBL files
new_pac_file = open("DATA.PAC","wb")
append1 =  open("DATA.TBL","wb")

##Append pad data
append1.seek(0,0)
append1.write(true_nof_hex)
append1.seek(4,0)
append1.write(pad_hex)

##Generate F_SIZE and FILENAME LISTs
for f in os.listdir(basedir):
    path = os.path.join(basedir, f)
    fsize = os.path.getsize(path)
    f_size_table.append(fsize)
    filenames.append(path)

# ##Error message stuff
# nof_warning = len(os.listdir(basedir))
# if nof_warning != true_nof:
#     print ()
#     print (textwrap.fill("///ERROR///: The amount of files in the DATA folder is not 1563.", width = 80))
#     print ()
#     append1.close()
#     new_pac_file.close()
#     os.remove("DATA.PAC")
#     os.remove("DATA.TBL")
#     a = input("///INPUT///: Press a key to exit")
#     if a:
#         exit(0)

##Merge all files in DATA folder
for fname in filenames:
    with open(fname, "rb") as infile:
        new_pac_file.write(infile.read())

##Close DATA.PAC
new_pac_file.close()

##Generate new offsets and append them to DATA.TBL
for f in os.listdir(basedir):
    f_offset = f_offset + f_size_table[val]
    f_offset_table.append(f_offset)
    
    file_offset = f_offset_table[val].to_bytes(4, "little")
    file_size = f_size_table[val].to_bytes(4, "little")
    
    append1.write(file_offset)
    append1.write(file_size)

    val += 1

append1.close()
new_pac_file.close()
