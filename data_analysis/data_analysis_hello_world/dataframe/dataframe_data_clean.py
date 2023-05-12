import logging

import pandas as pd

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    """
    -从 Excel、CSV、数据库中获取到的数据并不是非常完美的，可能混入了重复值、异常值、缺失值，
    也可能存在格式不统一、量纲不统一等问题。因此在开始数据分析之前，对数据进行清洗特别重要

    在对数据进行清晰和操作前，有一些重要的认识：
    1.DataFrame对象的很多方法都有一个名为inplace参数(默认值False 不修改原对象),如果设为True，那会直接修改原DataFrame上，让方法的返回值为None
    """

    data = {
        "eno": [
            1359,
            2056,
            3088,
            3211,
            3233,
            3244,
            3251,
            3344,
            3577,
            3588,
            4466,
            5234,
            5566,
            7800,
        ],
        "ename": [
            "胡一刀",
            "乔峰",
            "李莫愁",
            "张无忌",
            "丘处机",
            "欧阳锋",
            "张翠山",
            "黄蓉",
            "杨过",
            "朱九真",
            "苗人凤",
            "郭靖",
            "宋远桥",
            "张三丰",
        ],
        "job": [
            "销售员",
            "分析师",
            "设计师",
            "程序员",
            "程序员",
            "程序员",
            "程序员",
            "销售主管",
            "会计",
            "会计",
            "销售员",
            "出纳",
            "会计师",
            "总裁",
        ],
        "mgr": [
            3344.0,
            7800.0,
            2056.0,
            2056.0,
            2056.0,
            None,
            2056.0,
            7800.0,
            5566.0,
            5566.0,
            3344.0,
            5566.0,
            7800.0,
            None,
        ],
        "sal": [
            1800,
            5000,
            3500,
            3200,
            3400,
            3200,
            4000,
            3000,
            2200,
            2500,
            2500,
            2000,
            4000,
            9000,
        ],
        "comm": [
            200.0,
            1500.0,
            800.0,
            None,
            None,
            100.0,
            None,
            800.0,
            None,
            200.0,
            300.0,
            None,
            1000.0,
            1200.0,
        ],
        "dno": [30, None, 20, 20, 20, 20, 20, 30, 10, 10, 30, 10, 10, 20],
    }

    need_clean_data = pd.DataFrame(data).set_index("eno")
    logging.info(f"need_clean_data: \n{need_clean_data}")

    logging.info(
        f"-----------------------------空值处理------------------------------------------"
    )
    # 使用isnull或isna， 找出数据表中的缺失值
    logging.info(f"need_clean_data.isnull: \n{need_clean_data.isnull()}")
    logging.info(f"need_clean_data.isna: \n{need_clean_data.isna()}")

    # 删除这些缺失值使用dropna方法,axis参数可以指定沿着0轴还是1轴(纵轴)删除，默认是沿0轴(横轴)删除
    logging.info(f"need_clean_data.dropna: \n{need_clean_data.dropna()}")
    logging.info(f"need_clean_data.dropna(axis=1): \n{need_clean_data.dropna(axis=1)}")

    # 使用fillna对空值进行填充，通过value参数可以用指定值填充，通过method=ffill 参数可以用表格中前一个单元格填充，通过method=bfill参数可以用表格中后一个单元格填充
    logging.info(
        f"need_clean_data.fillna(value=0): \n{need_clean_data.fillna(value=0)}"
    )

    logging.info(
        f"-----------------------------重复处理------------------------------------------"
    )
    # 判断行是否存在重复值(不指定参数时默认判断行索引是否重复)
    logging.info(f"need_clean_data.duplicated: \n{need_clean_data.duplicated('job')}")

    # 删除重复值 keep参数可以控制在遇到重复值时的处理方法，保留第一项/最后一项(last)/一个都不用保留
    logging.info(
        f"need_clean_data.drop_duplicates: \n{need_clean_data.drop_duplicates('job')}"
    )
    logging.info(
        f"need_clean_data.drop_duplicates: \n{need_clean_data.drop_duplicates('job', keep='last')}"
    )

    logging.info(
        f"-----------------------------预处理------------------------------------------"
    )
    sales_df = pd.read_excel(
        "file_for_read/2020_sales_data.xlsx",
        usecols=["销售日期", "销售区域", "销售渠道", "品牌", "销售数量"],
    )
    logging.info(f"sales_data_df: \n{sales_df}")
    # 为sales_data追加列
    # 通过日期时间类型列的dt属性，获得一个访问日期时间的对象
    sales_df["年"] = sales_df["销售日期"].dt.year
    sales_df["月份"] = sales_df["销售日期"].dt.month
    sales_df["日"] = sales_df["销售日期"].dt.day
    sales_df["季度"] = sales_df["销售日期"].dt.quarter
    sales_df["星期"] = sales_df["销售日期"].dt.weekday
    logging.info(f"sales_data_df: \n{sales_df}")
