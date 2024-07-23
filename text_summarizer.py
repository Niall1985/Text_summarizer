import fitz 
import nltk
import spacy
from transformers import pipeline
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nlp = spacy.load("en_core_web_sm")

def text_extraction(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    return text


def extractive_summarizer(text, num_sentences=3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english') + list(punctuation))
    words = [word for word in words if word not in stop_words]
    word_frequencies = Counter(words)
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = ' '.join(summarized_sentences)
    return summary

def abstractive_summarizer(text):
    summarizer = pipeline('summarization')
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def main():
    pdf_path = "C:\\Users\\Niall Dcunha\\Desktop\\Transfered from ASUS\\SIRE 2.0 BRD Niall D'cunha.pdf"

    text = text_extraction(pdf_path)

    extractive_summary = extractive_summarizer(text)
    print("Extractive summary:\n", extractive_summary)

    print("\n")
    abstractive_summary = abstractive_summarizer(text)
    print("Abstractive summary:\n", abstractive_summary)


if __name__ == "__main__":
    main()