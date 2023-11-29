#!/bin/bash

TOOL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$TOOL_DIR"
echo "$PWD"
export PATH="$TOOL_DIR:$PATH"
echo "export PATH=\"$TOOL_DIR:\$PATH\"" >> ~/.bashrc
source ~/.bashrc