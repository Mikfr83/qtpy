# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtScxml classes and functions."""

from . import (
    PYQT5,
    PYQT6,
    PYSIDE2,
    PYSIDE6,
    QtBindingsNotFoundError,
    QtBindingMissingModuleError,
)

if PYQT5:
    raise QtBindingMissingModuleError(name='QtScxml')
elif PYQT6:
    raise QtBindingMissingModuleError(name='QtScxml')
elif PYSIDE2:
    from PySide2.QtScxml import *
elif PYSIDE6:
    from PySide6.QtScxml import *
else:
    raise QtBindingsNotFoundError()