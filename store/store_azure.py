from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'nagelmade' # Must be replaced by your <storage_account_name>
    account_key = 'BYUPBKq6aP4HBsJyhKoquIirVKC+zKeMjjyc+fIR5+tF+KHyvXA1j8sYrWYLt5JsorV3/2cR8z5gBNU+90b8kQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'nagelmade' # Must be replaced by your storage_account_name
    account_key = 'gjppBxSsPPJlUrpQLSNLzna09MzfDpRU8G9GyS1BGwd0/YMkj5LxS6WCjsuS35KO2Wm7pr5TR6wkxEXMFR3o6g==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None