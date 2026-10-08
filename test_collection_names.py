"""Checks the collection title guard used when uploading."""

from tools.utils.cli_menu import validate_title

for good in ["abc", "Caribbean Frontiers", "notes-2024.v1"]:
    validate_title(good)

for bad in ["t", "ab", " abc", "abc ", "a:b", "_abc", "a" * 513]:
    try:
        validate_title(bad)
    except ValueError:
        continue
    raise AssertionError(f"{bad!r} should be rejected")

print("All title checks passed")
