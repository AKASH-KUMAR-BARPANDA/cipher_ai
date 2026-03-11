# Cipher AI

## Overview
**Cipher AI** is a modular personal AI assistant activated by the wake phrase `“Hey Cipher”`. It uses FastAPI, LangChain, and LangGraph agents to understand voice commands and execute tasks such as system control and web automation via Playwright. Designed to scale into an IoT ecosystem with ESP32, vision models, and mobile interfaces.

## Vision & Objectives
To build a **scalable**, **centralized AI platform** that seamlessly integrates:
- Intuitive **voice interfaces**
- Sophisticated **AI reasoning**
- Flexible **automation tools**
- Diverse **IoT hardware**



## 🏛️ Master Architecture (Future-Ready)

```text
                   +-------------------+
                   |   Wake Word       |
                   |   "Hey Cipher"    |
                   +---------+---------+
                             |
                             v
                    +----------------+
                    | Voice Capture  |
                    | Laptop / ESP32 |
                    +--------+-------+
                             |
                             v
                      +-------------+
                      | Speech-to-Text|
                      |  (Whisper)    |
                      +------+---------+
                             |
                             v
                        +----------+
                        | FastAPI  |
                        | Cipher   |
                        | Server   |
                        +----+-----+
                             |
         +-------------------+------------------+
         |                                      |
         v                                      v
   +-----------+                         +-------------+
   | LangGraph |                         |  Memory DB  |
   | Agent     |                         |  MongoDB    |
   +-----+-----+                         +-------------+
         |
         v
   +----------- Tools Layer -----------------------------+
   |                                                     |
   |  Browser Tool      → Playwright                     |
   |  System Tool       → Laptop Control                 |
   |  Search Tool       → Web APIs                       |
   |  IoT Tool          → ESP32 Devices                  |
   |  Vision Tool       → Camera + PyTorch               |
   |  Knowledge Tool    → PostgreSQL                     |
   +-----------------------------------------------------+
                             |
                             v
      +-------------------------------+
      |        User Interfaces        |
      |                               |
      |  Flutter Mobile App           |
      |  Streamlit Dashboard          |
      +-------------------------------+
```
---
The system components flow logically:
1. **Voice Input** → Wake-word detection & audio capture.
2. **Processing** → Transcription `(Whisper)` & orchestration `(FastAPI)`.
3. **Logic** → Reasoning `(LangChain/LangGraph)` & memory lookup.
4. **Execution** → Tool invocation `(Browser, System, IoT, etc.)`.
5. **Feedback** → Dashboards & companion mobile interfaces.

## System Modules
- **Voice Interaction**: Detects "Hey Cipher" and streams pristine audio.
- **AI Agent**: The cognitive core for command reasoning and tool selection.
- **Automation**: Executes system-level actions and web navigation.
- **Memory & Knowledge**: Stores history and preferences for contextual awareness.
- **IoT Control**: Communicates securely with microcontrollers and sensors.
- **Vision & Perception**: Processes camera feeds for environmental context.
- **User Interface**: Provides visual monitoring and manual overriding controls.

---

## 📁 Project Folder Architecture

The repository is organized into modular components. 

```text
cipher_ai/
├── core/                   # Central orchestrator and fundamental utilities
│   ├── config/             # Environment variables and system configurations
│   ├── logger/             # Centralized logging system
│   └── exceptions/         # Custom error handling classes
│
├── agents/                 # AI Reasoning logic
│   ├── base/               # Base AI agent structures
│   ├── workflows/          # Multi-step LangGraph workflows
│   └── prompts/            # System prompts and instruction templates
│
├── tools/                  # Execution scripts and actionable plugins
│   ├── system/             # OS-level control (open apps, manage files)
│   ├── browser/            # Web automation scripts (Playwright)
│   ├── search/             # Internet search and API retrievals
│   └── iot/                # Hardware and smart device controls
│
├── services/               # Background jobs and external audio processors
│   ├── speech/             # Whisper STT and text-to-speech services
│   └── wakeword/           # Porcupine / openWakeWord listeners
│
├── database/               # Database connection layers
│   ├── mongodb/            # Flexible memory and conversation logs
│   └── postgresql/         # Structured relational knowledge
│
├── api/                    # FastAPI server
│   ├── routes/             # REST endpoints (status, manual triggers)
│   └── websockets/         # Real-time voice/data streaming
│
├── ui/                     # Streamlit dashboard for monitoring
│   ├── components/         # Reusable UI widgets
│   └── pages/              # Analytics, logs, and settings views
│
├── mobile/                 # Flutter companion application codebase
│
├── esp32/                  # Microcontroller firmware (C++/Arduino)
│   ├── mic_node/           # Remote audio capture firmware
│   └── control_node/       # Hardware relay control code
│
└── models/                 # Local machine learning models
    ├── whisper/            # Local STT weights
    └── vision/             # PyTorch models for camera perception
```
---
## Technology Stack
- **Backend**: **FastAPI** `(High-speed orchestration)`
- **AI & Agents**: **LangChain**, **LangGraph**, **PyTorch** `(Reasoning & Machine Learning)`
- **Automation**: **Playwright** `(Web data extraction)`
- **Databases**: **MongoDB** `(Flexible memory)`, **PostgreSQL** `(Relational knowledge)`
- **Embedded**: **ESP32**, **ESP32-CAM** `(Edge processing & vision)`
- **Interfaces**: **Flutter** `(Mobile UX)`, **Streamlit** `(Web Dashboards)`
- **Speech Processing**: **Whisper (or similar)** `(Accurate audio transcription)`

## Development Roadmap
- **Phase 1**: Voice input & agent-based task execution (Local).
- **Phase 2**: Multi-step workflows & persistent memory.
- **Phase 3**: Web automation & smart data retrieval.
- **Phase 4**: IoT control integration (ESP32).
- **Phase 5**: Computer vision & gesture recognition.
- **Phase 6**: Mobile interface deployment (Flutter).
- **Phase 7**: System monitoring dashboard (Streamlit).
- **Phase 8**: Adaptive learning & behavioral automation.

## Expected Capabilities
- **Voice Control**: End-to-end hands-free system management.
- **Intelligent Automation**: Autonomous multi-step operations.
- **IoT Management**: Command over physical environments.
- **Visual Perception**: Real-time context awareness from camera feeds.
- **Adaptive Learning**: Anticipating user needs based on historical usage.

---

## 🚀 Development Phases

### Phase 1 (Current)

**Voice → Agent → Laptop**

**Features:**
- Wake word detection
- Speech recognition
- AI agent
- System commands
- Browser automation

**Execution Flow:**
```text
   "Hey Cipher"
        ↓
  Speech → Text
        ↓
 LangChain Agent
        ↓
  Tool Execution
        ↓
   Laptop task
```

**Example Commands:**
```text
"Hey Cipher, open YouTube"
"Hey Cipher, search latest AI papers"
"Hey Cipher, open VSCode"
```

---

### Phase 2 

Adding **memory**, **reasoning**, and complex **workflows** using **LangGraph**.

**Upgrades:**
- **Memory**: Persistent context and state awareness across conversations.
- **Reasoning**: Advanced logic for navigating unpredictable tasks.
- **Workflows**: Multi-step, interconnected sub-agent routing.

**Example Command:**
```text
"Hey Cipher, prepare study mode"
```

*Cipher executes:*
```text
[✓] Turn on focus music
[✓] Open notes
[✓] Start timer
[✓] Block distracting sites
```

---

## 🎙️ Wake Word System

Powered by **Porcupine** or **openWakeWord** for constant, low-power listening.

**Pipeline:**
```text
   Microphone
        ↓
 Wake word detection ("Hey Cipher")
        ↓
 Trigger recording
        ↓
 Speech recognition (Whisper)
```

---

## ✨ Final Result

Your desk system will look like:

```text
User:   Hey Cipher

Cipher: Yes Akash?

```text
User:   "Hey Cipher, prepare study mode"
```

*Cipher executes:*
```text
[✓] Turn on focus music
[✓] Open notes
[✓] Start timer
[✓] Block distracting sites
```
