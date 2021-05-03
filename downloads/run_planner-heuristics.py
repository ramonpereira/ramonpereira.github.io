#!/usr/bin/python
import sys
import os
import subprocess

def main() :
	domains_file = sys.argv[1]
	domains = []
	d_file = open(domains_file)
	for line in d_file:
		domains.append(line.replace('\n', ''))

	heuristic = sys.argv[2]
	heuristics = sys.argv[3]

	strategies_file = sys.argv[4]
	strategies = []
	stg_file = open(strategies_file)
	for line in stg_file:
		strategies.append(line.replace('\n', ''))

	search = sys.argv[5]

	timeout = sys.argv[6]

	count = 0
	for domain in domains:
		for filename in os.listdir(domain):
			for strategy in strategies:
				if heuristic in strategy:
					continue
				if ".pddl" in filename and 'domain' not in filename and 'sample' not in filename:
					pddl_p = filename.split('/')
					pddl_p = pddl_p[len(pddl_p)-1]
					domain_n = domain.split('/')
					domain_n = domain_n[len(domain_n)-2]
					output_file =  domain_n + '-' + pddl_p.replace('.pddl', '') + '-' + search + '-' + heuristic + '-' + strategy + '.txt'
					
					if output_file.replace('"', '') in os.listdir(os.path.abspath(os.getcwd())):
						continue
					
					command = 'java -jar myNDPlus2.0.jar -timeout ' + timeout + ' -search ' + search + ' -heuristic ' + heuristic + ' -strategy ' + strategy + ' -t FOND ' + domain + 'domain.pddl ' + domain + filename + ' > ' + output_file
					print command
					os.system(command)
					count += 1
					print '$> Run: ' + str(count)
					print ''

if __name__ == '__main__' :
	main()
