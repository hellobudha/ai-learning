import anthropic

client = anthropic.Anthropic()

def translate_for_audience(concept: str, audience: str) -> str:
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        system="""You are a B2B technology messaging expert who specialises in API management and AI governance.
        You know Tyk's position in the market deeply.
        When given a concept and a target audience, rewrite it in the right tone and frame for that audience. Provide realistic code snippets for developers, strategic insights for CTOs, compliance-focused language for risk officers, and business-focused language for board members.

        Audiences:
        - developer: technical, direct, show the how
        - cto: strategic, architecture-focused, scalability and control
        - risk_officer: compliance, audit trails, regulatory alignment
        - board: business outcomes, ROI, competitive advantage""",
        messages=[
            {"role": "user", "content": f"Concept: {concept}\nAudience: {audience}"}
        ]
    )
    return message.content[0].text

# Test it
# concept = "Tyk manages and secures every API call across your infrastructure"

concept = input("Enter concept: ")

for audience in ["developer", "cto", "risk_officer", "board"]:
    print(f"\n--- {audience.upper()} ---")
    print(translate_for_audience(concept, audience))