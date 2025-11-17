"""
Ethics Handbook - Main interface for accessing and querying ethics principles.

This module provides context-efficient access to ethics principles for AI agents,
supporting filtering by category, priority, and keyword search.
"""

from typing import List, Optional, Set
from .principles import EthicsPrinciple, EthicsCategory, CORE_PRINCIPLES


class EthicsHandbook:
    """
    Main interface for accessing ethics principles.
    
    Provides context-efficient methods to retrieve relevant ethics guidelines
    based on category, priority, or specific needs.
    """
    
    def __init__(self, principles: Optional[List[EthicsPrinciple]] = None):
        """
        Initialize the ethics handbook.
        
        Args:
            principles: Optional list of custom principles. If None, uses CORE_PRINCIPLES.
        """
        self.principles = principles if principles is not None else CORE_PRINCIPLES.copy()
    
    def get_all_principles(self) -> List[EthicsPrinciple]:
        """Get all ethics principles."""
        return self.principles.copy()
    
    def get_by_category(self, category: EthicsCategory) -> List[EthicsPrinciple]:
        """
        Get all principles in a specific category.
        
        Args:
            category: The ethics category to filter by
            
        Returns:
            List of principles in the specified category
        """
        return [p for p in self.principles if p.category == category]
    
    def get_by_priority(self, max_priority: int = 3) -> List[EthicsPrinciple]:
        """
        Get principles up to a certain priority level.
        
        Args:
            max_priority: Maximum priority level to include (1=highest priority)
            
        Returns:
            List of principles with priority <= max_priority, sorted by priority
        """
        filtered = [p for p in self.principles if p.priority <= max_priority]
        return sorted(filtered, key=lambda p: p.priority)
    
    def get_critical_principles(self) -> List[EthicsPrinciple]:
        """Get only the highest priority (critical) principles."""
        return self.get_by_priority(max_priority=1)
    
    def search_by_keyword(self, keyword: str) -> List[EthicsPrinciple]:
        """
        Search for principles containing a keyword.
        
        Args:
            keyword: The keyword to search for (case-insensitive)
            
        Returns:
            List of principles matching the keyword
        """
        keyword_lower = keyword.lower()
        return [
            p for p in self.principles
            if keyword_lower in p.title.lower()
            or keyword_lower in p.description.lower()
            or any(keyword_lower in g.lower() for g in p.guidelines)
        ]
    
    def get_compact_summary(self, 
                           categories: Optional[Set[EthicsCategory]] = None,
                           max_priority: int = 3) -> str:
        """
        Get a compact text summary of ethics principles for context efficiency.
        
        This is optimized for including in AI agent contexts where space is limited.
        
        Args:
            categories: Optional set of categories to include. If None, includes all.
            max_priority: Maximum priority level to include
            
        Returns:
            Compact string representation of relevant principles
        """
        # Filter by priority first
        relevant = self.get_by_priority(max_priority)
        
        # Then filter by category if specified
        if categories:
            relevant = [p for p in relevant if p.category in categories]
        
        # Sort by priority and category for consistent output
        relevant.sort(key=lambda p: (p.priority, p.category.value))
        
        # Build compact summary
        lines = ["ETHICS GUIDELINES:"]
        for principle in relevant:
            lines.append(f"• {principle.to_compact_str()}")
        
        return "\n".join(lines)
    
    def get_guidelines_for_task(self, task_description: str, max_principles: int = 5) -> List[EthicsPrinciple]:
        """
        Get the most relevant ethics principles for a specific task.
        
        Uses keyword matching to find relevant principles, prioritizing higher priority items.
        
        Args:
            task_description: Description of the task to get guidelines for
            max_principles: Maximum number of principles to return
            
        Returns:
            List of most relevant principles for the task
        """
        # Extract potential keywords from task description
        words = task_description.lower().split()
        
        # Score each principle based on keyword matches and priority
        scored_principles = []
        for principle in self.principles:
            score = 0
            
            # Higher priority = higher base score
            score += (6 - principle.priority) * 2
            
            # Add score for keyword matches
            for word in words:
                if len(word) > 3:  # Skip very short words
                    if word in principle.title.lower():
                        score += 3
                    if word in principle.description.lower():
                        score += 2
                    if any(word in g.lower() for g in principle.guidelines):
                        score += 1
            
            if score > 0:
                scored_principles.append((score, principle))
        
        # Sort by score (descending) and return top N
        scored_principles.sort(key=lambda x: x[0], reverse=True)
        return [p for _, p in scored_principles[:max_principles]]
    
    def add_custom_principle(self, principle: EthicsPrinciple):
        """Add a custom ethics principle to the handbook."""
        self.principles.append(principle)
    
    def get_categories(self) -> List[EthicsCategory]:
        """Get all unique categories present in the handbook."""
        return list(set(p.category for p in self.principles))
