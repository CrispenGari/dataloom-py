class PkNotDefinedException(Exception):
    pass


class InvalidArgumentsException(Exception):
    pass


class InvalidPropertyException(Exception):
    pass


class InvalidDropOperationException(Exception):
    pass


class InvalidConnectionURI(Exception):
    pass


class TooManyPkException(Exception):
    pass


class UnsupportedDialectException(ValueError):
    pass


class UnsupportedTypeException(ValueError):
    pass


class InvalidFiltersForTableColumnException(ValueError):
    pass


class InvalidColumnValuesException(ValueError):
    pass


class InvalidFilterValuesException(ValueError):
    pass


class UnknownColumnException(ValueError):
    pass


class InvalidOperatorException(ValueError):
    pass


class UnknownRelationException(Exception):
    pass
