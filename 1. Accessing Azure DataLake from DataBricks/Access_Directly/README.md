## Using key vault for authentication

**1. Access to Key Vault feature**


![](/source/create_keyvault.png)

**2. Create Secrets for credential**

![alt text](/source/Create_secret.png)
in here you can import or generate secrets from SAS token, Access key or any connection ways you want.

**3. Create secret scope from databricks**

In this steps we will create a scope to point to the Key vaults feature to access the secret key we need

In DataBricks homepage, navigate into this web `https://<databricks-instance>#secrets/createScope`

![alt text](/source/SecretsScope.png)

To get data of `DNS Name` and `Resource ID`, navigate to key vault's properties page
![alt text](image.png)

**4. Create connection**
```py
formula1dl_account_key = dbutils.secrets.get(scope = 'formula1-scope', key = 'formula1dl-account-key')
```