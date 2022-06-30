#calculate the plag
import sys
import glob
import seqMatcher


n=len(sys.argv)
class item:
    token = ""
    plag_ratio = 0
    match_list = []

def compare(item1, item2):
    if item1.plag_ratio < item2.plag_ratio :
        return -1
    elif item1.plag_ratio < item2.plag_ratio :
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
        format_f = fname_str.split('_')
      
        if(len(format_f)>1 and format_f[1] == "companion.ml"):
            continue
        companion_name = fname_str+"_companion.ml"
        
        duple = plagerised_ratio(directory+fname_str,directory+companion_name)
    '''
        curr = item()
        curr.token = fname_str.split('.')[0]
        curr.plag_ratio = duple[0]
        curr.match_list = duple[1]
        list_of_files.append(curr)
    
    list_of_files.sort(key=compare)
    
    for stud in list_of_files :
        print("%s ,  %lf \n" % (stud.token,stud.plag_ratio))
        copy_file_name = "results/"++"/"+stud.token+".txt"
        copy_file = open(copy_file_name,'w')

        for str in stud.match_list:
            copy_file.write(str+"\n")
    '''

compute_plag("/home/abhinav/Desktop/mitacs/code/mini/modified_files/hw1")
        


