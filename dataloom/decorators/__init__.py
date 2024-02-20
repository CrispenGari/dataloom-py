from dataloom.exceptions import InvalidPropertyException
from dataloom.columns import (
    PrimaryKeyColumn,
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    ForeignKeyColumn,
)
import typing, dataloom  # noqa
import inspect


def initialize(
    to_dict: bool = False,
    init: bool = True,
    repr: bool = False,
    repr_identifier: str | None = None,
):
    """
    initialize
    ----------
    Constructor method for the initialize decorator.

    Parameters
    ----------
    to_dict : bool, optional
        If True, generates a to_dict method for the decorated class. Default is False.
    init : bool, optional
        If True, generates an __init__ method for the decorated class. Default is True.
    repr : bool, optional
        If True, generates a __repr__ method for the decorated class. Default is False.
    repr_identifier : str | None, optional
        The identifier to be used in the __repr__ method. Default is None.

    Returns
    -------
    Callable[[Any], type[wrapper]]
        A callable that takes a class and returns a wrapped version of it.

    Examples
    --------
    >>> from dataloom import (
    ...     Loom,
    ...     Model,
    ...     PrimaryKeyColumn,
    ...     Column,
    ...     CreatedAtColumn,
    ...     UpdatedAtColumn,
    ...     TableColumn,
    ...     ForeignKeyColumn,
    ...     Filter,
    ...     ColumnValue,
    ...     Include,
    ...     Order,
    ...     experimental_decorators,
    ... )
    ...
    ... @initialize(repr=True, to_dict=True, init=True, repr_identifier="id")
    ... class Profile(Model):
    ...     __tablename__: Optional[TableColumn] = TableColumn(name="profiles")
    ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
    ...     avatar = Column(type="text", nullable=False)
    ...     userId = ForeignKeyColumn(
    ...         User,
    ...         maps_to="1-1",
    ...         type="int",
    ...         required=True,
    ...         onDelete="CASCADE",
    ...         onUpdate="CASCADE",
    ...     )


    """

    def fn(cls):
        args = []
        for name, field in inspect.getmembers(cls):
            if isinstance(field, PrimaryKeyColumn):
                args.append(name)
            elif isinstance(field, Column):
                args.append(name)
            elif isinstance(field, CreatedAtColumn):
                args.append(name)
            elif isinstance(field, UpdatedAtColumn):
                args.append(name)
            elif isinstance(field, ForeignKeyColumn):
                args.append(name)

        class wrapper(cls):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

        init_code = ""

        if init:
            init_args = ", ".join([f"{p} = None" for p in args])
            init_code += f"def __init__(self, {init_args}) -> None:\n"
            for attr_name in args:
                init_code += f"    self.{attr_name} = {attr_name}\n"

        init_code += "\n"
        if to_dict:
            init_code += "@property\n"
            init_code += "def to_dict(self) -> dict:\n"
            init_code += "    return {\n"
            for key in args:
                init_code += f"         '{key}' : self.{key},\n"
            init_code += "    }\n\n"

        if repr_identifier is None:
            identifier = args[0]
        else:
            identifier = repr_identifier
            if repr_identifier not in args:
                raise InvalidPropertyException(
                    f"'{cls.__name__}' has no property '{repr_identifier}'."
                )

        if repr:
            init_code += "def __repr__(self) -> str:\n"
            init_code += (
                f"    return f'<{cls.__name__}:{identifier}={{self.{identifier}}}>'\n\n"
            )

        local_ns = {}
        # Execute the dynamically generated methods
        exec(init_code, globals(), local_ns)
        wrapper.__init__ = local_ns["__init__"]
        wrapper.__repr__ = local_ns.get("__repr__")
        wrapper.to_dict = local_ns.get("to_dict")
        wrapper.__name__ = cls.__name__
        return wrapper

    return fn


__all__ = [initialize]
