# adapters/metal_adapter.py
# Adapter for Metal Blockchain (Metal L1 / Avalanche Subnet)
# Implements OpenChain Profile Standard (OCPS v0.1.2)
import requests

OCPS_VERSION = "0.1.2"

def fetch_chain_metadata():
    return {
        "chain_name": "Metal Blockchain",
        "ocps_version": OCPS_VERSION,
        "rpc_url": "https://api.metalblockchain.org/ext/bc/C/rpc",
        "explorer_url": "https://explorer.metalblockchain.org",
        "consensus": "Snowman (Avalanche Subnet)",
        "network_type": "mainnet",
        "chain_id": "metal-mainnet",
        "native_token": "METAL"
    }

def fetch_governance_data():
    # If the repo's YAML contains more detailed fields, add them here.
    # Placeholder / safe defaults derived from the YAML structure.
    return {
        "validator_count": 45,
        "validators_sample": [],            # optional: list of validator dicts
        "avg_stake_weight": 2380000,
        "governance_type": "delegated PoS"
    }

def fetch_token_distribution():
    return {
        "token_supply": 23800000,
        "circulating_supply": 22000000,
        "top_holder_ratio": 0.21,
        "token_contract": None              # native token, not an ERC-style contract
    }

def fetch_additional_fields():
    # Add any extra YAML fields not covered above here.
    return {
        "website": "https://metalblockchain.org",
        "contact": None,
        "notes": "Converted from adapter.yaml to Python adapter."
    }

def transform_to_OCPS():
    meta = fetch_chain_metadata()
    gov = fetch_governance_data()
    tok = fetch_token_distribution()
    extra = fetch_additional_fields()

    profile = {
        "ocps_version": meta.get("ocps_version", OCPS_VERSION),
        "chain_name": meta.get("chain_name"),
        "chain_id": meta.get("chain_id"),
        "rpc_url": meta.get("rpc_url"),
        "explorer_url": meta.get("explorer_url"),
        "consensus": meta.get("consensus"),
        "network_type": meta.get("network_type"),
        "native_token": meta.get("native_token"),
        "validator_count": gov.get("validator_count"),
        "avg_stake_weight": gov.get("avg_stake_weight"),
        "governance_type": gov.get("governance_type"),
        "token_supply": tok.get("token_supply"),
        "circulating_supply": tok.get("circulating_supply"),
        "top_holder_ratio": tok.get("top_holder_ratio"),
        "token_contract": tok.get("token_contract"),
        "website": extra.get("website"),
        "notes": extra.get("notes")
    }
    return profile

if __name__ == "__main__":
    profile = transform_to_OCPS()
    import json
    print(json.dumps(profile, indent=2))
