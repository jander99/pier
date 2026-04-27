from __future__ import annotations

import hashlib
from typing import Any

from pydantic import BaseModel, Field, model_validator


class AgentInstallSpec(BaseModel):
    agent_name: str
    version: str | None = None
    root_script: str | None = None
    user_script: str | None = None
    verification_command: str | None = None
    cache_key: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_scripts(self) -> "AgentInstallSpec":
        if not self.root_script and not self.user_script:
            raise ValueError("AgentInstallSpec requires root_script or user_script")
        return self

    def fingerprint(self) -> str:
        if self.cache_key:
            return self.cache_key
        payload = "\n".join(
            [
                self.agent_name,
                self.version or "",
                self.root_script or "",
                self.user_script or "",
                self.verification_command or "",
            ]
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]
