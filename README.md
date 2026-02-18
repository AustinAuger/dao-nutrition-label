# DAO Nutrition Label

![DAO Nutrition Label Hero](visuals/dao-nutrition-label-hero.png)

**The food nutrition label for DAOs — transparency in 30 seconds.**

![GitHub stars](https://img.shields.io/github/stars/AustinAuger/dao-nutrition-label?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/AustinAuger/dao-nutrition-label?style=for-the-badge)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![v0.2 Coming Soon](https://img.shields.io/badge/Next%20Milestone-v0.2-orange?style=for-the-badge)

**See a real label here → [Live IPFS Example](https://dweb.link/ipfs/bafybeifjpj2lqibtgmwv7u7e5lonzbriz2zq4wiyuyp267lelnbzohpvwm)**

---

An open-source, community-driven transparency profile standard for measuring decentralization for DAOs and Metal Blockchain ecosystem projects.

Built on the **OpenChain Profile Standard (OCPS v0.1.2)** with visual “nutrition label” summaries, IPFS pinning, and on-chain attestations.

---

## Features
- ✅ YAML + JSON + PDF profile formats  
- ✅ IPFS pinned transparency certificates  
- ✅ On-chain attestation on XPR Network  
- ✅ zk-DID extension for privacy-preserving compliance  
- ✅ Aligned with EIP-4824 for cross-chain discoverability  

---

## Standards Alignment
The DAO Nutrition Label focuses on **what** decentralization metrics matter.  
It builds on [EIP-4824](https://eips.ethereum.org/EIPS/eip-4824) (`dao://` URI scheme) and adds the missing visual + certification layer.

---

## How It Works (10-minute contribution)
1. Copy [`profiles/sample_dao.yaml`](./profiles/sample_dao.yaml)  
2. Rename it to your DAO name (e.g. `my-dao.yaml`)  
3. Fill in your details  
4. Open a Pull Request to the [`profiles/`](./profiles/) folder  

Every profile helps the entire Metal Blockchain community!

---

## DAO Profile Template

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
Extensions
dao-nutrition-label-zkdid-extension (v0.1)
Zero-knowledge DID verification for age/sanctions compliance while staying privacy-first.
→ extensions/dao-nutrition-label-zkdid-extension-v0.1.yaml
```
## Examples
**DAO with zk-DID access control**  
→ [`examples/dao-with-zkdid.yaml`](./examples/dao-with-zkdid.yaml)

---

## IPFS & On-Chain Transparency
- Sample Profile IPFS CID: `bafkreicsmi3psin7klvrsarl36b3zoxlv2722ru3yhqzne2tmhc6fqss3u`  
- Live Visual Label: [View on IPFS](https://dweb.link/ipfs/bafybeifjpj2lqibtgmwv7u7e5lonzbriz2zq4wiyuyp267lelnbzohpvwm)  
- On-chain Attestation (XPR Network): [Explorer Link](https://explorer.xprnetwork.org/transaction/2d6b62ded2f59965a2ad911972291f60e453275dcab58c954f1f657ed1fda349)  
  Attestor: austinauger

---

## Visuals
![DAO Nutrition Label](visuals/dao-nutrition-label-hero.png)  
[📁 Open visuals folder](./visuals/)

---

## Docs
- [Vision](docs/vision_doc.md)  
- [Public Explainer](docs/public_explainer.md)  
- [v0.2 Roadmap](docs/v0.2_roadmap.md)

---

## Next Milestone – v0.2
- Automated GitHub Actions for IPFS pinning & attestation  
- Expanded contributor tooling  
- Community education assets  
- Full standardization of the visual label

---

## Contributing
Pull requests and issues are welcome!  
**Best way to start:** Submit your DAO profile using the 10-minute guide above.  

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for details.

---

## License
This project is licensed under [Creative Commons Attribution 4.0 International](./LICENSE).

---

**🚀 Ready to make your DAO transparent?**  
**Submit your DAO profile in 10 minutes →** [`profiles/`](./profiles/)

Every profile counts. Let’s build trust together on Metal Blockchain& Beyond!🤘
