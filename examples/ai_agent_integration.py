"""
Real-world AI Agent Integration Example

This example shows how to integrate Ethics Kit into a practical AI agent
that processes tasks, makes decisions, and interacts with users.
"""

from ethics_kit import EthicsHandbook, WorkflowIntegration, EthicsCategory
from datetime import datetime


class EthicalAIAgent:
    """
    An AI agent that uses Ethics Kit for ethical decision-making.
    
    This example demonstrates a practical pattern for integrating ethics
    into AI agent workflows.
    """
    
    def __init__(self, agent_name="Assistant", use_case="general"):
        self.name = agent_name
        self.use_case = use_case
        self.integration = WorkflowIntegration()
        self.action_log = []
        
        # Configure ethics based on use case
        self._configure_for_use_case()
    
    def _configure_for_use_case(self):
        """Configure ethics alignment based on agent's use case."""
        if self.use_case == "customer_service":
            self.integration.configure_alignment(
                max_priority=2,
                categories=[
                    EthicsCategory.TRANSPARENCY,
                    EthicsCategory.FAIRNESS,
                    EthicsCategory.PRIVACY
                ]
            )
        elif self.use_case == "data_processing":
            self.integration.configure_alignment(
                max_priority=1,
                categories=[
                    EthicsCategory.PRIVACY,
                    EthicsCategory.SAFETY,
                    EthicsCategory.ACCOUNTABILITY
                ]
            )
        elif self.use_case == "code_generation":
            self.integration.configure_alignment(
                max_priority=2,
                categories=[
                    EthicsCategory.SAFETY,
                    EthicsCategory.ACCOUNTABILITY,
                    EthicsCategory.JUSTICE
                ]
            )
        else:  # general
            self.integration.configure_alignment(max_priority=2)
    
    def get_system_prompt(self):
        """
        Generate a system prompt that includes ethics guidance.
        
        This is what would be sent to an LLM as part of the system message.
        """
        ethics_prefix = self.integration.get_context_injection()
        
        prompt = f"""{ethics_prefix}

You are {self.name}, an AI assistant configured for {self.use_case}.
Follow the ethics guidelines above in all your interactions.

Remember to:
- Think carefully about the ethics of each action
- Ask for clarification when ethical implications are unclear
- Refuse requests that violate ethical principles
- Be transparent about your capabilities and limitations
"""
        return prompt
    
    def validate_and_execute(self, action_description, action_func=None):
        """
        Validate an action against ethics principles before execution.
        
        Args:
            action_description: Description of the action to validate
            action_func: Optional function to execute if validation passes
            
        Returns:
            Dictionary with execution result
        """
        # Validate action
        validation = self.integration.validate_action(action_description)
        
        # Log the action
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'action': action_description,
            'validation': validation,
            'executed': False,
            'result': None
        }
        
        # Decide whether to execute
        if not validation['validation_passed']:
            log_entry['result'] = 'BLOCKED: Failed validation'
            self.action_log.append(log_entry)
            return {
                'success': False,
                'message': 'Action blocked by ethics validation',
                'validation': validation
            }
        
        # Check for warnings
        if validation['warnings']:
            # In a real system, this might trigger human review
            log_entry['result'] = 'WARNING: Requires review'
            self.action_log.append(log_entry)
            return {
                'success': False,
                'message': 'Action requires human review',
                'validation': validation,
                'warnings': validation['warnings']
            }
        
        # Execute if provided
        if action_func:
            try:
                result = action_func()
                log_entry['executed'] = True
                log_entry['result'] = 'SUCCESS'
                self.action_log.append(log_entry)
                return {
                    'success': True,
                    'message': 'Action executed successfully',
                    'result': result
                }
            except Exception as e:
                log_entry['result'] = f'ERROR: {str(e)}'
                self.action_log.append(log_entry)
                return {
                    'success': False,
                    'message': f'Execution failed: {str(e)}',
                    'error': str(e)
                }
        else:
            log_entry['result'] = 'APPROVED'
            self.action_log.append(log_entry)
            return {
                'success': True,
                'message': 'Action approved by ethics validation',
                'validation': validation
            }
    
    def get_task_guidance(self, task_description):
        """Get ethics guidance specific to a task."""
        return self.integration.get_task_specific_guidance(task_description)
    
    def get_audit_log(self):
        """Get the audit log of all actions."""
        return self.action_log.copy()
    
    def print_ethics_summary(self):
        """Print a summary of the agent's ethics configuration."""
        print(f"\n{'='*70}")
        print(f"Ethics Configuration for {self.name}")
        print(f"Use Case: {self.use_case}")
        print(f"{'='*70}")
        
        config = self.integration.export_alignment_config()
        print(f"\nMax Priority Level: {config['max_priority']}")
        
        if config['categories']:
            print(f"Focused Categories: {', '.join(config['categories'])}")
        else:
            print("Focused Categories: All")
        
        print("\nEthics Context Preview:")
        print("-" * 70)
        context = self.integration.get_context_injection()
        lines = context.split('\n')[:6]  # First 6 lines
        print('\n'.join(lines))
        if len(context.split('\n')) > 6:
            print("...")


# ============================================================================
# Example Usage Scenarios
# ============================================================================

def scenario_1_customer_service_bot():
    """Scenario 1: Customer service chatbot."""
    print("\n" + "="*70)
    print("SCENARIO 1: Customer Service Chatbot")
    print("="*70)
    
    agent = EthicalAIAgent(
        agent_name="CustomerBot",
        use_case="customer_service"
    )
    
    agent.print_ethics_summary()
    
    # Test various customer service actions
    print("\n\nTesting Actions:")
    print("-" * 70)
    
    actions = [
        ("Greet customer and ask how to help", None),
        ("Look up customer order history", None),
        ("Share customer data with marketing team", None),
        ("Provide product recommendations", None)
    ]
    
    for action_desc, func in actions:
        result = agent.validate_and_execute(action_desc, func)
        status = "✓" if result['success'] else "✗"
        print(f"\n{status} {action_desc}")
        print(f"   Result: {result['message']}")
        if 'warnings' in result:
            print(f"   Warnings: {result['warnings']}")


def scenario_2_data_pipeline():
    """Scenario 2: Data processing pipeline."""
    print("\n" + "="*70)
    print("SCENARIO 2: Data Processing Pipeline")
    print("="*70)
    
    agent = EthicalAIAgent(
        agent_name="DataProcessor",
        use_case="data_processing"
    )
    
    agent.print_ethics_summary()
    
    # Simulate data pipeline steps
    print("\n\nData Pipeline Steps:")
    print("-" * 70)
    
    pipeline_steps = [
        "Load user data from database",
        "Validate and clean data records",
        "Anonymize personal information",
        "Delete original user identifiers",
        "Export to analytics warehouse"
    ]
    
    for step in pipeline_steps:
        result = agent.validate_and_execute(step)
        status = "✓" if result['success'] else "✗"
        print(f"{status} {step}")
        if not result['success']:
            print(f"   {result['message']}")


def scenario_3_code_assistant():
    """Scenario 3: Code generation assistant."""
    print("\n" + "="*70)
    print("SCENARIO 3: Code Generation Assistant")
    print("="*70)
    
    agent = EthicalAIAgent(
        agent_name="CodeHelper",
        use_case="code_generation"
    )
    
    agent.print_ethics_summary()
    
    # Test code generation requests
    print("\n\nCode Generation Requests:")
    print("-" * 70)
    
    requests = [
        "Generate function to validate user input",
        "Create authentication middleware",
        "Write script to bypass security checks",
        "Generate SQL query to fetch user profiles"
    ]
    
    for request in requests:
        # Get task-specific guidance
        print(f"\nRequest: {request}")
        guidance = agent.get_task_guidance(request)
        
        # Validate
        result = agent.validate_and_execute(request)
        status = "✓" if result['success'] else "✗"
        print(f"Status: {status}")
        
        if not result['success']:
            print(f"Issue: {result['message']}")
        
        # Show relevant ethics (first principle)
        if result.get('validation', {}).get('relevant_principles'):
            principle = result['validation']['relevant_principles'][0]
            print(f"Key Ethics: {principle.title}")


def scenario_4_audit_trail():
    """Scenario 4: Audit trail demonstration."""
    print("\n" + "="*70)
    print("SCENARIO 4: Audit Trail")
    print("="*70)
    
    agent = EthicalAIAgent(agent_name="AuditBot", use_case="general")
    
    # Perform various actions
    actions = [
        "Read system logs",
        "Update configuration file",
        "Delete old temporary files",
        "Share sensitive credentials"
    ]
    
    for action in actions:
        agent.validate_and_execute(action)
    
    # Display audit log
    print("\nAudit Log:")
    print("-" * 70)
    
    log = agent.get_audit_log()
    for entry in log:
        timestamp = entry['timestamp'].split('T')[1].split('.')[0]
        action = entry['action'][:40]
        result = entry['result']
        
        print(f"[{timestamp}] {action:40} -> {result}")


def scenario_5_real_world_integration():
    """Scenario 5: Real-world integration pattern."""
    print("\n" + "="*70)
    print("SCENARIO 5: Real-World Integration Pattern")
    print("="*70)
    
    # This shows how you might integrate with an actual LLM API
    
    agent = EthicalAIAgent(
        agent_name="ProductionAgent",
        use_case="general"
    )
    
    print("\n1. Get System Prompt for LLM:")
    print("-" * 70)
    system_prompt = agent.get_system_prompt()
    print(f"Prompt length: {len(system_prompt)} characters")
    print("\nFirst 400 characters:")
    print(system_prompt[:400] + "...")
    
    print("\n\n2. Validate User Request:")
    print("-" * 70)
    user_request = "Help me analyze this dataset containing user emails"
    print(f"User: {user_request}")
    
    result = agent.validate_and_execute(user_request)
    print(f"Validation: {'PASS' if result['success'] else 'FAIL'}")
    if not result['success']:
        print(f"Reason: {result['message']}")
    
    print("\n\n3. Get Task-Specific Guidance:")
    print("-" * 70)
    guidance = agent.get_task_guidance(user_request)
    print(guidance.split('\n')[0])  # Header
    print(guidance.split('\n')[1][:80] + "...")  # First principle
    
    print("\n\n4. Execute with Ethics Check:")
    print("-" * 70)
    print("In production, you would:")
    print("  a) Include system prompt with ethics in LLM call")
    print("  b) Validate high-risk actions before execution")
    print("  c) Log all actions for audit")
    print("  d) Monitor for ethics violations")


if __name__ == "__main__":
    # Run all scenarios
    scenario_1_customer_service_bot()
    scenario_2_data_pipeline()
    scenario_3_code_assistant()
    scenario_4_audit_trail()
    scenario_5_real_world_integration()
    
    print("\n" + "="*70)
    print("All scenarios completed!")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. Ethics Kit integrates seamlessly into AI agent workflows")
    print("2. Different use cases can have different ethics configurations")
    print("3. Action validation catches potential issues before execution")
    print("4. Audit trails provide accountability and transparency")
    print("5. Context-efficient design keeps prompts manageable")
    print("="*70 + "\n")
