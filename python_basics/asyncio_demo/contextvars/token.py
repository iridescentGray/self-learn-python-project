import contextvars

"""

contextvars.Token 最大的用处就是和 reset 搭配使用，对状态进行重置。

"""

context_var = contextvars.ContextVar("context_var")
# 调用 context_var.set 的时候，其实会返回一个 contextvars.Token
token = context_var.set("val")
print(f"token: {token}")


# Token 对象有一个 var 属性，它是只读的，会返回指向此 token 的 ContextVar 对象。

print(
    f"token.var: {token.var}"
)  # <ContextVar name='context_var' at 0x000002038EA6E4F0>

# Token 对象有一个 var 属性，它是只读的，会返回指向此 token 的 ContextVar 对象。
print(f"token.var is context_var : {token.var is context_var}")  # True
print(f"token.var.get(): {token.var.get()}")  # val

# Token的old_value属性: 返回上一次 set 设置的值，如果是第一次 set,那么没有历史数据，会返回一个 <Token.MISSING>
# 此token 是第一次 set时，被返回的,所以没有历史数据
print(f"token.old_value: {token.old_value}")  # token.old_value: <Token.MISSING>
token = context_var.set("val1")
# 返回上一次 set 的值
print(f"token.old_value after set: {token.old_value}")


context_var.reset(token)
# 查看reset后的值
print(f"context_var.get() after reset : {context_var.get()}")  # val
