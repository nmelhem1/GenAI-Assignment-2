# Homework 2 Report: Strategic Research Partnership Proposal Workflow

## Business Use Case

For this assignment, I built a generative AI workflow for drafting first-look strategic partnership proposals in a healthcare research context.

In this scenario, a Director of Global Strategic Partnerships receives a short “Partner Insight Packet” containing rough notes about a potential partner institution, its goals, and its needs. The system transforms these notes into a polished first-pass proposal that can be reviewed and refined by a human decision-maker before external use.

This workflow targets high-stakes partnership development, which often involves repetitive, structured writing tasks. By automating the initial draft, leadership teams can save time, ensure a consistent proposal structure (e.g., Executive Summary, Strategic Fit, Proposed Areas of Collaboration, Expected Mutual Benefits, Recommended Next Steps), and respond to opportunities faster.

---

## Model Choice

I chose **gpt-4.1-mini** (accessed via the OpenAI API) as the foundation for this prototype.

I selected this model because it is cost-effective for repeated testing, easy to integrate into a Python script, and capable of generating polished, professionally structured writing. Since my goal was to demonstrate a stable, reproducible workflow and improve it through prompt iteration, I focused on one model rather than formally comparing multiple providers.

---

## Baseline vs. Final Design Comparison

Iterative prompt design was crucial for grounding the model’s outputs in the provided facts rather than allowing it to confidently hallucinate.

### Baseline

The initial system prompt asked the model to generate a professional, evidence-conscious proposal without inventing unsupported facts. While the output was polished, the model still introduced unsupported assumptions.

For example, it described Melhem Scientific as having “extensive regional expertise,” “regulatory knowledge,” and “licensed education programs,” even though none of these details were included in the input. This blurred the line between fact and inference.

---

### Revision 1

I introduced explicit rules restricting the model to only use information provided in the input and clarified that Melhem Scientific should be described as a **potential** partner rather than an established capability.

This improved factual grounding and made the tone more cautious. However, the model still used somewhat assertive phrasing, such as stating the company was “positioned to support” and had the “capability to engage” with regional ecosystems.

---

### Final Design (Revision 2)

The final revision introduced stricter anti-hallucination constraints. I explicitly prohibited inventing capabilities, partnerships, or regulatory expertise, and required cautious language such as “may,” “could,” or “potentially” when information was uncertain.

Most importantly, I added an escalation rule: if the input suggests ethical concerns, legal risks, or data-integrity issues, the system should not generate a persuasive proposal and instead flag the case for urgent human review.

This version performed best. It reduced unsupported assumptions, handled uncertainty more honestly, and clearly separated known information from unknown variables through a structured **“Items Needing Human Review”** section.

---

## Where the Prototype Still Fails or Requires Human Review

Even with a strict prompt, this prototype should not operate independently.

The main remaining limitation is a persistent tendency toward persuasive inference. For example, the final output still occasionally implies general expertise (e.g., “understanding of the Middle Eastern healthcare landscape”) even when not explicitly supported by the input.

More importantly, the system cannot verify regulatory facts, legal constraints, institution-specific capabilities, or cross-border compliance requirements. These are critical in healthcare partnerships and cannot be delegated to a language model.

Therefore, the system should be treated strictly as a drafting assistant, not a fact-checker or decision-maker.

---

## Deployment Recommendation

I would not recommend deploying this system for fully automated external use.

However, I do recommend deploying it as an internal first-draft assistant for partnership teams, under strict controls.

A safe deployment requires:

1. A constrained prompt with strong anti-hallucination rules  
2. A stable evaluation set that includes edge and failure cases  
3. Mandatory human validation before any external communication  
4. Automatic escalation for ethically sensitive or high-risk scenarios  

With these human-in-the-loop safeguards, the workflow can significantly improve efficiency and consistency. Without them, the risk of generating persuasive but unsupported claims—especially in a healthcare context—is too high.
