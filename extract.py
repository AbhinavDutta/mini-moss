#calculate n^2 jaccard values and create companion of every file
import sys
import glob
import os
import shutil


if os.path.exists("modified_files"):
    shutil.rmtree("modified_files")


os.mkdir("modified_files")

def extract(directory):
    #looks at the sync folder , creates our own folder of exercises
    files = glob.glob(directory + '/**/*.ml',recursive=True)
    for fname in files:
        fname_str = str(fname)
        print(fname_str+"\n")
        if(fname_str[0] == 'X' and fname_str[1] == '/'):
            continue
        stud_id = fname_str.split('/')
        outfilename = ""

        #creating a directory for each exercise
        exercise_name = (stud_id[len(stud_id)-1]).split('.',1)[0]
        if not os.path.exists("modified_files/"+exercise_name):
            os.mkdir("modified_files/"+exercise_name)
        del stud_id[-1]


        #creating a copy
        flip = False
        for wrd in stud_id:
            if(flip):
                outfilename = outfilename+wrd
            if(wrd=="sync"):
                flip=True
        copy_file_name = "modified_files/"+exercise_name+"/"+outfilename+".ml"
        copy_file = open(copy_file_name,'w')

        with open(fname, 'r') as readfile:
            contents = readfile.read()
            copy_file.write(contents)

        
        #creating a companion
        companion_file_name = copy_file_name+"_companion.ml"
        companion_file = open(companion_file_name,'a') 

        for comp in files :
            other_stud_id = str(comp).split('/')
            other_exercise_name = (other_stud_id[len(other_stud_id)-1]).split('.',1)[0]
            if(other_exercise_name != exercise_name):
                continue
            if comp == fname:
                continue
            with open(comp, 'r') as readfile:
                contents = readfile.read()
                companion_file.write(contents)

directory=""      
if(len(sys.argv)>1):
    directory=sys.argv[1]
else:
    directory="/home/abhinav/Desktop/mitacs/code/sync"

extract(directory)
