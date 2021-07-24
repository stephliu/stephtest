# Databricks notebook source
## Databricks notebook source
import sys
sys.path.append("/Workspace/Projects/stephanie.liu@databricks.com/demo")



# COMMAND ----------

df = spark.read.format(“txt”).load(“test.txt”) 



# COMMAND ----------

from pathlib import Path

print(Path("/Workspace/Projects/stephanie.liu@databricks.com/demo/data.csv").read_text())



# COMMAND ----------

# MAGIC %python
# MAGIC dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

# COMMAND ----------

import sys
sys.argv[0]

# COMMAND ----------


