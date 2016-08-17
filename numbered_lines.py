#!/usr/bin/env python3
"""Function to write line numbers to a file"""
import math
def numbered_lines(filename):
	write_file(read_file(filename))


def read_file(filename):
	list_lines = []
	with open(filename,"r") as read_file:
		for lines in read_file:
			lines = lines.strip()
			list_lines += lines.split("\n")
	return list_lines

def write_file(list_lines):
	with open("t_write.txt","w") as w_file:
		#enumerate the read lines and write to file using index number
		for idx,words in enumerate(list_lines):
			if words == "":
				pass
			else:
				words = str(idx+1) + " " + words
				w_file.write(words +"\n")
		
			

def main():
    numbered_lines("small.txt")

if __name__ == "__main__":
    main()
