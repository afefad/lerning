from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = dict()

def register(func: Callable) -> Callable:
    """Декоратор регистрирует функцию как плагин"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name: str) -> str:
    return 'Привет, {name}!'.format(name=name)

@register
def say_goodbye(name: str) -> str:
    return 'пока, {name}!'.format(name=name)

print(PLUGINS)
print(say_hello('tom'))