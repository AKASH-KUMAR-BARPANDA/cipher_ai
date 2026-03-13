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
   | LangChain |                         |  Memory DB  |
   | Agents    |                         |  MongoDB    |
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
│   ├── command_router/     # Routing logic for agent commands
│   └── voice_processing/   # Wake word listening and audio processing
│
├── agents/                 # AI Reasoning logic and graph definitions
│   ├── cipher_agent.py     # Main agent implementation
│   └── agent_graph.py      # LangGraph workflow definition
│
├── tools/                  # Execution scripts and actionable plugins
│   ├── browser_tool.py     # Web automation (Playwright)
│   ├── iot_tool.py         # Hardware controls
│   ├── search_tool.py      # Search and API retrievals
│   ├── system_tool.py      # OS-level control
│   └── vision_tool.py      # Vision processing tools
│
├── services/               # Background jobs and external processors
│   ├── automation_service.py # Automation management
│   ├── iot_service.py      # IoT communication
│   ├── speech_service.py   # Speech-to-text (Whisper)
│   └── vision_service.py   # Vision processing logic
│
├── database/               # Database connection layers
│   ├── mongodb.py          # MongoDB utilities
│   └── postgres.py         # PostgreSQL utilities
│
├── api/                    # FastAPI server implementation
│   └── main.py             # API entry point
│
├── ui/                     # Dashboards and monitoring interfaces
│   └── streamlit/          # Streamlit monitoring application
│
├── mobile/                 # Mobile application codebase
│   └── flutter_app/        # Flutter companion app
│
├── esp32/                  # Microcontroller firmware (C++/Arduino)
│   └── firmware/           # ESP32 firmware code
│
├── models/                 # Local machine learning models
│   └── pytorch_models/     # Model weights and definitions
│
├── main.py                 # Application entry point
├── pyproject.toml          # Project configuration (uv)
└── uv.lock                 # Dependency lock file
```
---
## Technology Stack
- **Backend**: **FastAPI** `(High-speed orchestration)`
- **AI & Agents**: **LangChain**, **LangGraph**, **PyTorch** `(Reasoning & Machine Learning)`
- **Automation**: **Playwright** `(Web data extraction)`
- **Databases**: **MongoDB**, **PostgreSQL** `(Relational and NoSQL storage)`
- **Package Management**: **uv** `(Lightning-fast Python dependency management)`
- **Embedded**: **ESP32**, **ESP32-CAM** `(Edge processing & vision)`
- **Interfaces**: **Flutter** `(Mobile UX)`, **Streamlit** `(Web Dashboards)`
- **Speech Processing**: **Whisper** `(Accurate audio transcription)`

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
