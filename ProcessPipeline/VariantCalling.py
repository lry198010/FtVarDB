#!/home/lry/miniconda3/bin/python

import os
import time
import RunExternalProgram as rep

def get_num_lines(str_in,sep="\n"):
    lines = str_in.split(sep)
    return(len(lines))

cmd_string="ls -lh /"
result = rep.run_external_prog(get_num_lines,cmd_string, sep="\n")
print(result)
print(get_num_lines("abc\nefg\nefg"))


