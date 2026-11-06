from risk import analyze

def test_flags_missing_verification_and_minting():
    result = analyze({"contract_verified": False, "owner_can_mint": True})
    assert result["flag_count"] >= 2
    assert result["assessment"] == "manual_review_required"
