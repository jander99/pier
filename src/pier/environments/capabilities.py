"""Capability flags describing what an environment type can do.

One ``EnvironmentCapabilities`` instance per environment, computed at
construction time and stored as ``self.capabilities``. Validators and
call sites read from it instead of from individual properties.
"""

from pydantic import BaseModel


class EnvironmentCapabilities(BaseModel):
    gpus: bool = False
    """Whether the environment can allocate GPUs to containers."""

    disable_internet: bool = False
    """Whether the environment can run containers without internet access."""

    filtered_egress: bool = False
    """Whether the environment can allow only declared outbound inference hosts."""

    preinstall_agents: bool = False
    """Whether the environment can install selected agents at image build time."""

    windows: bool = False
    """Whether the environment can run Windows containers."""

    mounted: bool = False
    """Whether the environment mounts log directories as host filesystems."""
