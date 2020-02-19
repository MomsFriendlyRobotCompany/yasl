
try:
    from importlib_metadata import version # type: ignore
except ImportError:
    from importlib.metadata import version # type: ignore

from .spark import Spark

__version__ = version("yasl")
__license__ = 'MIT'
__author__ = 'Kevin Walchko'
# __doc__ = u"""
# Draw bar graphs from input data. By default, it draws a vertical bar
# chart, but you can also draw a horizontal bar chart if you want.
# """
