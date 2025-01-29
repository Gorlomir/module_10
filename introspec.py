import inspect

def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info['attributes'] = attributes

    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['methods'] = methods

    try:
        info['module'] = obj.__module__
    except AttributeError:
        info['module'] = None

    return info

if __name__ == "__main__":
    class Primer:
        def __init__(self, value):
            self.value = value

        def method(self):
            return self.value

    example_instance = Primer(42)
    print(introspection_info(example_instance))