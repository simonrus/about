#/bin/python3

## Step1 scan recursively over all files

import os
import pdb
path = "./notes"
dest = "_posts"
magic_prefix = "Active-"

def processFile(src, dest):   
    state_none = 0
    state_hdr_start = 1
    state_hdr_stop = 2
    state_post_start = 3

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
           

        dest_lines = src_lines[skiplines:]
        
        for i in dest_lines:
            f_out.write(i)
        
        f_in.close()
        f_out.close()

    

for root,d_names,f_names in os.walk(path):    
    if ("notes" in root):
        category = os.path.split(os.path.split(root)[0])[1]
        
        for post_fn in f_names:
            ## Find all with name Active...dd
            if ((post_fn.startswith(magic_prefix)) and (".bak" not in post_fn)):
                #print (root, post_fn)
                new_filename = post_fn[len(magic_prefix):]
                src = os.path.join(root, post_fn)
                dest = os.path.join(dest, new_filename)
                #print (root, category, src, "->", dest)
                processFile(src, dest)
                ## Copy file with new name without Active prefix

                




## extract tag, remove first line

