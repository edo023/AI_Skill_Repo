---
name: esme-2.6-expert
description: Triggered when asked about EcoStruxure Machine Expert (ESME) 2.6, PacDrive, Modicon, LMC, HMI, TM5, TM7, safety logic, or other Schneider Electric PLC/HMI libraries. Provides guidelines to search the local ESME 2.6 documentation.
---

# ESME 2.6 Expert Skill

This skill allows the agent to act as an expert on Schneider Electric's **EcoStruxure Machine Expert (ESME) 2.6** suite by using the locally downloaded and structured manual.

## Documentation Location

The complete, segmented manual in Markdown format is stored at:
📁 `C:\Users\Alfre\.gemini\antigravity\scratch\ESME_2.6\`

## Category Structure

The manual is divided into 9 top-level categories:
1. `01_EcoStruxure Machine Expert`: Safety Logic Controllers, Lexium Safety, PLCopen Safety.
2. `02_Software`: Logic Builder, libraries (Modbus, SysLog, TcpUdp, Web server, etc.), templates.
3. `03_How To`: Guides and tutorials.
4. `04_Service Tools`: Controller Assistant, Diagnostics, Gateway, Installer.
5. `05_Controllers`: Logic controllers (M241, M251, M262), Motion controllers (LMC), PacDrive 3.
6. `06_Drives, Motors and Robotic`: Lexium drives (32, 52, 62), motors, robots (delta, cartesian).
7. `07_IOs`: Expansion modules (TM3, TM5, TM7), cartridges, tower lights, third-party IOs.
8. `08_HMI`: Harmony GTO/GTU/GXU, hardware and configuration.
9. `09_Industrial PC`: Panel PCs, Box PCs, Rack PCs, hardware/user guides.

## Search Protocol

When answering queries about ESME 2.6:
1. Use the search script at `.agents/skills/esme-2.6-expert/scripts/search_esme.py` to search for keywords in the documentation.
2. Run the script from the command line:
   `python C:\Users\Alfre\.gemini\antigravity\scratch\gemini-skills\.agents\skills\esme-2.6-expert\scripts\search_esme.py --query "your search terms"`
3. Examine the returned matching file paths and read the most relevant files using the `view_file` tool to extract exact details (code snippets, parameters, wiring diagrams).
4. Always cite the file name and path in your response to the user so they can reference it in their workspace.
