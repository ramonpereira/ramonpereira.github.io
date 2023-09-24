# Multi-Agent Coordination and Cooperation using Landmarks, Centroids, and Minimum Covering States

## Background
Multi-Agent (MA) Planning is a fundamental problem for multi-agent autonomous systems [1,2].
Planning for multiple agents sometimes requires cooperation among the agents in order to generate non-conflicting plans for achieving their respective goals [3,4].
The coordination process among the agents may need to rely on achieving intermediate relevant states (sub-goals) to avoid conflict and redundant actions in a coordinated team plan [3,4].

## Description
The aim of this project is to develop a MA Planning approach by taking into account both coordination and cooperation. 
To do so, one would need to formalize MA Planning environments using a planning description languange (Planning Domain Definition Language (PDDL), i.e., MA-PDDL [5]).
The environment setting for formalising MA Planning domain models include we will be using in this project is a discrete deterministic planning setting with a unique known initial state, durationless actions, deterministic actions, which can be taken only one at a time.

Some examples of MA Planning and its formalism can be found here:
- http://users.cecs.anu.edu.au/~thiebaux/workshops/ICAPS03/proceedings/brenner.pdf
- https://github.com/stolba/MADLAPlanner/tree/master/benchmarks

For MA Planning coordination and cooperation, one could use the code base of a state-of-the-art MA Planner [6], as follows:
- https://github.com/stolba/MADLAPlanner

To extract relavant intermediate states for MA Planning coordination and cooperation, one will be using Landmarks, Centroids, and Minimum Covering states:
- MA Planning Landmarks [7]: https://ojs.aaai.org/index.php/ICAPS/article/view/13719
- Centroids and Minimum Covering states [8]: https://ojs.aaai.org/index.php/ICAPS/article/view/3497

Other useful links:
- This Wiki provides easy access to resources related to the field of AI Planning: https://planning.wiki

## Deliverables
- A report describing the problem, as well as the developed approach, the domains used for the experiments and evaluation, and the related work;
- A project on GitHub containing the developed approach, experiments, etc.

## References
[1] Malik Ghallab, Dana S. Nau, and Paolo Traverso. 2004. Automated Planning - Theory and Practice. (1st ed.). Elsevier.
[2] Brafman, R. I., and Domshlak, C. 2008. From One to Many: Planning for Loosely Coupled Multi-Agent Systems. In: ICAPS.2008. 
[3] Y. Dimopoulos and P. Moraitis. 2006. Multi-Agent Coordination and Cooperation through Classical Planning. In: IEEE/WIC/ACM International Conference on Intelligent Agent Technology.
[4] Torreño et al. 2017. Cooperative Multi-agent Planning: A Survey. In: ACM Computing Surveys.
[5] Michael Brenner. 2006. A Multiagent Planning Language. In: ICAPS Workshop.
[6] MADLAPlanner: https://github.com/stolba/MADLAPlanner
[7] Štolba et al. 2015. Admissible Landmark Heuristic for Multi-Agent Planning. In: ICAPS.
[8] Pozanco et al. 2019. Finding Centroids and Minimum Covering States in Planning. In: ICAPS.



