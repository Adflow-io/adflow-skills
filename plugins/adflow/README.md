# Adflow

De verbinding met Adflow, als MCP-server (`https://app.adflow.io/api/v1/mcp`, zie `.mcp.json`). Andere Adflow-plugins
gebruiken deze verbinding, zodat die maar één keer bestaat.

Na het installeren log je één keer in met je eigen Adflow-account (in Claude Code via `/mcp`, server
`plugin:adflow:adflow`). Heb je Adflow ook als connector in claude.ai, zet die dan uit, anders heb je hem dubbel.
