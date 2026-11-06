def analyze(token: dict) -> dict:
    flags = []
    if not token.get("contract_verified", False):
        flags.append("Contract source is not marked verified by the supplied data.")
    if token.get("owner_can_mint", True):
        flags.append("Owner minting capability is reported.")
    if token.get("owner_can_pause", True):
        flags.append("Owner pause capability is reported.")
    if token.get("liquidity_locked", False) is not True:
        flags.append("Liquidity lock is not confirmed by the supplied data.")
    if token.get("holder_count", 0) < 100:
        flags.append("Low reported holder count; verify data source and context.")
    return {
        "flags": flags,
        "flag_count": len(flags),
        "assessment": "manual_review_required",
        "disclaimer": "Heuristic only; not an audit, scam detector, or investment advice."
    }

if __name__ == "__main__":
    sample = {"contract_verified": False, "owner_can_mint": True,
              "owner_can_pause": False, "liquidity_locked": False, "holder_count": 25}
    print(analyze(sample))
