"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.
This injection module is the root and imports / instantiates all other task directory classes containing task objects.

"""

from .ESI.TaskDirectory import TaskDirectory as ESITaskDirectory


class TaskDirectory(object):
    """
    Root tasks directory for quickly finding other task directories

    This root task directory contains all directory containing tasks as attributes.
    """

    ESI: ESITaskDirectory = ESITaskDirectory()
