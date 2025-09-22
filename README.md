<p align="center">
  <img src="gdg_b.webp" alt="logo" width="100">
</p>

<h1 align="center">Byte Pair Tokenizer</h1>

---

*Implementation of the BPE tokenization algorithm from scratch (without tiktoken).*  

🌟 **A BPE Tokenizer used in LLMs**  
👉 A more optimized version is used by OpenAI for GPT models!  
This project is a **minimal implementation** of the algorithm, designed to **demonstrate the core principles of subword tokenization**—a crucial foundation for all modern language models.  

I used an AI assistant to handle repetitive tasks (like syntactical cleanup and text preprocessing), so I could focus entirely on the **algorithmic design and core logic** of the BPE algorithm itself.  

---

## 🚀 What’s Inside
- **`tokenizer.py`** → The heart of the project, containing the `BPE` class with methods for training, encoding, and decoding.  
- **`main.py`** → A simple CLI client to interact with the tokenizer.  

---

## 💡 Why BPE?
**Byte Pair Encoding (BPE)** creates a vocabulary of **subword units** (like *"ing"* or *"tion"*) by iteratively merging the most frequent pairs of characters in a text.  

✅ Benefits:  
- Handles **new or complex words** by breaking them into familiar sub-parts  
- Keeps the **vocabulary size manageable**  
- A **fundamental solution** for tokenizing language in AI  

  Drawbacks of this implementation:
- Cannot handle special characters (eg ! , % $)  
- Not an optimal implementation, slow, uses </w> for end of word, but cannot differentiate if "</w>"  is a part of data text.
- Not suited for very large datasets (ie actual requirments)
  
---

## ⚡ Notes
- A simpler way to use this algorithm in real-world projects is via [**tiktoken**](https://github.com/openai/tiktoken), OpenAI’s optimized implementation.  
- This repo focuses on a **from-scratch educational approach**, so you can truly understand how BPE works under the hood.  

---

<p align="center">
  Made using Python
</p>
