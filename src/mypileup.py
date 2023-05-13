#!/usr/bin/env python

"""
Command-line script to perform  pileup of BAM files

Similar to samtools mpileup
"""

import argparse

def main():
    parser = argparse.ArgumentParser(
    	prog="mypileup",
    	description="Command-line script to perform  pileup of BAM files"
    )

    # Input
    parser.add_argument("bam", help="Indexed BAM file", \
    		type=str)

    # Output
    parser.add_argument("-o", "--out", help="Write output to file. " \
    		"Default: stdout", metavar="FILE", type=str, required=False)

    # Other options
    parser.add_argument("-f", "--fasta-ref", \
    		help="faidx indexed reference sequence file", \
    		type=str, metavar="FILE", required=False)
    parser.add_argument("-r", help="region in which pileup is " \
    		"generated. Format chr:start-end", \
    		type=str, metavar="REG", required=False)

    # Parse args
    args = parser.parse_args()

if __name__ == "__main__":
    main()