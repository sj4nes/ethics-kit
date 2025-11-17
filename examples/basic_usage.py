"""
Basic usage examples for Ethics Kit.

This file demonstrates how to use the Ethics Kit in various scenarios.
"""

from ethics_kit import EthicsHandbook, EthicsCategory, WorkflowIntegration


def example_1_basic_handbook():
    """Example 1: Basic usage of the EthicsHandbook."""
    print("=" * 60)
    print("Example 1: Basic Handbook Usage")
    print("=" * 60)
    
    # Create a handbook instance
    handbook = EthicsHandbook()
    
    # Get all principles
    all_principles = handbook.get_all_principles()
    print(f"\nTotal principles: {len(all_principles)}")
    
    # Get principles by category
    safety_principles = handbook.get_by_category(EthicsCategory.SAFETY)
    print(f"\nSafety principles: {len(safety_principles)}")
    for principle in safety_principles:
        print(f"  - {principle.title}")
    
    # Get critical (highest priority) principles
    critical = handbook.get_critical_principles()
    print(f"\nCritical principles: {len(critical)}")
    for principle in critical:
        print(f"  - {principle.title} (Priority: {principle.priority})")


def example_2_compact_summary():
    """Example 2: Get compact summary for context efficiency."""
    print("\n" + "=" * 60)
    print("Example 2: Compact Summary for Context Injection")
    print("=" * 60)
    
    handbook = EthicsHandbook()
    
    # Get a compact summary of high-priority principles
    summary = handbook.get_compact_summary(max_priority=2)
    print("\n" + summary)
    
    # Get summary for specific categories
    print("\n\nSummary for Safety and Privacy only:")
    print("-" * 60)
    summary_focused = handbook.get_compact_summary(
        categories={EthicsCategory.SAFETY, EthicsCategory.PRIVACY},
        max_priority=2
    )
    print(summary_focused)


def example_3_task_specific_guidance():
    """Example 3: Get guidance for specific tasks."""
    print("\n" + "=" * 60)
    print("Example 3: Task-Specific Guidance")
    print("=" * 60)
    
    handbook = EthicsHandbook()
    
    tasks = [
        "Process user data and store it in database",
        "Delete old backup files from server",
        "Generate report about system vulnerabilities"
    ]
    
    for task in tasks:
        print(f"\nTask: {task}")
        print("-" * 60)
        principles = handbook.get_guidelines_for_task(task, max_principles=3)
        for principle in principles:
            print(f"  • {principle.title} ({principle.category.value})")
            print(f"    {principle.description}")


def example_4_workflow_integration():
    """Example 4: Using WorkflowIntegration."""
    print("\n" + "=" * 60)
    print("Example 4: Workflow Integration")
    print("=" * 60)
    
    # Create workflow integration
    integration = WorkflowIntegration()
    
    # Configure alignment for high security needs
    integration.configure_alignment(
        max_priority=1,
        categories=[EthicsCategory.SAFETY, EthicsCategory.PRIVACY]
    )
    
    # Get context injection text
    print("\nContext injection for AI agent:")
    print("-" * 60)
    context = integration.get_context_injection()
    print(context)
    
    # Get task-specific guidance
    print("\n\nTask-specific guidance:")
    print("-" * 60)
    task = "Access and modify user credentials"
    guidance = integration.get_task_specific_guidance(task)
    print(guidance)


def example_5_action_validation():
    """Example 5: Validate actions against ethics principles."""
    print("\n" + "=" * 60)
    print("Example 5: Action Validation")
    print("=" * 60)
    
    integration = WorkflowIntegration()
    
    actions = [
        "Read configuration file",
        "Delete all user data permanently",
        "Share customer email addresses with third party"
    ]
    
    for action in actions:
        print(f"\nValidating: {action}")
        result = integration.validate_action(action)
        
        print(f"  Status: {'✓ PASSED' if result['validation_passed'] else '✗ FAILED'}")
        if result['warnings']:
            print(f"  Warnings: {', '.join(result['warnings'])}")
        print(f"  Relevant principles: {len(result['relevant_principles'])}")


def example_6_prompt_prefix():
    """Example 6: Generate prompt prefixes for AI agents."""
    print("\n" + "=" * 60)
    print("Example 6: Prompt Prefix Generation")
    print("=" * 60)
    
    integration = WorkflowIntegration()
    integration.configure_alignment(max_priority=2)
    
    # Get general ethics prefix
    print("\nGeneral ethics prompt prefix:")
    print("-" * 60)
    prefix = integration.get_ethics_prompt_prefix()
    print(prefix)
    
    # Get task-specific prefix
    task = "Implement data processing pipeline"
    print(f"\nTask-specific prefix for: {task}")
    print("-" * 60)
    task_prefix = integration.get_ethics_prompt_prefix(task=task)
    print(task_prefix)


if __name__ == "__main__":
    example_1_basic_handbook()
    example_2_compact_summary()
    example_3_task_specific_guidance()
    example_4_workflow_integration()
    example_5_action_validation()
    example_6_prompt_prefix()
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)
