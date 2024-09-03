
def email_decorator(func):
    def wrapper():
        print("Dear interns, ")
        func()
        print("Best regards, ")
        print("your new boss")
    return wrapper

@email_decorator
def greeting_message():
    print("Welcome to your new job!")
    
greeting_message()

