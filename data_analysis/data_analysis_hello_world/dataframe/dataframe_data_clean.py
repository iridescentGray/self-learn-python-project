import logging

import numpy as np
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
        f"-----------------------------数据预处理------------------------------------------"
    )
    sales_df = pd.read_excel(
        "file_for_read/2020_sales_data.xlsx"
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

    logging.info(
        f"-----------------------------数据深度预处理------------------------------------------"
    )
    # 深度的分析和挖掘，字符串、日期时间这样的非数值类型都需要处理成数值，因为非数值类型没有办法计算相关性
    # 字符串类型，通常有三类处理方法：
    # 1.有序变量（Ordinal Variable）：若字符串数据有顺序关系，可以对字符串进行序号化处理。
    # 2.分类变量（Categorical Variable）/ 名义变量（Nominal Variable）：字符串数据没有大小关系和等级之分，可以用独热编码的方式处理成哑变量（虚拟变量）矩阵。
    # 3.定距变量（Scale Variable）：字符串有大小高低，且可进行加减运算，那么只需要将字符串处理成对应的数值即可。

    deep_data_handle_df = pd.DataFrame(
        data={
            '姓名': ['关羽', '张飞', '赵云', '马超', '黄忠'],
            '职业': ['医生', '医生', '程序员', '画家', '教师'],
            '学历': ['研究生', '大专', '研究生', '高中', '本科']
        }
    )
    logging.info(f"deep_data_preproces_df: \n{deep_data_handle_df}")
    # 将职业处理成哑变量矩阵。 对应处理方法2.分类变量
    logging.info(f"deep_data_preproces_df_dummies: \n{pd.get_dummies(deep_data_handle_df['职业'])}")

    logging.info(
        f"-----------------------------离散化/分箱------------------------------------------"
    )
    # 若变量的取值是连续值，那么它的取值有无数种可能，那对数据分组时会非常的不方便
    # 之所以把离散化叫做分箱，是因为我们可以预先设置一些箱子，每个箱子代表了数据取值的范围，即实现离散化
    dataframe_from_excel = pd.read_excel(
        io="file_for_read/points_settlement.xlsx", index_col="id"
    )
    # 用describe的返回值作为cut的依据
    logging.info(f"dataframe_from_excel_describe(): \n{dataframe_from_excel.describe()}")
    # 依据describe返回，min 110.050000,max 122.590000，分4段（每3分一组的4个箱子）
    paragraph = np.arange(110, 123, 3)
    # right参数默认值为True，表示箱子左开右闭；False左闭右开
    excel_data_cut_by_paragraph = pd.cut(dataframe_from_excel.score, paragraph, right=False)
    logging.info(f"excel_data_cut_by_paragraph: \n{excel_data_cut_by_paragraph}")

    # pandas还提供了一个名为qcut的函数，可以指定分位数对数据进行分箱