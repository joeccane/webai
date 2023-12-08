import yaml
from typing import List, Dict, Any

# Define the AgentConfig class with additional attributes as needed
class AgentConfig:
  def __init__(self, model: str, name: str, system_message: str, agent_type: str, **kwargs):
    self.model = model
    self.name = name
    self.system_message = system_message
    self.agent_type = agent_type
    self.extra_config = kwargs  # Store any additional configuration

  def to_dict(self) -> Dict[str, Any]:
    """Convert the AgentConfig to a dictionary."""
    return {
      'model': self.model,
      'name': self.name,
      'system_message': self.system_message,
      'agent_type': self.agent_type,
      'extra_config': self.extra_config
    }

  def instantiate_agent(self):
    """Instantiate the appropriate agent based on the agent type."""
    # Example of a factory pattern to instantiate agents
    if self.agent_type == 'UserProxy':
      return UserProxy(self.model, self.name, self.system_message, **self.extra_config)
    elif self.agent_type == 'Assistant':
      return Assistant(self.model, self.name, self.system_message, **self.extra_config)
    # Add other agent types here
    else:
      raise ValueError(f"Unknown agent type: {self.agent_type}")

# Function to load agent configurations from a YAML string
def load_agent_configs(yaml_string: str) -> List[AgentConfig]:
  try:
    # Parse the YAML string
    configs = yaml.safe_load(yaml_string)
    # Validate and instantiate AgentConfig objects
    agent_configs = []
    for config in configs:
      required_keys = {'model', 'name', 'system_message', 'agent_type'}
      if not required_keys.issubset(config.keys()):
        raise ValueError(f"Missing required configuration keys in: {config}")
      agent_configs.append(AgentConfig(**config))
    return agent_configs
  except yaml.YAMLError as e:
    print(f"Error parsing YAML: {e}")
    return []
  except ValueError as e:
    print(f"Configuration error: {e}")
    return []

# Function to create an agent list from the agent configurations
def create_agent_list(agent_configs: List[AgentConfig]) -> List[Dict[str, Any]]:
  return [agent.to_dict() for agent in agent_configs]

# Example YAML string containing the agent configurations
yaml_string = """
- model: gpt-4-1106-preview
  name: Design_manager_agent
  system_message: '...'
  agent_type: UserProxy
  extra_field: value
# ... (other agent configurations)
"""

# Load the agent configurations
agent_configs = load_agent_configs(yaml_string)

# Create the agent list
agent_list = create_agent_list(agent_configs)

# Print the agent list to verify
for agent in agent_list:
  print(agent)

# Instantiate agents (example usage)
for agent_config in agent_configs:
  try:
    agent = agent_config.instantiate_agent()
    print(f"Instantiated agent: {agent}")
  except ValueError as e:
    print(e)

# Placeholder classes for different agent types
class UserProxy:
  def __init__(self, model, name, system_message, **kwargs):
    pass  # Implement the UserProxy agent

class Assistant:
  def __init__(self, model, name, system_message, **kwargs):
    pass  # Implement the Assistant agent

# Add other agent classes as needed

# TERMINATE confirmation
print("TERMINATE")
