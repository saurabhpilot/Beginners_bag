#!/usr/bin/python
import sys
import re

def extract_names(filename):
	names=[]
	f = open(filename, 'rU')
        text = f.read()
	year_match = re.search(r'Popularity in (\d\d\d\d)',text)
	if (year_match):
		names.append(year_match.group(1))
	else:
		sys.stderr.write('Couldn\'t find the year!\n')
		sys.exit(1)
	tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)', text)
        #print tuples
	names_to_rank =  {}
    	for rank_tuples in tuples:
		(rank, boyname, girlname) = rank_tuples
		if boyname not in names_to_rank:
			names_to_rank[boyname]=rank
		if girlname not in names_to_rank:
			names_to_rank[girlname]=rank
	sorted_names = sorted(names_to_rank.keys())
        for name in sorted_names:
        	names.append(name + " " + names_to_rank[name])			
	f.close()
	return names


def main():
	args = sys.argv[1:]
	
	if not args:
		print 'usage: [--summaryfile] file [file ...]'
		sys.exit(1)
	summary = False
	if args[0] == '--summaryfile':
		summary = True
		del args[0]
	# +++your code here+++
  	# For each filename, get the names, then either print the text output
  	# or write it to a summary file
  	# LAB(begin solution)
  	for filename in args:
    		names = extract_names(filename)
    	        # Make text out of the whole list
    	        text = '\n'.join(names)

	if summary:
		outf = open(filename + '.summary', 'w')
		outf.write(text + '\n')
		outf.close()
	else:
		print text
		
if __name__ == '__main__':
  main()


