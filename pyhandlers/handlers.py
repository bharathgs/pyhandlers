import warnings
from functools import wraps

__all__ = ["error_handler", "deprecation_warnings_handler"]


def error_handler(errors=(Exception, ), default=""):
    """
    generic error handler decorator.
    decorate the functions where you 
    expect some kind of error and 
    when encountered do some sort of 
    error handling with it.

    parameters: 
    ----------

    errors: tuple
        errors that you expect to catch.

    default: str, function, class
        when you catch an error, define how to handle it
        you can pass a string, or some function or 
        class to handle the error

    returns: 
    -------

    decorated function
    """
    def funcator(func):
        @wraps(func)
        def deep_inside(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors as e:
                print("error: ", repr(e))
                return default(*args, **kwargs) if hasattr(default, '__call__') else default
        return deep_inside
    return funcator


def deprecation_warnings_handler(function):
    '''This is a decorator which can be used to ignore deprecation warnings occurring in a function.'''
    def new_function(*args, **kwargs):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            return function(*args, **kwargs)
    new_function.__name__ = function.__name__
    new_function.__doc__ = function.__doc__
    new_function.__dict__.update(function.__dict__)
    return new_function
