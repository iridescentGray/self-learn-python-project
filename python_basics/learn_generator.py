# 生成器generator
if __name__ == "__main__":
    print(
        "----------------------generator function type--------------------------------"
    )

    def gen_type():
        yield

    print(type(gen_type()))  # 输出 <class 'generator'> 带yield的函数都是 generator
    print(type(gen_type))  # 输出 <class 'function'>  未调用的生成器，还是function
    print(gen_type)  # 输出 <function gen_type at>  未调用的生成器，还是function
    print("----------------------generator function--------------------------------")

    def number_gen(num):
        print("starting number_gen...")
        while num < 10:
            num = num + 1
            yield num

    gen_nums = number_gen(0)
    for gen_num in gen_nums:
        print(gen_num)
    print(type(gen_nums))  # 输出 <class 'generator'> 带yield的函数都是 generator
    print(gen_nums)  # 输出 <generator object number_gen> 带yield的函数都是 generator

    print("----------------------List Generative --------------------------------")
    my_list = [x * x for x in range(10)]
    print(type(my_list))  # <class 'list'>
    print(my_list)

    print("----------------------Generative--------------------------------")
    genera = (x * x for x in range(10))  # 外层是()，就是generator类型
    print(type(genera))  # 输出 <class 'generator'>，生成式
    print(genera)  # 输出 <generator object <genexpr> at>，生成式

    print(
        "----------------------double Generative func--------------------------------"
    )

    def double_number_gens(double_num):
        print("starting double_number_gens...")
        while double_num < 10:
            double_num = double_num + 1
            print("one double_num" + str(double_num))
            yield double_num

        while double_num > 0:
            double_num = double_num - 1
            print("two double_num" + str(double_num))
            yield double_num

    for double_gen_num in double_number_gens(1):
        print(double_gen_num)
