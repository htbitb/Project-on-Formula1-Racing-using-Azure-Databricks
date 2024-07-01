## Accessing DataLake from Databricks

In here we are using 2 ways to take the data from ADLS gen2, which one is access directly and the other is mounting the path in the data lake.

### Mounting Data
Mounting refers to attaching an external storage system to Databricks File System (DBFS). When you mount a data lake, you create a directory in DBFS that maps to a path in the data lake.

**Advantages:**
* **Simplified Path Access:** Once mounted, you can access data using simple paths (`e.g., /mnt/mydatalake/myfolder/`), which can be more convenient than specifying full URLs.
* **Centralized Configuration**: Credentials and configuration are set up once during the mounting process, simplifying access for multiple users and notebooks.
* **Consistent Access**: The mounted path can be used by all users in the Databricks workspace, ensuring consistency.

**Disadvantages:**
* **Setup Overhead**: Requires initial setup to configure the mount point.
* **Limited Flexibility**: Changing the credentials or configuration for a mount point requires remounting.
* **Permissions**: All users with access to the Databricks workspace can access the mounted data, which might not always be desirable.
```python
# Mounting ADLS to DBFS
configs = {
  "fs.azure.account.auth.type": "OAuth",
  "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
  "fs.azure.account.oauth2.client.id": "<client-id>",
  "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="myScope", key="clientSecret"),
  "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<tenant-id>/oauth2/token"
}

dbutils.fs.mount(
  source = "abfss://<container>@<storage-account>.dfs.core.windows.net/",
  mount_point = "/mnt/mydatalake",
  extra_configs = configs)
```
<br>

### Direct Access Using Access Keys/ SAS Tokens/ Server Principals/ cluster Scope.

This approach allows to access directly to the data in containers, does not involve mounting the data to DBFS.

**Advantages:**
* **Flexibility**: You can easily switch between different storage accounts or containers without remounting.
* **Granular Access Control**: SAS tokens can provide fine-grained access control, such as read-only access for specific operations.
* **Temporary Access**: SAS tokens can be generated with expiration times, providing temporary access to data.

**Disadvantages:**
* **Management Overhead**: You need to manage and distribute credentials or tokens securely.
* **Complex Paths**: Accessing data requires specifying full URLs, which can be more cumbersome than using mounted paths.
* **Inconsistent Access**: Each user or notebook might need to configure credentials individually, leading to potential inconsistencies.

```python
# Setting up Spark configurations for direct access
spark.conf.set("fs.azure.account.key.<storage-account>.blob.core.windows.net", "<access-key>")
# Or using SAS token
# spark.conf.set("fs.azure.sas.<container>.<storage-account>.blob.core.windows.net", "<sas-token>")

# Reading data directly
df = spark.read.csv("wasbs://<container>@<storage-account>.blob.core.windows.net/path/to/file.csv")
df.show()
```

### Key Vault
Using Azure Key Vault with Databricks enhances security, simplifies secret management, ensures compliance, and integrates seamlessly with other Azure services. It provides a robust mechanism for handling sensitive information and ensures best practices in secret management and application security.
