"""
Unit and regression test for the evidence package.
"""

# Import package, test suite, and other packages as needed
import evidence
import pytest
import sys

def test_evidence_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "evidence" in sys.modules
