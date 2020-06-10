import os


class Settings():

    def __init__(self):
        self.OS_PROJECT_DOMAIN_NAME = os.getenv('OS_PROJECT_DOMAIN_NAME')
        self.OS_USER_DOMAIN_NAME = os.getenv('OS_USER_DOMAIN_NAME')
        self.OS_PROJECT_NAME = os.getenv('OS_PROJECT_NAME')
        self.OS_TENANT_NAME = os.getenv('OS_TENANT_NAME')
        self.OS_USERNAME = os.getenv('OS_USERNAME')
        self.OS_PASSWORD = os.getenv('OS_PASSWORD')
        self.OS_AUTH_URL = os.getenv('OS_AUTH_URL')
        self.OS_INTERFACE = os.getenv('OS_INTERFACE')
        self.OS_IDENTITY_API_VERSION = int(
            os.getenv('OS_IDENTITY_API_VERSION')
        )
        self.OS_REGION_NAME = os.getenv('OS_REGION_NAME')
        self.OS_AUTH_PLUGIN = os.getenv('OS_AUTH_PLUGIN')
        self.OS_MISTRAL_URL = os.getenv('OS_MISTRAL_URL')
