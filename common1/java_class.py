import os.path
import time


class JavaClass(object):
    def __init__(self, class_name: str, class_path: str = None, class_code: str = None):
        self.class_name = class_name

        if class_path is not None and class_code is not None:
            raise Exception(f"Got both class path and code for java class {class_name}, choose one.")

        if class_path is not None:
            with open(class_path) as f:
                self.class_code = f.read()
        else:
            self.class_code = class_code

    def save_class(self, dir_path: str) -> None:
        if not os.path.isdir(dir_path):
            raise Exception(f"Invalid directory for saving the class - {dir_path}")

        # Write the class code in the directory
        with open(os.path.join(dir_path, f"{self.class_name}.java"), "w") as f:
            f.write(self.class_code)