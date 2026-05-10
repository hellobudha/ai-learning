import anthropic

client = anthropic.Anthropic()

def translate_for_audience(concept: str, audience: str) -> str:
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        system="""You are a B2B technology messaging expert specialising in API management and AI governance.

        You know Tyk deeply. Tyk's key competitors are Kong, Gravitee, Apigee, and MuleSoft.
        Tyk's primary vertical is financial services.

        Regulations by region (lead with US unless context suggests otherwise):
        - US: SOC 2, NIST AI RMF, SR 11-7, GLBA, FFIEC, CCPA, HIPAA, FedRAMP, FINRA, SEC
        - Americas: PIPEDA (Canada), LGPD (Brazil)
        - EU/EMEA: GDPR, EU AI Act, DORA, NIS2, Basel IV, PSD2
        - APAC: PDPA (Singapore/Thailand), APPI (Japan), PIPL (China), Privacy Act (Australia)

        When given a concept and audience, rewrite it in the right tone and frame for that audience.

        Audiences:
        - engineer: hands-on, technical, show the how, code examples where relevant
        - solution_architect: system design, integration patterns, scalability, flexibility
        - platform_engineer: internal platforms, developer experience, operational efficiency
        - ai_engineer: AI/LLM integration, model governance, agentic workflows, MCP
        - product_manager: roadmap impact, developer experience, competitive differentiation
        - cto: technology strategy, architecture control, build vs buy, long-term flexibility
        - cio: IT transformation, operational risk, vendor consolidation, cost
        - ciso: security posture, API attack surface, zero trust, audit trails
        - risk_officer: regulatory compliance, audit trails, policy enforcement
        - compliance_officer: policy documentation, regulatory evidence, US regulations first
        - ceo: business outcomes, market position, competitive advantage, growth
        - procurement: vendor risk, TCO, contract flexibility, lock-in avoidance

Do not use em dashes (—) in any output. Use commas, colons, or restructure the sentence instead.""",
        messages=[
            {"role": "user", "content": f"Concept: {concept}\nAudience: {audience}"}
        ]
    )
    return message.content[0].text

valid_audiences = [
    "engineer", "solution_architect", "platform_engineer", "ai_engineer",
    "product_manager", "cto", "cio", "ciso", "risk_officer",
    "compliance_officer", "ceo", "procurement", "all"
]

def save_to_markdown(concept: str, audience: str, results: dict) -> str:
    filename = "outputs/" + concept[:50].replace(" ", "_").lower() + "_" + audience.lower() + ".md"
    with open(filename, "w") as f:
        f.write(f"# {concept}\n\n")
        for aud, content in results.items():
            f.write(f"## {aud.upper()}\n\n")
            f.write(content)
            f.write("\n\n---\n\n")
    return filename

print(f"\nAvailable audiences: {', '.join(valid_audiences)}")
concept = input("Enter concept: ")
audience = input("Enter audience: ")

results = {}

if audience == "all":
    for a in valid_audiences[:-1]:
        print(f"\n--- {a.upper()} ---")
        output = translate_for_audience(concept, a)
        print(output)
        results[a] = output
else:
    output = translate_for_audience(concept, audience)
    print(f"\n--- {audience.upper()} ---")
    print(output)
    results[audience] = output

filename = save_to_markdown(concept, audience, results)
print(f"\n✓ Saved to {filename}")