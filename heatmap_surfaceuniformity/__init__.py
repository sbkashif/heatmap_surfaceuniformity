"""
heatmap_surfaceuniformity
Code to determine surface uniformity of a given structure. It would generate a heatmap on the relative z-coordinates for surface atoms.
"""

# Add imports here
from .HeatMapCode import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
