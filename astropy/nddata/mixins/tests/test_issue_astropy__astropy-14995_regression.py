import numpy as np
import pytest
from astropy.nddata import NDDataRef

def test_mask_propagation_constant_and_nddataref():
    array = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    mask = np.array([[0, 1, 64], [8, 0, 1], [2, 1, 0]])
    nref_nomask = NDDataRef(array)
    nref_mask = NDDataRef(array, mask=mask)

    # Multiply by a constant (operand without mask)
    result_const = nref_mask.multiply(1., handle_mask=np.bitwise_or)
    assert isinstance(result_const, NDDataRef)
    assert np.array_equal(result_const.mask, mask)
    # Ensure a copy was made, not the original mask object
    assert not np.may_share_memory(result_const.mask, mask)

    # Multiply by another NDDataRef without mask
    result_nd = nref_mask.multiply(nref_nomask, handle_mask=np.bitwise_or)
    assert isinstance(result_nd, NDDataRef)
    assert np.array_equal(result_nd.mask, mask)
    assert not np.may_share_memory(result_nd.mask, mask)
