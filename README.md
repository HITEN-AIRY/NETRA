# 🚀 NETRA — Next-Gen Reconnaissance Framework

NETRA is a **modular, scalable, and intelligence-driven reconnaissance framework** built in Python, designed to outperform traditional subdomain enumeration and recon tools by combining **passive intelligence, certificate transparency, active enumeration, and AI-assisted analysis** under a single orchestrated pipeline.

NETRA is built with a **phase-based architecture**, focusing on correctness, scalability, and extensibility — not quick hacks.

---

## 🧠 Core Philosophy

Most recon tools:

* mix discovery and validation
* run uncontrolled async tasks
* break at scale
* are hard to extend

**NETRA is different.**

NETRA strictly separates:

* **Discovery vs Validation**
* **Logic vs Execution**
* **Data vs Intelligence**

This makes NETRA **faster, safer, and future-ready**.

---

## 🏗️ High-Level Architecture

```
Discovery Engines
  ├── Passive Recon
  ├── Certificate Transparency
  ├── Active Enumeration
        ↓
Central Orchestrator
        ↓
Async Task Engine (Batch DNS)
        ↓
Correlation & Validation
        ↓
Intelligence Scoring
        ↓
Normalized Output & Recon Memory
```

---

## ⚙️ Key Features

* ✅ Centralized orchestration layer
* ✅ Async task engine with controlled concurrency
* ✅ Batch DNS resolution (high-performance)
* ✅ Passive + Active recon fusion
* ✅ Certificate Transparency parsing (Amass-style depth)
* ✅ AI-assisted scoring & wordlist expansion
* ✅ Wildcard DNS detection
* ✅ Schema-normalized output
* ✅ Phase-based extensibility

---

## 📦 Project Structure

```
netra/
├── core/
│   ├── orchestrator.py      # Central controller
│   ├── task_engine.py       # Async concurrency control
│   ├── correlator.py        # Deduplication & correlation
│   ├── validator.py         # Final validation layer
│
├── dns/
│   ├── resolver.py          # Batch DNS resolver
│   ├── wildcard.py          # Wildcard detection
│
├── passive/
│   └── search.py            # Passive recon sources
│
├── certs/
│   └── ct_parser.py         # Certificate transparency parsing
│
├── active/
│   └── enumerator.py        # Active enumeration engine
│
├── intelligence/
│   └── scorer.py            # AI-based scoring logic
│
├── output/
│   └── writer.py            # Normalized output writer
│
├── tests/
│   ├── test_dns_batch.py
│   └── test_full_pipeline.py
```

---

## 🔱 Development Phases

### 🔹 Phase 0 — Foundation (Completed)

**Goal:** Build a correct and extensible recon pipeline.

* DNS core & wildcard detection
* Passive recon engine
* Certificate Transparency parsing
* Active enumeration
* Correlation & deduplication
* Validation layer
* Normalized output
* Modular architecture

✔ Status: **Completed**

---

### 🔹 Phase 1 — Performance & Scalability (Completed)

**Goal:** Make NETRA fast and reliable at scale.

* Async Task Engine (controlled concurrency)
* Batch DNS resolution
* Separation of discovery & validation
* Performance metrics per phase
* Output schema standardization
* Code hygiene & polish

✔ Status: **Completed**

---

### 🔹 Phase 2 — HTTP Intelligence (Planned)

**Goal:** Identify *what is alive and interesting*.

Planned features:

* HTTP probing (200 / 301 / 403 / 500)
* Page titles
* Response headers
* Basic tech fingerprinting
* Async HTTP engine

🟡 Status: **Planned**

---

### 🔹 Phase 3 — Recon Memory & Persistence (Planned)

**Goal:** Make recon stateful and historical.

Planned features:

* Persistent recon storage
* Diffing between scans
* Change detection
* Recon history & trend analysis

🟡 Status: **Planned**

---

### 🔹 Phase 4 — Advanced Intelligence (Planned)

**Goal:** Smarter recon, not louder recon.

Planned features:

* ML-assisted prioritization
* Noise reduction
* Risk scoring
* Context-aware recon decisions

🟡 Status: **Planned**

---

## 🤖 AI in NETRA

AI in NETRA is **not gimmicky**.

It is used for:

* Scoring recon results
* Prioritizing meaningful subdomains
* Intelligent wordlist expansion
* Reducing noise

AI **never replaces logic** — it enhances it.

---

## 🧪 Testing

NETRA includes:

* Isolated batch DNS tests
* Full pipeline integration tests
* Safe test domains (`example.com`)

All phases are tested end-to-end before being considered complete.

---

## 🎯 Use Cases

* Bug bounty reconnaissance
* Red team asset discovery
* Security research
* Large-scale domain enumeration
* Recon automation research

---

## ⚠️ Disclaimer

NETRA is built for **ethical security research only**.
The author does not support or encourage illegal activity.

---

## 👤 Author

**Hiten Singh Airy**
Cybersecurity & Systems Engineering
Project NETRA — Long-term research & development

---

## 🛣️ Roadmap Snapshot

| Phase   | Status      |
| ------- | ----------- |
| Phase 0 | ✅ Completed |
| Phase 1 | ✅ Completed |
| Phase 2 | 🟡 Planned  |
| Phase 3 | 🟡 Planned  |
| Phase 4 | 🟡 Planned  |

---

## ⭐ Final Note

NETRA is not a one-off tool.
It is a **long-term, evolving reconnaissance framework** built with engineering discipline, not shortcuts.


