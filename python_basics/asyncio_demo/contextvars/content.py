import contextvars

context_var1 = contextvars.ContextVar("context_var1")
context_var1.set("val1")
context_var2 = contextvars.ContextVar("context_var2")
context_var2.set("val2")

"""
copy_context的返回值实现 collections.abc.Mapping,我们可以像操作字典一样操作它
内含了所有set的值
"""

context = contextvars.copy_context()
print(len(context))

for ctx, value in context.items():
    print(ctx.get(), ctx.name, value)
