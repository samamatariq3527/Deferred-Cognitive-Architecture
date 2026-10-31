# Deferred Cognitive Architecture (DCA)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23839670.svg)](https://doi.org/10.5281/zenodo.23839670)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> **Author:** Samama Tariq  
> **Whitepaper PDF:** [Download Full Whitepaper](./dca_whitepaper.pdf)  
> **Official Citation DOI:** https://doi.org/10.5281/zenodo.23839670

---

## Abstract

Modern Large Language Models (LLMs) incur quadratic computational complexity $O(N^2)$ as context lengths scale, leading to severe energy costs, latency, and context degradation ("Lost in the Middle"). The Deferred Cognitive Architecture (DCA) replaces monolithic execution with a modular, three-tiered framework governed by a "Retrieve-First, Think-Second" protocol. By isolating mechanical I/O retrieval into low-power micro-pipelines and deferring heavy System-2 reasoning until pre-filtered data is delivered, DCA achieves sub-linear $O(k)$ computational complexity, 100% deterministic recall, and zero factual hallucinations caused by context clutter.

---

## Core System Architecture

1. **Tier 1: Mechanical I/O & Dynamic Routing Engine**
   - Deterministic point-to-point routing using ultra-lightweight models or exact key-matching.
   - Low compute overhead ($O(1)$ lookup time).

2. **Tier 2: Asynchronous Producer-Consumer Relays**
   - Non-blocking I/O queues decoupling retrieval latency from inference engines.
   - Decoupled out-of-band indexing allowing live, dynamic vector store updates without re-indexing context windows.

3. **Tier 3: Deferred Reasoning Engine (System-2)**
   - High-parameter LLM invocation triggered *only* after context payload is filtered and structured.
   - Reduces context overhead from $N$ total tokens to $k$ relevant tokens ($k \ll N$).

---
---

## 🧪 Reference Prototype

The `prototype/` directory contains a minimal Python reference implementation (`dca_core.py`) demonstrating the three-tier Deferred Cognitive Architecture:

* **Tier 1 (Mechanical Router):** $O(1)$ deterministic filtering to extract relevant $k$-tokens.
* **Tier 2 (Async Relays):** Non-blocking background queue ingestion.
* **Tier 3 (Deferred Reasoning):** System-2 model invocation strictly on clean, pre-filtered payloads ($k \ll N$).

### Running the Prototype Locally

1. Clone your repository or navigate into your local folder:
   ```bash
   git clone https://github.com/samamatariq3527/Deferred-Cognitive-Architecture.git
   cd Deferred-Cognitive-Architecture


## Citation

If you use or reference DCA in your research or system design, please cite:

```bibtex
@publication{tariq_samama_2026_dca,
  author       = {Samama Tariq},
  title        = {Deferred Cognitive Architecture (DCA): Resolving Context Degradation \& Compute Bottlenecks in Large Language Models},
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.23839670},
  url          = {[https://doi.org/10.5281/zenodo.23839670](https://doi.org/10.5281/zenodo.23839670)}
}
