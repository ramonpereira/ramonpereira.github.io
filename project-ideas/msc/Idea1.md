# Goal and Plan Recognition in the Robot Operating System

## Background
Goal Recognition is the task of discerning the intended goal of an agent aims to achieve given a sequence of observations [3], whereas Plan Recognition consists of identifying the plan (i.e., sequence of actions) to achieve such an intended goal [2].
The most effective approaches to Goal and Plan Recognition rely on Artificial Intelligence (AI) Planning techniques.
However, such recognition approaches have not been properly applied and evaluated in real-world scenarios, such as the Robot Operating System (ROS) [1].

## Description
The aim of the project is to implement some of the existing Goal and Plan Recognition techniques in the literature [2,3] in the Robot Operating System (ROS) [1].  It is also expected to experiment and evaluate the implemented techniques over different robot application domains, such as robot navigation, quadrotor unmanned aerial vehicle (UAV) missions, etc. 

An open-source implementation of ROS for Artificial Intelligence (AI) Planning (ROSPlan) [4] is available on GitHub: 
- https://github.com/KCL-Planning/ROSPlan

An AI planner for ROS is also available on GitHub, as follows:
- https://github.com/phuicy/downward

## Deliverables
- A report describing the developed approaches, as well as the experiments used for evaluation, and the related work;
- A project on GitHub containing the code, experiments, etc.

## References
[1] Meneguzzi, F.; and Pereira, R. F. A Survey on Goal Recognition as Planning. 2020. In IJCAI.
[2] Cashmore, M.; Fox, M.; Long, D.; Magazzeni, D.; Carrera, A.; Palomeras, N.; Hurtos, N.; and Carreras, M. 2015. ROSPlan: Planning in the Robot Operating System. In ICAPS.
[3] Quigley, M.; Conley, K.; Gerkey, B.; Faust, J.; Foote, T.; Leibs, J.; Wheeler, R.; and Ng, A. Y. 2009. ROS: An Open-Source Robot Operating System. In ICRA Workshop on Open Source Software.
[4] Ramirez, M.; and Geffner, H. 2009. Plan Recognition as Planning. In IJCAI.