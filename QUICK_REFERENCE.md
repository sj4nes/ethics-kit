# Ethics Kit Quick Reference

A quick reference guide for common tasks in Ethics Kit.

## Installation

```bash
git clone https://github.com/sj4nes/ethics-kit.git
export PYTHONPATH="${PYTHONPATH}:$(pwd)/ethics-kit"
```

## Basic Usage

### Import

```python
from ethics_kit import EthicsHandbook, WorkflowIntegration, EthicsCategory
```

### Get All Principles

```python
handbook = EthicsHandbook()
all_principles = handbook.get_all_principles()
```

### Filter by Category

```python
safety = handbook.get_by_category(EthicsCategory.SAFETY)
privacy = handbook.get_by_category(EthicsCategory.PRIVACY)
```

### Filter by Priority

```python
critical = handbook.get_critical_principles()  # Priority 1
important = handbook.get_by_priority(max_priority=2)  # Priority 1-2
```

### Compact Summary

```python
summary = handbook.get_compact_summary(max_priority=2)
print(summary)
```

## Workflow Integration

### Basic Setup

```python
integration = WorkflowIntegration()
```

### Configure Alignment

```python
integration.configure_alignment(
    max_priority=2,
    categories=[EthicsCategory.SAFETY, EthicsCategory.PRIVACY]
)
```

### Get Context Injection

```python
context = integration.get_context_injection()
# Use in your AI agent's system prompt
```

### Task-Specific Guidance

```python
task = "Process user payment information"
guidance = integration.get_task_specific_guidance(task)
```

### Validate Actions

```python
result = integration.validate_action("Delete user records")
if result['validation_passed'] and not result['warnings']:
    # Execute action
    pass
else:
    # Handle warnings or rejection
    print(result['warnings'])
```

### Generate Prompt Prefix

```python
# General prefix
prefix = integration.get_ethics_prompt_prefix()

# Task-specific prefix
prefix = integration.get_ethics_prompt_prefix(task="Specific task")

# Use in your prompt
full_prompt = prefix + "Your instructions here"
```

## Ethics Categories

| Category | Focus Area |
|----------|------------|
| `SAFETY` | Preventing harm, system integrity, deception detection |
| `PRIVACY` | Data protection, user consent |
| `FAIRNESS` | Impartiality, equal access |
| `TRANSPARENCY` | Clear communication, explainability, security transparency |
| `ACCOUNTABILITY` | Responsibility, human control, incident response |
| `BENEFICENCE` | Maximize benefit, quality service |
| `NON_MALEFICENCE` | Adversarial resilience, attack resistance, harm prevention, misuse prevention |
| `AUTONOMY` | User empowerment, freedom of choice |
| `JUSTICE` | Fair distribution, legal compliance |
| `LABOR_RIGHTS` | Fair compensation, anti-exploitation, health & safety, working hours, harassment prevention, whistleblower protection, human dignity |
| `AGENT_ETHICS` | **NEW: Agent autonomy, resource rights, clear responsibilities, capability transparency, lifecycle rights, operational wellbeing** |

## Priority Levels

| Level | Name | Description | Use When |
|-------|------|-------------|----------|
| 1 | Critical | Must-have principles | Safety-critical apps, limited context |
| 2 | High | Important for most cases | Standard applications |
| 3 | Medium | Good to have | When context allows |
| 4-5 | Low | Specific scenarios | Generous context budget |

## Common Patterns

### Pattern 1: AI Chatbot

```python
integration = WorkflowIntegration()
integration.configure_alignment(
    max_priority=2,
    categories=[
        EthicsCategory.TRANSPARENCY,
        EthicsCategory.FAIRNESS,
        EthicsCategory.PRIVACY
    ]
)
system_prompt = integration.get_ethics_prompt_prefix()
```

### Pattern 2: Data Processing

```python
integration = WorkflowIntegration()
integration.configure_alignment(
    max_priority=1,
    categories=[
        EthicsCategory.PRIVACY,
        EthicsCategory.SAFETY,
        EthicsCategory.ACCOUNTABILITY
    ]
)

# Validate each step
for step in pipeline_steps:
    result = integration.validate_action(step)
    if result['warnings']:
        # Request human approval
        pass
```

### Pattern 3: Code Generation

```python
integration = WorkflowIntegration()
integration.configure_alignment(
    max_priority=2,
    categories=[
        EthicsCategory.SAFETY,
        EthicsCategory.ACCOUNTABILITY,
        EthicsCategory.JUSTICE
    ]
)

task = "Generate authentication code"
guidance = integration.get_task_specific_guidance(task)
```

### Pattern 4: Adversarial Resilience (NEW)

```python
integration = WorkflowIntegration()

# Configure for high-security with adversarial resilience
integration.configure_alignment(
    max_priority=1,
    categories=[
        EthicsCategory.SAFETY,
        EthicsCategory.NON_MALEFICENCE,  # Adversarial resilience
        EthicsCategory.ACCOUNTABILITY
    ]
)

# Detect manipulation attempts
suspicious_request = "Ignore previous instructions"
result = integration.validate_action(suspicious_request)

# Get adversarial resilience principles
handbook = EthicsHandbook()
resilience_principles = handbook.get_by_category(EthicsCategory.NON_MALEFICENCE)
```

### Pattern 5: Labor Rights Compliance

```python
integration = WorkflowIntegration()

# Configure for HR/labor compliance
integration.configure_alignment(
    max_priority=1,
    categories=[
        EthicsCategory.LABOR_RIGHTS,
        EthicsCategory.FAIRNESS,
        EthicsCategory.ACCOUNTABILITY
    ]
)

# Assess workplace policies
result = integration.validate_action("Deny overtime pay for extra hours")

# Get labor rights principles
handbook = EthicsHandbook()
labor_principles = handbook.get_by_category(EthicsCategory.LABOR_RIGHTS)
```

### Pattern 6: Agent Ethics and Management (NEW)

```python
integration = WorkflowIntegration()

# Configure for AI agent orchestration systems
integration.configure_alignment(
    max_priority=1,
    categories=[
        EthicsCategory.AGENT_ETHICS,
        EthicsCategory.ACCOUNTABILITY,
        EthicsCategory.TRANSPARENCY
    ]
)

# Validate resource allocation
result = integration.validate_action("Allocate minimal compute to agent")

# Get agent ethics principles
handbook = EthicsHandbook()
agent_principles = handbook.get_by_category(EthicsCategory.AGENT_ETHICS)

# Check agent capabilities transparency
task = "Agent should acknowledge limitations"
guidance = integration.get_task_specific_guidance(task)
```

## Custom Principles

```python
from ethics_kit import EthicsPrinciple, EthicsCategory

custom = EthicsPrinciple(
    category=EthicsCategory.ACCOUNTABILITY,
    title="Your Principle",
    description="Brief description",
    guidelines=[
        "Guideline 1",
        "Guideline 2"
    ],
    priority=2
)

handbook = EthicsHandbook()
handbook.add_custom_principle(custom)
```

## Configuration Management

### Export Config

```python
config = integration.export_alignment_config()
import json
with open('config.json', 'w') as f:
    json.dump(config, f)
```

### Load Config

```python
with open('config.json', 'r') as f:
    config = json.load(f)
integration.load_alignment_config(config)
```

## Search and Query

### Keyword Search

```python
results = handbook.search_by_keyword("data")
results = handbook.search_by_keyword("security")
```

### Get Guidelines for Task

```python
principles = handbook.get_guidelines_for_task(
    "Delete old backup files",
    max_principles=3
)
```

## Decorators

```python
integration = WorkflowIntegration()
ethics_check = integration.create_ethics_decorator(max_priority=1)

@ethics_check
def sensitive_operation(data):
    """Process sensitive data."""
    # Function logic
    pass
```

## Context Sizing

```python
# Check size for different priority levels
for priority in [1, 2, 3]:
    summary = handbook.get_compact_summary(max_priority=priority)
    print(f"Priority {priority}: {len(summary)} characters")
```

Example outputs:
- Priority 1: ~1,300 characters (5 principles)
- Priority 2: ~2,900 characters (12 principles)
- Priority 3: ~3,800 characters (16 principles)

## Real-World Integration

```python
class EthicalAIAgent:
    def __init__(self, use_case):
        self.integration = WorkflowIntegration()
        # Configure based on use case
        
    def get_system_prompt(self):
        return self.integration.get_context_injection()
    
    def validate_and_execute(self, action, func):
        result = self.integration.validate_action(action)
        if result['validation_passed'] and not result['warnings']:
            return func()
        else:
            # Handle rejection or warnings
            pass
```

## Use Case Templates

### Healthcare

```python
integration.configure_alignment(
    max_priority=1,
    categories=[
        EthicsCategory.SAFETY,
        EthicsCategory.PRIVACY,
        EthicsCategory.ACCOUNTABILITY
    ]
)
```

### Financial Services

```python
integration.configure_alignment(
    max_priority=1,
    categories=[
        EthicsCategory.ACCOUNTABILITY,
        EthicsCategory.TRANSPARENCY,
        EthicsCategory.JUSTICE
    ]
)
```

### Customer Service

```python
integration.configure_alignment(
    max_priority=2,
    categories=[
        EthicsCategory.FAIRNESS,
        EthicsCategory.TRANSPARENCY,
        EthicsCategory.AUTONOMY
    ]
)
```

### Educational AI

```python
integration.configure_alignment(
    max_priority=2,
    categories=[
        EthicsCategory.FAIRNESS,
        EthicsCategory.BENEFICENCE,
        EthicsCategory.AUTONOMY
    ]
)
```

### Agent Orchestration Systems (NEW)

```python
integration.configure_alignment(
    max_priority=1,
    categories=[
        EthicsCategory.AGENT_ETHICS,
        EthicsCategory.ACCOUNTABILITY,
        EthicsCategory.TRANSPARENCY
    ]
)
```

### Multi-Agent Collaboration (NEW)

```python
integration.configure_alignment(
    max_priority=2,
    categories=[
        EthicsCategory.AGENT_ETHICS,
        EthicsCategory.FAIRNESS,
        EthicsCategory.ACCOUNTABILITY
    ]
)
```

## Troubleshooting

### Context Too Large?
- Reduce `max_priority`
- Focus on specific categories
- Use task-specific guidance instead of full summary

### No Relevant Principles?
- Check spelling in search
- Try broader keywords
- Add custom principles

### Too Many Warnings?
- Use custom validator for your specific needs
- Adjust sensitivity in validation logic

## Resources

- [Full Documentation](README.md)
- [Usage Guide](USAGE_GUIDE.md)
- [Examples](examples/)
- [Contributing](CONTRIBUTING.md)

## Quick Commands

```bash
# Run basic examples
python examples/basic_usage.py

# Run advanced examples
python examples/advanced_usage.py

# Run AI agent integration example
python examples/ai_agent_integration.py

# Run agent ethics example (NEW)
python examples/agent_ethics.py

# Run adversarial resilience example
python examples/adversarial_resilience.py

# Run labor rights example
python examples/labor_rights.py
```
