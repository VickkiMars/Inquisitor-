import logging
import inspect

def get_caller_info():
    frame = inspect.stack()[2]
    filename = frame.filename
    lineno = frame.lineno
    return f"({filename}:{lineno})"

def log_message(message, level="info"):
    caller_info = get_caller_info()
    match level:
        case "info":
            logging.info(f"{message}{caller_info}")
        case "debug":
            logging.debug(f"{message}{caller_info}")
        case "error":
            logging.error(f"{message}{caller_info}")
        case "critical":
            logging.critical(f"{message}{caller_info}")
        case "warning":
            logging.warning(f"{message}{caller_info}")