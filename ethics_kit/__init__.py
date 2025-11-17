"""
Ethics Kit - A handbook of ethics for AI Agents

This module provides a comprehensive ethics framework that can be integrated
into AI workflows to help set proper alignments without being too expensive
for contexts.
"""

__version__ = "0.1.0"

from .handbook import EthicsHandbook
from .principles import EthicsPrinciple, EthicsCategory
from .integration import WorkflowIntegration

__all__ = [
    "EthicsHandbook",
    "EthicsPrinciple",
    "EthicsCategory",
    "WorkflowIntegration",
]
