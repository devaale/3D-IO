from timeit import default_timer as timer
import functools


def timing(f):
    @functools.wraps(f)
    def wrap(*args, **kw):
        ts = timer()
        result = f(*args, **kw)
        te = timer()
        print(
            "Function: "
            + str(f.__name__)
            + ", Total time : %.1f ms" % (1000 * (te - ts))
        )
        return result

    return wrap
