# Talks by Prof. Dr. Thomas Weise

## 1. Introduction

[Here](https://thomasweise.github.io/talks) you can find some of the talks given by Prof. Dr. Thomas Weise (汤卫思教授). 

- [Comparing Optimization Algorithms](https://thomasweise.github.io/talks/comparingOptimizationAlgorithms.pdf)
- [Frequency Fitness Assignment](https://thomasweise.github.io/talks/ffa.pdf)

## 2. Talk Abstracts

- **[Frequency Fitness Assignment](https://thomasweise.github.io/talks/ffa.pdf):**&nbsp;Optimization problems are situations where we have to pick one of many possible choices and want to do this in such a way that we reach a pre-defined goal at a minimum cost.
    Classical optimization problems include the Traveling Salesperson Problem, the Maximum Satisfiability Problem (MaxSat), and the Bin Packing problem, for example.
    Since these problems are NP-hard and solving them to optimality would require exponential runtime in the worst case, metaheuristic algorithms have been developed that deliver near-optimal solutions in acceptable runtime.
    Examples for classical metaheuristics are the (1+1)&nbsp;EA, Simulated Annealing&nbsp;(SA), and the Standard Genetic Algorithm&nbsp;(SGA).
    Since we want that such algorithms should behave the same in both quick benchmarking experiments and in practical application, we would like them to exhibit invariance properties.
    Whereas the (1+1)&nbsp;EA is invariant under all order-preserving transformations of the objective function value, SA is not invariant under scaling of the objective function and the SGA is not invariant under translations of the objective function.
    Frequency Fitness Assignment&nbsp;(FFA) is an algorithm module that can be plugged into existing algorithms and makes them invariant under all injective transformations of the objective function value&nbsp;(which goes far beyond order-preserving transformations).
    We plug FFA into the (1+1)&nbsp;EA.
    We show that the resulting (1+1)&nbsp;FEA can solve Trap, TwoMax, and Jump problems in polynomial runtime, whereas the (1+1)&nbsp;EA needs exponential runtime.
    Moreover, the (1+1)&nbsp;FEA performs very significantly faster on the NP-hard MaxSat problem.
    We conclude the presentation with an outline of other properties of FFA and our other recent works.

## 3. Speaker Biography
Prof.&nbsp;Dr.&nbsp;Thomas WEISE&nbsp;(汤卫思), male, German, born in 1981, holds a full professorship at Hefei University&nbsp;(合肥大学) in the city Hefei&nbsp;(合肥市) in the province Anhui&nbsp;(安徽省) in China.
He received his Diplom-Informatiker (i.e., a combined Bachelor&nbsp;(学士) and Master’s&nbsp;(硕士) degree) in Computer Science from the Chemnitz University of Technology&nbsp;(德国开姆尼茨工业大学) in Chemnitz, Germany&nbsp;(德国开姆尼茨市) in 2005 and his doctoral degree&nbsp;(博士) from the University of Kassel&nbsp;(德国卡塞尔大学) in Kassel, Germany&nbsp;(德国卡
塞尔市) in 2009.
Prof.&nbsp;Weise joined the School of Computer Science and Technology&nbsp;(计算机科学与技术学院) of the University of
Science and Technology of China&nbsp;(USTC, 中国科学技术大学) in Hefei as PostDoc&nbsp;(博士后) from 2009 to 2011.
He then was promoted to Associate Professor&nbsp;(副教授) in the same school.
In 2016, Prof.&nbsp;Weise moved to Hefei University&nbsp;(合肥大学) to found the Institute of Applied Optimization&nbsp;(IAO, 应用优化研究所), which he leads as director, at the School of Artificial Intelligence and Big Data&nbsp;(人工智能与大数据学院).
Prof.&nbsp;Weise holds the 2025 Huangshan Friendship Award of Anhui Province&nbsp;(安徽省黄山友谊奖), the 2020 Hefei City Friendship Award&nbsp;(外国专家“友谊奖”), the title Hefei Specially Recruited Foreign Expert&nbsp;(合肥市特聘外国专家证书首批市“引进外国高端人才计划”), and has received the Foreign Expert Office of Hefei University&nbsp;(合肥大学外国专家工作室).

The research field of Prof. Weise is metaheuristic optimization, where he made important contributions to both fundamental and applied research.
Prof.&nbsp;Weise is the author of over 50&nbsp;journal articles and 79&nbsp;conference papers.
He has authored 139&nbsp;peer-reviewed scientific publications in total.
According to GoogleScholar, his work has been cited more than 4500&nbsp;times and he has an h-index of&nbsp;30 and an i10-index of&nbsp;59.
He has authored or co-authored works in journals such as the IEEE Transactions on Evolutionary Computation, the IEEE Computational Intelligence Magazine, the IEEE Transactions on Image Processing, Information Fusion, Pattern Recognition, Information Sciences, Applied Soft Computing, Soft Computing, the European Journal of Operational Research, Evolutionary Computation, the Journal of Global Optimization, the Journal of Computer Science &amp; Technology, and the Journal of Combinatorial Optimization.
Prof.&nbsp;Weise is editorial board member of Applied Soft Computing and reviewer for over 30&nbsp;journals and over 70&nbsp;conferences.
His book&nbsp;"[Global Optimization Algorithms &mdash; Theory and Application](https://www.researchgate.net/publication/200622167)" has been cited more than 1300&nbsp;times.

The recent works of Prof.&nbsp;Weise focus on Frequency Fitness Assignment&nbsp;(FFA) and benchmarking of optimization algorithms.
FFA is an algorithm module that creates the strongest invariance property of optimization algorithms with respect to the objective function value possible.
If we can solve an optimization problem with a certain algorithm, we want that the algorithm  behaves the same, i.e., that it still "works," on a slightly different problem.
Without such invariance properties, experimental benchmark results would be useless, as they would not
carry over to the real-world problems we try to solve.
Good algorithms today offer invariance under scaling and shifting of objective value or even under all order-preserving transformations.
One major recent academic achievement of Prof.&nbsp;Weise is the development of an optimization approach called Frequency Fitness Assignment&nbsp;(FFA) that is invariant under all injective transformations of the objective function value.
In other words, this method performs the same even if the objective function is encrypted. 
This is baffling, surprising, and the strongest invariance property ever guaranteed by any non-trivial optimization algorithm.
Prof.&nbsp;Weise also showed that the performance an algorithm on the NP-hard MAX-SAT problem is improved by FFA and that its average runtime on several benchmark problems can be reduced from exponential to polynomial. 

Besides achievements in fundamental research, Prof.&nbsp;Weise has contributed for many years to the benchmarking of optimization algorithms, documented by first-author articles in the 中科院大区1区 journals Applied Soft Computing and IEEE Computational Intelligence Magazine&nbsp;(CAA-A类).
He was one of the pioneers of the idea of automated benchmark systems more than a decade ago, which nowadays are used in many fields of optimization and created open source benchmarking systems such as AOAB (for continuous optimization), TSPSuite (for benchmarking algorithms that solve the Traveling Salesperson Problem), the optimizationBenchmarking.org tool suite (for general optimization methods), and the novell Python experiment execution and evaluation framework [moptipy](https://thomasweise.github.io/moptipy).


## 4. License
Most of the material provided in this repository is released under the Attribution-NonCommercial-ShareAlike 4.0 International license (CC&nbsp;BY&#8209;NC&#8209;SA&nbsp;4.0), see [http://creativecommons.org/licenses/by-nc-sa/4.0](http://creativecommons.org/licenses/by-nc-sa/4.0) for a summary.

Exceptions to this licensing are all LaTeX classes and commands.
Other exceptions are explicitly mentioned, e.g., sometimes a graphic may be under copyright held by another person or organization.

## 5. Contact
If you have any questions or suggestions, please contact
Prof. Dr. Thomas Weise (汤卫思教授)
at the Institute of Applied Optimization (应用优化研究所, IAO)
of the School of Artificial Intelligence and Big Data ([人工智能与大数据学院](http://www.hfuu.edu.cn/aibd))
of [Hefei University](http://www.hfuu.edu.cn/english/) ([合肥大学](http://www.hfuu.edu.cn/)),
in Hefei, Anhui, China (中国安徽省合肥市)
via email to [tweise@hfuu.edu.cn](mailto:tweise@hfuu.edu.cn) with CC to [tweise@ustc.edu.cn](mailto:tweise@ustc.edu.cn).
