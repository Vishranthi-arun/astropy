import numpy as np
from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

def test_nested_compound_separability():
    cm = m.Linear1D(10) & m.Linear1D(5)
    model = m.Pix2Sky_TAN() & cm
    result = separability_matrix(model)
    expected = np.array([[ True,  True, False, False],
                         [ True,  True, False, False],
                         [False, False,  True, False],
                         [False, False, False,  True]])
    assert np.array_equal(result, expected)
