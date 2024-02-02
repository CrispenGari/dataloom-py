class PkNotDefinedException(Exception):
    pass


class TooManyPkException(Exception):
    pass


class UnsupportedDialectException(ValueError):
    pass


class UnsupportedTypeException(ValueError):
    pass
