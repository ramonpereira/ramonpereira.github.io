# Robust Planning in Real and Realistic Domain Models

## Background
Planning is a fundamental research area of Artificial Intelligence (AI), defined as devising a plan of action to achieve a goal [1, 2]. The many conflicting environmental constraints to be considered when generating a plan (sequence of actions) to achieve a goal include (but are not limited to) whether the environment is fully or partially observable, stochastic or deterministic, static or dynamic and whether our model of that environment supports the presence of single or multiple agents [3]. Robust and efficient planning in real and realistic domain models have been a challenge for the AI Planning community. More realistic domain models usually contain complex constraints with respect to the environment dynamics that are not easily addressed in most domain-independent purely symbolic AI planners in the literature.

## Project Description

The aim of this project is to formalise real and realistic domain models for AI Planning, and experiment and evaluate the formalised domains using state-of-the-art AI planners in the literature.

The environment settings for formalising real and realistic domain models include, but are not limited to the following:
 - Discrete deterministic planning (a unique known initial state, duration-less actions, deterministic actions, which can be taken only one at a time, and single or multi-agent planning);
 - Continuous planning (a unique known initial state, duration-less actions, deterministic or non-deterministic actions, which can be taken only one at a time, and single or multi-agent planning);
 - Discrete-time non-deterministic planning (duration-less actions, non-deterministic actions with probabilities, full observability, maximisation of a reward function, and single or multi-agent planning);
 - Planning in hybrid systems with both discrete and continuous control variables;

Some examples of real and realistic domain models can be found here:
- http://users.cecs.anu.edu.au/~patrik/sigaps/index.php?n=Main.RealDomains

For planning, there exists several different AI planners are able to plan over the environment settings described above, such as:

- Discrete deterministic planning: 
https://github.com/jendrikseipp/scorpion

- Continuous planning: 
https://ompl.kavrakilab.org/planners.html

- Discrete-time non-deterministic planning:
https://github.com/thiagopbueno/tf-mdp
https://cassandra.org/projects/software/pomdp-solve.html
https://github.com/pucrs-automated-planning/mdp-python-reference

- Hybrid planning:
https://github.com/KCL-Planning/DiNo
https://sites.google.com/view/enhsp/

Other useful links:
- This Wiki provides easy access to resources related to the field of AI Planning: https://planning.wiki
- An AI Planning Modeling Framework: https://github.com/aig-upf/tarski

## Deliverables
- A report describing the formalised domain models, as well as the planners used for experiments and evaluation, and the related work;
- A project on GitHub containing the domain models, the planners, experiments, etc.

## References
[1] Malik Ghallab, Dana S. Nau, and Paolo Traverso. 2004. Automated Planning - Theory and Practice. (1st ed.). Elsevier.
[2] Stuart Russell and Peter Norvig. 2005. Artificial Intelligence: A Modern Approach (3rd ed). Pearson Series in Artificial Intelligence.
[3] Hector Geffner and Blai Bonet. 2013. A Concise Introduction to Models and Methods for Automated Planning (1st edition). Morgan & Claypool Publishers.
