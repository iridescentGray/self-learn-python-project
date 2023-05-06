import logging

import numpy as np
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # np的空值
    logging.info(f'null {np.NaN}')
    logging.info(f'null {np.nan}')
    logging.info(f'NaN  {np.NaN is None}')
    logging.info(f'NaN  {np.nan is None}')
    logging.info(f'NaN  {np.nan is np.NaN}')


