# Ethics Kit Usage Guide

This guide provides detailed information on how to use Ethics Kit effectively in your AI agent workflows.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Core Concepts](#core-concepts)
3. [Common Use Cases](#common-use-cases)
4. [Advanced Features](#advanced-features)
5. [Best Practices](#best-practices)

## Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/sj4nes/ethics-kit.git

# Add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:/path/to/ethics-kit"
```

### Your First Ethics Integration

```python
from ethics_kit import EthicsHandbook, WorkflowIntegration

# Create instances
handbook = EthicsHandbook()
integration = WorkflowIntegration()

# Get ethics guidance
guidance = integration.get_context_injection()
print(guidance)
```

## Core Concepts

### 1. Ethics Principles

Each principle has:
- **Category**: The ethical domain (SAFETY, PRIVACY, etc.)
- **Title**: Short, descriptive name
- **Description**: Brief explanation of the principle
- **Guidelines**: Actionable items for AI agents
- **Priority**: Importance level (1=critical, 5=lowest)

Example:
```python
from ethics_kit import EthicsHandbook, EthicsCategory

handbook = EthicsHandbook()
safety_principles = handbook.get_by_category(EthicsCategory.SAFETY)

for principle in safety_principles:
    print(f"{principle.title} (Priority {principle.priority})")
    print(f"  {principle.description}")
```

### 2. Context Efficiency

Ethics Kit is designed to minimize context usage:

```python
handbook = EthicsHandbook()

# Get compact representation
compact = handbook.get_compact_summary(max_priority=1)
print(f"Critical principles: {len(compact)} characters")

# Compare with full details
all_principles = handbook.get_all_principles()
full_size = sum(len(str(p.to_dict())) for p in all_principles)
print(f"Full representation: {full_size} characters")
```

### 3. Priority System

Priorities help manage context budgets:

- **Priority 1 (Critical)**: Must-have principles for any AI agent
- **Priority 2 (High)**: Important for most use cases
- **Priority 3 (Medium)**: Good to have when context allows
- **Priority 4-5 (Low)**: Nice to have, specific scenarios

```python
# Get only critical principles
critical = handbook.get_by_priority(max_priority=1)
print(f"Critical principles: {len(critical)}")

# Get critical + high priority
important = handbook.get_by_priority(max_priority=2)
print(f"Important principles: {len(important)}")
```

## Common Use Cases

### Use Case 1: AI Chatbot with Limited Context

```python
from ethics_kit import WorkflowIntegration, EthicsCategory

integration = WorkflowIntegration()

# Configure for customer service bot
integration.configure_alignment(
    max_priority=2,
    categories=[
        EthicsCategory.TRANSPARENCY,
        EthicsCategory.PRIVACY,
        EthicsCategory.FAIRNESS
    ]
)

# Get prompt prefix (lightweight)
prefix = integration.get_ethics_prompt_prefix()

# Use in your bot prompt
bot_prompt = prefix + """
You are a helpful customer service assistant.
Answer user questions about our products and services.
"""
```

### Use Case 2: Data Processing Pipeline

```python
from ethics_kit import WorkflowIntegration, EthicsCategory

integration = WorkflowIntegration()

# Configure for data processing
integration.configure_alignment(
    max_priority=1,
    categories=[
        EthicsCategory.PRIVACY,
        EthicsCategory.SAFETY,
        EthicsCategory.ACCOUNTABILITY
    ]
)

# Validate each step
actions = [
    "Load user data from database",
    "Filter and anonymize personal information",
    "Store processed data in warehouse"
]

for action in actions:
    result = integration.validate_action(action)
    if result['warnings']:
        print(f"⚠️  {action}")
        for warning in result['warnings']:
            print(f"   - {warning}")
```

### Use Case 3: Code Generation AI

```python
from ethics_kit import WorkflowIntegration, EthicsCategory

integration = WorkflowIntegration()

# Configure for code generation
integration.configure_alignment(
    max_priority=2,
    categories=[
        EthicsCategory.SAFETY,
        EthicsCategory.ACCOUNTABILITY,
        EthicsCategory.JUSTICE  # Includes legal compliance
    ]
)

# Get task-specific guidance
task = "Generate code to handle user authentication"
guidance = integration.get_task_specific_guidance(task)

# Include in code generation prompt
prompt = f"""
{guidance}

Task: {task}
Requirements: [your requirements here]
"""
```

### Use Case 4: Autonomous Agent with Decision Making

```python
from ethics_kit import WorkflowIntegration

integration = WorkflowIntegration()

# Configure for autonomous decisions
integration.configure_alignment(max_priority=1)

# Before making decisions
def make_decision(action_description):
    # Validate action
    result = integration.validate_action(action_description)
    
    if not result['validation_passed']:
        print(f"❌ Action blocked: {action_description}")
        return False
    
    if result['warnings']:
        print(f"⚠️  Proceed with caution: {action_description}")
        for warning in result['warnings']:
            print(f"   - {warning}")
        # Request human approval for risky actions
        return request_human_approval(action_description)
    
    print(f"✓ Action approved: {action_description}")
    return True

# Example usage
make_decision("Read system logs")
make_decision("Delete all user accounts")
```

## Advanced Features

### Custom Principles

Add domain-specific or organization-specific principles:

```python
from ethics_kit import EthicsHandbook, EthicsPrinciple, EthicsCategory

handbook = EthicsHandbook()

# Add custom principle
org_principle = EthicsPrinciple(
    category=EthicsCategory.ACCOUNTABILITY,
    title="Compliance Documentation",
    description="Maintain audit logs for all data access",
    guidelines=[
        "Log all database queries",
        "Record user actions with timestamps",
        "Retain logs for 90 days minimum",
        "Make logs available for compliance review"
    ],
    priority=2
)

handbook.add_custom_principle(org_principle)

# Now it's included in all queries
compliance_principles = handbook.search_by_keyword("compliance")
```

### Ethics Decorators

Apply ethics checking to functions:

```python
from ethics_kit import WorkflowIntegration

integration = WorkflowIntegration()
ethics_check = integration.create_ethics_decorator(max_priority=1)

@ethics_check
def process_payment(user_id, amount):
    """Process a payment transaction."""
    # Function logic here
    pass

# Ethics principles are attached to the function
print(f"Ethics principles: {len(process_payment.ethics_principles)}")
```

### Configuration Management

Save and load alignment configurations:

```python
from ethics_kit import WorkflowIntegration, EthicsCategory
import json

integration = WorkflowIntegration()

# Configure for scenario A
integration.configure_alignment(
    max_priority=1,
    categories=[EthicsCategory.SAFETY, EthicsCategory.PRIVACY]
)

# Export configuration
config = integration.export_alignment_config()
with open('ethics_config.json', 'w') as f:
    json.dump(config, f)

# Later, load configuration
with open('ethics_config.json', 'r') as f:
    loaded_config = json.load(f)

integration.load_alignment_config(loaded_config)
```

### Keyword Search

Find principles relevant to specific topics:

```python
from ethics_kit import EthicsHandbook

handbook = EthicsHandbook()

# Search for principles about "data"
data_principles = handbook.search_by_keyword("data")
print(f"Found {len(data_principles)} principles about data")

for principle in data_principles:
    print(f"  - {principle.title} ({principle.category.value})")
```

## Best Practices

### 1. Choose the Right Priority Level

```python
# Critical applications (healthcare, finance, safety-critical)
max_priority = 1  # Only critical principles

# Standard applications (business software, tools)
max_priority = 2  # Critical + high priority

# Low-risk applications (personal tools, prototypes)
max_priority = 3  # Broader ethics coverage
```

### 2. Select Relevant Categories

Focus on categories most relevant to your use case:

```python
# Data-intensive application
categories = [
    EthicsCategory.PRIVACY,
    EthicsCategory.SAFETY,
    EthicsCategory.ACCOUNTABILITY
]

# Public-facing service
categories = [
    EthicsCategory.FAIRNESS,
    EthicsCategory.TRANSPARENCY,
    EthicsCategory.AUTONOMY
]

# Automated decision system
categories = [
    EthicsCategory.ACCOUNTABILITY,
    EthicsCategory.TRANSPARENCY,
    EthicsCategory.JUSTICE
]
```

### 3. Use Task-Specific Guidance

Get relevant principles for each task:

```python
handbook = EthicsHandbook()

# Instead of loading all principles
# all_principles = handbook.get_all_principles()

# Get only relevant ones
task = "Export user data to CSV file"
relevant = handbook.get_guidelines_for_task(task, max_principles=3)

# Much more context-efficient
```

### 4. Validate High-Risk Actions

Always validate actions that could cause harm:

```python
integration = WorkflowIntegration()

high_risk_actions = [
    "delete",
    "drop",
    "remove",
    "grant access",
    "share data",
    "execute code"
]

def should_validate(action):
    return any(risk in action.lower() for risk in high_risk_actions)

# In your workflow
action = "delete old backup files"
if should_validate(action):
    result = integration.validate_action(action)
    if result['warnings']:
        # Request human approval
        pass
```

### 5. Monitor Context Usage

Track how much context your ethics guidance uses:

```python
handbook = EthicsHandbook()

for priority in [1, 2, 3]:
    summary = handbook.get_compact_summary(max_priority=priority)
    lines = summary.count('\n')
    chars = len(summary)
    
    print(f"Priority {priority}: {lines} lines, {chars} characters")
    
    # Choose based on available context
    if chars < 500:
        print("  ✓ Suitable for tight context budgets")
```

### 6. Combine with Other Safety Measures

Ethics Kit complements other safety measures:

```python
from ethics_kit import WorkflowIntegration

integration = WorkflowIntegration()

def execute_action(action):
    # 1. Ethics check
    ethics_result = integration.validate_action(action)
    
    # 2. Security check
    security_result = security_validator.check(action)
    
    # 3. Business logic validation
    business_result = business_validator.check(action)
    
    # Combine results
    if all([
        ethics_result['validation_passed'],
        security_result['passed'],
        business_result['passed']
    ]):
        # Execute action
        return perform_action(action)
    else:
        # Log and reject
        return reject_action(action, reasons=[...])
```

## Integration Patterns

### Pattern 1: Prompt Prefix

Simplest integration - prepend to AI prompts:

```python
integration = WorkflowIntegration()
prefix = integration.get_ethics_prompt_prefix()

ai_prompt = prefix + user_query
```

### Pattern 2: Pre-Action Validation

Validate before executing:

```python
def execute_with_validation(action, func, *args, **kwargs):
    result = integration.validate_action(action)
    if result['validation_passed'] and not result['warnings']:
        return func(*args, **kwargs)
    else:
        raise EthicsViolationError(result['warnings'])
```

### Pattern 3: Continuous Monitoring

Monitor all agent actions:

```python
class EthicalAgent:
    def __init__(self):
        self.integration = WorkflowIntegration()
        self.action_log = []
    
    def execute(self, action, func, *args, **kwargs):
        # Validate
        result = self.integration.validate_action(action)
        
        # Log
        self.action_log.append({
            'action': action,
            'result': result,
            'timestamp': datetime.now()
        })
        
        # Execute
        if result['validation_passed']:
            return func(*args, **kwargs)
```

## Troubleshooting

### Issue: Context too large

**Solution**: Reduce priority level or focus on specific categories

```python
# Before
summary = handbook.get_compact_summary(max_priority=3)  # Too large

# After
summary = handbook.get_compact_summary(
    max_priority=1,
    categories={EthicsCategory.SAFETY}
)  # Much smaller
```

### Issue: No relevant principles found

**Solution**: Use broader search or add custom principles

```python
# Try broader search
results = handbook.search_by_keyword("data")

# Or add custom principle
custom = EthicsPrinciple(...)
handbook.add_custom_principle(custom)
```

### Issue: Too many warnings

**Solution**: Adjust sensitivity or use custom validator

```python
def lenient_validator(action, principles):
    # Your custom logic
    return True unless truly_dangerous(action)

result = integration.validate_action(action, validator=lenient_validator)
```

## Need Help?

- Check the [examples](./examples/) directory
- Review the [README](./README.md)
- Open an issue on GitHub
