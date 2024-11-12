from dataclasses import dataclass
from typing import List, Optional, Sequence

CONTAINER_LOCATION_PATH_ID = "path://"


@dataclass
class ServiceSecret:
    """
    Holds onto configuration for the secrets to be used in the container.

    Attributes:
      secret_name: The name of the secret as stored in the AWS Secrets Manager
      environment_key: The ARN of the secret as stored in the AWS Secrets Manager
    """

    secret_name: str
    """The name of the secret as stored in the AWS Secrets Manager"""

    environment_key: str
    """The name to use for the environment variable within the container"""


class ServiceProps:
    """
    ECS service properties

    container_name: the name of the container
    container_port: the container application port
    container_memory: the container application memory
    container_location:
      supports "path://" for building container from local (i.e. path://docker/MyContainer)
      supports docker registry references (i.e. ghcr.io/sage-bionetworks/schematic-thumbor:latest)
    container_env_vars: a json dictionary of environment variables to pass into the container
      i.e. {"EnvA": "EnvValueA", "EnvB": "EnvValueB"}
    container_secrets: List of `ServiceSecret` resources to pull from AWS secrets manager
    container_command: Optional commands to run in the container
    """

    def __init__(
        self,
        container_name: str,
        container_port: int,
        container_memory: int,
        container_location: str,
        container_env_vars: dict,
        container_secrets: List[ServiceSecret],
        container_command: Optional[Sequence[str]] = None,
    ) -> None:
        self.container_name = container_name
        self.container_port = container_port
        self.container_memory = container_memory
        if CONTAINER_LOCATION_PATH_ID in container_location:
            container_location = container_location.removeprefix(
                CONTAINER_LOCATION_PATH_ID
            )
        self.container_location = container_location
        self.container_env_vars = container_env_vars
        self.container_secrets = container_secrets
        self.container_command = container_command
