# Sentiment Analysis using VADER

This script analyzes the sentiment of a given text using the VADER (Valence Aware Dictionary and sEntiment Reasoner) Sentiment Analyzer.

## Requirements

- Python 3.x
- VADER Sentiment Analyzer (`pip install vaderSentiment`)

## Usage

1. **Install Dependencies**: Ensure you have the `vaderSentiment` package installed.

   ```bash
   pip install vaderSentiment
   
2. **Run the Script**: Update the text variable in the script with the text you want to analyze.

   ```bash
   python your_script_name.py

3. **Output**: The script will return the sentiment scores, which include:

* **Positive**: Proportion of positive sentiment.
* **Negative**: Proportion of negative sentiment.
* **Neutral**: Proportion of neutral sentiment.
* **Compound**: Overall sentiment score, ranging from -1 (most negative) to 1 (most positive).

## License

MIT License
