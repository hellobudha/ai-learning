import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "In one sentence, what is the most important thing API management and AI have in common?"}
    ]
)

print(message.content[0].text)