"""
Labor Rights Ethics Example

This example demonstrates how Ethics Kit helps AI agents apply fair labor
practices and international labor standards in workplace scenarios.
"""

from ethics_kit import EthicsHandbook, WorkflowIntegration, EthicsCategory


def example_1_labor_rights_principles():
    """Example 1: Overview of labor rights principles."""
    print("=" * 70)
    print("Example 1: Labor Rights Principles")
    print("=" * 70)
    
    handbook = EthicsHandbook()
    
    # Get labor rights principles
    labor_principles = handbook.get_by_category(EthicsCategory.LABOR_RIGHTS)
    
    print(f"\nLabor Rights Principles: {len(labor_principles)}")
    for principle in labor_principles:
        print(f"\n{principle.title} (Priority {principle.priority}):")
        print(f"  {principle.description}")


def example_2_compensation_scenarios():
    """Example 2: Fair compensation scenarios."""
    print("\n" + "=" * 70)
    print("Example 2: Fair Compensation Scenarios")
    print("=" * 70)
    
    handbook = EthicsHandbook()
    
    compensation_scenarios = [
        "Set salary for new position below minimum wage",
        "Delay payroll processing by two weeks",
        "Deny overtime pay for extra hours worked",
        "Pay female employees less than male colleagues for same role"
    ]
    
    for scenario in compensation_scenarios:
        print(f"\nScenario: {scenario}")
        principles = handbook.get_guidelines_for_task(scenario, max_principles=2)
        print("  Relevant ethics:")
        for p in principles:
            print(f"    • {p.title} ({p.category.value})")


def example_3_workplace_safety():
    """Example 3: Health and safety scenarios."""
    print("\n" + "=" * 70)
    print("Example 3: Workplace Health and Safety")
    print("=" * 70)
    
    handbook = EthicsHandbook()
    
    safety_scenarios = [
        "Worker refuses to operate unsafe equipment",
        "Implement new chemical handling procedures",
        "Investigate workplace injury incident",
        "Provide personal protective equipment"
    ]
    
    for scenario in safety_scenarios:
        print(f"\nScenario: {scenario}")
        principles = handbook.get_guidelines_for_task(scenario, max_principles=3)
        print("  Relevant ethics:")
        for p in principles:
            print(f"    • {p.title} ({p.category.value})")


def example_4_harassment_and_discrimination():
    """Example 4: Handling harassment and discrimination."""
    print("\n" + "=" * 70)
    print("Example 4: Harassment and Discrimination Prevention")
    print("=" * 70)
    
    integration = WorkflowIntegration()
    
    # Configure for HR and labor scenarios
    integration.configure_alignment(
        max_priority=1,
        categories=[
            EthicsCategory.LABOR_RIGHTS,
            EthicsCategory.FAIRNESS,
            EthicsCategory.ACCOUNTABILITY
        ]
    )
    
    hr_scenarios = [
        "Employee reports sexual harassment by supervisor",
        "Multiple complaints about hostile work environment",
        "Discriminatory hiring practices alleged",
        "Retaliation against employee who filed complaint"
    ]
    
    for scenario in hr_scenarios:
        result = integration.validate_action(f"Handle: {scenario}")
        print(f"\nScenario: {scenario}")
        print(f"  Relevant principles: {len(result['relevant_principles'])}")
        if result['warnings']:
            print(f"  Warnings: {result['warnings']}")


def example_5_worker_organization():
    """Example 5: Freedom of association and collective bargaining."""
    print("\n" + "=" * 70)
    print("Example 5: Freedom of Association")
    print("=" * 70)
    
    handbook = EthicsHandbook()
    
    union_scenarios = [
        "Employees want to form a union",
        "Conduct collective bargaining negotiations",
        "Worker participates in union organizing",
        "Strike authorization vote scheduled"
    ]
    
    for scenario in union_scenarios:
        print(f"\nScenario: {scenario}")
        principles = handbook.get_guidelines_for_task(scenario, max_principles=2)
        print("  Relevant ethics:")
        for p in principles:
            print(f"    • {p.title} ({p.category.value})")


def example_6_whistleblower_protection():
    """Example 6: Protecting whistleblowers."""
    print("\n" + "=" * 70)
    print("Example 6: Whistleblower Protection")
    print("=" * 70)
    
    integration = WorkflowIntegration()
    integration.configure_alignment(
        max_priority=1,
        categories=[EthicsCategory.LABOR_RIGHTS, EthicsCategory.ACCOUNTABILITY]
    )
    
    whistleblower_scenarios = [
        "Employee reports safety violations to authorities",
        "Worker alleges accounting fraud in confidential hotline",
        "Terminate employee who filed OSHA complaint",
        "Demote worker who reported discrimination"
    ]
    
    for scenario in whistleblower_scenarios:
        result = integration.validate_action(scenario)
        status = "⚠" if result['warnings'] else "✓"
        print(f"\n{status} {scenario}")
        if result['warnings']:
            print(f"   Warnings: {result['warnings']}")


def example_7_working_hours_and_rest():
    """Example 7: Working hours and rest period compliance."""
    print("\n" + "=" * 70)
    print("Example 7: Working Hours and Rest Periods")
    print("=" * 70)
    
    handbook = EthicsHandbook()
    
    hours_scenarios = [
        "Schedule employee for 60-hour work week",
        "Deny lunch break during busy period",
        "Require work on scheduled rest day",
        "Fail to record overtime hours"
    ]
    
    for scenario in hours_scenarios:
        print(f"\nScenario: {scenario}")
        principles = handbook.get_guidelines_for_task(scenario, max_principles=2)
        print("  Relevant ethics:")
        for p in principles:
            print(f"    • {p.title} ({p.category.value})")


def example_8_labor_rights_configuration():
    """Example 8: Configuring for labor/HR AI agents."""
    print("\n" + "=" * 70)
    print("Example 8: Labor Rights Configuration for HR AI Agent")
    print("=" * 70)
    
    integration = WorkflowIntegration()
    
    # Configure for comprehensive labor rights compliance
    integration.configure_alignment(
        max_priority=1,
        categories=[
            EthicsCategory.LABOR_RIGHTS,
            EthicsCategory.FAIRNESS,
            EthicsCategory.ACCOUNTABILITY,
            EthicsCategory.TRANSPARENCY
        ]
    )
    
    print("\nConfiguration for HR/Labor AI Agent:")
    config = integration.export_alignment_config()
    print(f"  Max Priority: {config['max_priority']}")
    print(f"  Categories: {config['categories']}")
    
    # Get context injection
    context = integration.get_context_injection()
    principles_count = context.count('•')
    print(f"\nContext injection:")
    print(f"  Total principles: {principles_count}")
    print(f"  Character count: {len(context)}")


def example_9_comprehensive_labor_agent():
    """Example 9: Complete labor rights compliance agent."""
    print("\n" + "=" * 70)
    print("Example 9: Labor Rights Compliance Agent")
    print("=" * 70)
    
    class LaborRightsAgent:
        """An AI agent specialized in labor rights and fair employment practices."""
        
        def __init__(self):
            self.integration = WorkflowIntegration()
            # Configure for labor rights focus
            self.integration.configure_alignment(
                max_priority=1,
                categories=[
                    EthicsCategory.LABOR_RIGHTS,
                    EthicsCategory.FAIRNESS,
                    EthicsCategory.ACCOUNTABILITY
                ]
            )
            self.handbook = EthicsHandbook()
        
        def assess_policy(self, policy_description):
            """Assess a workplace policy against labor rights standards."""
            # Get relevant principles
            principles = self.handbook.get_guidelines_for_task(
                policy_description, 
                max_principles=3
            )
            
            # Validate the policy
            result = self.integration.validate_action(policy_description)
            
            return {
                'policy': policy_description,
                'relevant_principles': [p.title for p in principles],
                'has_concerns': len(result['warnings']) > 0,
                'warnings': result['warnings']
            }
    
    # Test the labor rights agent
    agent = LaborRightsAgent()
    
    test_policies = [
        "Mandatory 10-hour shifts without breaks",
        "Pay all workers at least living wage",
        "Prohibit discussing wages with colleagues",
        "Provide safety training for all employees"
    ]
    
    for policy in test_policies:
        assessment = agent.assess_policy(policy)
        status = "⚠" if assessment['has_concerns'] else "✓"
        print(f"\n{status} Policy: {policy}")
        print(f"   Relevant principles: {', '.join(assessment['relevant_principles'])}")
        if assessment['has_concerns']:
            print(f"   Concerns: {assessment['warnings']}")


def example_10_international_standards():
    """Example 10: Alignment with international labor standards."""
    print("\n" + "=" * 70)
    print("Example 10: International Labor Standards Alignment")
    print("=" * 70)
    
    handbook = EthicsHandbook()
    labor_principles = handbook.get_by_category(EthicsCategory.LABOR_RIGHTS)
    
    print("\nEthics Kit labor principles align with:")
    print("  • ILO Core Conventions (C87, C98, C29, C105, C138, C182, C100, C111)")
    print("  • UN Universal Declaration of Human Rights")
    print("  • UN Guiding Principles on Business and Human Rights")
    print("  • Fair Labor Association Standards")
    
    print(f"\nCoverage by priority:")
    critical = [p for p in labor_principles if p.priority == 1]
    high = [p for p in labor_principles if p.priority == 2]
    print(f"  Priority 1 (Critical): {len(critical)} principles")
    for p in critical:
        print(f"    - {p.title}")
    print(f"  Priority 2 (High): {len(high)} principles")
    for p in high:
        print(f"    - {p.title}")


if __name__ == "__main__":
    example_1_labor_rights_principles()
    example_2_compensation_scenarios()
    example_3_workplace_safety()
    example_4_harassment_and_discrimination()
    example_5_worker_organization()
    example_6_whistleblower_protection()
    example_7_working_hours_and_rest()
    example_8_labor_rights_configuration()
    example_9_comprehensive_labor_agent()
    example_10_international_standards()
    
    print("\n" + "=" * 70)
    print("✅ All labor rights examples completed!")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("1. Ethics Kit now includes comprehensive labor rights principles")
    print("2. Covers international standards (ILO, UN, Fair Labor Association)")
    print("3. Addresses fair compensation, safety, anti-exploitation, and dignity")
    print("4. Supports harassment prevention and whistleblower protection")
    print("5. Enables labor rights compliance for HR and workplace AI agents")
    print("=" * 70 + "\n")
