from mistralclient.api import client
from openstack.keystone import Keystone
from settings import Settings

class Mistral():

    def __init__(self, session):
        self.client = client.client(
            session=session,
            mistral_url=Settings().OS_MISTRAL_URL
        )

    def get_workflows(self):
        return self.client.workflows.list()

    def create_execution(self, workflow, input):
        return self.client.executions.create(
            workflow_identifier=workflow,
            workflow_input=input
        )