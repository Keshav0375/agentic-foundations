from __future__ import annotations

from anthropic import Anthropic

from .config import Settings


def build_anthropic_client(settings: Settings) -> Anthropic:
    """Factory. Inject this into agents — never instantiate Anthropic() inline."""
    return Anthropic(api_key=settings.anthropic_api_key)