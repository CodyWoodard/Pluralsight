from functools import wraps


def email_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # args = ("desk",)
        # kwargs = {}
        print("Dear interns, ")
        func(*args, **kwargs)
        # func("desk")
        print("Best regards, ")
        print("your new boss")
    return wrapper

@email_decorator
def greeting_message(x):
    """ Welcome to Keep message

    Args:
        x (any): desk
    """
    print(f"Welcome to your new {x}")
    
greeting_message("desk")
print(greeting_message.__name__)
print(greeting_message.__doc__)
