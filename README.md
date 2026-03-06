# Claude PostgreSQL Extension

A [Claude Desktop Extension](https://www.anthropic.com/engineering/desktop-extensions) (.mcpb) that connects Claude to your PostgreSQL database using [postgres-mcp](https://github.com/crystaldba/postgres-mcp).

Non-technical users can install this extension and connect to a PostgreSQL database without touching the terminal or editing config files.

## Features

- Browse schemas, tables, and column details
- Run SQL queries directly from Claude
- Analyze query performance and execution plans
- Get index recommendations
- Choose between read-only (restricted) or full (unrestricted) access

## Install

1. Download the latest `.mcpb` file from [Releases](https://github.com/tangibleMaterials/claude-postgres-extension/releases)
2. Open Claude Desktop
3. Go to **Settings > Extensions**
4. Drag the `.mcpb` file into the settings window
5. Fill in your database connection details

## Configuration

The extension will prompt you for:

| Field | Description | Default |
|---|---|---|
| Database Host | Hostname or IP of your PostgreSQL server | `localhost` |
| Database Port | Port number | `5432` |
| Database Name | The database to connect to | — |
| Username | PostgreSQL username | — |
| Password | PostgreSQL password (stored securely via OS keychain) | — |
| Access Mode | `restricted` (read-only) or `unrestricted` (read/write) | `restricted` |

## Building from source

Requires [Node.js](https://nodejs.org/) (for the mcpb CLI).

```bash
git clone https://github.com/tangibleMaterials/claude-postgres-extension.git
cd claude-postgres-extension
npx @anthropic-ai/mcpb pack .
```

This produces a `.mcpb` file you can install in Claude Desktop.

## How it works

This extension packages the [postgres-mcp](https://github.com/crystaldba/postgres-mcp) MCP server as a Claude Desktop Extension. It uses the `uv` runtime type, so Python and all dependencies are installed automatically — no manual setup required.

## License

MIT
