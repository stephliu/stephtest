# Databricks notebook source
# MAGIC %md
# MAGIC # Using Treasure Data with Python and Pandas
# MAGIC 
# MAGIC Treasure Data has a [python client](https://github.com/treasure-data/td-client-python), which means pandas/python users can connect directly from their iPython Notebooks.
# MAGIC 
# MAGIC All you need is a Treasure Data account, which you can get from [here](https://console.treasuredata.com/users/sign_up)

# COMMAND ----------

import tdclient
import pandas as pd
import numpy as np
%matplotlib inline

# COMMAND ----------

# MAGIC %md
# MAGIC ## Getting Treasure Data's apikey
# MAGIC 
# MAGIC You need to get your Treasure Data API key. There are two ways to fetch your API keys after you sign up for Treasure Data.
# MAGIC 
# MAGIC 1. **From web console**: Please access [this URL](https://console.treasuredata.com/users/current). At the right most column, you can retrieve the API key. You want to use the Normal, not Write-Only API keys to run queries.
# MAGIC 2. **From CLI**: If you are the `td` command user, running the following command exposes your API key.
# MAGIC     ```
# MAGIC     td apikey:show
# MAGIC     ```

# COMMAND ----------

apikey = 'Your API key here' # Setting your API key

# COMMAND ----------

client = tdclient.Client(apikey) # instantiating the client

# COMMAND ----------

# MAGIC %md
# MAGIC ## Running a query against the sample dataset
# MAGIC 
# MAGIC As you can see below, running queries is easy. Just use the `query` method, which accepts three arguments.
# MAGIC 
# MAGIC 1. The first argument is the name of the database
# MAGIC 2. The second argument is the query string (Make sure you use single quotes if you are using the Presto engine!)
# MAGIC 3. The optional keyword arguments. I am using `type='presto'` here to use Presto and not Hive.

# COMMAND ----------

job = client.query('sample_datasets',
                   "SELECT TD_TIME_FORMAT(time, 'yyyy') AS t, SUM(volume) "
                   "FROM nasdaq "
                   "WHERE symbol='AMZN' "
                   "GROUP BY TD_TIME_FORMAT(time, 'yyyy') "
                   "ORDER BY t", type='presto')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Asynchronous execution
# MAGIC 
# MAGIC Your query creates a job asynchronously. Please check the job is
# MAGIC 
# MAGIC 1. finished (`job.finished()` should return `True`)
# MAGIC 2. successful (`job.status()` should return `success`)

# COMMAND ----------

[job.status(), job.finished()]

# COMMAND ----------

results = [r for r in job.result()]

# COMMAND ----------

results_df = pd.DataFrame.from_records(results, columns=('year', 'AMZN trade volume'))

# COMMAND ----------

results_df.plot(x='year')
