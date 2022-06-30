#thanks to Shashwat Sanket @shashwatsanket997 for suggesting the use of python difflib module
from difflib import SequenceMatcher
from cleanUP import *
import sys
import glob
import os
import shutil
from functools import cmp_to_key
if os.path.exists("results"):
    shutil.rmtree("results")


os.mkdir("results")

def plagerised_ratio(filename1, filename2):

    tokens1 = tokenize(filename1) #(elements of cleaned up code, their position in original code, position in cleaned up code)
    file1 = toText(tokens1)  #cleaned up code - greatly increases effectiveness of plagiarism checker
    tokens2 = tokenize(filename2)
    file2 = toText(tokens2)
    SM = SequenceMatcher(None, file1, file2)
    similarity_ratio = SM.ratio()
    #print(similarity_ratio)   # ratio of plagiarised content
    
    blocks = list(SM.get_matching_blocks()) #elements  of blocks[] - (start-file1, start-file2, length)
    blocks = blocks[: -1] #remove the last dummy match
    f1 = open(filename1, "r")
    str_l = []
    for i in blocks:
        flag = 0
        start = 0
        end = 0
        for j in range(len(tokens1)):
            if tokens1[j][2] == i[0]:  #linking start of matching block to position in cleaned up code
                start = tokens1[j][1]  #linking position in cleaned up code to position in original code file
                flag = 1
            if tokens1[j][2] == (i[0] + i[2] - 1): #linking end to cleaned up code
                end = tokens1[j][1]  #linking to original code file
                break
        if  flag == 1 and end-start>0 :  #printing significant blocks of plagiarized content
            #the start and end of matching blocks is linked to the original code to properly mark the plagiarized content
            f1.seek(start, 0)
            str_l.append((f1.read(end - start)))
    
    return (similarity_ratio,str_l)

#fn1 = input("Enter the path/name of program 1: ")
#fn2 = input("Enter the path/name of program 2: ")
#plagerised_ratio(fn1, fn2)


class item:
    token = ""
    plag_ratio = 0
    match_list = []

def compare(item1, item2):
    if item1.plag_ratio < item2.plag_ratio :
        return -1
    elif item1.plag_ratio > item2.plag_ratio :
        return 1
    else:
        return 0

# Calling
# list.sort(key=compare)

def compute_plag(directory):
    files = glob.glob(directory + '/**/*.ml',recursive=True)
    list_of_files = []
    
    for fname in files:
        fname_str = str(fname)
        format_f = (fname_str.split('/'))[-1].split('_')

        if(len(format_f)>1 and format_f[1] == "companion.ml"):
            continue
        companion_name = fname_str+"_companion.ml"
        
        duple = plagerised_ratio(fname_str,companion_name)
    
        curr = item()
        curr.token = format_f[0]
        curr.plag_ratio = duple[0]
        curr.match_list = duple[1]
        list_of_files.append(curr)
    
    sorted(list_of_files, key=cmp_to_key(compare))

    print(len(list_of_files))
    for stud in list_of_files :
        print(stud.token)
        print(stud.plag_ratio)
        copy_file_name = "results/"+stud.token+".txt"
        copy_file = open(copy_file_name,'w')

        for str_ in stud.match_list:
            copy_file.write(str_+"\n")
    

compute_plag("/home/abhinav/Desktop/mitacs/code/mini/modified_files/hw1")
        


