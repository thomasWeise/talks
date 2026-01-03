
from typing import Final

from moptipyapps.tsp.instance import Instance

#: the problem instance that we are working with
INSTANCE: Final[Instance] = Instance.from_resource("cn11")

#: the number of cities
N: Final[int] = INSTANCE.n_cities

C: list[str] = ["Shanghai (上海)", "Beijing (北京)", "Nanjing (南京)", "Hefei (合肥)", "Harbin (哈尔滨)", "Kunming (昆明)", "Wuhan (武汉)", "Xi'an (西安)", "Chongqing (重庆)", "Changsha (长沙)", "Hong Kong (香港)"]

for i in range(N):
    for j in range(i + 1, N):
        dij = INSTANCE[i, j]
        for k in range(j + 1, N):
            dik = INSTANCE[i, k]
            dkj = INSTANCE[k, j]
            dikj = dik + dkj
            if dikj < dij:
                print(f"{C[i]} - {C[j]} = {dij} km")
                print(f"{C[i]} - {C[k]} = {dik} km")
                print(f"{C[k]} - {C[j]} = {dkj} km")
                print(f"{dik} + {dkj} = {dikj} < {dij}")
                print()
