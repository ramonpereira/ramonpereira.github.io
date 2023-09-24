# Planimation of Grid-Based Planning Problems Specified in PDDL

## Background and Problem Description
Automated Planning is a fundamental research area of Artificial Intelligence (AI), defined as devising a plan of action to achieve a goal [1, 2, 3]. 
There exist several AI Planning tools for edit and visualise planning problems and solution plans, such as http://planning.domains.
Planimation is an open source framework to visualise sequential solution plans of AI Planning problems specified in PDDL (Planning Domain Definition Language).

## Project Description
The aim of this project is to develop a webtool formalise, generate and visualise grid-based AI Planning problems specified in PDDL.
Here are some grid-based domains that we could use for the project:
- Sokoban: https://en.wikipedia.org/wiki/Sokoban
- Transport Puzzle: https://en.wikipedia.org/wiki/Transport_puzzle
- Rush Hour: https://en.wikipedia.org/wiki/Rush_Hour_(puzzle)
- Path-planning with customisable characthers and scenarios, e.g., Zelda, Sonic, Dungeons and Dragons, Mario Bros, etc.

The ideal functionalities of this webtool are as follows:
- Generate customisable grid-based AI planning problems with different grid sizes and objects (e.g., for Sokoban, a grid 10x10, with obstacles and 5 boxes).
- Generate an animation based on the extracted plan for the customisable AI planning problems.

In this project, the environment setting for formalising AI Planning domain models and problems is discrete deterministic planning (a unique known initial state, durationless actions, deterministic actions, which can be taken only one at a time, and single or multi-agent planning).

For planning, there exists several different AI planners are able to plan over the environment setting described above, such as:
https://github.com/jendrikseipp/scorpion
https://github.com/aibasel/pyperplan

Other useful links:
- This Wiki provides easy access to resources related to the field of AI Planning: https://planning.wiki

## Deliverables
- A report describing the developed webtool, as well as the formalised domain models, the planners used for experiments and evaluation, and some background and related work;
- A project on GitHub containing the webtool, the domain models, the used planners, experiments, etc.

## References
[1] Malik Ghallab, Dana S. Nau, and Paolo Traverso. 2004. Automated Planning - Theory and Practice. (1st ed.). Elsevier.
[2] Stuart Russell and Peter Norvig. 2005. Artificial Intelligence: A Modern Approach (3rd ed). Pearson Series in Artificial Intelligence.
[3] Hector Geffner and Blai Bonet. 2013. A Concise Introduction to Models and Methods for Automated Planning (1st edition). Morgan & Claypool Publishers.
[4] Planimation: https://nirlipo.github.io/project/planimation/


Planimation Video

https://youtu.be/Cj2rWdt1YQU


