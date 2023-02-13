from abc import ABCMeta, abstractmethod


class IBuilder(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def build_part_a():
        return

    @staticmethod
    @abstractmethod
    def build_part_b():
        return

    @staticmethod
    @abstractmethod
    def build_part_c():
        return

    @staticmethod
    @abstractmethod
    def get_result():
        return
