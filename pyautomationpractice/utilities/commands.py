import time

from .pkg_log import logger

__all__ = ["wait_until"]


def wait_until(condition, *args, poll_cycle=1, timeout=30, **kwargs):
    """Custom Wait Command.

    Args:
        condition: any callable that returns a boolean
        *args: Positional Arguments to be passed to the condition function
        poll_cycle: Defaulted to 1 second.
        timeout: in seconds to poll. Defaults to 30 seconds
        **kwargs: Key word arguments that's required to be passed in to condition
    Returns:
        condition_seen: boolean - status of condition met within timeout period.
    """
    start = time.perf_counter()
    time_waited = 0
    condition_seen = False
    while (time_waited < timeout) and not condition_seen:
        if condition(*args, **kwargs):
            condition_seen = True
        else:
            time.sleep(poll_cycle)
        time_waited = time.perf_counter() - start
    logger.info(
        f"After {round(time_waited)} seconds, function {condition.__name__} returned {condition_seen}"
    )
    return condition_seen
