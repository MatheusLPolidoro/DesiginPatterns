from abc import ABCMeta, abstractmethod

class IA(metaclass=ABCMeta):
    """Interface da classe A."""
    @staticmethod
    @abstractmethod
    def method_a():
        ...

class IB(metaclass=ABCMeta):
    """Interface da classe B."""
    @staticmethod
    @abstractmethod
    def method_b():
        ...

class A(IA):
    """Implementação da classe A."""
    def method_a(self):
        print("method A")

class B(IB):
    """Implementação da classe B."""
    def method_b(self):
        print("method B")

class ClassBAdapter(IA):
    """Classe que adapta a classe B para a interface A."""
    def __init__(self):
        self.class_b = B()

    def method_a(self):
        self.class_b.method_b()


def client():
    for item in A(), ClassBAdapter():
        item.method_a()

if __name__ == '__main__':
    client()
