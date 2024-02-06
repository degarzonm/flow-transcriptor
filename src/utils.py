import os

def format_and_print(transcript, word_confidences):
    """Formats and prints the transcript and word confidences."""
    words = [word for word, _ in word_confidences]
    confidences = [str(conf) for _, conf in word_confidences]

    # Calculate the maximum length of each word for alignment
    max_length = max(len(word) for word in words) if words else 0

    # Format and print the transcript
    formatted_transcript = ' '.join(word.ljust(max_length) for word in words)
    formatted_confidences = ' '.join(conf.ljust(max_length) for conf in confidences)

    if formatted_transcript:
        print("T:"+formatted_transcript)
        print("C:"+formatted_confidences)
    