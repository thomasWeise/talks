from os import remove
from typing import Final

from moptipy.evaluation.progress import Progress
from moptipy.evaluation.progress import from_logs as pr_from_logs
from moptipy.utils.strings import sanitize_names
from pycommons.io.path import Path

#: the results directory
RESULTS_DIR: Final[Path] = Path(__file__).up(3).resolve_inside("results")


def path_to_file(pr: Progress, base_dir: str) -> Path:
    """
    Get the path that would correspond to the log file of this end result.

    Obtain a path that would correspond to the log file of this end
    result, resolved from a base directory `base_dir`.

    :param base_dir: the base directory
    :returns: the path to a file corresponding to the end result record
    """
    return Path(base_dir).resolve_inside(
        pr.algorithm).resolve_inside(pr.instance).resolve_inside(
        sanitize_names([pr.algorithm, pr.instance,
                        hex(pr.rand_seed)]) + ".txt")


runs: list[Progress] = []  # we will load the data into this list
pr_from_logs(path=RESULTS_DIR,  # the result directory
             consumer=runs.append,  # put the data into data
             time_unit="ms",  # time is in FEs (as opposed to "ms")
             f_name="plainF")  # use raw, unscaled objective values

delete: list[Progress] = []
for pr in runs:
    start: int = int(pr.time[0])
    if pr.algorithm.startswith("a"):
        if start > 12200:
            delete.append(pr)
    elif start > 1:
        delete.append(pr)

for pr in delete:
    print(pr)
    remove(path_to_file(pr, RESULTS_DIR))
