# LLM Prompt Perturbation Analysis

This project explores how minor prompt perturbations affect the output of an open-source LLM.

## Base Prompt

What is the capital of France?

## Perturbed Prompts

1. Whats the capital of France?
2. Can you tell me the capital city of France?
3. Which city serves as the capital of France?
4. What is France's capital?

## Model Used

google/flan-t5-small

## Analysis

The outputs remained consistent across all prompt variations. Minor wording changes and typographical variations did not significantly affect the model's output. The model consistently identified Paris as the capital of France.

## Output

Base Prompt Output:
Paris

Perturbed Prompt Outputs:
Paris
Paris
Paris
Paris
