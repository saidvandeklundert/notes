import logging


logger = logging.getLogger("app_name")
logger.setLevel(logging.INFO)
logger.info("info message")
logger.debug("debug message")

# add stream to STDERR:
import sys

stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.INFO)
logger.addHandler(stderr_handler)

logger.info("info message")
logger.debug("debug message")

#
import mod_1
import mod_2

mod_1.some_func()
mod_2.some_func()
# Note: mod_2 func will not log to stderr because the logger
# is not referring to "app_name"
