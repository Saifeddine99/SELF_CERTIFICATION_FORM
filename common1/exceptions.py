class RecognizedSiteException(Exception):
    def __init__(self, err_msg: str):
        super(Exception, self).__init__(err_msg)


class Redirect(RecognizedSiteException):
    def __init__(self, err_msg: str):
        super(Exception, self).__init__(err_msg)


class InvalidExerciseException(RecognizedSiteException):
    def __init__(self, err_msg: str):
        super(Exception, self).__init__(err_msg)


class InvalidChapterException(RecognizedSiteException):
    def __init__(self, err_msg: str):
        super(Exception, self).__init__(err_msg)


class JavaProgramException(Exception):
    def __init__(self, err_msg: str, err_info: str):
        super(Exception, self).__init__(err_msg)
        self.err_info = err_info