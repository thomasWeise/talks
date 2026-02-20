[![build](https://github.com/thomasWeise/talks/actions/workflows/build.yaml/badge.svg)](https://github.com/thomasWeise/talks/actions/workflows/build.yml)
[![https://thomasweise.github.io](https://shields.io/badge/home-thomasweise.github.io-009000)](https://thomasweise.github.io)

# Talks by Prof.&nbsp;Dr.&nbsp;Thomas Weise

## 1. Introduction

[Here](https://thomasweise.github.io/talks) you can find some of the talks given by Prof.&nbsp;Dr.&nbsp;Thomas Weise (汤卫思教授). 

- [Comparing Optimization Algorithms](https://thomasweise.github.io/talks/comparingOptimizationAlgorithms.pdf)
- [Frequency Fitness Assignment](https://thomasweise.github.io/talks/ffa.pdf)
- [An Introduction to Optimization](https://thomasweise.github.io/talks/optimization.pdf)
- [Metaheuristic Optimization in Python:&nbsp;`moptipy`](https://thomasweise.github.io/talks/moptipy.pdf)
- [Frequency Fitness Assignment as Research Direction](https://thomasweise.github.io/talks/researchDirectionFFA.pdf)

## 2. Talk Abstracts

### 2.1. Comparing Optimization Algorithms 
**[Comparing Optimization Algorithms](https://thomasweise.github.io/talks/comparingOptimizationAlgorithms.pdf):**&nbsp;Today, there exists a variety of different optimization algorithms, ranging from exact methods to metaheuristics.
When we try to solve an optimization problem, our goal is to use the right algorithm, i.e., the one that performs the best.
However, how can we decide which algorithm offers the best performance?
And how do we even define what performance is?
We give an overview on the two aspects of performance, solution quality and runtime&nbsp;(which can be measured either as clock time or in form of algorithm steps).
Since many optimization algorithms are randomized, it is necessary to execute them several times on a given problem instance to get reliable information.
We also need to use several different problem instances, because all instances can be different and some may be harder while others can be easier.
This leads to a pile of data, which needs to be reduced to single statistics, such as those of distribution center&nbsp;(arithmetic mean, median, and geometric mean) and spread&nbsp;(standard deviation and quantiles).
Furthermore, just comparing such statistics may not be sufficient as well, because they are only estimates stemming from usually small populations of data.
Therefore, the concept of non-parametric statistical tests is explored.
When we compare multiple sets of data we need to do multiple tests, which means that we need to correct the significance threshold.
We also notice that comparing results gathered at some point in time using tests is not necessarily sufficient, because optimization algorithms are often anytime algorithms.
At some early time, algorithm&nbsp;*A* may be better, while at another time, algorithm&nbsp;*B* may be better.
Curves describing the whole runtime progress of algorithms are therefore useful tools.
We conclude the talke with some recommendations to avoid pitfalls and on what is considered cheating in experimentation with optimization methods.


### 2.2. Frequency Fitness Assignment
**[Frequency Fitness Assignment](https://thomasweise.github.io/talks/ffa.pdf):**&nbsp(FFA, <span style="color:gray;font-size:90%">频率适应度分配</span>) is a novel approach to metaheuristic optimization.
Optimization problems are situations where we have to pick one of many possible choices and want to do this in such a way that we reach a pre-defined goal at a minimum cost.
Classical optimization problems include the Traveling Salesperson Problem, the Maximum Satisfiability Problem&nbsp;(MaxSAT), and the Bin Packing problem, for example.
Many of these problems are NP-hard and solving them to optimality would require exponential runtime in the worst case.
Therefore, metaheuristic algorithms have been developed that can deliver good (but not necessarily optimal) solutions in acceptable runtime.
Examples for classical metaheuristics are the (1+1)&nbsp;EA, Simulated Annealing&nbsp;(SA), and the Standard Genetic Algorithm&nbsp;(SGA).
Since we want that such algorithms should behave the same in both quick benchmarking experiments and in practical application, we would like them to exhibit invariance properties.
Whereas the (1+1)&nbsp;EA is invariant under all order-preserving transformations of the objective function value, SA is not invariant under scaling of the objective function and the SGA is not invariant under translations of the objective function.
Frequency Fitness Assignment&nbsp;(FFA) is an algorithm module that can be plugged into existing algorithms and makes them invariant under all injective transformations of the objective function value&nbsp;(which goes far beyond order-preserving transformations).
We plug FFA into the (1+1)&nbsp;EA.
We show that the resulting (1+1)&nbsp;FEA can solve Trap, TwoMax, and Jump problems in polynomial runtime, whereas the (1+1)&nbsp;EA needs exponential runtime.
Moreover, the (1+1)&nbsp;FEA performs very significantly faster on the NP-hard MaxSAT problem.
We conclude the presentation with an outline of other properties of FFA and our other recent works.
Find out more about FFA at <https://thomasweise.github.io/research/areas/ffa>.


### 2.3. An Introduction to Optimization
[An Introduction to Optimization](https://thomasweise.github.io/talks/optimization.pdf) is a talk designed for giving a brief introduction to optimization for an audience unfamiliar with the topic.
It builds on high school knowledge and drives it further by iteratively tackling problems that can be solved by equations, by simple algorithms, and by an advanced algorithm.
Then we arrive at a category of problems that algorithms can no longer solve both efficiently and exactly.
These are the problems requiring metaheuristic optimization algorithms.
We then finally take a brief look into some basic concepts underlying these algorithms.


### 2.4. Metaheuristic Optimization in Python:&nbsp;`moptipy`
**[Metaheuristic Optimization in Python:&nbsp;`moptipy`](https://thomasweise.github.io/talks/moptipy.pdf)** gives a brief introduction the [Python](https://thomasweise.github.io/programmingWithPython) framework [`moptipy`](https://thomasweise.github.io/moptipy).
This framework, developed by our team, allows you to conduct repeatable, replicable, self-documenting experiments that can be executed in parallel or in a distributed fashion.
It implements many of the basic metaheuristic algorithms as well as some experimental methods like FFA.
Moreover, it also provides the tools to statistically evaluate the experimental results and to plot various diagrams.
This is free open source software that can be installed via `pip install moptipy`.
It ships with many examples.
The additional package [`moptipyapps`](https://thomasweise.github.io/moptipyapps) provides search spaces and operators for many well-known optimization problems, such as the Quadratic Assignment Problem&nbsp;(QAP), the Traveling Salesperson Problem&nbsp;(TSP), the Traveling Tournament Problem&nbsp;(TTP), or the two-dimensional bin packing task, complementing the domains already built into `moptipy`, namely the Job Shop Scheduling Problem&nbsp;(JSSP) and discrete benchmark functions.
[not finished]


### 2.5. Frequency Fitness Assignment as Research Direction
**[Frequency Fitness Assignment as Research Direction](https://thomasweise.github.io/talks/researchDirectionFFA.pdf)** briefly outlines the research direction *Frequency Fitness Assignment*&nbsp(FFA, <span style="color:gray;font-size:90%">频率适应度分配</span>) of our team.
It begins by introducing the field of optimization with a particular focus on metaheuristics.
It then discusses how FFA works and how it can be plugged into metaheuristic optimization algorithms.
We then show the past achievements resulting from this strand of research before giving pointers to the future tasks and challenges ahead.


## 3. Speaker Biography
Prof.&nbsp;Dr.&nbsp;Thomas WEISE&nbsp;<span style="color:gray;font-size:90%">(汤卫思)</span> holds a full professorship at Hefei University&nbsp;<span style="color:gray;font-size:90%">(合肥大学)</span> in the city Hefei&nbsp;<span style="color:gray;font-size:90%">(合肥市)</span> in the province Anhui&nbsp;<span style="color:gray;font-size:90%">(安徽省)</span> in China.
He received his Diplom-Informatiker in Computer Science from the Chemnitz University of Technology&nbsp;<span style="color:gray;font-size:90%">(德国开姆尼茨工业大学)</span> in Chemnitz, Germany&nbsp;<span style="color:gray;font-size:90%">(德国开姆尼茨市)</span> in 2005 and his doctoral degree&nbsp;<span style="color:gray;font-size:90%">(博士)</span> from the University of Kassel&nbsp;<span style="color:gray;font-size:90%">(德国卡塞尔大学)</span> in Kassel, Germany&nbsp;<span style="color:gray;font-size:90%">(德国卡塞尔市)</span> in 2009.
Prof.&nbsp;Weise joined the School of Computer Science and Technology&nbsp;<span style="color:gray;font-size:90%">(计算机科学与技术学院)</span> of the University of
Science and Technology of China&nbsp;<span style="color:gray;font-size:90%">(USTC, 中国科学技术大学)</span> in Hefei as PostDoc&nbsp;<span style="color:gray;font-size:90%">(博士后)</span> from&nbsp;2009 to&nbsp;2011.
He then was promoted to Associate Professor&nbsp;<span style="color:gray;font-size:90%">(副教授)</span> in the same school.
In 2016, Prof.&nbsp;Weise moved to the School of Artificial Intelligence and Big Data&nbsp;<span style="color:gray;font-size:90%">(人工智能与大数据学院)</span> of Hefei University&nbsp;<span style="color:gray;font-size:90%">(合肥大学)</span> as Full Professor.
Prof.&nbsp;Weise holds the 2025&nbsp;Huangshan Friendship Award of Anhui Province&nbsp;<span style="color:gray;font-size:90%">(安徽省黄山友谊奖)</span> and the 2020&nbsp;Hefei City Friendship Award&nbsp;<span style="color:gray;font-size:90%">(外国专家“友谊奖”)</span>.

The research field of Prof.&nbsp;Weise is metaheuristic optimization, where he made contributions to both fundamental and applied research.
Prof.&nbsp;Weise is the author of over 50&nbsp;journal articles and 80&nbsp;conference papers.
He has authored more than 140&nbsp;scientific publications in total.
According to GoogleScholar, his work has been cited more than 4500&nbsp;times and he has a h-index of&nbsp;30 and an i10-index of&nbsp;60.
He has authored or co-authored works in journals such as the IEEE&nbsp;Transactions on Evolutionary Computation, the IEEE&nbsp;Computational Intelligence Magazine, the IEEE&nbsp;Transactions on Image Processing, Information Fusion, Pattern Recognition, Information Sciences, Applied Soft Computing, Soft Computing, the European Journal of Operational Research, Evolutionary Computation, the Journal of Global Optimization, the Journal of Computer Science &amp; Technology, and the Journal of Combinatorial Optimization.
Prof.&nbsp;Weise is editorial board member of Applied Soft Computing and reviewer for over 30&nbsp;journals and over 70&nbsp;conferences.
His book&nbsp;"[Global Optimization Algorithms &mdash; Theory and Application](https://www.researchgate.net/publication/200622167)" has been cited more than 1300&nbsp;times.

The recent works of Prof.&nbsp;Weise focus on [Frequency Fitness Assignment](https://thomasweise.github.io/talks/ffa.pdf)&nbsp;(FFA) and [benchmarking of optimization algorithms](https://thomasweise.github.io/talks/comparingOptimizationAlgorithms.pdf).
FFA is an algorithm module that creates the strongest invariance property of optimization algorithms with respect to the objective function value possible.
If we can solve an optimization problem with a certain algorithm, we want that the algorithm  behaves the same, i.e., that it still "works," on a slightly different problem.
Without such invariance properties, experimental benchmark results would be useless, as they would not
carry over to the real-world problems we try to solve.
Good algorithms today offer invariance under scaling and shifting of objective value or even under all order-preserving transformations.
One major recent academic achievement of Prof.&nbsp;Weise is the development of an optimization approach called Frequency Fitness Assignment&nbsp;(FFA) that is invariant under all injective transformations of the objective function value.
In other words, this method performs the same even if the objective function is encrypted. 
This is baffling, surprising, and the strongest invariance property ever guaranteed by any non-trivial optimization algorithm.
Prof.&nbsp;Weise also showed that the performance an algorithm on the NP-hard MaxSAT problem is improved by FFA and that its average runtime on several benchmark problems can be reduced from exponential to polynomial. 

Besides achievements in fundamental research, Prof.&nbsp;Weise has contributed for many years to the benchmarking of optimization algorithms, documented by first-author articles in Applied Soft Computing and IEEE&nbsp;Computational Intelligence Magazine.
He was one of the early developers of automated benchmark systems more than a decade ago, which nowadays are used in many fields of optimization and created open source benchmarking systems such as AOAB&nbsp;(for continuous optimization), TSPSuite&nbsp;(for benchmarking algorithms that solve the Traveling Salesperson Problem), the optimizationBenchmarking.org tool suite&nbsp;(for general optimization methods), and the novell [Python](http://thomasweise.github.io/programmingWithPython) experiment execution and evaluation framework [moptipy](https://thomasweise.github.io/moptipy).


## 4. License
Most of the material provided in this repository is released under the Attribution-NonCommercial-ShareAlike 4.0 International license (CC&nbsp;BY&#8209;NC&#8209;SA&nbsp;4.0), see [http://creativecommons.org/licenses/by-nc-sa/4.0](http://creativecommons.org/licenses/by-nc-sa/4.0) for a summary.

Exceptions to this licensing are all LaTeX classes and commands.
Other exceptions are explicitly mentioned, e.g., sometimes a graphic may be under copyright held by another person or organization.

Examples of graphics that do not fall under the Creative Commons license but whose copyright belong to other institutions are:

- `CWTW2024FFAOWBFGSORLSOTQAP_p7_snippet.[pdf|svg]` in directory `shared/graphics/papers`, which is part of a paper published by and under the copyright of SciTePress
- `HS2000LSAFSAEEp46.[pdf|svg]` in directory `shared/graphics/papers`, which is part of a paper published by and under the copyright of Springer
- `LWLvdBTW2024ATTSPWFFAAHA_p12_snippet.[pdf|svg]` in directory `shared/graphics/papers`, which is part of a paper published by and under the copyright of SciTePress
- `WLCW2021SJSSPWUABFGS_p4_snippet.[pdf|svg]` in directory `shared/graphics/papers`, which is part of a paper published by and under the copyright of ACM
- `WWLC2021FFAMOAIUBTOTOFV.[pdf|svg]` in directory `shared/graphics/papers`, which is part of a paper published by and under the copyright of IEEE
- `WWLCL2023FFAOWBFGSCBE.[pdf|svg]` in directory `shared/graphics/papers`, which is part of a paper published by and under the copyright of IEEE
- `WWLCL2023FFAOWBFGSCBE_p10_snippet.[pdf|svg]` in directory `shared/graphics/papers`, which is part of a paper published by and under the copyright of IEEE
- `WWTY2014EEIAWGP_07_snippet.[pdf|svg]` in directory `shared/graphics/papers`, which is part of a paper published by and under the copyright of IEEE
- `WWWTDY2014FFA.[pdf|svg]` in directory `shared/graphics/papers`, which is part of a paper published by and under the copyright of IEEE
- The illustration of Euclid von Alexandria in `shared/graphics/euclidOfAlexandria` is [attributed](https://www.antike-griechische.de/Euklid.pdf) to the painter Charles Paul Landon (1760-1826). Source:&nbsp;[Vikidia](https://fr.vikidia.org/wiki/Cat%C3%A9gorie:Image_Euclide), where it is *domaine public,* i.e., in the Public Domain.


## 5. Other Interesting Things
- We provide an open source and free [book](https://thomasweise.github.io/programmingWithPython) and course on [Python programming](https://thomasweise.github.io/programmingWithPython).
- We provide an open source and free [book](https://thomasweise.github.io/databases) and course on [Databases](https://thomasweise.github.io/databases).
- We provide an open source [Python library](https://thomasweise.github.io/moptipy) on [metaheuristic optimization](https://thomasweise.github.io/moptipy) that supports the automated replicable execution of self-documenting experiments in a parallel and distributed fashion as well as statistical result evaluation.


## 6. Contact
If you have any questions or suggestions, please contact
Prof.&nbsp;Dr.&nbsp;[Thomas Weise](https://thomasweise.github.io) (汤卫思教授)
of the School of Artificial Intelligence and Big Data ([人工智能与大数据学院](http://www.hfuu.edu.cn/aibd))
of [Hefei University](http://www.hfuu.edu.cn/english/) ([合肥大学](http://www.hfuu.edu.cn/)),
in Hefei, Anhui, China (中国安徽省合肥市)
via email to [tweise@hfuu.edu.cn](mailto:tweise@hfuu.edu.cn) with CC to [tweise@ustc.edu.cn](mailto:tweise@ustc.edu.cn).
