def res(data=None, message="Ok", success=True, code=200):
    return {
        "success": success,
        "message": message,
        "data": data,
    }, code


# datetime 转换格式
def format_datetime_to_json(datetime, format="%Y-%m-%d %H:%M:%S"):
    return datetime.strftime(format)
