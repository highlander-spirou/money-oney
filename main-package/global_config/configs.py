import os
class GlobalConfigObject:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_current_dir():
        current_dir = os.getcwd()
        return current_dir

    def _add_config(self, key, value):
        self.key = value

g = GlobalConfigObject()
    