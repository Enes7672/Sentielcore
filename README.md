# Asynchronous Log Monitoring & Threat Mitigation Pipeline

An asynchronous, event-driven micro-SIEM (Security Information and Event Management) core built with Python. This system is engineered to handle high-throughput system logs with minimal resource overhead by leveraging non-blocking network programming, decentralized execution, and concurrent task delegation.

---

## 🧠 System Architecture & Workflow

Unlike tightly-coupled monolithic systems, this pipeline uses a decoupled **Producer-Consumer** design pattern built entirely on top of Python's `asyncio` event loop. 



The data lifecycle flows seamlessly through the following stages:

1. **Ingress Layer (`network.nexus`):** Starts an asynchronous TCP server. As log entries stream in from external sources, the server instantly pushes them into a thread-safe `asyncio.Queue`. This guarantees that network connections remain open and responsive, regardless of downstream processing times.
2. **Orchestration Layer (`core.anlik_izleme`):** Operates an efficiency-optimized asynchronous event loop that constantly monitors the queue. It remains idle until a log entry lands, immediately shifting the payload to the execution core.
3. **Analysis Engine (`core.analiz_etme`):** Scans the raw log string against pre-configured, high-risk operational keywords (`error`, `critical`, `failed`).
4. **Mitigation Layer (`core.core` & `yoneticiler.asenkron`):** If a threat status (`TEHLIKE`) is detected, an atomic mitigation sequence (`mudahale_et`) fires instantly. Concurrently, heavy disk I/O operations required for long-term audit reporting are offloaded via `asyncio.create_task`. This fire-and-forget mechanism ensures the main monitoring loop remains free to process incoming logs without blocking.

---

## 📁 Directory Topology

The project is modularly structured to enforce clean **Separation of Concerns (SoC)** across all layers:

```text
├── 📂 core/                  # Core Business Logic & Analysis Layer
│   ├── analiz_etme.py        # Tokenizes and filters streaming log payloads
│   ├── anlik_izleme.py       # Asynchronous queue listener and loop supervisor
│   ├── core.py               # Orchestrates detection-to-mitigation decision pathways
│   └── mudahale_et.py        # Synchronous immediate action handler for threat detection
├── 📂 network/               # Ingress & Network Protocol Layer
│   └── nexus.py              # Asynchronous TCP Server managing the internal asyncio.Queue
├── 📂 services/              # Shared Services
│   └── raporla.py            # Low-level I/O utility handles persistent disk storage
├── 📂 yoneticiler/           # System Administration & Task Scheduling
│   ├── asenkron.py           # Handles non-blocking background reporting execution
│   └── yonetici.py           # Application bootstrap and initialization supervisor
├── confing.py                # Central environment configuration management
├── main.py                   # Global application entrypoint
└── dockerfile                # Containerization & deployment manifest
🚀 Architectural Advantages
Non-Blocking Network Design: High-traffic environments will not cause packet drops or socket starvation since incoming socket buffering is decoupled from data processing via async queues.

Pluggable Analysis Engine: The evaluation layer (LogAnalyzer) is highly isolated. It can be upgraded to support regex pattern matching or machine-learning-driven threat models without touching the core network layer.

Container-Native Infrastructure: Seamlessly ships as a lightweight, independent microservice across modern container orchestration frameworks like Docker or Kubernetes.

🛠️ Deployment & Execution Guide
Prerequisites
Python 3.12+ (For native local runtime execution)

Docker (For isolated containerized environments)

Local Execution:
To spin up the monitor locally on your machine, run:

Bash
python main.py
Docker Containerization:
The repository includes an optimized dockerization manifest designed to bound resources and safeguard isolation during production runs.

Bash
# 1. Build the lightweight production Docker image
docker build -t log-monitor .

# 2. Deploy the container detached, mapping the internal TCP daemon port
docker run -d -p 12345:12345 --name active-monitor log-monitor
