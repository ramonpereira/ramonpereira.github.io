#!/usr/bin/python
import sys
import os
import subprocess

def main() :
	benchmarks = sys.argv[1]
	heuristic = sys.argv[2]

	heuristics = ''
	heuristics_file = sys.argv[3]
	hs_file = open(heuristics_file)
	for line in hs_file:
		heuristics = line

	strategies_file = sys.argv[4]
	strategies = []
	stg_file = open(strategies_file)
	for line in stg_file:
		strategies.append(line.replace('\n', ''))

	search = sys.argv[5]

	timeout = sys.argv[6]

	count = 0
	for filename in os.listdir(benchmarks):
		for strategy in strategies:
			if heuristic in strategy:
				continue
			if ".sas" in filename and not "tidy" in filename and not "triangle" in filename:
				pddl_p = filename.split('/')
				pddl_p = pddl_p[len(pddl_p)-1]

				output_file =  pddl_p.replace('.sas', '') + '-' + search + '-' + heuristic + '_' + heuristics + '-' + strategy + '.txt'

				if output_file.replace('"', '') in os.listdir(os.path.abspath(os.getcwd())):
					continue
				
				command = 'java -jar myNDPlus2.0.jar -timeout ' + timeout + ' -search '  + search + ' -heuristic ' + heuristic + ' -heuristics ' + heuristics + ' -strategy ' + strategy + ' ' + benchmarks + filename + ' > ' + output_file
				print command
				os.system(command)
				count += 1
				print '$> Run: ' + str(count)
				print ''

if __name__ == '__main__' :
	main()
