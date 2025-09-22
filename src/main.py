import argparse
from tokenizer import BPE
import re # regex for cleaning text

def main():
    parser = argparse.ArgumentParser(description="Minimal BPE Tokenizer")
    parser.add_argument("--text", type=str, default="../alice.txt", help="path to input file")
    parser.add_argument("--merges", type=int, default=50, help="number of merges")
    parser.add_argument("--encode", type=str, help="text to encode")
    parser.add_argument("--decode", nargs='+', type=int, help="pids to decode")
    parser.add_argument("--save", action="store_true", help="save output to output.txt")
    args = parser.parse_args()

    with open(args.text, "r", encoding="utf-8") as f:
        text = f.read()

   
    #Replacing non-alphnumeric characters with a space
    text_cleaned = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    
    text_cleaned = text_cleaned.lower() #Convert to lowercase for consistent tokenization
    #Replace multiple spaces with a single space
    text_cleaned = re.sub(r'\s+', ' ', text_cleaned).strip() # strip leading and trailing spaces

    tokenizer = BPE()
    
    tokenizer.train(text_cleaned, args.merges)

    outputs = [] # an empty list initialised to store the output of encoding and decoding

    if args.encode:
        #for encoding, the input text should also be cleaned to match the training one
        encode_text_cleaned = re.sub(r'[^a-zA-Z0-9\s]', ' ', args.encode).lower()
        encode_text_cleaned = re.sub(r'\s+', ' ', encode_text_cleaned).strip()
        
        tokens, ids = tokenizer.encode_sentence(encode_text_cleaned)
        outputs.append(f"Encoded tokens: {tokens}")
        outputs.append(f"Encoded ids: {ids}")

    if args.decode:
        text = tokenizer.decode(args.decode)
        outputs.append(f"Decoded text: {text}")

    result = "\n".join(outputs)
    print(result)

    if args.save:
        with open("../output.txt", "w", encoding="utf-8") as f:
            f.write(result)

if __name__ == "__main__":
    main()