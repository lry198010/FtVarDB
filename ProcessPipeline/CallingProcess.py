import os
import time
import configparser
import argparse
import pathlib
import RunExternalProgram as rep

def prepare_files(wd,files,move_to_wd=True):
    '''
    prepare file for analysis,if move_to_wd is true, then
    all input file and output file will copy or output in 
    the work dir, and the function return the files 
    modified path
    '''
    new_files = {}
    for k, v in files.item():
        new_files[k] = v

    if move_to_wd:
        for k, v in new_files.item():
            if pathlib.path(v).exists():


def fastqdump():
    pass

def QC():
    pass

def read_align():
    pass

def gatk_HaplotypeCaller(cmd_str,SM, basebam=".basecall.bamout.bam"):
    '''
Run gatk HaplotypeCaller
    '''
    pathlib.Path(basebam).touch()
    with open(SM + basebam,"w") as f:
        pass
    result = rep.run_external_prog(None, cmd_str)
    return(result) 

def gatk_CombinGVCFs():
    pass
