# Markdown to Alpaca formatted JSON

My input files will be in the form of markdown. For fine tuning purposes, I'd like to turn this into a JSON file in alpaca format.

The question is, how do we do that?

```json
[
    {
        "instruction": "Some instruction",
        "input": "Some additional context",
        "output": "The expected output"
    }
]
```

How can I create something like this dynamically, without resulting essentially to using an LLM to train an LLM.

For example, given:

```md
## Data Vs Information

**Data** are a collection of raw facts, measurements or statitistics, often used as a foundation for reasoning, discussion or calculation to produce information.

**Information** is data that has been processed and changed into a meaningful and useful form for interpretation.
i.e: Information is data that has been contextualized via processess such as aggregation, manipulation and organization.


Information is affect by:

- Time (Timeliness, Currency, Frequency)
- Content (Accuracy, Relevance, Completeness)
- Form (Clarity, Detail, Order, Presentation)
```

And turning it into something like:

```json
[
    {
        "instruction": "Tell me about {Data Vs Information}",
        "input": "",
        "output": "Data are a collection of raw facts, measurements or statistics..."
    }
]
```

I intentionally structure all of my notes to have sensible headings in a hierarchy that I believed would be easy too read and interpret, but I guess I won't really know until further testing.

The idea, is that for an instruction, we can have a pre-prompt, alongside the heading title, but the key will be ensuring that the hierarchy is still semantically sensible.

In other words, given:

```md
## Database Architectures & Major Types of Databases.

...

### Centralized

...

### Distributed

...

### Transactional vs Decision Supposrt Systems.

...

## Types of Databases

...
```

I'd like to establish a hierarchy like:

```json
{
    "Database Architecture & Major Types of Databases": {
        "content": "some content",
        "children": [
            {
                "Centralized": {
                    "content": "some other content",
                    "children": []
                }
            },
            {
                "Distributed": {
                    "content": "Then some other content",
                    "children": []
                }
            }
        ]
    },
    "Types of Databases": {
        "content": "Last set of content",
        "children": []
    }
}
```

Then using this hierarchy, I can maybe provide additional context for the alpaca json. For example:

```json
[
    {
        "instruction": "Give me information about {Database Architecture & Major Types of Databasees}",
        "input": "{Centralized, Distributed}",
        "output": "{content}"
    }
]
```
