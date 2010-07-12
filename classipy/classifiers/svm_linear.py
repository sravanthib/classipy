#!/usr/bin/env python
# (C) Copyright 2010 Brandyn A. White
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""SVM Classifier
"""

__author__ = 'Brandyn A. White <bwhite@cs.umd.edu>'
__license__ = 'GPL V3'

import numpy as np

import liblinear.linear
import liblinear.linearutil

from base import BinaryClassifier


class SVMLinear(BinaryClassifier):
    def __init__(self, options=None):
        super(SVMLinear, self).__init__()
        try:
            self._param = ' '.join(['-%s %s' % x for x in options.items()])
        except AttributeError:
            self._param = ''
        self._param += ' -q'  # Makes silent
        self.to_type = list
        
    def train(self, labels, values):
        """Build a model.

        Args:
            labels: List of integer labels
            values: List of list-like objects, all with the same dimensionality.
        """
        values = self._convert_values(values)
        prob  = liblinear.linear.problem(labels, values)
        param = liblinear.linear.parameter(self._param)
        self._m = liblinear.linearutil.train(prob, param)

    def predict(self, value):
        """Evaluates a single value against the training data.

        NOTE: Confidence is currently set to 0!

        Args:
            value: List-like object with same dimensionality used for training.

        Returns:
            Sorted (descending) list of (confidence, label)
        """
        value = self._convert_value(value)
        labels, stats, confidence = liblinear.linearutil.predict([-1], [value], self._m)
        return [(0., labels[0])]

def main():
    print(__doc__)

if __name__ == '__main__':
    main()