from dataloom.utils import is_collection


def get_args(params: list) -> list | tuple:
    args = []
    for arg in params:
        if is_collection(arg):
            args += list(arg)
        else:
            args.append(arg)
    return args
