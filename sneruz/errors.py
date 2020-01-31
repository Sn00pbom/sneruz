

class Error(Exception):
    """Base class for exceptions in this module"""


class TruthAssignmentError(Error):
    """Exception raised when a deduction is attempted with no truth assignment"""
