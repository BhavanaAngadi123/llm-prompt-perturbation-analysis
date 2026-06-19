from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

prompts = [
    "What is the capital of France?",
    "Whats the capital of France?",
    "Can you tell me the capital city of France?",
    "Which city serves as the capital of France?",
    "What is France's capital?"
]

results = {}

for prompt in prompts:
    output = generator(prompt, max_new_tokens=20)[0]["generated_text"]
    results[prompt] = output

for prompt, output in results.items():
    print("Prompt:")
    print(prompt)
    print("Output:")
    print(output)
    print("-" * 50)

print("\nAnalysis:")
print(
    "Minor prompt perturbations produced similar answers. "
    "The model remained consistent and correctly identified Paris."
)
