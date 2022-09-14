import logging


logger = logging.getLogger(__name__)


def some_func():
    logger.info("info message mod_2")
    import pdb

    pdb.set_trace()
    return
