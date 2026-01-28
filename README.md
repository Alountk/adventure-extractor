# AdventureExtractor 🗡️🐕

A lightweight, modular Python-based tool designed to analyze and extract video streaming links from "Hora de Aventura" fan-sites. This project is built with a "minimal dependency" philosophy, prioritizing custom implementations over heavy third-party libraries.

## 🚀 Project Overview
The goal of this project is to create a robust CLI tool that can:
1. Parse episode metadata.
2. Resolve third-party video host obfuscation (Streamtape, Fembed, etc.).
3. Stream/Download content directly using chunked requests.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Core Libraries:** - `requests`: For network handling.
    - `BeautifulSoup4`: For DOM parsing.
    - `re`: (Built-in) For regex-based link extraction.

---

## 📍 Project Breadcrumbs (Roadmap)

Below is the step-by-step implementation plan we are following:

- [x] **Step 1: Project Scaffolding**
    - Define repository structure.
    - Initialize base `AdventureScraper` class.
- [ ] **Step 2: Server Discovery (MVP)**
    - Identify and extract AJAX-based player options from the episode page.
    - Implement a basic CLI to list and select available servers.
- [ ] **Step 3: The Resolvers (The Core)**
    - Reverse engineer the "Handshake" of major video hosts.
    - Bypass redirection and hidden tokens to get the raw `.mp4` / `.m3u8` URL.
- [ ] **Step 4: Smart Downloader**
    - Implement a chunk-based downloader with progress bars.
    - Add support for re-sumable downloads.
- [ ] **Step 5: Automation & Bulk**
    - Ability to parse entire seasons or search for specific episodes.

---

## 📂 Structure
```text
adventure-extractor/
├── src/
│   ├── main.py          # Entry point
│   ├── scraper.py       # Main site logic
│   └── resolvers/       # Logic for each video host (Fembed, Streamtape, etc.)

## ⚖️ Disclaimer
This project is strictly for educational purposes. It is not intended for commercial use, monetization, or personal profit.