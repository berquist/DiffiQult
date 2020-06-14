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
# ignore warnings "ComplexWarning: Casting complex values to real discards the imaginary part"
import warnings

import numpy
from numpy.testing import Tester

from diffiqult.Molecule import System_mol
from diffiqult.Task import Tasks

__install_path__ = os.path.realpath(__file__)

warnings.simplefilter("ignore", numpy.ComplexWarning)


test = Tester().test
