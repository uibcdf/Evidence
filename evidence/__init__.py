"""
Evidence
This must be a short description of the project
"""
# versioningit
from ._version import __version__

__documentation_web__ = 'https://www.uibcdf.org/evidence'
__github_web__ = 'https://github.com/uibcdf/evidence'
__github_issues_web__ = __github_web__ + '/issues'


from .evidence import Evidence
from .reference import Reference
from .eco import ECO
from .main import is_evidence, compare, join
