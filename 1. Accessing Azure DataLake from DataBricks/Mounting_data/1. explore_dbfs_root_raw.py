# Databricks notebook source
# MAGIC %md
# MAGIC ## Explore DBFS root
# MAGIC 1. List all the folders in DBFS root
# MAGIC 2. Interact with DBFS file browser
# MAGIC 3. Upload file to DBFS root

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list(scope='project2scope')

# COMMAND ----------

storageAccountName = "adlsstorageforlearning"
storageAccountAccessKey = dbutils.secrets.get(scope='project2scope', key='keyaccess-adls-key1')
sasToken = dbutils.secrets.get(scope='project2scope', key='SasTokenADLSgen2')
blobContainerName = "raw"
mountPoint = "/mnt/data/raw"
if not any(mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
  try:
    dbutils.fs.mount(
      source = "wasbs://{}@{}.blob.core.windows.net".format(blobContainerName, storageAccountName),
      mount_point = mountPoint,
      extra_configs = {'fs.azure.account.key.' + storageAccountName + '.blob.core.windows.net': storageAccountAccessKey}
      # extra_configs = {'fs.azure.sas.' + blobContainerName + '.' + storageAccountName + '.blob.core.windows.net': sasToken}
    )
    print("mount succeeded!")
  except Exception as e:
    print("mount exception", e)

# COMMAND ----------

display(dbutils.fs.mounts())