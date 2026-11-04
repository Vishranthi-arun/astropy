import pytest
from astropy.table import Table

def test_qdp_lowercase_command(tmp_path):
    qdp_file = tmp_path / "test.qdp"
    qdp_file.write_text("read serr 1 2\n1 0.5 1 0.5\n")
    tbl = Table.read(qdp_file, format="ascii.qdp")
    # Expect one row and four columns (value and error for two variables)
    assert len(tbl) == 1
    assert len(tbl.colnames) == 4
