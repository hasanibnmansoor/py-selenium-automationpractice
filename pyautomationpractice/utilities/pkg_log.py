import logging
import sys

__all__ = ["logger"]


# Logging Setup
FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(module)s:%(funcName)s:%(lineno)d — %(message)s"
)


def console_log() -> logging.StreamHandler:
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def log(logger_name: str, log_level: str = "DEBUG") -> logging.Logger:
    log_handler = logging.getLogger(logger_name)
    LOG_LEVEL = getattr(logging, log_level)
    log_handler.setLevel(LOG_LEVEL)
    log_handler.addHandler(console_log())
    log_handler.propagate = False
    return log_handler


logger = log("AutomationPractice")
