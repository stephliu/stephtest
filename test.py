# Databricks notebook source
import sys
sys.path.append("/Workspace/Projects/stephanie.liu@databricks.com/demo")

# COMMAND ---------------

import foo

# COMMAND ---------------

from pathlib import Path

print(Path("/Workspace/Projects/stephanie.liu@databricks.com/demo/data.csv").read_text())

