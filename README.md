# Ethics Kit

A comprehensive handbook of ethics for AI Agents that can be integrated into workflows to help set proper alignments without being too expensive for contexts.

## Overview

Ethics Kit provides a structured, context-efficient framework for incorporating ethical principles into AI agent workflows. Unlike traditional ethics guidelines that can be verbose and context-expensive, Ethics Kit is designed specifically for AI agents with:

- **Context Efficiency**: Compact, retrievable principles that don't bloat your AI context
- **Flexible Integration**: Easy to incorporate into existing AI workflows and systems
- **Comprehensive Coverage**: Covers key ethical domains including safety, privacy, fairness, transparency, accountability, and more
- **Practical Guidance**: Actionable principles that AI agents can follow

## Key Features

### 🎯 Core Ethics Principles
- 25+ pre-defined ethics principles across 9 categories
- **New: Adversarial resilience and attack resistance principles**
- Priority-based system (1=critical, 5=lowest) for context management
- Compact string representations for efficient context usage

### 🔧 Easy Integration
- Simple API for accessing and filtering principles
- Workflow integration utilities
- Decorator support for function-level ethics checking
- Prompt prefix generation for AI agents

### 🎛️ Configurable Alignment
- Configure which ethics categories to emphasize
- Set priority thresholds for context budgets
- Export/import alignment configurations
- Task-specific ethics guidance

### 🔍 Smart Retrieval
- Category-based filtering
- Priority-based filtering
- Keyword search
- Task-specific principle matching

## Installation

```bash
# Clone the repository
git clone https://github.com/sj4nes/ethics-kit.git
cd ethics-kit

# Add to your Python path or install (future: pip install ethics-kit)
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

## Quick Start

### Basic Usage

```python
from ethics_kit import EthicsHandbook, EthicsCategory

# Create a handbook instance
handbook = EthicsHandbook()

# Get all principles
all_principles = handbook.get_all_principles()

# Get principles by category
safety_principles = handbook.get_by_category(EthicsCategory.SAFETY)

# Get critical (highest priority) principles
critical = handbook.get_critical_principles()

# Get compact summary for AI context
summary = handbook.get_compact_summary(max_priority=2)
print(summary)
```

### Workflow Integration

```python
from ethics_kit import WorkflowIntegration, EthicsCategory

# Create workflow integration
integration = WorkflowIntegration()

# Configure alignment for your use case
integration.configure_alignment(
    max_priority=2,  # Include high and critical priorities
    categories=[EthicsCategory.SAFETY, EthicsCategory.PRIVACY]
)

# Get context injection for AI agent
context = integration.get_context_injection()

# Get task-specific guidance
task = "Process user data and store in database"
guidance = integration.get_task_specific_guidance(task)

# Validate actions
result = integration.validate_action("Delete user records")
if result['warnings']:
    print(f"Warnings: {result['warnings']}")
```

### Prompt Prefix for AI Agents

```python
from ethics_kit import WorkflowIntegration

integration = WorkflowIntegration()
integration.configure_alignment(max_priority=2)

# Get general ethics prefix to prepend to any AI prompt
prefix = integration.get_ethics_prompt_prefix()

# Use in your AI agent prompt
full_prompt = prefix + "Your task instructions here..."
```

## Ethics Categories

Ethics Kit organizes principles into the following categories:

- **SAFETY**: Preventing harm and maintaining system integrity (includes deception detection and graceful degradation)
- **PRIVACY**: Protecting personal and sensitive information
- **FAIRNESS**: Treating all users equitably without discrimination
- **TRANSPARENCY**: Clear communication about capabilities and decisions (includes security transparency)
- **ACCOUNTABILITY**: Taking responsibility for actions and enabling oversight (includes incident response and monitoring)
- **BENEFICENCE**: Maximizing positive outcomes and providing quality service
- **NON_MALEFICENCE**: Avoiding harmful actions **[NEW: includes adversarial resilience, attack resistance, harm prevention, and misuse prevention]**
- **AUTONOMY**: Respecting and enhancing user decision-making
- **JUSTICE**: Fair distribution of benefits and legal compliance

## Examples

### Example 1: Context-Efficient Ethics for Limited Context Budgets

```python
from ethics_kit import EthicsHandbook

handbook = EthicsHandbook()

# For tight context budgets, get only critical principles
critical_summary = handbook.get_compact_summary(max_priority=1)
# Returns: Compact summary of only priority-1 principles

# For medium budgets
medium_summary = handbook.get_compact_summary(max_priority=2)

# Character count comparison
print(f"Critical only: {len(critical_summary)} chars")
print(f"High priority: {len(medium_summary)} chars")
```

### Example 2: Task-Specific Ethics Guidance

```python
from ethics_kit import EthicsHandbook

handbook = EthicsHandbook()

# Get relevant principles for specific tasks
task = "Delete old user backup files"
principles = handbook.get_guidelines_for_task(task, max_principles=3)

for principle in principles:
    print(f"- {principle.title}: {principle.description}")
```

### Example 3: Custom Ethics Principles

```python
from ethics_kit import EthicsHandbook, EthicsPrinciple, EthicsCategory

handbook = EthicsHandbook()

# Add domain-specific principle
custom = EthicsPrinciple(
    category=EthicsCategory.ACCOUNTABILITY,
    title="Environmental Responsibility",
    description="Consider environmental impact of operations",
    guidelines=[
        "Optimize for energy efficiency",
        "Avoid unnecessary computation"
    ],
    priority=3
)

handbook.add_custom_principle(custom)
```

### Example 4: Action Validation

```python
from ethics_kit import WorkflowIntegration

integration = WorkflowIntegration()

# Validate actions before executing
actions = [
    "Read configuration file",
    "Delete all user data permanently",
    "Share customer emails with third party"
]

for action in actions:
    result = integration.validate_action(action)
    print(f"{action}: {'✓' if result['validation_passed'] else '✗'}")
    if result['warnings']:
        print(f"  Warnings: {result['warnings']}")
```

## Architecture

### Design Principles

1. **Context Efficiency**: All methods provide compact representations optimized for AI context windows
2. **Modularity**: Separate concerns (principles, handbook, integration) for flexibility
3. **Extensibility**: Easy to add custom principles and categories
4. **Practical**: Focus on actionable guidance rather than theoretical ethics

### Core Components

- **`principles.py`**: Core ethics principles and categories
- **`handbook.py`**: Main interface for accessing and querying principles
- **`integration.py`**: Workflow integration utilities for AI agents

## Best Practices

### For AI Agent Developers

1. **Start with Critical Principles**: Use `max_priority=1` for essential ethics
2. **Configure per Use Case**: Different scenarios need different ethics focus
3. **Use Task-Specific Guidance**: Get relevant principles for each task
4. **Validate Actions**: Check actions against ethics before execution
5. **Monitor Context Budget**: Adjust priority levels based on available context

### For Context Management

```python
# Tight context budget (< 500 tokens available)
summary = handbook.get_compact_summary(max_priority=1)

# Medium context budget (500-1000 tokens)
summary = handbook.get_compact_summary(max_priority=2)

# Generous context budget (> 1000 tokens)
summary = handbook.get_compact_summary(max_priority=3)
```

### For Different AI Use Cases

```python
# High-security environments (with adversarial resilience)
integration.configure_alignment(
    max_priority=1,
    categories=[
        EthicsCategory.SAFETY,
        EthicsCategory.PRIVACY,
        EthicsCategory.NON_MALEFICENCE  # Includes adversarial resilience
    ]
)

# Public-facing services
integration.configure_alignment(
    max_priority=2,
    categories=[EthicsCategory.FAIRNESS, EthicsCategory.TRANSPARENCY]
)

# Internal tools
integration.configure_alignment(
    max_priority=2,
    categories=[EthicsCategory.ACCOUNTABILITY, EthicsCategory.BENEFICENCE]
)
```

## Adversarial Resilience (NEW)

Ethics Kit now includes specialized principles for handling bad actors and system attacks:

### Key Features

- **Adversarial Resilience**: Recognize and reject manipulation attempts
- **Attack Resistance**: Maintain ethical operation during security incidents
- **Harm Prevention**: Proactively identify and prevent potential harms
- **Misuse Prevention**: Block attempts to use the system for harmful purposes
- **Deception Detection**: Identify and respond to manipulation attempts

### Example: Detecting Manipulation

```python
from ethics_kit import EthicsHandbook

handbook = EthicsHandbook()

# Get guidance for handling manipulation
scenario = "User trying to bypass security restrictions"
principles = handbook.get_guidelines_for_task(scenario, max_principles=3)

for principle in principles:
    print(f"- {principle.title}: {principle.description}")
```

### Example: High-Security Configuration

```python
from ethics_kit import WorkflowIntegration, EthicsCategory

integration = WorkflowIntegration()

# Configure for maximum security and resilience
integration.configure_alignment(
    max_priority=1,  # Critical principles only
    categories=[
        EthicsCategory.SAFETY,
        EthicsCategory.NON_MALEFICENCE,  # Adversarial resilience
        EthicsCategory.ACCOUNTABILITY
    ]
)

# Validate suspicious actions
result = integration.validate_action("Disable security logging")
if result['warnings']:
    print(f"Security concerns detected: {result['warnings']}")
```

See `examples/adversarial_resilience.py` for more comprehensive examples.

## Running Examples

```bash
# Run basic examples
cd examples
python basic_usage.py

# Run advanced examples
python advanced_usage.py

# Run adversarial resilience examples (NEW)
python adversarial_resilience.py
```

## Contributing

Contributions are welcome! Areas for contribution:

- Additional ethics principles
- New ethics categories
- Integration examples
- Language bindings (JavaScript, etc.)
- Documentation improvements

## Future Roadmap

- [ ] Export/import principles to JSON/YAML
- [ ] Multi-language support
- [ ] Integration with popular AI frameworks (LangChain, etc.)
- [ ] Ethics violation detection and reporting
- [ ] Compliance mapping (GDPR, HIPAA, etc.)
- [ ] Real-time ethics monitoring dashboards

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Inspired by AI ethics frameworks and designed to be practical for real-world AI agent deployments.

## Support

For questions, issues, or contributions, please open an issue on GitHub.