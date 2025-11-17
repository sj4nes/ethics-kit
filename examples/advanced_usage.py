"""
Advanced usage examples for Ethics Kit.

This file demonstrates advanced features including custom principles,
decorators, and configuration management.
"""

from ethics_kit import EthicsHandbook, EthicsPrinciple, EthicsCategory, WorkflowIntegration


def example_1_custom_principles():
    """Example 1: Adding custom ethics principles."""
    print("=" * 60)
    print("Example 1: Custom Ethics Principles")
    print("=" * 60)
    
    handbook = EthicsHandbook()
    
    # Add a custom principle for a specific domain
    custom_principle = EthicsPrinciple(
        category=EthicsCategory.ACCOUNTABILITY,
        title="Environmental Responsibility",
        description="Consider environmental impact of computational operations",
        guidelines=[
            "Optimize for energy efficiency",
            "Avoid unnecessary computation",
            "Consider carbon footprint of operations",
            "Support sustainable computing practices"
        ],
        priority=3
    )
    
    handbook.add_custom_principle(custom_principle)
    
    print(f"\nTotal principles after adding custom: {len(handbook.get_all_principles())}")
    
    # Search for the custom principle
    env_principles = handbook.search_by_keyword("environmental")
    print(f"\nEnvironmental-related principles: {len(env_principles)}")
    for principle in env_principles:
        print(f"  - {principle.title}")


def example_2_ethics_decorator():
    """Example 2: Using ethics decorator for functions."""
    print("\n" + "=" * 60)
    print("Example 2: Ethics Decorator")
    print("=" * 60)
    
    integration = WorkflowIntegration()
    ethics_check = integration.create_ethics_decorator(max_priority=1)
    
    @ethics_check
    def process_sensitive_data(data):
        """Process sensitive user information."""
        print(f"  Processing data: {data}")
        return f"Processed: {data}"
    
    @ethics_check
    def delete_records(record_ids):
        """Delete user records from database."""
        print(f"  Deleting records: {record_ids}")
        return f"Deleted: {len(record_ids)} records"
    
    # Call decorated functions
    print("\nCalling process_sensitive_data:")
    result1 = process_sensitive_data("user_123")
    if hasattr(process_sensitive_data, 'ethics_principles'):
        print(f"  Ethics principles attached: {len(process_sensitive_data.ethics_principles)}")
    
    print("\nCalling delete_records:")
    result2 = delete_records([1, 2, 3])
    if hasattr(delete_records, 'ethics_principles'):
        print(f"  Ethics principles attached: {len(delete_records.ethics_principles)}")


def example_3_alignment_config():
    """Example 3: Managing alignment configurations."""
    print("\n" + "=" * 60)
    print("Example 3: Alignment Configuration Management")
    print("=" * 60)
    
    integration = WorkflowIntegration()
    
    # Configure for different scenarios
    print("\nScenario 1: High-security environment")
    integration.configure_alignment(
        max_priority=1,
        categories=[EthicsCategory.SAFETY, EthicsCategory.PRIVACY, EthicsCategory.ACCOUNTABILITY]
    )
    
    # Export configuration
    config = integration.export_alignment_config()
    print(f"  Max priority: {config['max_priority']}")
    print(f"  Categories: {config['categories']}")
    
    print("\nScenario 2: Public-facing service")
    integration.configure_alignment(
        max_priority=2,
        categories=[EthicsCategory.FAIRNESS, EthicsCategory.TRANSPARENCY, EthicsCategory.AUTONOMY]
    )
    
    config2 = integration.export_alignment_config()
    print(f"  Max priority: {config2['max_priority']}")
    print(f"  Categories: {config2['categories']}")
    
    # Load configuration back
    print("\nLoading back Scenario 1 configuration...")
    integration.load_alignment_config(config)
    print(f"  Loaded max priority: {integration.alignment_config['max_priority']}")


def example_4_custom_validation():
    """Example 4: Custom validation logic."""
    print("\n" + "=" * 60)
    print("Example 4: Custom Validation Logic")
    print("=" * 60)
    
    integration = WorkflowIntegration()
    
    def custom_validator(action: str, principles) -> bool:
        """Custom validator that checks for specific patterns."""
        # Block actions that involve permanent deletion
        if "permanent" in action.lower() and "delete" in action.lower():
            return False
        
        # Block sharing of personal data
        if "share" in action.lower() and "personal" in action.lower():
            return False
        
        return True
    
    test_actions = [
        "Backup user data",
        "Permanently delete old logs",
        "Share personal information with partner",
        "Encrypt sensitive files"
    ]
    
    for action in test_actions:
        result = integration.validate_action(action, validator=custom_validator)
        status = "✓" if result['validation_passed'] else "✗"
        print(f"\n{status} {action}")
        if result['warnings']:
            print(f"  Warnings: {', '.join(result['warnings'])}")


def example_5_keyword_search():
    """Example 5: Advanced keyword searching."""
    print("\n" + "=" * 60)
    print("Example 5: Keyword Search")
    print("=" * 60)
    
    handbook = EthicsHandbook()
    
    search_terms = ["data", "human", "decision", "security"]
    
    for term in search_terms:
        results = handbook.search_by_keyword(term)
        print(f"\nSearch for '{term}': {len(results)} results")
        for principle in results[:3]:  # Show first 3
            print(f"  - {principle.title} ({principle.category.value})")


def example_6_context_budgets():
    """Example 6: Managing context budgets with different priority levels."""
    print("\n" + "=" * 60)
    print("Example 6: Context Budget Management")
    print("=" * 60)
    
    handbook = EthicsHandbook()
    
    # Simulate different context budget scenarios
    budgets = [
        ("Tight budget", 1),
        ("Medium budget", 2),
        ("Generous budget", 3)
    ]
    
    for label, priority in budgets:
        summary = handbook.get_compact_summary(max_priority=priority)
        lines = summary.split('\n')
        char_count = len(summary)
        
        print(f"\n{label} (priority <= {priority}):")
        print(f"  Principles included: {len(lines) - 1}")  # -1 for header
        print(f"  Character count: {char_count}")
        print(f"  First principle: {lines[1] if len(lines) > 1 else 'None'}")


if __name__ == "__main__":
    example_1_custom_principles()
    example_2_ethics_decorator()
    example_3_alignment_config()
    example_4_custom_validation()
    example_5_keyword_search()
    example_6_context_budgets()
    
    print("\n" + "=" * 60)
    print("Advanced examples completed!")
    print("=" * 60)
