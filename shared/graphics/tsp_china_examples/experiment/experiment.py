"""The small TSP experiment."""
from typing import Any, Callable, Final

import numpy as np
from astar import find_path
from moptipy.algorithms.random_sampling import RandomSampling
from moptipy.algorithms.so.rls import RLS
from moptipy.api.algorithm import Algorithm
from moptipy.api.execution import Execution
from moptipy.api.experiment import run_experiment
from moptipy.api.process import Process
from moptipy.operators.permutations.op0_shuffle import Op0Shuffle
from moptipy.operators.permutations.op1_swap2 import Op1Swap2
from moptipy.operators.permutations.op1_swapn import Op1SwapN
from moptipy.spaces.permutations import Permutations
from moptipyapps.tsp.instance import Instance
from moptipyapps.tsp.tour_length import TourLength
from pycommons.io.path import Path

#: the problem instance that we are working with
INSTANCE: Final[Instance] = Instance.from_resource("cn11")

#: the number of cities
N: Final[int] = INSTANCE.n_cities

#: the nodes, i.e., the cities
NODES: Final[frozenset[int]] = frozenset(range(N))

#: the neighbors of each city, sorted by distance
SORTED_NEIGHBORS: Final[tuple[tuple[tuple[int, int], ...], ...]] = tuple(
    tuple(sorted((int(INSTANCE[i, j]), j) for j in range(N) if j != i))
    for i in range(N))

#: the maximum FEs
MAX_FES: Final[int] = 100_000_000

#: the shared objective function
OBJECTIVE: Final[TourLength] = TourLength(INSTANCE)

#: the shared solution space
SPACE: Final[Permutations] = Permutations(range(N))

#: the results directory
RESULTS_DIR: Final[Path] = Path(__file__).up(3).resolve_inside("results")


class AStar(Algorithm):
    """An implementation of the A* algorithm."""

    def __init__(self):
        """Initialize."""
        super().__init__()
        #: the internal solution
        self.__solution: Final[np.ndarray] = SPACE.create()
        #: the current process
        self.__process: Process | None = None

    def neighbors(self, x: tuple[int, ...]) -> list[tuple[int, ...]]:
        result: list[tuple[int, ...]] = []
        for k in NODES.difference(x):
            y = list(x)
            y.append(k)
            result.append(tuple(y))
        return result

    def distance_between(self, x: tuple[int, ...], y: tuple[int, ...]) -> int:
        ly: int = tuple.__len__(y)
        lx: int = tuple.__len__(x)
        y1: int = y[ly - 1]

        if ly != (lx + 1):
            raise ValueError(f"Invalid lengths {ly} and {lx}.")
        if y[0:lx] != x:
            raise ValueError(f"{y} does not fit to {x}.")
        r = int(INSTANCE[x[lx - 1], y1])
        if ly < N:
            return r
        r += int(INSTANCE[y1, x[0]])
        self.__solution[:] = y
        if self.__process is not None:
            if not self.__process.should_terminate():
                z = self.__process.evaluate(self.__solution)
        return r

    def is_goal_reached(self, x: tuple[int, ...], _) -> bool:
        return (tuple.__len__(x) >= N) or ((self.__process is not None) and (
            self.__process.should_terminate()))

    def heuristic_cost_estimate(self, x: tuple[int, ...], _) -> int:
        remaining: frozenset[int] = NODES.difference(x[1:])
        total: int = 0
        for k in x:
            for dist, j in SORTED_NEIGHBORS[k]:
                if j in remaining:
                    total += dist
                    break
        return total

    def solve(self, process: Process) -> None:
        self.__process = process
        find_path(tuple([int(process.get_random().integers(N))]),
                  None, self.neighbors, False,
                  self.heuristic_cost_estimate, self.distance_between,
                  self.is_goal_reached)

    def __str__(self) -> str:
        return "astar"


def base_setup(_) -> Execution:
    """
    Create the baseline setup.

    :return: the setup
    """
    return Execution().set_objective(OBJECTIVE).set_solution_space(
        SPACE).set_log_improvements(True).set_max_fes(MAX_FES)


#: the shared A* instance
ASTAR: Final[AStar] = AStar()
#: the shared op0
OP0: Final[Op0Shuffle] = Op0Shuffle(SPACE)
#: the shared random sampling
RS: Final[RandomSampling] = RandomSampling(OP0)
#: the shared op1 s2
OP1_S2: Final[Op1Swap2] = Op1Swap2()
#: the rls op1 swap 2
RLSS2: Final[RLS] = RLS(OP0, OP1_S2)
#: the shared op1 sn
OP1_SN: Final[Op1SwapN] = Op1SwapN()
#: the rls op1 swap N
RLSSN: Final[RLS] = RLS(OP0, OP1_SN)


def setup(a: Algorithm) -> Callable[[Any], Execution]:
    return lambda _, __a=a: base_setup(None).set_algorithm(__a)


nruns: list[int] = [(10 * r) + 1 for r in range(34)]
nruns.append(333)
nruns.sort()

run_experiment(
    base_dir=RESULTS_DIR,
    instances=[lambda: INSTANCE.name],
    setups=[setup(ASTAR), setup(RS), setup(RLSS2), setup(RLSSN)],
    n_runs=nruns,
    perform_warmup=False,
    perform_pre_warmup=True,
)
