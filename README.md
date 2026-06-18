# Gemini Agent Custom Skills Repository

This is a private repository containing custom agent skills.

## Structure

* `.agents/skills/`: Holds the directories for each custom skill.
  * `<skill-name>/SKILL.md`: The skill definition file containing instructions and rules for the agent.
  * `<skill-name>/scripts/`: Supporting utility scripts used by the skill.
  * `<skill-name>/references/`: References and documentation used by the skill.

## How to Use

1. Set this directory as your active workspace.
2. The agent will automatically discover and load the workspace skills defined in the `.agents/skills/` directory.
