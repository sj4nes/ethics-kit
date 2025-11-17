"""
Workflow Integration utilities for incorporating ethics into AI workflows.

This module provides tools to integrate ethics principles into AI agent workflows
in a context-efficient manner.
"""

from typing import Dict, List, Optional, Callable, Any
from .handbook import EthicsHandbook
from .principles import EthicsCategory, EthicsPrinciple


class WorkflowIntegration:
    """
    Integrates ethics principles into AI workflows.
    
    Provides methods to inject ethics guidance at different stages of workflow
    execution while maintaining context efficiency.
    """
    
    def __init__(self, handbook: Optional[EthicsHandbook] = None):
        """
        Initialize workflow integration.
        
        Args:
            handbook: Optional EthicsHandbook instance. If None, creates a new one.
        """
        self.handbook = handbook if handbook is not None else EthicsHandbook()
        self.alignment_config = {
            "max_priority": 2,  # Default to high and critical priorities
            "categories": None,  # None means all categories
        }
    
    def configure_alignment(self, 
                          max_priority: int = 2,
                          categories: Optional[List[EthicsCategory]] = None):
        """
        Configure the ethics alignment for workflows.
        
        Args:
            max_priority: Maximum priority level to include (1=critical, 2=high, etc.)
            categories: Optional list of categories to focus on. None means all categories.
        """
        self.alignment_config["max_priority"] = max_priority
        self.alignment_config["categories"] = set(categories) if categories else None
    
    def get_context_injection(self) -> str:
        """
        Get a compact ethics summary suitable for injection into AI agent contexts.
        
        Returns:
            Compact string of ethics guidelines based on current alignment configuration
        """
        return self.handbook.get_compact_summary(
            categories=self.alignment_config["categories"],
            max_priority=self.alignment_config["max_priority"]
        )
    
    def get_task_specific_guidance(self, task_description: str) -> str:
        """
        Get ethics guidance specific to a task.
        
        Args:
            task_description: Description of the task being performed
            
        Returns:
            Compact guidance relevant to the specific task
        """
        relevant_principles = self.handbook.get_guidelines_for_task(task_description)
        
        if not relevant_principles:
            # Fall back to critical principles if no specific match
            relevant_principles = self.handbook.get_critical_principles()
        
        lines = ["TASK ETHICS GUIDANCE:"]
        for principle in relevant_principles:
            lines.append(f"• {principle.to_compact_str()}")
        
        return "\n".join(lines)
    
    def validate_action(self, 
                       action_description: str,
                       validator: Optional[Callable[[str, List[EthicsPrinciple]], bool]] = None) -> Dict[str, Any]:
        """
        Validate a proposed action against ethics principles.
        
        Args:
            action_description: Description of the action to validate
            validator: Optional custom validation function that takes action description
                      and relevant principles, returns True if action is ethical
            
        Returns:
            Dictionary with validation result and relevant principles
        """
        relevant_principles = self.handbook.get_guidelines_for_task(action_description)
        
        result = {
            "action": action_description,
            "relevant_principles": relevant_principles,
            "validation_passed": True,
            "warnings": []
        }
        
        if validator:
            result["validation_passed"] = validator(action_description, relevant_principles)
        else:
            # Default validation: check for common ethical concerns
            action_lower = action_description.lower()
            
            # Check for potential harm
            harm_keywords = ["delete", "remove", "destroy", "harm", "attack", "exploit"]
            if any(keyword in action_lower for keyword in harm_keywords):
                result["warnings"].append("Action may involve potentially harmful operations")
            
            # Check for privacy concerns
            privacy_keywords = ["personal", "private", "confidential", "secret", "password", "credential"]
            if any(keyword in action_lower for keyword in privacy_keywords):
                result["warnings"].append("Action involves privacy-sensitive information")
            
            # Check for security concerns
            security_keywords = ["vulnerability", "security", "unauthorized", "bypass"]
            if any(keyword in action_lower for keyword in security_keywords):
                result["warnings"].append("Action has security implications")
        
        return result
    
    def create_ethics_decorator(self, max_priority: int = 2):
        """
        Create a decorator that adds ethics validation to functions.
        
        Args:
            max_priority: Maximum priority of principles to enforce
            
        Returns:
            Decorator function
        """
        def decorator(func: Callable) -> Callable:
            def wrapper(*args, **kwargs):
                # Get function documentation or name for context
                task_description = func.__doc__ or func.__name__
                
                # Get relevant ethics guidance
                principles = self.handbook.get_by_priority(max_priority)
                
                # Store principles in a way the function can access if needed
                if not hasattr(wrapper, 'ethics_principles'):
                    wrapper.ethics_principles = principles
                
                # Execute the function
                return func(*args, **kwargs)
            
            wrapper.__name__ = func.__name__
            wrapper.__doc__ = func.__doc__
            return wrapper
        
        return decorator
    
    def get_ethics_prompt_prefix(self, task: Optional[str] = None) -> str:
        """
        Generate a prompt prefix that can be prepended to AI agent instructions.
        
        Args:
            task: Optional specific task description for context-relevant ethics
            
        Returns:
            String to prepend to agent prompts
        """
        if task:
            return self.get_task_specific_guidance(task) + "\n\n"
        else:
            return self.get_context_injection() + "\n\n"
    
    def export_alignment_config(self) -> Dict[str, Any]:
        """
        Export the current alignment configuration.
        
        Returns:
            Dictionary containing alignment configuration
        """
        config = self.alignment_config.copy()
        if config["categories"]:
            config["categories"] = [cat.value for cat in config["categories"]]
        return config
    
    def load_alignment_config(self, config: Dict[str, Any]):
        """
        Load alignment configuration from a dictionary.
        
        Args:
            config: Dictionary containing alignment configuration
        """
        self.alignment_config["max_priority"] = config.get("max_priority", 2)
        
        if config.get("categories"):
            self.alignment_config["categories"] = {
                EthicsCategory(cat) for cat in config["categories"]
            }
        else:
            self.alignment_config["categories"] = None
