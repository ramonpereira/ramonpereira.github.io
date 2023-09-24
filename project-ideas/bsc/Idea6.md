# Solving Visual Coding Games (Blockly) via Generalised Planning

## Background and Problem Description
Automated Planning is a fundamental research area of Artificial Intelligence (AI), defined as devising a plan of action to achieve a particular goal state from an initial state [1, 2, 3]. In contrast, Generalised Planning is a type of AI planning problem that encodes multiple different individual goal and initial states, and the solution is
a generalised plan that is capable to solve this multiple goals from different initial states [4]. A generalised plan can be casted as a procedural program, and in Generalised Planning such procedural programs are formally defined as planning programs.
Blockly Games are a series of educational games to teach programming and coding. The educational games are designed for people who have not had prior experience with computer programming and coding [5]. 

## Project Description
The aim of this project is to develop a web-tool that will be able to solve Blockly Games via Generalised Planning. 
The idea is efficiently employing Generalised Planning techniques to solve educational programming/coding games.

The ideal functionalities of this web-tool are as follows:
- Generate customisable Blockly Games problems;
- Generate a generalised plan capable to solve a set of Blockly Games problems; and
- Develop an animated tool that is capable to show the plan solving the defined Blockly Games problems.

For planning, there exists several different Generalised Planning solvers are able to extract planning programs, as follows:

https://github.com/aig-upf/automated-programming-framework

https://github.com/aig-upf/pgp-landmarks

https://github.com/rleap-project/best-first-generalized-planning

Other useful links:
- This Wiki provides easy access to resources related to the field of AI Planning: https://planning.wiki

## Deliverables
- A report describing the developed webtool, as well as the formalised domain models, the planners used for experiments and evaluation, and some background and related work;
- A project on GitHub containing the webtool, the domain models, the used planners, experiments, etc.

## References
[1] Malik Ghallab, Dana S. Nau, and Paolo Traverso. 2004. Automated Planning - Theory and Practice. (1st ed.). Elsevier.
[2] Stuart Russell and Peter Norvig. 2005. Artificial Intelligence: A Modern Approach (3rd ed). Pearson Series in Artificial Intelligence.
[3] Hector Geffner and Blai Bonet. 2013. A Concise Introduction to Models and Methods for Automated Planning (1st edition). Morgan & Claypool Publishers.
[4] Jiménez et al. 2018. A Review of Generalized Planning. In: The Knowledge Engineering Review.
[5] Blockly Games.
