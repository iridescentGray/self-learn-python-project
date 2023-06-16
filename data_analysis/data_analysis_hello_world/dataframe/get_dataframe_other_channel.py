import logging

import pandas as pd

logging.basicConfig(level=logging.INFO)


def read_local_csv():
    """
    read_csv函数的参数非常多，下面接受几个比较重要的参数：
        index_col：用作行索引（标签）的列
        sep / delimiter：分隔符，默认是,
        header：表头（列索引）的位置，默认值是infer，用第一行的内容作为表头（列索引）
        usecols：需要加载的列，可以使用序号或者列名
        true_values / false_values：哪些值被视为布尔值True / False
        skiprows：通过行号、索引或函数指定需要跳过的行
        skipfooter：要跳过的末尾行数
        nrows：需要读取的行数
        na_values：哪些值被视为空值
    """
    dataframe_from_csv = pd.read_csv(
        "file_for_read/points_settlement.csv", index_col="id"
    )
    logging.info(f"dataframe_from_csv: \n{dataframe_from_csv}")


def read_local_excel():
    """
    read_excel与上面的read_csv非常相近，多了一个sheet_name参数来指定数据表的名称，
    不同于 CSV 文件，没有sep或delimiter这样的参数。
    下面的代码中，read_excel函数的skiprows参数是一个 Lambda 函数，通过该 Lambda 函数指定只读取 Excel 文件的表头和其中10%的数据，跳过其他的数据。
    """
    dataframe_from_excel = pd.read_excel(
        io="file_for_read/points_settlement.xlsx", index_col="id"
    )
    logging.info(f"dataframe_from_excel: \n{dataframe_from_excel}")


if __name__ == "__main__":
    read_local_csv()
    read_local_excel()
