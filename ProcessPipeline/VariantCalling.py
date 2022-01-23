#!/home/lry/miniconda3/bin/python
import os
import time
from configparser import ConfigParser
import argparse
import pathlib
import RunExternalProgram as rep
import CallingProcess as callp

para_f = "para.in"

parser = argparse.ArgumentParser(description="Variants Calling Processing!")
parser.add_argument("-i", "--input", dest="input_f",
        help="Input file for analysis, one sample per line, for paired sequence, the _1 and _2 file was separated by space")
parser.add_argument("-s", "--sample", dest="sample",
        help="file to analysis")
parser.add_argument("-c", "--conf", dest="conf",
        help="Configure file for analysis,default [para.ini]")
parser.add_argument("-w", "--workdir", dest="workdir",
        help="Work dir, default [./]")
parser.add_argument("-m", "--mapdir", dest="mapdir",
        help="map file dir, default [./]")
parser.add_argument("-g", "--gvcfdir", dest="gvcfdir",
        help="gvcf dir, default [./]")

args = parser.parse_args()
if args.conf: para_f = args.conf

cparser = ConfigParser()
cparser.read(para_f)

gatk_path = cparser.get("program","gatkcom")
refseq = cparser.get("sequence","refseq")
mapdir = cparser.get("datadir","mapdir")
haplotypecall_str = cparser.get("gatk","HaplotypeCaller")

cmd_str = haplotypecall_str.format(gatkcom=gatk_path,refseq=refseq,ISM="",OSM="",OSMBAM="")
print(cmd_str)

#result = callp.gatk_HaplotypeCaller(cmd_str,SM, basebam=".basecall.bamout.bam"):
#print(result)
print("Finished!")
