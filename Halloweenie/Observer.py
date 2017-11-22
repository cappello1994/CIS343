from abc import ABCMeta, abstractmethod

"""Abstract class for implementing the Observer Pattern."""
class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass
