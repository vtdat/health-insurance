from openstack.keystone import Keystone
from novaclient import client
from novaclient.api_versions import APIVersion


class Nova():

    def __init__(self, session):
        self.client = client.Client(
            APIVersion('2.35'),
            session=session
        )

    def get_client(self):
        return self.client

    def get_servers(self):
        return self.client.servers.list()

    def get_aggregates(self):
        return self.client.aggregates.list()

    def get_flavors(self):
        return self.client.flavors.list()
    
    def get_hypervisors(self):
        return self.client.hypervisors.list()
    
    def get_hypervisors(self, uuid):
        return self.client.hypervisors.get(uuid)
    
    def disable_hypervisor_service(self, hypervisor):
        return self.client.services.disable(hypervisor, 'nova-compute')

    def enable_hypervisor_service(self, hypervisor):
        return self.client.services.enable(hypervisor, 'nova-compute')

    def create_server(
        self, name, image, flavor, nics, hypervisor_hostname=None
    )
        return self.client.servers.create(
            name=name,
            image=image,
            flavor=flavor,
            nics=nics,
            hypervisor_hostname=hypervisor_hostname
        )
