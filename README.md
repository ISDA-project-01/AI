# VishalAI Parallel Intelligence Cluster (VAPIC)

VAPIC is a self-hosted, CPU-only **5-PC Parallel Multi-AI Consensus & Verification System** built for lightweight Windows 10/11 environments on a private LAN.

```text
                         INTERNET
                            |
                       TP-LINK ROUTER
                            |
        ------------------------------------------------
        |             |             |          |       |
       PC1           PC2           PC3        PC4     PC5
     MASTER        AI NODE       AI NODE     AI NODE  AI NODE
  (Gemma 2:2B)    (Qwen2.5)     (Gemma2)     (Llama) (DeepSeek)
        |
     Laptop (ADMIN)
        |
  Supervisor / Normal Phones
```

## Features
- **Equal Peer Architecture**: All AI nodes receive the exact user query concurrently.
- **Parallel Dispatch & Verification**: Master dispatches tasks, collects responses, evaluates consensus quality, and executes verification rounds.
- **Final Synthesis**: Gemma 2:2B synthesizes a single, unified response.
- **Multi-Modal Input**: Text, voice (Whisper), files, images, and web search aggregation.
- **Web Dashboards**: Normal User UI (`/`), Laptop Admin Console (`/admin`), and Mobile Supervisor Control (`/supervisor`).

## Quick Start
1. Run `PC1/setup.bat` on PC1 to launch the Master Gateway API.
2. Run `PC2/setup.bat` through `PC5/setup.bat` on respective peer PCs.
3. Access user interface at `http://<PC1_IP>:8000/`.
