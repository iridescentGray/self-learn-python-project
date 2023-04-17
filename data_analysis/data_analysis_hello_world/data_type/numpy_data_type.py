import logging

import numpy as np

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    simple_array = np.array([1, 2, 3, 4, 5])
    logging.info("simple_array: %s", simple_array)
    range_array = np.arange(0, 20, 2)
    logging.info("range_array: %s", range_array)
    linspace_array = np.linspace(-5, 5, 101)
    logging.info("linspace_array: %s", linspace_array)
