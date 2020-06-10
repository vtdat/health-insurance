from keystoneauth1.identity import v3
from keystoneauth1 import session
from settings import Settings


class Keystone(Settings):

    def __init__(self):
        super().__init__()
        auth = v3.Password(
            auth_url=self.OS_AUTH_URL,
            username=self.OS_USERNAME,
            password=self.OS_PASSWORD,
            project_name=self.OS_PROJECT_NAME,
            user_domain_name=self.OS_USER_DOMAIN_NAME,
            project_domain_name=self.OS_PROJECT_DOMAIN_NAME
        )

        self.session = session.Session(auth=auth)
