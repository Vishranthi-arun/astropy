import io
import pytest
from astropy.table import QTable
import astropy.units as u

def test_rst_writer_accepts_header_rows():
    tbl = QTable({'wave': [350, 950] * u.nm, 'response': [0.7, 1.2] * u.count})
    buf = io.StringIO()
    # Should not raise an exception
    tbl.write(buf, format='ascii.rst', header_rows=['name', 'unit'])
    output = buf.getvalue()
    # Basic sanity checks: column names are present in the output
    assert 'wave' in output
    assert 'response' in output