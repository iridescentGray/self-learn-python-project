def reg_args_valid(parser):
    parser.add_argument("username", type=str, location="json")
    # dest 则表示设置了参数的别名
    parser.add_argument("password", type=str, dest="pwd", location="json")
