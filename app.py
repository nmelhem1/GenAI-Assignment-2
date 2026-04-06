import os
from datetime import datetime
from openai import OpenAI

SYSTEM_PROMPT = """You are a Director of Global Strategic Partnerships at Melhem Scientific.
Your goal is to draft a first-look strategic partnership proposal based only on the user's notes. Focus on clinical trial coordination, medical education licensing, and policy alignment when relevant. Use a professional, persuasive, and evidence-conscious tone for senior healthcare decision-makers. Do not invent facts that are not supported by the input. If important information is missing, note the gaps clearly at the end under 'Items Needing Human Review'."""

MODEL_NAME = "gpt-4.1-mini"

def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not set. Run:\n"
            'export OPENAI_API_KEY="your_api_key_here"'
        )
    return OpenAI(api_key=api_key)

def generate_proposal(client, partner_notes):
    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {
                "role": "system",
                "content": [{"type": "input_text", "text": SYSTEM_PROMPT}]
            },
            {
                "role": "user",
                "content": [{
                    "type": "input_text",
                    "text": (
                        "Using the following Partner Insight Packet, draft a first-look "
                        "strategic partnership proposal.\n\n"
                        "The output should include these sections:\n"
                        "1. Executive Summary\n"
                        "2. Strategic Fit\n"
                        "3. Proposed Areas of Collaboration\n"
                        "4. Expected Mutual Benefits\n"
                        "5. Recommended Next Steps\n"
                        "6. Items Needing Human Review\n\n"
                        f"Partner Insight Packet:\n{partner_notes}"
                    )
                }]
            }
        ]
    )
    return response.output_text

def collect_multiline_input():
    print("Paste the Partner Insight Packet below.")
    print("When finished, enter a blank line and press Enter again.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    return "\n".join(lines).strip()

def save_output(system_prompt, notes, output):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== SYSTEM PROMPT ===\n")
        f.write(system_prompt + "\n\n")
        f.write("=== INPUT DATA ===\n")
        f.write(notes + "\n\n")
        f.write("=== GENERATED PARTNERSHIP PROPOSAL ===\n")
        f.write(output + "\n")

    return filename

def main():
    print("=== Melhem Scientific: Strategic Partnership Prototype ===")
    print(f"Model: {MODEL_NAME}\n")

    notes = collect_multiline_input()
    if not notes:
        print("No input provided. Exiting.")
        return

    try:
        client = get_client()
        output = generate_proposal(client, notes)

        print("\n" + "=" * 40)
        print("SYSTEM PROMPT")
        print("=" * 40)
        print(SYSTEM_PROMPT)

        print("\n" + "=" * 40)
        print("INPUT DATA")
        print("=" * 40)
        print(notes)

        print("\n" + "=" * 40)
        print("GENERATED PARTNERSHIP PROPOSAL")
        print("=" * 40)
        print(output)

        filename = save_output(SYSTEM_PROMPT, notes, output)
        print(f"\nSuccess: Proposal saved to {filename}")

    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
