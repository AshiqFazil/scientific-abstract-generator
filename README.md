
## Scientific Abstract Generator

The **Scientific Abstract Generator** is an AI-powered web application that helps researchers and students generate high-quality scientific abstracts automatically based on the paper title, keywords, and research domain.

This project combines modern Natural Language Processing (NLP) techniques with a simple and intuitive web interface to make the process of drafting scientific abstracts faster, more consistent, and accessible to everyone.

---

### About the Project

This project is built for academic and research communities, especially:

* Researchers drafting initial abstracts.
* Students writing academic papers.
* Technical writers and journal editors who want to explore AI-assisted content.

The system is built to:

* Generate abstracts using a trained sequence-to-sequence language model (T5).
* Preprocess and clean text data before training to improve quality.
* Evaluate generated abstracts using metrics like ROUGE and BLEU.
* Provide an interactive web interface to generate and view abstracts instantly.

---

### Features

* **AI-based generation**: Uses a fine-tuned T5 model to create coherent, domain-relevant abstracts.
* **Clean text preprocessing**: Removes stop words, punctuation, and normalizes text.
* **Evaluation metrics**: Automatically computes ROUGE and BLEU scores to validate model quality.
* **User-friendly web interface**: Enter title, keywords, and domain to generate an abstract instantly.
* **Copy and share**: Copy generated abstracts for further editing and inclusion.
* **Word count**: See how long your abstract is immediately.

---

### Technologies Used

* **Python**: Main programming language.
* **PyTorch & Transformers**: For model training and inference.
* **Pandas & NumPy**: Data handling and processing.
* **NLTK & spaCy**: Natural language preprocessing.
* **Flask & Flask-CORS**: Backend web server and API.
* **HTML, CSS, JavaScript**: Frontend interface.
* **Evaluation libraries**: ROUGE and SacreBLEU for quality checking.
* **Other utilities**: tqdm, python-dotenv, and others.

---

### How It Works

1. **Preprocessing**: Raw scientific titles and abstracts are cleaned and normalized.
2. **Model training**: A sequence-to-sequence model (T5) is fine-tuned on processed data.
3. **Evaluation**: Generated abstracts are evaluated with ROUGE and BLEU metrics.
4. **Web interface**: Users can enter a paper title, keywords, and domain; the backend serves the generated abstract.

---

### Installation & Running

1. **Clone the repository**:

```bash
git clone <repository-url>
cd scientific-abstract-generator
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Download required NLP resources**:

```python
import nltk
nltk.download('stopwords')
python -m spacy download en_core_web_sm
```

4. **Preprocess data**:

```bash
python scripts/preprocess.py
```

5. **Train the model**:

```bash
python scripts/train_model.py
```

6. **Evaluate the model**:

```bash
python scripts/evaluate_model.py
```

7. **Run the web app**:

```bash
python scripts/web_app.py
```

Open your browser and visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### Usage

* Enter the paper title, relevant keywords (comma-separated), and select a research domain.
* Click **Generate Abstract**.
* The system returns an AI-generated abstract, displays word count, and allows you to copy the text.

---
