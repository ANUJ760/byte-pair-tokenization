## byte-pair-tokenization
*Implementation of BPE tokenization algorithm from scratch (without tiktoken).*  


🌟 A BPE Tokenizer used in LLMs
-> A more optimised version is used by OpenAI for gpt models!
This one is a minimal implementation of the algorithm. This project provides a demonstration of the core principles of subword tokenization, which is a crucial first step for all modern language models.

I've used an AI assistant to handle the more tedious parts of development, like syntactical cleanup and text preprocessing, allowing me to focus entirely on the algorithmic approach and core logic of the BPE algorithm itself.

🚀 What's Inside
tokenizer.py: The heart of the project, containing the BPE class with methods for training, encoding, and decoding.

main.py: A simple command-line interface client to interact with the tokenizer.

💡 Why BPE?
BPE is a technique that creates a vocabulary of subword units (like "ing" or "tion") by iteratively merging the most frequent pairs of characters in a text. This approach solves two major problems: it handles new or complex words by breaking them down into familiar parts, and it keeps the vocabulary size manageable. It's a solution to a fundamental problem in AI.

A simpler way to use this algorithm is through the tiktoken library, which is the more widely used implementation, as it does not require "from scratch" and implementaions and focuses on outputs.