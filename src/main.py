from tokenizer import BPE
import argparse

def main():
    parser = argparse.ArgumentParser(description='Byte Pair Encoding (BPE) tokenizer')
    # Add command-line arguments (parameters)
    parser.add_argument('--text', type=str, default="../alice.txt", help='Input file path')
    parser.add_argument('--merge_no', type=int, default=50, help='Output file path')
    parser.add_argument('--encode', type=str, help='encode the input text into subwords')
    parser.add_argument('--decode', help='decode the id back into the original text')
    args = parser.parse_args() # Store parameter values in args instance
    
    with open(args.text, 'r', encoding='utf-8') as f:
        text = f.read()
    tokenizer_obj = BPE()
    tokenizer_obj.train(text, args.merge_no) # Train the BPE model on the input text and merge numbers
    if args.encode:
        tokens, ids = tokenizer_obj.encode_sentence(args.encode)
        print('Encoded:', tokens)
        print('IDs:', ids)
    if args.decode:
        decoded_text = tokenizer_obj.decode_ids(args.decode)
        print('Decoded:', decoded_text)
        
 