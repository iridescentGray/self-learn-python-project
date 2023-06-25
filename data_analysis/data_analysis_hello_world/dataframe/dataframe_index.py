import logging

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    """
    -索引是重要的基础
    """
    logging.info(
        f"----------------------------范围索引（RangeIndex）------------------------------------------"
    )
    sales_data = np.random.randint(400, 1000, 12)
    month_index = pd.RangeIndex(1, 13, name='月份')
    range_idx_ser = pd.Series(data=sales_data, index=month_index)
    logging.info(f"month_ser index: \n{range_idx_ser}")
    logging.info(
        f"----------------------------分类索引（CategoricalIndex）------------------------------------------"
    )
    cate_index = pd.CategoricalIndex(
        ['苹果', '香蕉', '苹果', '苹果', '桃子', '香蕉'],
        ordered=True,
        categories=['苹果', '香蕉', '桃子']
    )
    categorical_idx_ser = pd.Series(data=range(6), index=cate_index)
    logging.info(f"categorical_idx_ser: \n{categorical_idx_ser}")
    # group by index
    logging.info(f"categorical_idx_ser group by: \n{categorical_idx_ser.groupby(level=0).sum()}")

    logging.info(
        f"----------------------------多级索引（MultiIndex）------------------------------------------"
    )
    # from_product方法通过第一个参数的两组数据的笛卡尔积，构造了多级索引。
    multi_index = pd.MultiIndex.from_product((np.arange(1001, 1006), ['期中', '期末']), names=['学号', '学期'])
    multi_index_df = pd.DataFrame(data=np.random.randint(60, 101, (10, 3)), columns=['语文', '数学', '英语'],
                                  index=multi_index)

    logging.info(f"multi_index_df: \n{multi_index_df}")
    # 计算每个学生的成绩，期中占25%，期末占75%
    logging.info(
        f"multi_index_df: \n{multi_index_df.groupby(level=0).agg(lambda x: x.values[0] * 0.25 + x.values[1] * 0.75)}")

    logging.info(
        f"----------------------------日期时间索引（DatetimeIndex）------------------------------------------"
    )
    # 间隔10天
    date_range_periods_10 = pd.date_range('2021-1-1', '2021-6-1', periods=10)
    logging.info(f"Date time Index periods=10: \n{date_range_periods_10}")
    # 间隔一星期
    date_range_periods_week = pd.date_range('2021-1-1', '2021-6-1', freq='W')

    logging.info(f"Date time Index, calculate': \n{date_range_periods_week - pd.DateOffset(days=2)}")
    logging.info(f"Date time Index, calculate': \n{date_range_periods_week + pd.DateOffset(days=2)}")
