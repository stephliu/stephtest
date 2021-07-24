# Databricks notebook source
# MAGIC %md
# MAGIC ### Enable Files in Repos
# MAGIC Import this notebook into the desired workspace and run the two cells below to enable Files in Repos. 
# MAGIC 
# MAGIC ####Please note: It takes about 2 minutes for the new conf flag to get picked up by the webapp. Wait a few minutes before trying to work with non-notebook files. 
# MAGIC 
# MAGIC Once your workspace is enabled, remember that you need to attach to a cluster running DBR 8.0 and above for the feature to work. See documentation included with the onboarding email for more details. 

# COMMAND ----------

import os
os.environ["DATABRICKS_INSTANCE"] = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get()
os.environ["DATABRICKS_TOKEN"] = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

# COMMAND ----------

# MAGIC %sh 
# MAGIC 
# MAGIC curl -s -X PATCH -H "Authorization: Bearer $DATABRICKS_TOKEN" $DATABRICKS_INSTANCE/api/2.0/workspace-conf -d '{ "enableWorkspaceFilesystem": "true" }'
# MAGIC curl -s -X GET -H "Authorization: Bearer $DATABRICKS_TOKEN" $DATABRICKS_INSTANCE/api/2.0/workspace-conf?keys=enableWorkspaceFilesystem

# COMMAND ----------

# MAGIC %md
# MAGIC ### Do not forget to enable Files on your DBR 8.0 cluster
# MAGIC To do so click Clusters--> Advanced Options--> Spark --> Environment Variables. Add following variable 'WSFS_ENABLE=true' and then restart your cluster
