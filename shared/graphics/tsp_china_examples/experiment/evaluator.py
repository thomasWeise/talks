"""Evaluate the experimental results."""
from typing import Final

from moptipy.evaluation.axis_ranger import AxisRanger
from moptipy.evaluation.plot_progress import plot_progress
from moptipy.evaluation.progress import Progress
from moptipy.evaluation.progress import from_logs as pr_from_logs
from moptipy.evaluation.stat_run import StatRun
from moptipy.evaluation.stat_run import from_progress as sr_from_progress
from moptipy.utils.plot_utils import create_figure, save_figure
from pycommons.io.path import Path

#: the results directory
RESULTS_DIR: Final[Path] = Path(__file__).up(3).resolve_inside("results")

#: the results directory
EVALUATION_DIR: Final[Path] = RESULTS_DIR.up(1).resolve_inside("evaluation")
EVALUATION_DIR.ensure_dir_exists()

NAME_AS: Final[str] = "A★"
NAME_RS: Final[str] = "Random Sampling"
NAME_RLS2: Final[str] = "RLS-2"
NAME_RLSN: Final[str] = "RLS-N"
ALL_NAMES: Final[tuple[str, ...]] = (
    NAME_RS, "rs", NAME_AS, "astar",
    NAME_RLS2, "rls_swap2", NAME_RLSN, "rls_swapn")

for time_dim in ("FEs", "ms"):

    runs: list[Progress] = []  # we will load the data into this list
    pr_from_logs(path=RESULTS_DIR,  # the result directory
                 consumer=runs.append,  # put the data into data
                 time_unit=time_dim,  # time is in FEs (as opposed to "ms")
                 f_name="plainF")  # use raw, unscaled objective values
    stats: list[StatRun] = []

    def name(nm: str) -> str:
        if nm.startswith("a"):
            return NAME_AS
        if nm.startswith("rs"):
            return NAME_RS
        if nm.endswith("swap2"):
            return NAME_RLS2
        if nm.endswith("swapn"):
            return NAME_RLSN
        return nm

    # Let us now convert the progress data to statistics runs.
    # We apply StatRun.from_progress to a copy of the data and append all
    # new StatRuns to the original data list.
    # This function will automatically choose to compute statistics over
    # algorithm*instance combinations unless we tell it otherwise.
    # We tell it to compute the arithmetic means.
    sr_from_progress(source=runs,  # iterate over _copy_ of data
                     statistics="mean",  # compute the mean f over FEs
                     consumer=stats.append)  # and store to data list

    #: the maximum FEs
    MAX: int = 100_000_000 if time_dim.startswith("F") else 1_000_000
    MIN: int = 1 if time_dim.startswith("F") else 1
    FMAX: int = 16_000 if time_dim.startswith("F") else 11_750

    for i, sel in enumerate([(NAME_RS, ), (NAME_AS, NAME_RS),
                             (NAME_AS, NAME_RS, NAME_RLS2),
                             ALL_NAMES]):
        width: float = 3.5
        fig = create_figure(width=width, height=width / 4 * 2.25)  # create an empty, 4"-wide figure
        # We now plot the single runs AND the mean result quality over time into
        # the same diagram. Notice that the system will again automatically choose
        # an appropriate style.
        plot_progress(
            progresses=[sr for sr in stats if name(sr.algorithm) in sel],
            figure=fig, algorithm_namer=name, x_label_location=0.01,
            y_axis=AxisRanger.for_axis(
                "plainF", log_scale=False, chosen_max=FMAX),
            x_axis=AxisRanger.for_axis(
                time_dim, log_scale=True, chosen_max=MAX, chosen_min=MIN),
            algorithm_sort_key=ALL_NAMES.index)
        save_figure(
            fig=fig,  # save the figure
            file_name=f"progress_over_log_{time_dim}_{i + 1}",
            dir_name=EVALUATION_DIR, formats="svg")
        del fig  # dispose figure
