import contextvars


"""
run 方法接收一个 callable,如果在里面修改了值
对于  ContextVars 而言,run方法里设置的值无效
对于 Context 而言,run方法里设置的值有效
"""

context_var1 = contextvars.ContextVar("context_var1")
context_var1.set("val1")
context_var2 = contextvars.ContextVar("context_var2")
context_var2.set("val2")

context = contextvars.copy_context()


def change(val1, val2):
    context_var1.set(val1)
    context_var2.set(val2)
    print(context_var1.get(), context[context_var1])
    print(context_var2.get(), context[context_var2])


context.run(change, "Other1", "Other2")

print(
    "----------------Not Influence context_var1.get(), but Influence context-------------"
)
print(context_var1.get(), context[context_var1])
print(context_var2.get(), context[context_var2])
