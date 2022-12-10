class MetaInterface(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(instance)

    def __subclasscheck__(cls, subclass) -> bool:
        method_list = [method for method in dir(cls) if method.startswith('__') is False]
        is_subclass = True
        for method in method_list:
            is_subclass = hasattr(subclass, method) and callable(getattr(subclass, method))
            if not is_subclass:
                break
        return is_subclass


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Meta:
    interface = MetaInterface
    singleton = MetaSingleton
