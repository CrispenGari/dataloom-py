class PkNotDefinedException(Exception):
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


class UnknownColumnException(ValueError):
    pass


class InvalidOperatorException(ValueError):
    pass
