# GVisor-Audit-2026 / ARCH-PROT-2025
## CSP Bypass & Origin Trial Research

This repository contains the proof of concept (PoC) for a logic bypass identified in the **DigitalCredentialsService** during the Google Chrome Origin Trial for `script-src-v2`.

### Findings
* **Target:** issuetracker.google.com
* **Vector:** Origin-Binding Failure via openid4vp.
* **Impact:** Unauthorized token reproduction in non-validated origins.

### Audit Environment
* **Device:** ZTE V30 (Mobile)
* **OS:** Android / Termux
* **Sandbox:** gVisor (Silent execution verified)

**Researcher:** Víctor Hugo Obando González (nek)
