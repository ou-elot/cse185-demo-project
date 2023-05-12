#!/usr/bin/env python

"""
Command-line script to perform 
pileup of BAM files

Similar to samtools mpileup
"""

import argparse


def main():
    parser = argparse.ArgumentParser(
    	prog="mypileup",
    	description=__doc__
    )

    # Input
    parser.add_argument("bam", help="Indexed BAM file", \
    		type=str)

    # Output
    parser.add_argument("--out", help="Write output to file. " \
    		"Default: stdout", type=str, required=False)

    # Other options
    parser.add_argument("-r", help="region in which pileup is " \
    		"generated. Format chr:start-end", \
    		type=str, required=False)

    # Parse args
    args = parser.parse_args()

if __name__ == "__main__":
    main()