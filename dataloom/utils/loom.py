def get_args(params: list) -> list | tuple:
    args = []
    for arg in params:
        if isinstance(arg, list):
            args += arg
        elif isinstance(arg, tuple):
            args += list(arg)
        else:
            args.append(arg)
    return args
