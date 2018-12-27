import sys, os, csv, time

def loadRealHypothesy() :
    real_hyp = ''
    instream = open('real_hyp.dat')
    for line in instream:
        real_hyp = line

    instream.close()
    return real_hyp

def loadHypotheses() :
    hyps = []
    instream = open('hyps.dat')

    for line in instream :
        hyps.append(line)

    instream.close()
    return hyps

def isTimedOut() :
    if os.path.exists('timed-out.dat'):
        return True

    return False

def loadMaxHypotheses() :
    maxHyps = []

    if not os.path.exists('max-hyps.dat'):
        return None

    instream = open('max-hyps.dat')
    for line in instream :
        maxHyps.append(line)

    instream.close()
    return maxHyps

def wasRecognizedCorrectly(recognizedGoals, realGoal):
    if recognizedGoals is not None:
        for goal in recognizedGoals:
            goal = goal.replace('\n', '')
            realGoal = realGoal.replace('\n', '')
            if goal == realGoal:
                return True
    
    return False    

def doExperiments(domainName, observability):
    totalProblems = 0
    counterProblems = 0
    counterTimedOutProblems = 0
    counterTruePositiveProblems = 0
    counterFalsePositiveProblems = 0
    candidateGoals = 0
    totalReturnedGoals = 0
    startTime = time.time()
    experimentsResult = ''

    for obs in observability :
        startTime = time.time()
        counterProblems = 0
        counterTruePositiveProblems = 0
        counterFalsePositiveProblems = 0
        candidateGoals = 0
        totalReturnedGoals = 0

        problems_path = 'experiments/' + domainName + '/' + obs + '/'
        for problem_file in os.listdir(problems_path):
            if problem_file.endswith(".tar.bz2"):
                cmdClean = 'rm -rf *.pddl *.dat *.log'
                os.system(cmdClean)

                print problems_path + problem_file
                cmdUntar = 'tar xvjf ' + problems_path + problem_file
                os.system(cmdUntar)

                goals = loadHypotheses()
                realGoal = loadRealHypothesy()               

                cmdRecognizer = 'mono PIPSS.exe -d domain.pddl -p template.pddl -i 0 -t 1800'
                os.system(cmdRecognizer)
                
                if isTimedOut():
					counterTimedOutProblems = counterTimedOutProblems + 1
					continue

                counterProblems = counterProblems + 1
                candidateGoals = candidateGoals + len(goals)
                recognizedGoals = loadMaxHypotheses()

                goalWasRecognizedCorrecly = wasRecognizedCorrectly(recognizedGoals, realGoal)
                if goalWasRecognizedCorrecly:
                    counterTruePositiveProblems = counterTruePositiveProblems + 1
                    totalReturnedGoals = totalReturnedGoals + len(recognizedGoals)
                elif not goalWasRecognizedCorrecly and recognizedGoals is not None:
                    totalReturnedGoals = totalReturnedGoals + len(recognizedGoals)
                elif recognizedGoals is None:
                    counterTruePositiveProblems = counterTruePositiveProblems + 1
                    totalReturnedGoals = totalReturnedGoals + len(goals)
        
        totalCandidateGoals = float(candidateGoals / counterProblems)
        counterProblems = float(counterProblems)
        counterTruePositiveProblems = float(counterTruePositiveProblems)
        counterFalsePositiveProblems = (totalReturnedGoals - counterTruePositiveProblems)
        trueNegativeCounter = float((counterProblems*(candidateGoals / counterProblems)) - counterFalsePositiveProblems)
        trueNegativeCounter = float(trueNegativeCounter)
        falseNegativeCounter = float(counterProblems - counterTruePositiveProblems)
        accuracy = float(counterTruePositiveProblems / counterProblems)
        precision = float(counterTruePositiveProblems / (counterTruePositiveProblems + counterFalsePositiveProblems))
        recall = float(counterTruePositiveProblems / (counterTruePositiveProblems + falseNegativeCounter))
        if((precision+recall) == 0):
                f1score = 0
        else: f1score = 2 * ( (precision*recall) / (precision+recall) )
        fallout = counterFalsePositiveProblems / (trueNegativeCounter + counterFalsePositiveProblems)
        missrate = float(falseNegativeCounter / (falseNegativeCounter + counterTruePositiveProblems))
        totalT = (time.time() - startTime)
        totalTime = float(totalT / counterProblems)
        avgRecognizedGoals = float(totalReturnedGoals/counterProblems)

        obsPrint = obs
        if obs == 'full':
            obsPrint = '100'

        result = obsPrint + '\t' + str(accuracy) + '\t' + str(precision) + '\t' + str(recall) + '\t' + str(f1score) + '\t' + str(fallout) + '\t' + str(missrate) + '\t' + str(avgRecognizedGoals) + '\t' + str(totalTime) + '\n';
        experimentsResult = experimentsResult + result
        totalProblems = totalProblems + counterProblems

    fileResult = open(str(domainName) + '-goal_recognition-yolanda.txt', 'w')
    print str(domainName) + '-goal_recognition-yolanda.txt'
    print experimentsResult
    print '$> Total Problems: ' + str(totalProblems)
    print '$> Total Timed out Problems: ' + str(counterTimedOutProblems)
    fileResult.write(experimentsResult)
    fileResult.close()

def main():
    domainName = sys.argv[1]

    observability = ['10', '30', '50', '70', '100']
    doExperiments(domainName, observability)

    cmdClean = 'rm -rf *.pddl *.dat *.log'
    os.system(cmdClean)

if __name__ == '__main__' :
    main()
