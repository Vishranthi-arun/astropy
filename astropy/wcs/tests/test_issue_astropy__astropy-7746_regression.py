import numpy as np
import pytest
from astropy.wcs import WCS

def test_wcs_pix2world_empty_inputs():
    # Create a minimal 2‑D WCS
    w = WCS(naxis=2)
    w.wcs.crpix = [0.0, 0.0]
    w.wcs.cdelt = [1.0, 1.0]
    w.wcs.crval = [0.0, 0.0]
    w.wcs.ctype = ["RA---TAN", "DEC--TAN"]

    # Call with empty coordinate lists
    result = w.wcs_pix2world([], [], 0)

    # Expect a list of two empty numpy arrays
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], np.ndarray) and isinstance(result[1], np.ndarray)
    assert result[0].size == 0 and result[1].size == 0