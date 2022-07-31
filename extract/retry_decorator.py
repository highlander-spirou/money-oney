from functools import wraps

def retry_on_min_len(min_element):
    def outer(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            counter = 0
            results = f(*args, **kwargs)
            while counter < 5:
                if len(results) > min_element:
                    break
                else:
                    print(f'retry {counter + 1} times')
                    results = f(*args, **kwargs)
                    counter += 1
            return results
        return wrapper
    return outer

def retry_on_none(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        counter = 0
        try:
            results = f(*args, **kwargs)
            while counter < 5:
                if results is not None:
                    break
                else:
                    print(f'retry {counter + 1} times')
                    results = f(*args, **kwargs)
                    counter += 1
        except:
            print(f'retry {counter + 1} times')
            results = f(*args, **kwargs)
            counter += 1
        return results
    return wrapper