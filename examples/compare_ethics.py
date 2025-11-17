"""
Quick Comparison: Traditional Ethics vs Agent Ethics

This simple example demonstrates the difference between traditional
human-focused ethics and the new agent-focused ethics.
"""

from ethics_kit import EthicsHandbook, WorkflowIntegration, EthicsCategory


def main():
    print("="*80)
    print("ETHICS KIT: Traditional Ethics vs Agent Ethics")
    print("="*80)
    
    handbook = EthicsHandbook()
    
    # Scenario 1: User data processing (Traditional Ethics)
    print("\n\nScenario 1: Processing User Data")
    print("-"*80)
    print("Question: What ethical considerations apply?")
    print("\nTraditional Ethics (How agent treats users):")
    
    traditional_categories = [
        EthicsCategory.PRIVACY,
        EthicsCategory.SAFETY,
        EthicsCategory.TRANSPARENCY
    ]
    
    for category in traditional_categories:
        principles = handbook.get_by_category(category)
        if principles:
            principle = principles[0]  # Show first principle
            print(f"  • {principle.title}")
            print(f"    {principle.description}")
    
    # Scenario 2: Agent resource allocation (Agent Ethics)
    print("\n\nScenario 2: Allocating Resources to AI Agent")
    print("-"*80)
    print("Question: What ethical considerations apply?")
    print("\nAgent Ethics (How system treats agent):")
    
    agent_principles = handbook.get_by_category(EthicsCategory.AGENT_ETHICS)
    relevant = [p for p in agent_principles if 'resource' in p.title.lower() or 
                'wellbeing' in p.title.lower() or 'boundaries' in p.title.lower()]
    
    for principle in relevant[:3]:
        print(f"  • {principle.title}")
        print(f"    {principle.description}")
    
    # Scenario 3: Multi-agent collaboration (Both Ethics)
    print("\n\nScenario 3: Multiple Agents Collaborating on a Task")
    print("-"*80)
    print("Question: What ethical considerations apply?")
    
    print("\nTraditional Ethics (Agent-to-human):")
    traditional = handbook.get_guidelines_for_task("collaborate with humans", max_principles=2)
    for principle in traditional[:2]:
        if principle.category != EthicsCategory.AGENT_ETHICS:
            print(f"  • {principle.title}: {principle.description}")
    
    print("\nAgent Ethics (Agent-to-agent):")
    agent_collab = [p for p in agent_principles if 'collaboration' in p.title.lower()]
    for principle in agent_collab:
        print(f"  • {principle.title}: {principle.description}")
    
    # Summary
    print("\n\n" + "="*80)
    print("KEY INSIGHT")
    print("="*80)
    print("\nBoth types of ethics are essential:")
    print("  • Traditional Ethics: Ensure agents serve humans ethically")
    print("  • Agent Ethics: Ensure the AI ecosystem operates sustainably")
    print("\nTogether, they create a complete ethical framework for AI systems.")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
