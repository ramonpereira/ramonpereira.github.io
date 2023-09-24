# Tie-Break Strategies for Heuristic Search in Cyclic and Non-Cyclic AND/OR Graphs

## Background and Problem Description
Automated Planning is a fundamental research area of Artificial Intelligence (AI), defined as devising a plan of action to achieve a goal state from an initial state [1, 2]. Fully Observable Non-Deterministic (FOND) Planning is a type of AI Planning setting that models uncertainty through actions with non-deterministic effects [3,4].

Existing FOND planning algorithms are effective and employ a wide range of techniques, namely, heuristic search, replanning, model checking, SAT-solving, etc. In AI Planning, tie-breaking refers to the process of selecting between multiple possible actions that have the same level of desirability according to a planning algorithm's evaluation function [8.9]. When multiple actions have the same desirability score, tie-breaking is used to determine which action should be chosen. The choice of tie-breaking strategy can have a significant impact on the performance and effectiveness of a planning algorithm. Therefore, selecting an appropriate tie-breaking strategy is an important consideration in designing an effective AI planning system.

## Project Description
The aim of this project is to develop tie-break strategies for AND/OR heuristic search in cyclic and non-cyclic AND/OR graphs.

Existing FOND Planning solvers that rely on heuristic search do not efficiently use tie-break strategies, as opposed to Classical Planning solvers (Fast-Downward), which employ tie-break strategies to improve their efficiency [8,9].

FOND Planning solvers that employ heuristic search are:

- MyND [5,6]: https://bitbucket.org/robertmattmueller/mynd/

- Paladinus [7]: https://github.com/ramonpereira/paladinus

The FOND Planning solvers could be modified to test the developed tie-break strategies.

The environment planning setting for formalising non-deterministic domain models and problems is discrete-time non-deterministic planning with goal states (duration-less actions, non-deterministic actions with uniform probabilities, full observability, and single or multi-agent planning), as known as FOND Planning.

Here you can find some examples of FOND Planning domains and problems:

https://github.com/QuMuLab/planner-for-relevant-policies/tree/master/fond-benchmarks

Other useful links:

- This Wiki provides easy access to resources related to the field of AI Planning: https://planning.wiki

## Deliverables
- A report describing the formalised tie-breaking strategies, as well as the planners used for experiments and evaluation, benchmarks, and the essential background and related work;

- A project on GitHub containing the tie-breaking strategies, domain models and benchmarks, planners, experiments, etc.

## References
[1] Malik Ghallab, Dana S. Nau, and Paolo Traverso. 2004. Automated Planning - Theory and Practice. (1st ed.). Elsevier.

[2] Stuart Russell and Peter Norvig. 2005. Artificial Intelligence: A Modern Approach (3rd ed). Pearson Series in Artificial Intelligence.

[3] Hector Geffner and Blai Bonet. 2013. A Concise Introduction to Models and Methods for Automated Planning (1st edition). Morgan & Claypool Publishers.

[4] Cimatti, A.; Pistore, M.; Roveri, M.; and Traverso, P. 2003. Weak, Strong, and Strong Cyclic Planning via Symbolic Model Checking. In: Artificial Intelligence, 147(1-2).

[5] Mattmuller, R.; Ortlieb, M.; Helmert, M.; and Bercher, P. 2010. Pattern Database Heuristics for Fully Observable Non-Deterministic Planning. In: ICAPS.

[6] Mattmuller, R. 2013. Informed Progression Search for Fully Observable Nondeterministic Planning. Ph.D. Thesis, Albert-Ludwigs-Universitat Freiburg.

[7] Pereira, R. F.; Pereira, A. G.; Messa, F.; and Giacomo, G. D. 2022. Iterative Depth-First Search for FOND Planning. In: ICAPS.

[8] Masataro Asai and Alex Fukunaga. 2017. Tie-Breaking Strategies for Cost-Optimal Best-First Search. In: Journal of Artificial Intelligence Research.

[9] Corrêa et al. 2018. Analyzing Tie-Breaking Strategies for the A∗ Algorithm. In: IJCAI. 

