"""
TODO:

Fn is a class decorator which takes a callable (`f`).
Fn has a `transform_callable` method, which transform `f` into a different callable,
with an additional Any parameter at the beginning, while preserving the remaining parts
of the function signature.

Note: you're only requried to add type annotations without implementing transform_callable.
"""


from typing import Callable, Concatenate, ParamSpec, TypeVar, Generic, Any

P = ParamSpec("P")
R = TypeVar("R", covariant=True)
VnCallable = TypeVar("VnCallable", bound=Callable)


class Fn(Generic[VnCallable]):
    def __init__(self, f: VnCallable) -> None:
        self.f = f

    def transform_callable(
        self: "Fn[Callable[P, R]]",
    ) -> Callable[Concatenate[Any, P], R]:
        ...


## End of your code ##
from typing import assert_type


@Fn
def example(a: int, b: str, c: float, *, d: bool = False) -> None:
    return


assert_type(example.f(1, "1", 1.0, d=False), None)

a: Any = 11111111
b = example.transform_callable()(a, 1, "1", 1.0, d=False)
assert_type(b, None)

example.transform_callable()(1, "1", 1.0, d=False)  # expect-type-error
