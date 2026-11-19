import pytest

from supply.depcheck import (
    verify_checksum,
    pinned_version,
    lock_bypassed,
    source_allowed,
    verify_signature,
    resolve_version,
)


def test_checksum_match():
    import hashlib
    h = hashlib.sha256(b"abc").hexdigest()
    assert verify_checksum(b"abc", h) is True


def test_checksum_mismatch():
    assert verify_checksum(b"abc", "deadbeef") is False


def test_pinned_exact_version():
    assert pinned_version("pkg==1.2.3") is True


def test_range_version_not_pinned():
    assert pinned_version("pkg>=1.0,<2") is False


def test_lock_file_not_bypassed():
    assert lock_bypassed({"use_lock": True}) is False


def test_bypass_config_detected():
    assert lock_bypassed({"use_lock": False}) is True


def test_source_whitelist_match():
    assert source_allowed("https://pypi.org/pkg", ["pypi.org"]) is True


def test_source_off_whitelist():
    assert source_allowed("https://evil.com/pkg", ["pypi.org"]) is False


def test_signature_valid():
    assert verify_signature("pub", "sig-ok", b"abc") is True


def test_signature_invalid():
    assert verify_signature("pub", "sig-bad", b"abc") is False


def test_locked_version_used():
    assert resolve_version("pkg", {"pkg": "1.2.3"}) == "1.2.3"


def test_drift_version_rejected():
    import pytest
    with pytest.raises(ValueError):
        resolve_version("pkg>=1.0", {})


def test_empty_checksum_rejected():
    assert verify_checksum(b"abc", "") is False


def test_http_source_rejected():
    assert source_allowed("http://pypi.org/pkg", ["pypi.org"]) is False


def test_missing_lock_rejected():
    import pytest
    with pytest.raises(ValueError):
        resolve_version("pkg", {})
