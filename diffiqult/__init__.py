"""
=================================================================
TODO
  DiffiQult: an autodifferentiable electronic structure package
==================================================================
Description:
Rationale:
How to cite DiffiQulT::

"""

import os
__install_path__ = os.path.realpath(__file__)

import numpy
# ignore warnings "ComplexWarning: Casting complex values to real discards the imaginary part"
import warnings
warnings.simplefilter("ignore", numpy.ComplexWarning)


from numpy.testing import Tester
test = Tester().test

from diffiqult.Task import Tasks
from diffiqult.Molecule import System_mol
