import logging

import matplotlib.pyplot as plt
import seaborn as sns

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    sns.set_theme()
    plt.rcParams["font.sans-serif"] = ["SimHei", "Songti SC", "STFangsong"]
    plt.rcParams['axes.unicode_minus'] = False

    # 从网络中加载例子数据
    tips_df = sns.load_dataset('tips')
    logging.info(f"type tips_df {type(tips_df)}")
    logging.info(f"tips_df {tips_df}")
    logging.info(
        f"----------------------------分布图------------------------------------------"
    )
    sns.histplot(data=tips_df, x='total_bill', kde=True)
    plt.show()

    logging.info(
        f"---------------------------点对图------------------------------------------"
    )
    sns.pairplot(data=tips_df, hue='sex')
    plt.show()
    # 修改颜色
    sns.pairplot(data=tips_df, hue='sex', palette='Dark2')
    plt.show()
    logging.info(
        f"---------------------------联合分布图------------------------------------------"
    )
    sns.jointplot(data=tips_df, x='total_bill', y='tip', hue='sex')
    plt.show()

    logging.info(
        f"---------------------------线性回归模型图------------------------------------------"
    )
    # 类似于DataFrame的 corr 方法,可以显示两个变量的相关性
    sns.lmplot(data=tips_df, x='total_bill', y='tip', hue='sex')
    plt.show()

    logging.info(
        f"---------------------------箱线图/小提琴图------------------------------------------"
    )
    # 了解账单金额的集中和离散趋势，可以绘制箱线图或小提琴图
    sns.boxplot(data=tips_df, x='day', y='total_bill')
    plt.show()
    sns.violinplot(data=tips_df, x='day', y='total_bill')
    plt.show()
