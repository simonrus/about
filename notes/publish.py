#/bin/python3

## Step1 scan recursively over all files

import os
import re
import pdb
import datetime
path = "./notes"
dest = "_posts"
magic_prefix = "Active-"

def extractModifiedDate(string):
    regexp = r"\d+-\d+-\d+T\d+:\d+:\d+.\d+Z"
    date_strings_all = re.findall(regexp,string)
    date = None
    if (len(date_strings_all) == 1):
        date = datetime.datetime.strptime(date_strings_all[0], "%Y-%m-%dT%H:%M:%S.%fZ")

    return date

def processFile(src, dest):   
    state_none = 0
    state_hdr_start = 1
    state_hdr_stop = 2
    state_post_start = 3

    modified_date = None

    print("Process file ", src,  " -> ", dest)

    state = state_none
    skiplines = 0
    with open(src, "r") as f_in, open(dest, "w+") as f_out:
        
        src_lines = f_in.readlines()
       
        for line in src_lines:
            #pdb.set_trace()
           
            if ("---" in line):
                state = state + 1

            if (state == state_post_start):
                break

            skiplines = skiplines + 1

            if state == state_hdr_start:
                if ("modified" in line):
                    modified_date = extractModifiedDate(line)
                    
           

        dest_lines = src_lines[skiplines:]
        
        for i in dest_lines:
            f_out.write(i)
        
        if (modified_date is not None):
            f_out.write(os.linesep)
            f_out.write("*Last update:" + modified_date.strftime("%d %B %Y") + "*" + os.linesep)

        f_in.close()
        f_out.close()

    

for root,d_names,f_names in os.walk(path):    
    if ("notes" in root):
        category = os.path.split(os.path.split(root)[0])[1]
        
        for post_fn in f_names:
            ## Find all with name Active...dd
            print(root, post_fn, f_names)
            if ((post_fn.startswith(magic_prefix)) and (".bak" not in post_fn)):
                #print (root, post_fn)
                new_filename = post_fn[len(magic_prefix):]
                src = os.path.join(root, post_fn)
                dest_filename = os.path.join(dest, new_filename)
                print (root, category, src, "->", dest_filename)
                processFile(src, dest_filename)
                ## Copy file with new name without Active prefix

                




## extract tag, remove first line

