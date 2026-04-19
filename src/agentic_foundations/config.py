from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True, slots=True)
class Settings:
    anthropic_api_key: str
    anthropic_model: str
    log_level: str
    max_agent_iterations: int

    @classmethod
    def from_env(cls) -> "Settings":
        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise RuntimeError("ANTHROPIC_API_KEY is required")
        return cls(
            anthropic_api_key=key,
            anthropic_model=os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-5"),
            log_level=os.environ.get("LOG_LEVEL", "INFO"),
            max_agent_iterations=int(os.environ.get("MAX_AGENT_ITERATIONS", "10")),
        )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings.from_env()