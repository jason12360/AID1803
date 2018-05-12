def add_path(path):
    def _add_path(fn):
        def __add_path(s):
            with open(path,'a') as file_obj:
                file_obj.write(fn(s))
        return __add_path
    return _add_path

@add_path('good.txt')
def print_help(s):
    return s.__doc__



print_help('def')
 