# Text Summarization Script

## Overview

This Python script performs text summarization using a frequency-based approach. It reads an input text, processes it to remove noise, calculates word frequencies, scores sentences based on word frequencies, and then generates a summary of the text by selecting the most relevant sentences.

## Features

- **Text Preprocessing**: Cleans the input text by removing references, non-alphabetic characters, and extra spaces.
- **Word Frequency Calculation**: Computes the frequency of each word and normalizes it.
- **Sentence Scoring**: Scores sentences based on the frequency of words contained in them.
- **Summary Generation**: Selects and outputs the top 5 sentences to form a concise summary.

## Requirements

- Python 3.x
- NLTK (Natural Language Toolkit)

To install the required Python libraries, you can use the following command:
```bash
pip install nltk
```

## Setup

1. **Download NLTK Resources**:
   Ensure you have the necessary NLTK resources installed. Run the following Python commands:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

2. **Script Execution**:
   Save the script to a file, for example, `text_summarizer.py`.

## How to Use

1. **Run the Script**:
   Execute the script from the command line:
   ```bash
   python text_summarizer.py
   ```

2. **Enter the Input Text**:
   When prompted, enter the text you want to summarize. For example:
   ```
   Artificial Intelligence (AI) has rapidly evolved over the past few decades, transforming various industries and aspects of daily life. From virtual assistants like Siri and Alexa to advanced algorithms used in healthcare for diagnosing diseases, AI technologies are increasingly integrated into our lives. The applications of AI extend to areas such as autonomous vehicles, where self-driving cars use AI to navigate and make real-time decisions. In finance, AI is employed for fraud detection and algorithmic trading, improving the efficiency of financial operations. Despite its advancements, AI also raises ethical concerns, including issues related to privacy, job displacement, and decision-making transparency. As AI continues to develop, it is crucial to address these concerns and ensure that the technology is used responsibly.
   ```

3. **View the Summary**:
   The script will output the summarized text, which includes the top 5 most relevant sentences from the input text.

## Code Explanation

1. **Text Preprocessing**:
   - Removes references (e.g., `[1]`), non-alphabetic characters, and extra spaces.
   - Tokenizes the text into sentences and words.

2. **Word Frequency Calculation**:
   - Computes and normalizes the frequency of each word.

3. **Sentence Scoring**:
   - Scores each sentence based on the frequency of its constituent words, considering only sentences with fewer than 20 words.

4. **Summary Generation**:
   - Selects the top 5 sentences with the highest scores and joins them to create a summary.

## Example

Given the input text:

```
Artificial Intelligence (AI) has rapidly evolved over the past few decades, transforming various industries and aspects of daily life. From virtual assistants like Siri and Alexa to advanced algorithms used in healthcare for diagnosing diseases, AI technologies are increasingly integrated into our lives. The applications of AI extend to areas such as autonomous vehicles, where self-driving cars use AI to navigate and make real-time decisions. In finance, AI is employed for fraud detection and algorithmic trading, improving the efficiency of financial operations. Despite its advancements, AI also raises ethical concerns, including issues related to privacy, job displacement, and decision-making transparency. As AI continues to develop, it is crucial to address these concerns and ensure that the technology is used responsibly.
```

The script may output:

```
Summarized text: Artificial Intelligence (AI) has rapidly evolved over the past few decades, transforming various industries and aspects of daily life. The applications of AI extend to areas such as autonomous vehicles, where self-driving cars use AI to navigate and make real-time decisions. In finance, AI is employed for fraud detection and algorithmic trading, improving the efficiency of financial operations. Despite its advancements, AI also raises ethical concerns, including issues related to privacy, job displacement, and decision-making transparency.
```

## Contributing

Feel free to contribute to this project by suggesting improvements or submitting pull requests.

## License

This project is licensed under the  GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

---
