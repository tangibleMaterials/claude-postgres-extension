#!/usr/bin/env python3
"""Entry point for the postgres-mcp Desktop Extension."""

import os
import sys

# Inject --access-mode from environment if not already in argv
access_mode = os.environ.get("POSTGRES_MCP_ACCESS_MODE", "restricted")
if "--access-mode" not in sys.argv:
    sys.argv.extend(["--access-mode", access_mode])

from postgres_mcp import main

main()
