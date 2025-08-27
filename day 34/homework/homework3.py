#Boss level: Nested Functions: Define a function that contains another function inside it and calls the inner function.
def outer_function():
    def inner_function():
        print("Hello from inner function!")
    inner_function()

outer_function()