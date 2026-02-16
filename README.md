<p align="center">
  <a href="./README.md">
    <img src="https://img.shields.io/badge/version-v0.1.2-blue" alt="Version">
  </a>
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/license-CC--BY%204.0-green" alt="License">
  </a>
  <a href="#ipfs-transparency">
    <img src="https://img.shields.io/badge/IPFS-pinned-blue" alt="IPFS">
  </a>
  <a href="#next-milestone">
    <img src="https://img.shields.io/badge/status-active-brightgreen" alt="Status">
  </a>
  <a href="#features">
    <img src="https://img.shields.io/badge/built%20with-community%20governance-blue" alt="Built With">
  </a>
</p>
<p align="center">
  <a href="./CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/Contribute-Guide-brightgreen" alt="Contribute Guide">
  </a>
</p>

# An open-source, community-driven transparency profile standard for measuring decentralization for DAOs and Metal Blockchain ecosystem projects.

---

# 🚀 START CONTRIBUTING YOUR DAO PROFILE! 🚀

💡 **All DAO profiles live here:** [`profiles/`](./profiles/)  
📄 **Copy the sample file, fill in your details, and submit your contribution.**  
🙏 Every profile helps build transparency for the Metal Blockchain community!

---

## Table of Contents

- [Features](#features)
- [Standards Alignment](#standards-alignment)
- [Contributing](#contributing)
- [DAO Profile Template](#dao-profile-template)
- [License](#license)
- [Docs](#docs)
- [IPFS Transparency](#ipfs-transparency)
- [On-Chain Attestation](#on-chain-attestation)
- [Visuals](#visuals)
  - [DAO Nutrition Label](#dao-nutrition-label)
- [Next Milestone](#next-milestone)

---

## Features
- ✅ YAML, JSON, PDF profile structures  
- ✅ IPFS pinned transparency certificates  
- ✅ On-chain attestation foundation  
- ✅ Supports upcoming regulatory clarity

---

## Standards Alignment
The DAO Nutrition Label aligns with broader DAO transparency initiatives like [EIP-4824](https://eips.ethereum.org/EIPS/eip-4824), which defines a `dao://` URI scheme for discovering DAO metadata. While EIP-4824 focuses on *where* DAO metadata lives, The DAO Nutrition Label focuses on *what* decentralization metrics are, and how they are transparently measured and certified for DAOs.

Future versions of The DAO Nutrition Label will explore JSON-LD export for cross-chain `dao://` discoverability, enabling aligned, chain-agnostic DAO transparency while building community-driven certification tooling in the Metal Blockchain ecosystem.

## The DAO Nutrition Label Extensions

This repository also defines optional DAO Nutrition Label extensions that may be
referenced by DAO profiles or blockchain governance frameworks.

### Available Extensions

- **dao-nutrition-label-zkdid-extension (v0.1)**  
  Enables zero-knowledge verification of decentralized identity (DID)
  claims for privacy-preserving, compliance-ready smart contract access
  and regulated finance use cases.

  ### Examples

- **DAO with zk-DID access control**  
  Demonstrates how a DAO can use the DAO Nutrition Label zk-DID
  extension to enforce age and sanctions compliance using
  zero-knowledge proofs.  
  → `examples/dao-with-zkdid.yaml`

---

## Contributing
Pull requests and issues are welcome to improve metrics and tooling.

---

## DAO Profile Template

All contributed DAO profiles live in the [`profiles/`](./profiles/) folder. To contribute:

1. Copy the [`sample_dao.yaml`](./profiles/sample_dao.yaml) file  
2. Rename it to your DAO’s name (e.g., `mydao.yaml`)  
3. Fill in your DAO’s details, governance model, and transparency info  
4. Commit your file via pull request

**Sample DAO profile content:**

```yaml
dao_name: ExampleDAO
chain: Metal Blockchain (XPR Network)
version: v0.1.2
created: 2025-09-08
contributors:
  - name: Austin Auger
    role: Maintainer
governance:
  model: Token-weighted voting
  token: EXM
  supply: 1,000,000
  quorum: 15%
  voting_period: 7 days
transparency:
  ipfs_cid: bafkreicsmi3psin7klvrsarl36b3zoxlv2722ru3yhqzne2tmhc6fqss3u
  attestation_tx: 2d6b62ded2f59965a2ad911972291f60e453275dcab58c954f1f657ed1fda349
  attestor: austinauger
notes: >
  This is a sample DAO profile submission for contributors to copy and adapt.
```

---

## License

<p align="center">
  <a href="./LICENSE">
    <img src="https://img.shields.io/github/license/AustinAuger/metal-blockchain-ocps-v0.1.2?color=blue&label=License" alt="License Badge">
  </a>
</p>

This repository is licensed under the terms described in the [LICENSE file](./LICENSE).
---

## 📚 Docs  
- [Vision](docs/vision_doc.md)  
- [Public Explainer](docs/public_explainer.md)  
- [Roadmap](docs/v0.2_roadmap.md)  

💡 **All DAO profiles live here:** [profiles/](./profiles/)  
---

[## IPFS Transparency
We pin DAO Nutrition Label profiles to IPFS for verifiable decentralization snapshots:  
- **Current CID:** `bafkreicsmi3psin7klvrsarl36b3zoxlv2722ru3yhqzne2tmhc6fqss3u`  
- **View on IPFS Gateway:**  
  - [dweb.link](https://dweb.link/ipfs/bafybeifjpj2lqibtgmwv7u7e5lonzbriz2zq4wiyuyp267lelnbzohpvwm)  
  - [ipfs.io](https://ipfs.io/ipfs/bafybeifjpj2lqibtgmwv7u7e5lonzbriz2zq4wiyuyp267lelnbzohpvwm)](https://bafybeifjpj2lqibtgmwv7u7e5lonzbriz2zq4wiyuyp267lelnbzohpvwm.ipfs.dweb.link/)

---

## On-Chain Attestation

<p align="center">
  <img src="https://img.shields.io/badge/Attestor-austinauger-blue" alt="Attestor">
  <img src="https://img.shields.io/badge/CID-bafkreicsmi3psin7klvrsarl36b3zoxlv2722ru3yhqzne2tmhc6fqss3u-lightgrey" alt="IPFS CID">
  <a href="https://explorer.xprnetwork.org/transaction/2d6b62ded2f59965a2ad911972291f60e453275dcab58c954f1f657ed1fda349">
    <img src="https://img.shields.io/badge/View-On%20Chain-green" alt="View On-Chain">
  </a>
</p>

**Details:**  
- **Attestor:** austinauger  
- **On-chain memo:** `OCPS v0.1.2 CID: bafkreicsmi3psin7klvrsarl36b3zoxlv2722ru3yhqzne2tmhc6fqss3u`  
- ✅ **View on XPRNetwork Explorer:** [Click here](https://explorer.xprnetwork.org/transaction/2d6b62ded2f59965a2ad911972291f60e453275dcab58c954f1f657ed1fda349)  
- **IPFS CID:** [`bafkreicsmi3psin7klvrsarl36b3zoxlv2722ru3yhqzne2tmhc6fqss3u`](https://dweb.link/ipfs/bafkreicsmi3psin7klvrsarl36b3zoxlv2722ru3yhqzne2tmhc6fqss3u)
---

## Visuals

### DAO Nutrition Label
<p align="center">
  <img src="visuals/metal-blockchain-ocps-v0.1.2_Nutrition_Label_1.JPG" width="300">
  <img src="visuals/Sample_DAO_Label.png" alt="DAO Nutrition Label" width="300">
  <img src="visuals/DAO_SAMPLE_2.jpeg" alt="DAO Nutrition Label 2" width="300">
  <img src="visuals/metal-blockchain-ocps-v0.1.2_Nutrition_Label_7.JPG" width="300">
</p>

---

## Next Milestone
We are preparing for **DAO Nutrition Label v0.2** to include:  
- DAO Nutrition Label standardization  
- GitHub Actions for automated IPFS pinning and attestation log updates  
- Contributor workflow for submitting DAO transparency profiles  
- Expanded documentation for on-chain attestation tutorials  
- Community education assets for X, GitHub, and DAO forums  

Ready to certify transparency together! 

---

## Extensions

- **DAO Nutrition Label zk-DID Extension (v0.1)**  
  Enables zero-knowledge verification of decentralized identity (DID) claims
  for privacy-preserving compliance and smart contract access control.  
  File: `extensions/dao-nutrition-label-zkdid-extension-v0.1.yaml`

---

## Examples

- **DAO with zk-DID access control**  
  Demonstrates how a DAO can use the DAO Nutrition Label zk-DID extension
  to enforce age and sanctions compliance using zero-knowledge proofs.  
  File: `examples/dao-with-zkdid.yaml`

---

## Extensions

- **DAO Nutrition Label zk-DID Extension (v0.1)**  
  Enables zero-knowledge verification of decentralized identity (DID) claims
  for privacy-preserving compliance and smart contract access control.  
  File: `extensions/dao-nutrition-label-zkdid-extension-v0.1.yaml`

---

## Examples

- **DAO with zk-DID access control**  
  Demonstrates how a DAO can use the DAO Nutrition Label zk-DID extension
  to enforce age and sanctions compliance using zero-knowledge proofs.  
  File: `examples/dao-with-zkdid.yaml`

---

## DAO Nutrition Label Flow

```text
DAO Nutrition Label Core
           │
           ▼
DAO Nutrition Label zk-DID Extension (v0.1)
           │
           ▼
Example Regulated DAO Profile
(`examples/dao-with-zkdid.yaml`)

---

## License

This project is licensed under the terms described in the [LICENSE](./LICENSE) file.

---

## Contributing (optional)

If you want to contribute, please open a pull request or submit an issue
with a clear description. Contributions should follow the DAO Nutrition Label
format and maintain proper YAML and Markdown standards.

---

## Documentation (optional)

Additional documentation and specifications are available in the
`docs/` folder or via GitHub Pages if enabled.



