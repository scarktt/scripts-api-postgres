#!/bin/sh
set -e

# Get the list of available Click commands
AVAILABLE_COMMANDS=$(python -m src.main --help | awk '{print $1}')

if echo "$AVAILABLE_COMMANDS" | grep -qw "$1"; then
  # Run Click command
  exec python -m src.main "$@"
else
  # Run any other command (e.g., pytest, bash, etc.)
  exec "$@"
fi
