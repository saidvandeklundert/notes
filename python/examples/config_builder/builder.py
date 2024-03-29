from model import *
import os
from pathlib import Path
import json
from jinja2 import Environment, FileSystemLoader


def load_communities() -> Communities:
    """Mocking data retrieval from 'something'."""
    communities = Communities(
        **yaml.safe_load(
            """
    std_communities:
      COMMUNITY_1 : '1:1'
      COMMUNITY_2 : '2:2' 
      COMMUNITY_3 : '3:3'
    """
        )
    )

    return communities


def load_secrets_from_vault() -> Dict[str, str]:
    """Retreives secrets information from Vault"""
    return {
        "admin_password": "admin",
        "admin_username": "admin",
        "root_hash": "$ABC123",
    }


def load_information_from_ssot() -> Network:
    """Retreives information from SSOT"""
    network = Network(
        **yaml.safe_load(
            """
devices:
- name: R1
  serial: BX109
  model: MX10008
  platform: juniper
  mgmt: 10.0.0.1/31
  role: spine
  interfaces:
    - name: et-0/0/0
      ipv4: 192.168.1.1/31
      description: core_link
    - name: et-0/0/1
      ipv4: 192.168.1.3/31
      description: core_link 
- name: R2
  serial: BX109
  model: MX10008
  platform: juniper
  mgmt: 10.0.0.2/31
  role: leaf
  interfaces:
    - name: et-0/0/0
      ipv4: 192.168.1.5/31
      description: core_link
    - name: et-0/0/1
      ipv4: 192.168.1.7/31
      description: core_link
"""
        )
    )
    return network


class NetworkBuilder:
    """Class that builds the data schema and the network configuration"""

    def __init__(self, network: Network, communities: Communities, secrets: dict):
        self.network = network
        self.communities = communities
        self.secrets = secrets
        self.build_network()
        self.create_schema()
        self.render_templates()

    def build_network(self):
        """Implements additional build logic

        In this example, only community data is added to the network device.

        """
        for device in self.network.devices:
            if device.role == "leaf":
                device.communities = self.communities
            device.secrets = self.secrets

        return self.network

    def create_schema(self):
        """Create a per_device_schema"""
        for device in self.network.devices:
            with open(f"{device.name}.json", "w") as f:
                f.write(device.json(indent=2))

    def render_templates(self):
        print("rendering templates")
        for file_name in Path(os.getcwd()).glob("**/*.json"):
            with open(file_name) as f:
                data = json.load(f)
                device_name = data["name"]
                print(data)
                file_loader = FileSystemLoader("templates")
                env = Environment(loader=file_loader)

                template = env.get_template("template.j2")
                output = template.render(data=data)

                if output:
                    # avoid the Jinja whitespace nonesense:
                    output = "\n".join(
                        [line for line in output.splitlines() if line.strip()]
                    )
                    with open(f"{device_name}.cfg", "w") as f:
                        f.write(output)
                    print(output)
                else:
                    raise RuntimeError("No template output!!")


if __name__ == "__main__":

    community_input = load_communities()
    secrets_input = load_secrets_from_vault()
    network_input = load_information_from_ssot()
    network = NetworkBuilder(
        network=network_input, communities=community_input, secrets=secrets_input
    )
