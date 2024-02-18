from transformers import pipeline

# Load the T5 model
summarizer = pipeline("summarization", model="t5-base")

# Read text from a file
with open("trans.txt", "r") as f:
    text = f.read()

# Generate the summary
summary = summarizer(text, max_length=130, min_length=30)

# Save the summary to a new text file
with open("summary.txt", "w") as f:
    f.write(summary[0]['summary_text'])

print("Summary generated and saved to summary.txt")
