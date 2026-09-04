# JULES MASTER PROMPT — 5-PC PARALLEL MULTI-AI CLUSTER

Build a complete, working, self-hosted **5-PC Parallel Multi-AI Cluster** for a private LAN.

Do NOT give me only an explanation, architecture, pseudocode, or partial examples.

I want you to **create the complete project files and implementation** so that I can place the project on the five Windows PCs and follow the included setup guide.

The project must be designed for:

- 5 Windows 10 PCs
- 8 GB RAM per PC
- No GPU
- CPU-only AI inference
- 1 Windows 11 laptop with 8 GB RAM
- 1 TP-Link Wi-Fi router
- Router Ethernet connected to the 5 PCs
- Router also used by the laptop and 2 phones
- Private LAN
- Internet available through the router
- No dependency on the CS lab Ethernet network
- No Docker requirement
- No Linux requirement
- No Node.js requirement
- Python-based orchestration
- Lightweight enough for 8 GB RAM machines
- CLI-first AI nodes
- Web interfaces only where required
- The laptop is the administrator/manager/DNS/API management machine
- Phone 1 is the remote supervisor/operator
- Phone 2 is the normal/ideal user

IMPORTANT:

This is NOT a conventional distributed task system where each PC receives a different specialty.

Every AI node must receive the **same user task** independently.

The system is a:

**PARALLEL MULTI-MODEL CONSENSUS / VERIFICATION SYSTEM**

All AI models are peers.

No model should be permanently considered superior to another.

---

# 1. REQUIRED ARCHITECTURE

Create this architecture:

```text
                         INTERNET
                            |
                       TP-LINK ROUTER
                            |
        ------------------------------------------------
        |             |             |          |       |
       PC1           PC2           PC3        PC4     PC5
     MASTER        AI NODE       AI NODE     AI NODE  AI NODE
        |
        |
     Laptop
   ADMIN/MANAGER
        |
   Supervisor Phone
        |
      User Phone
```

The five PCs are connected to the same private TP-Link LAN.

The laptop is the administration and management system.

PC1 is the MASTER.

PC1 must coordinate PC2-PC5.

The laptop must NOT perform heavy AI processing.

The laptop is primarily:

- Administrator
- Manager
- Monitoring dashboard
- Configuration manager
- DNS manager
- Supervisor control interface
- Cluster health viewer
- Log viewer
- System performance viewer

---

# 2. PC ROLES

## PC1 — MASTER

PC1 must run:

- Gemma 2:2B
- OpenAI Whisper Base
- Master coordinator
- Parallel request dispatcher
- Result collector
- Consensus engine
- Verification loop
- Quality evaluator
- Final answer synthesizer
- File processing coordinator
- API gateway
- User request manager
- Job manager
- Cluster health monitor
- Logging
- Supervisor command receiver

PC1 produces the final user-facing answer.

Gemma 2:2B should be used for final synthesis, but it must NOT blindly decide that its own answer is correct.

---

## PC2

Run:

- Qwen2.5-Coder-3B-Instruct

OR, if hardware/resource testing shows it is more appropriate:

- Qwen2.5-7B-Instruct

The system must provide a configurable model selection setting.

---

## PC3

Run:

- Gemma-2-2B-IT

OR another verified lightweight Gemma model that is actually available and compatible with the selected runtime.

Do NOT assume a model tag exists.

Verify the exact model name before writing configuration.

---

## PC4

Run:

- Llama-3.2-3B-Instruct

OR:

- Llama-3.1-Minitron-4B

Again, verify the exact downloadable/runtime-compatible model before using it.

---

## PC5

Run:

- DeepSeek-R1-Distill-Qwen-1.5B

OR, only if hardware testing proves practical:

- DeepSeek-R1-Distill-Llama-8B

Do not force an 8B model onto an 8 GB RAM CPU-only machine if it causes instability.

---

# 3. EQUAL PEER PRINCIPLE

This is extremely important.

DO NOT implement:

```text
PC2 = reasoning worker
PC3 = general worker
PC4 = analysis worker
PC5 = deep-context worker
```

Instead implement:

```text
PC2 = Peer AI
PC3 = Peer AI
PC4 = Peer AI
PC5 = Peer AI
```

Every peer receives the same task.

Example:

```text
USER:
Explain quantum computing.

MASTER
 |
 +----> PC2
 |
 +----> PC3
 |
 +----> PC4
 |
 +----> PC5

All receive the same original task.
```

Each independently produces an answer.

The master compares them.

---

# 4. PARALLEL EXECUTION

The master must dispatch requests to all available AI nodes as concurrently as possible.

Do not process:

```text
PC2 → wait
PC3 → wait
PC4 → wait
PC5 → wait
```

Instead:

```text
PC2 ────────┐
PC3 ────────┤
PC4 ────────┼──> MASTER
PC5 ────────┘
```

Use asynchronous/concurrent Python networking where appropriate.

The master must track:

- Request ID
- Node ID
- Start time
- End time
- Latency
- Status
- Response
- Error
- Timeout
- Retry count
- Model name
- Model version
- Node health

---

# 5. VERIFICATION LOOP

The system must not blindly accept the first response.

Implement configurable iterative verification.

Example:

```text
USER REQUEST
     |
     v
MASTER
     |
     +------ PC2
     +------ PC3
     +------ PC4
     +------ PC5
     |
     v
COLLECT RESPONSES
     |
     v
COMPARE RESPONSES
     |
     +---- Agreement
     |
     +---- Contradiction
     |
     +---- Missing information
     |
     +---- Unsupported claims
     |
     v
QUALITY EVALUATION
     |
     +---- PASS ----> FINAL SYNTHESIS
     |
     +---- FAIL
              |
              v
       SECOND ROUND
              |
              v
       SAME TASK AGAIN
              |
              v
       RE-EVALUATE
```

Maximum rounds must be configurable.

For example:

```text
MAX_ROUNDS = 3
```

Do not create an infinite loop.

The system must stop when:

- Quality threshold is achieved
- Maximum rounds reached
- Supervisor stops the job
- User cancels
- Critical node failure occurs
- Resource limits are exceeded

---

# 6. CONSENSUS ENGINE

Create a consensus/verification layer.

It should compare:

- factual agreement
- contradictions
- completeness
- relevance
- instruction compliance
- answer consistency
- evidence where available
- code validity where applicable
- formatting requirements

Do NOT claim mathematical "100% accuracy."

Instead use a configurable quality score.

Example:

```text
quality_score = 0–100
```

Configuration:

```text
MIN_QUALITY_SCORE = 85
MAX_ROUNDS = 3
MIN_RESPONSES = 3
```

These must be configurable.

---

# 7. FINAL SYNTHESIS

After verification:

```text
PC2 response
PC3 response
PC4 response
PC5 response
        |
        v
MASTER
        |
        v
Gemma 2:2B
        |
        v
ONE FINAL RESPONSE
```

Gemma 2:2B must synthesize the verified information.

It must:

- remove duplicates
- resolve conflicts
- preserve correct information
- follow the original user's requirements
- produce one clean response
- never expose internal node details unless requested
- never invent agreement where disagreement exists

If the peer models disagree materially and verification cannot resolve the disagreement, the final response must clearly indicate uncertainty rather than fabricate certainty.

---

# 8. MODEL RUNTIME

Use a lightweight local model runtime appropriate for Windows CPU inference.

Prefer Ollama if it provides the simplest reliable deployment for the selected models.

Do not hard-code assumptions about model availability.

The setup must:

1. Detect whether the runtime is installed.
2. Install/provide instructions if missing.
3. Check CPU/RAM.
4. Check whether the requested model exists.
5. Pull the configured model if permitted.
6. Test inference.
7. Register the node with PC1.
8. Report health to PC1.

Do not automatically download huge models without a configuration/confirmation mechanism.

---

# 9. API ARCHITECTURE

I do NOT want users to manually deal with internal ports.

The application should expose clean hostnames through the private DNS configuration.

For example:

```text
master.<PRIVATE_DOMAIN>
pc1.<PRIVATE_DOMAIN>
pc2.<PRIVATE_DOMAIN>
pc3.<PRIVATE_DOMAIN>
pc4.<PRIVATE_DOMAIN>
pc5.<PRIVATE_DOMAIN>
api.<PRIVATE_DOMAIN>
admin.<PRIVATE_DOMAIN>
supervisor.<PRIVATE_DOMAIN>
```

Use a placeholder variable:

```text
PRIVATE_DOMAIN=your-private-domain
```

Do not assume `.vb` is a globally registered/public DNS TLD.

Support `.vb` as a configurable private/internal DNS namespace if desired, but document the difference between:

- private DNS name
- publicly registered domain
- public HTTPS certificate
- local TLS certificate

The system should make hostname configuration easy.

---

# 10. HTTPS

Provide HTTPS support for the LAN services.

Do not claim that changing DNS automatically creates HTTPS.

Implement/document a proper TLS/reverse-proxy architecture.

The normal user should access:

```text
https://api.<PRIVATE_DOMAIN>
```

The supervisor should access:

```text
https://supervisor.<PRIVATE_DOMAIN>
```

The administrator should access:

```text
https://admin.<PRIVATE_DOMAIN>
```

Internal AI APIs should remain inaccessible directly from the normal user unless explicitly enabled.

---

# 11. PORT ABSTRACTION

I do not want the user interface or API client to require:

```text
http://192.168.x.x:11434
```

Instead the application should use configured hostnames.

Internally, the node service may communicate with the model runtime on its local port.

Use configuration variables for all internal addresses.

The port number must never be hard-coded throughout the application.

Create a central configuration system.

---

# 12. LAPTOP ADMINISTRATOR

The Windows 11 8 GB laptop must run lightweight management functions only.

It should provide:

### Administration

- node discovery
- node registration
- node status
- CPU usage
- RAM usage
- disk usage
- uptime
- model information
- runtime information
- network latency
- current job
- queue
- logs
- errors
- restart request
- stop request
- configuration
- security settings

The laptop should NOT become a bottleneck for AI inference.

---

# 13. SUPERVISOR PHONE

Create a mobile-friendly `supervisor.html`.

The supervisor must be able to:

- authenticate
- view cluster status
- view all five PCs
- view individual AI responses
- view final answer
- view current round
- view quality score
- view contradictions
- view logs
- pause job
- resume job
- cancel job
- retry job
- send instructions to master
- request another verification round
- enable/disable individual nodes
- change model configuration
- change maximum rounds
- change quality threshold
- see system performance

All privileged actions must require authentication and authorization.

Do not expose administrative controls to the normal user.

---

# 14. NORMAL USER PHONE

Create a mobile-friendly `index.html`.

The normal user interface should support:

### Input

- text
- voice
- file upload
- image upload

### Output

- text
- generated code
- generated files
- downloadable files
- optional voice output

Provide a simple interface.

The normal user should NOT see:

- internal IP addresses
- model credentials
- supervisor controls
- node management
- internal logs
- private configuration
- administrator functions

---

# 15. VOICE

PC1 should use Whisper Base for speech-to-text.

Pipeline:

```text
PHONE MICROPHONE
      |
      v
AUDIO UPLOAD
      |
      v
PC1
      |
      v
WHISPER BASE
      |
      v
TEXT
      |
      v
MULTI-AI CLUSTER
      |
      v
FINAL RESPONSE
      |
      v
TEXT-TO-SPEECH
      |
      v
PHONE
```

Support:

- voice → text
- voice → AI response
- voice → voice

Keep Whisper local on PC1.

Use a configurable TTS provider or local TTS option.

---

# 16. FILE HANDLING

Support:

- upload
- download
- file analysis
- text extraction
- code files
- documents
- PDFs where practical
- images
- generated files

Create a secure file workspace.

Every job should have a unique ID.

Example:

```text
jobs/
  JOB-2026-000001/
      input/
      extracted/
      generated/
      logs/
      responses/
```

Do not allow arbitrary path traversal.

Restrict file operations to the configured workspace.

---

# 17. IMAGE RECOGNITION

Support image input.

The architecture should allow a compatible local vision model or external vision API.

Do not pretend Gemma 2:2B text-only can perform vision.

Create a provider abstraction:

```text
VisionProvider
```

Allow future providers to be added without rewriting the master.

---

# 18. WEB SEARCH

Implement a provider abstraction for web search.

Support at least 5 configurable search providers/APIs where legally and technically available.

For example:

```text
SearchProvider1
SearchProvider2
SearchProvider3
SearchProvider4
SearchProvider5
```

The system must:

- query multiple providers
- normalize results
- remove duplicates
- collect URLs/titles/snippets
- optionally fetch permitted page content
- provide evidence to the AI nodes
- preserve source attribution
- handle provider failure
- use fallbacks
- respect each provider's rate limits and terms

Do NOT hard-code fake "unlimited" APIs.

Do NOT bypass API quotas.

Use free tiers/free services where available and configurable.

---

# 19. TEXT-TO-CODE

The cluster must support coding requests.

Example:

```text
USER:
Create a Python calculator.

PC2 → code
PC3 → code
PC4 → code
PC5 → code

MASTER:
compare
test/validate where possible
request corrections
synthesize
```

For generated code, create optional validation.

For Python:

```text
syntax validation
```

For HTML/CSS/JS:

```text
basic validation
```

Do NOT automatically execute arbitrary generated code with unrestricted system privileges.

If execution is implemented, create a restricted/sandboxed execution mechanism and clearly document its security limitations.

---

# 20. DIRECT OUTPUT

Support structured outputs such as:

```text
JSON
CSV
TXT
HTML
Markdown
Python
JavaScript
```

Create file generation utilities.

---

# 21. NODE HEALTH SYSTEM

Each node must periodically report:

```text
node_id
hostname
IP
status
CPU
RAM
disk
uptime
model
runtime
model status
current job
queue
latency
last heartbeat
errors
```

Heartbeat interval should be configurable.

Example:

```text
HEARTBEAT_INTERVAL = 5
```

If a node stops responding:

```text
ONLINE
  ↓
TIMEOUT
  ↓
UNHEALTHY
  ↓
MASTER REMOVES IT FROM CURRENT ROUND
```

The master must continue operating if at least the configured minimum number of nodes remain available.

---

# 22. SYSTEM PERFORMANCE

Monitor:

- CPU %
- RAM %
- disk %
- network
- process status
- AI request latency
- tokens/second if runtime exposes it
- model load time
- queue length
- failures
- retries

The administrator and supervisor dashboards should show these values.

---

# 23. SECURITY

Implement:

- authentication
- authorization
- session handling
- API authentication
- supervisor authentication
- admin authentication
- request IDs
- audit logs
- rate limiting
- input validation
- file validation
- path traversal protection
- safe error messages

Never store passwords in source code.

Use environment/configuration secrets.

Do not expose administrative APIs publicly by default.

---

# 24. NETWORK SECURITY

The TP-Link router is the private network boundary.

Use a private LAN subnet.

Example:

```text
192.168.50.0/24
```

Use DHCP reservations/static leases so the nodes have predictable addresses.

Example:

```text
PC1 = 192.168.50.11
PC2 = 192.168.50.12
PC3 = 192.168.50.13
PC4 = 192.168.50.14
PC5 = 192.168.50.15
Laptop = 192.168.50.10
```

Do not assume these exact addresses are available.

Make them configurable.

---

# 25. WINDOWS IMPLEMENTATION

Everything must work on:

```text
Windows 10
Windows 11
```

Use:

- Python
- Batch files
- PowerShell only when necessary
- standard Windows networking
- lightweight services/processes

Avoid requiring:

- Linux
- Docker
- WSL
- Kubernetes
- GPU
- Node.js

unless absolutely necessary.

---

# 26. CMD SETUP

Create setup scripts that can be run from CMD.

The setup must:

1. Check Python.
2. Create virtual environment.
3. Install requirements.
4. Create directories.
5. create configuration.
6. check network.
7. check master connectivity.
8. install/configure model runtime.
9. pull/check model.
10. test AI.
11. start node.
12. display useful diagnostics.

Scripts must have clear error messages.

---

# 27. REQUIRED PROJECT STRUCTURE

Create this exact high-level structure:

```text
AI-CLUSTER/
│
├── PC1/
├── PC2/
├── PC3/
├── PC4/
├── PC5/
│
├── shared/
├── config/
├── docs/
├── jobs/
├── logs/
└── README.md
```

Each PC folder must contain its own setup script.

---

# 28. REQUIRED FIVE SETUP.BAT FILES

Create:

```text
PC1/setup.bat
PC2/setup.bat
PC3/setup.bat
PC4/setup.bat
PC5/setup.bat
```

Each must be specifically configured for that PC.

PC1 setup:

- Master
- Gemma 2:2B
- Whisper Base
- API
- coordinator

PC2 setup:

- Qwen model
- node service

PC3 setup:

- Gemma model
- node service

PC4 setup:

- Llama model
- node service

PC5 setup:

- DeepSeek model
- node service

---

# 29. REQUIRED PYTHON FILES

Create:

```text
main.py
node1.py
node2.py
node3.py
node4.py
api.py
```

Suggested responsibilities:

`main.py`

- master coordinator
- parallel dispatch
- consensus
- verification
- synthesis
- job management

`node1.py`

- PC2 peer-node client/server logic

`node2.py`

- PC3 peer-node client/server logic

`node3.py`

- PC4 peer-node client/server logic

`node4.py`

- PC5 peer-node client/server logic

`api.py`

- API gateway
- authentication
- user requests
- file endpoints
- supervisor endpoints
- status endpoints

You may add additional Python modules when required for maintainability.

Do NOT put the entire application into one enormous Python file.

---

# 30. REQUIRED FILES

At minimum create:

```text
setup.bat
main.py
node1.py
node2.py
node3.py
node4.py
api.py
requirements.txt
setupguide.md
index.html
administration.html
supervisor.html
configuration.md
README.md
```

Also create **14 additional supporting files** that are genuinely useful to make the system complete.

Choose those additional files based on the architecture.

Good examples include:

```text
config.yaml
.env.example
models.yaml
nodes.yaml
security.py
auth.py
monitor.py
consensus.py
search.py
files.py
voice.py
vision.py
logger.py
health.py
```

You may change the exact names if another structure is technically better, but keep the functionality.

The final project must therefore contain the required files plus the 14 supporting files.

---

# 31. CONFIGURATION FILE

Create a central configuration system.

It must contain configurable values for:

```text
master hostname
master IP
node IPs
ports
private domain
TLS
model names
model runtime
max rounds
quality threshold
heartbeat interval
request timeout
retry count
search providers
file limits
authentication
logging
```

Never scatter these values throughout the source code.

---

# 32. configuration.md

Create a comprehensive:

```text
configuration.md
```

It must explain:

1. complete architecture
2. hardware requirements
3. router setup
4. Ethernet wiring
5. IP addressing
6. DHCP reservations
7. DNS configuration
8. hostname configuration
9. HTTPS/TLS configuration
10. PC1 setup
11. PC2 setup
12. PC3 setup
13. PC4 setup
14. PC5 setup
15. laptop setup
16. phone setup
17. model installation
18. model configuration
19. API configuration
20. supervisor authentication
21. user authentication
22. search API configuration
23. Whisper configuration
24. TTS configuration
25. file configuration
26. image configuration
27. monitoring
28. logs
29. health checks
30. troubleshooting
31. security
32. backup
33. recovery
34. shutdown procedure
35. startup procedure
36. updating models
37. changing models
38. adding/removing nodes
39. performance tuning
40. resource limits

Use concrete commands wherever possible.

---

# 33. setupguide.md

Create a beginner-friendly step-by-step guide.

It must start from:

```text
Step 1 — Prepare router
Step 2 — Connect PCs
Step 3 — Configure IP addresses
Step 4 — Configure laptop
Step 5 — Run PC1/setup.bat
Step 6 — Run PC2/setup.bat
Step 7 — Run PC3/setup.bat
Step 8 — Run PC4/setup.bat
Step 9 — Run PC5/setup.bat
Step 10 — Verify nodes
Step 11 — Configure DNS
Step 12 — Configure HTTPS
Step 13 — Test API
Step 14 — Test parallel inference
Step 15 — Test verification loop
Step 16 — Test final synthesis
Step 17 — Test supervisor
Step 18 — Test normal user
Step 19 — Test voice
Step 20 — Test files
Step 21 — Test image processing
Step 22 — Test web search
Step 23 — Performance test
Step 24 — Security test
```

---

# 34. ADMINISTRATION.HTML

Create a professional administration dashboard.

Sections:

```text
Dashboard
Nodes
Models
Jobs
System
Network
DNS
API
Logs
Security
Files
Search
Voice
Configuration
```

Display:

```text
PC1
PC2
PC3
PC4
PC5
Laptop
```

with live status.

---

# 35. SUPERVISOR.HTML

Create a mobile-first supervisor dashboard.

It should have:

```text
Cluster status
Current job
Current round
Quality score
Peer responses
Conflicts
Final synthesis
Node controls
Pause
Resume
Stop
Retry
Re-run
Send instruction
Logs
Performance
```

Make it usable from an Android phone.

---

# 36. INDEX.HTML

Create the normal user interface.

Design goals:

- simple
- fast
- mobile friendly
- responsive
- no unnecessary UI
- text chat
- voice button
- file upload
- image upload
- download results
- code output
- generated files

---

# 37. LOGGING

Create structured logs.

Every request must receive:

```text
request_id
job_id
timestamp
user_id
round
node
model
status
latency
result
error
```

Do not log passwords or secrets.

---

# 38. MASTER JOB STATE

Every job should have a state machine.

Example:

```text
RECEIVED
 ↓
QUEUED
 ↓
DISPATCHING
 ↓
RUNNING
 ↓
COLLECTING
 ↓
VERIFYING
 ↓
RETRYING
 ↓
VERIFIED
 ↓
SYNTHESIZING
 ↓
COMPLETED
```

Possible error states:

```text
FAILED
TIMEOUT
CANCELLED
PARTIAL
```

---

# 39. API DESIGN

Create clean APIs such as:

```text
POST /api/chat
POST /api/voice
POST /api/files
POST /api/image
GET  /api/status
GET  /api/jobs/<id>
POST /api/jobs/<id>/cancel
POST /api/jobs/<id>/retry
GET  /api/nodes
GET  /api/nodes/<id>
GET  /api/logs
POST /api/supervisor/command
```

Use JSON responses.

Document every endpoint.

---

# 40. SUPERVISOR COMMAND SYSTEM

Supervisor commands should be structured.

Example:

```text
PAUSE_JOB
RESUME_JOB
CANCEL_JOB
RETRY_JOB
RESTART_NODE
DISABLE_NODE
ENABLE_NODE
CHANGE_MODEL
CHANGE_THRESHOLD
CHANGE_MAX_ROUNDS
REQUEST_VERIFICATION
REQUEST_STATUS
```

Every command must be authenticated and logged.

---

# 41. FAILURE HANDLING

The system must survive:

- PC offline
- model unavailable
- timeout
- network failure
- malformed response
- API failure
- search API failure
- file processing failure
- Whisper failure
- insufficient responses

Example:

```text
5 nodes available
 ↓
PC4 fails
 ↓
4 responses
 ↓
minimum required = 3
 ↓
continue
```

If insufficient nodes remain, report the problem rather than pretending consensus exists.

---

# 42. RESOURCE MANAGEMENT

Because every PC has only 8 GB RAM and no GPU:

Implement:

- configurable context size
- configurable concurrency
- model loading control
- request timeout
- memory-aware operation
- CPU monitoring
- queue management

Do not run unnecessary heavyweight processes.

Do not load multiple large models simultaneously on the same PC.

---

# 43. NO FALSE CLAIMS

The application/documentation must never claim:

```text
100% accurate
perfect AI
guaranteed correct
unlimited API
unlimited computation
```

Instead use:

```text
verified
cross-checked
consensus
confidence
quality score
uncertainty
```

---

# 44. AI PROVENANCE

The project must clearly identify:

- base model
- model version
- model provider
- license
- whether the model is pretrained/fine-tuned/distilled/merged
- what data was used
- what modifications were made

Do not falsely claim that I created the underlying foundation model.

If I later train adapters or weights, document that accurately.

---

# 45. MODEL LICENSE CHECK

Before selecting the exact model:

Verify:

- model availability
- model license
- redistribution requirements
- commercial-use restrictions
- model runtime compatibility
- RAM requirements
- CPU feasibility

Put the results into:

```text
MODEL-LICENSES.md
```

If a requested model is unavailable or unsuitable, choose the closest legitimate alternative and explain the change.

---

# 46. NETWORK DISCOVERY

Implement safe LAN node discovery or configurable static node registration.

The master must be able to determine:

```text
PC2 online
PC3 online
PC4 online
PC5 online
```

Avoid scanning arbitrary networks.

Only operate within the configured private LAN.

---

# 47. TEST SUITE

Create tests for:

```text
network
DNS
API
authentication
node registration
heartbeat
parallel inference
timeout
retry
consensus
verification
synthesis
file upload
file generation
voice
search
supervisor
permissions
```

Create a simple:

```text
test_cluster.bat
```

that runs the appropriate tests.

---

# 48. DEMONSTRATION MODE

Create a demo mode that does not require external APIs.

Example:

```text
demo question
 ↓
5 AI nodes
 ↓
parallel answers
 ↓
verification
 ↓
synthesis
 ↓
final response
```

This allows me to demonstrate the architecture in the CS lab even if Internet access is temporarily unavailable.

---

# 49. STARTUP

Create simple startup commands.

I want to be able to do something equivalent to:

```text
PC1 → start master
PC2 → start node
PC3 → start node
PC4 → start node
PC5 → start node
```

Make the exact commands available in the documentation.

Also provide:

```text
start_all.bat
stop_all.bat
status.bat
```

where technically possible.

---

# 50. SHUTDOWN

Provide safe shutdown procedures.

The master should stop accepting new jobs before shutting down.

Nodes should finish or cancel active jobs cleanly.

---

# 51. CODE QUALITY

Write production-style but understandable code.

Requirements:

- modular
- documented
- type hints where useful
- error handling
- logging
- configuration separation
- no hard-coded secrets
- no unnecessary dependencies
- clear comments
- meaningful variable names
- Windows compatibility

Do not create fake placeholder functions that appear implemented.

If something cannot be fully implemented locally, clearly isolate it behind a provider interface and document how to configure it.

---

# 52. README

Create a professional README explaining:

- what this project is
- architecture
- hardware
- software
- AI models
- parallel inference
- consensus
- verification
- final synthesis
- voice
- files
- images
- web search
- security
- dashboards
- setup
- limitations
- licenses

Include an architecture diagram using Markdown/ASCII.

---

# 53. FINAL FILE TREE

At the end of generation, output the exact final file tree.

It should look approximately like:

```text
AI-CLUSTER/
│
├── PC1/
│   └── setup.bat
│
├── PC2/
│   └── setup.bat
│
├── PC3/
│   └── setup.bat
│
├── PC4/
│   └── setup.bat
│
├── PC5/
│   └── setup.bat
│
├── main.py
├── node1.py
├── node2.py
├── node3.py
├── node4.py
├── api.py
├── requirements.txt
├── setupguide.md
├── configuration.md
├── README.md
├── index.html
├── administration.html
├── supervisor.html
│
├── [14 additional support files]
│
├── config/
├── jobs/
├── logs/
└── shared/
```

Adjust the exact tree if your implementation needs a better modular structure, but do not omit the required files.

---

# 54. IMPORTANT IMPLEMENTATION RULE

Do not optimize for making the code look impressive.

Optimize for:

```text
RELIABILITY
+
SIMPLICITY
+
LOW RAM
+
CPU COMPATIBILITY
+
SECURITY
+
MAINTAINABILITY
```

The five PCs are a real physical LAN cluster.

The system must work even if one node fails.

---

# 55. FINAL USER EXPERIENCE

The intended experience is:

```text
PHONE USER
    |
    v
PRIVATE DNS
    |
    v
MASTER PC1
    |
    +----------+----------+----------+
    |          |          |          |
    v          v          v          v
   PC2        PC3        PC4        PC5
    |          |          |          |
    +----------+----------+----------+
                   |
                   v
             MASTER VERIFY
                   |
            quality sufficient?
              /          \
            NO            YES
            |              |
            v              v
       new parallel     Gemma 2:2B
          round         synthesis
                           |
                           v
                     FINAL RESPONSE
                           |
                           v
                      USER PHONE
```

The supervisor can monitor/intervene at any point.

The administrator laptop manages the infrastructure.

The normal user only interacts with the user-facing API/UI.

---

# 56. JULES EXECUTION INSTRUCTIONS

Before writing files:

1. Inspect the entire requested architecture.
2. Identify implementation dependencies.
3. Verify the exact AI model names and runtime compatibility.
4. Verify Python package compatibility with Windows 10/11.
5. Design the configuration system.
6. Design the API.
7. Design the node protocol.
8. Design the master orchestration.
9. Design the consensus/verification loop.
10. Design security.
11. Design monitoring.
12. Then generate the complete files.

After generating the files:

1. Check imports.
2. Check syntax.
3. Check configuration consistency.
4. Check all referenced filenames.
5. Check all API endpoints.
6. Check master/node communication.
7. Check error handling.
8. Check Windows batch scripts.
9. Check that every required file exists.
10. Check that the 14 additional files exist.
11. Check documentation against the actual implementation.
12. Fix inconsistencies.
13. Provide a final installation order.

Do not stop after creating a skeleton.

I want a complete implementation that is ready for me to configure and deploy across my five PCs.

The system should be called:

**VishalAI Parallel Intelligence Cluster**

Use a clean internal project identifier such as:

```text
VAPIC
```

Keep all names, hostnames, passwords, API keys, IP addresses, and domain names configurable.