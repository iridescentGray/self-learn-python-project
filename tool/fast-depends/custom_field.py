from fast_depends import inject
from fast_depends.library import CustomField


class Header(CustomField):
    def use(self, /, **kwargs: dict) -> dict:
        kwargs = super().use(**kwargs)
        kwargs[self.param_name] = kwargs["headers"][self.param_name]
        return kwargs


@inject
def my_func(header_field: int = Header()):
    return header_field


print(my_func(headers={"header_field": "1"}))
