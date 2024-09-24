"""
This module processes text using Natural Language Processing techniques.
"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download required NLTK data
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

def process_text(text: str) -> str:
    """
    Process the input text by tokenizing, POS tagging, and applying simple capitalization rules.
    
    Args:
        text (str): The input text to be processed.
    
    Returns:
        str: The processed text with proper capitalization.
    """
    # Tokenize the input text
    tokens = word_tokenize(text)
    
    # Perform part-of-speech tagging
    tagged = pos_tag(tokens)
    
    # Apply simple capitalization rules
    processed_tokens = []
    capitalize_next = True
    for word, _ in tagged:
        if capitalize_next:
            word = word.capitalize()
            capitalize_next = False
        if word in '.!?':
            capitalize_next = True
        processed_tokens.append(word)
    
    # Join the processed tokens back into a string
    return ' '.join(processed_tokens)

if __name__ == "__main__":
    sample_text = "hello world. how are you? this is a test."
    processed_text = process_text(sample_text)
    print(f"Original: {sample_text}")
    print(f"Processed: {processed_text}")