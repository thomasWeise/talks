"""Make the examples."""
from typing import Final

from moptipy.operators.permutations.op0_shuffle import Op0Shuffle
from moptipy.operators.permutations.op1_swap2 import Op1Swap2
from moptipy.operators.permutations.op1_swapn import Op1SwapN
from moptipy.spaces.permutations import Permutations
from moptipyapps.tsp.instance import Instance
from moptipyapps.tsp.tour_length import TourLength
from numpy.random import default_rng
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

#: the shared op0
OP0: Final[Op0Shuffle] = Op0Shuffle(SPACE)
#: the shared op1 s2
OP1_S2: Final[Op1Swap2] = Op1Swap2()
#: the shared op1 sn
OP1_SN: Final[Op1SwapN] = Op1SwapN()

C: list[str] = ["Shanghai (上海)", "Beijing (北京)", "Nanjing (南京)", "Hefei (合肥)", "Harbin (哈尔滨)", "Kunming (昆明)", "Wuhan (武汉)", "Xi'an (西安)", "Chongqing (重庆)", "Changsha (长沙)", "Hong Kong (香港)"]
CNS: list[str] = [str.strip(cc[:cc.index(" ")]) for cc in C]
DNS: list[str] = [str.strip(cc[cc.rfind(" ") + 1:])[1:-1] for cc in C]


def cts(a, zzzz=CNS) -> str:
    start: int = a.index(3)
    return ", ".join(map(zzzz.__getitem__, a))


seed: int = 0

while True:
    random = default_rng(seed)
    seed += 1

    done: list[tuple[int, list[int]]] = []

    best_x = SPACE.create()
    OP0.op0(random, best_x)
    if best_x[0] != 3:
        continue
    best_f = OBJECTIVE.evaluate(best_x)
    if best_f < 14_000:
        continue
    new_x = SPACE.create()

    done.append((best_f, list(best_x)))
    always_add: bool = True
    for i in range(10000):
        OP1_SN.op1(random, new_x, best_x)
        new_f = OBJECTIVE.evaluate(new_x)
        if new_f < best_f:
            if new_x[0] == 3:
                best_f = new_f
                best_x, new_x = new_x, best_x
                done.append((best_f, list(best_x)))
                always_add = random.integers(2) <= 0
                if best_f <= INSTANCE.tour_length_lower_bound:
                    break
        elif always_add:
            always_add &= (random.integers(2) <= 0)
            done.append((new_f, list(new_x)))

    if best_f > INSTANCE.tour_length_lower_bound:
        continue

    if best_x[0] != 3:
        continue

    if not (6 < list.__len__(done) <= 12):
        continue

    can_do: bool = False
    last: tuple[int, list[int]] | None = None
    ofs = len(done) - 2
    diff: int = -1
    for current in done:
        if last is None:
            last = current
            continue
        if last[0] < current[0]:
            last = current
            continue
        vec_1 = last[1]
        vec_2 = current[1]
        diff = sum(vec_1[k] != vec_2[k] for k in range(N))
        if diff > 2:
            can_do = True
        last = current
    if not can_do:
        continue
    if diff <= 2:
        continue

    can_do: bool = True
    last: tuple[int, list[int]] | None = None
    ofs = len(done) - 2
    diff: int = -1
    for current in done:
        if last is None:
            last = current
            continue
        vec_1 = last[1]
        vec_2 = current[1]
        diff = sum(vec_1[k] != vec_2[k] for k in range(N))
        if diff > 4:
            can_do = False
        last = current
    if not can_do:
        continue

    for ff, xx in done:
        print(f"start={ff}; {cts(xx)}")
        continue

    print()
    for ff, xx in done:
        print(f"start={ff}; {cts(xx, DNS)}")

    break

exit(0)

seed: int = 0

while True:
    random = default_rng(seed)
    seed += 1

    done: list[tuple[int, list[int]]] = []

    best_x = SPACE.create()
    OP0.op0(random, best_x)
    best_f = OBJECTIVE.evaluate(best_x)
    if best_f < 14_000:
        continue
    new_x = SPACE.create()

    done.append((best_f, list(best_x)))
    always_add: bool = True
    for i in range(1000000):
        OP1_S2.op1(random, new_x, best_x)
        new_f = OBJECTIVE.evaluate(new_x)
        if new_f < best_f:
            best_f = new_f
            best_x, new_x = new_x, best_x
            done.append((best_f, list(best_x)))
            always_add = random.integers(2) <= 0
            if best_f <= INSTANCE.tour_length_lower_bound:
                break
        elif always_add:
            always_add &= (random.integers(2) <= 0)
            done.append((new_f, list(new_x)))

    if best_f <= INSTANCE.tour_length_lower_bound:
        continue

    if not (6 < list.__len__(done) <= 16):
        continue

    for ff, xx in done:
        print(f"start={ff}; {cts(xx)}")
        continue

    print()
    for ff, xx in done:
        print(f"start={ff}; {cts(xx, DNS)}")

    break
