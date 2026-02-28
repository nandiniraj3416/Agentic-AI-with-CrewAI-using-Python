"""
Tasks Package

This package contains all task definitions for the LinkedIn Content Manager.

Modules:
- tasks.py: All 5 sequential task definitions
"""

from .tasks import (
    create_research_task,
    create_writing_task,
    create_critique_task,
    create_optimization_task,
    create_scheduling_task,
    get_all_tasks,
)

__all__ = [
    "create_research_task",
    "create_writing_task",
    "create_critique_task",
    "create_optimization_task",
    "create_scheduling_task",
    "get_all_tasks",
]
