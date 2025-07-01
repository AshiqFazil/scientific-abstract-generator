
from rouge_score import rouge_scorer
from sacrebleu import corpus_bleu

def compute_rouge(predictions, references):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = [scorer.score(ref, pred) for ref, pred in zip(references, predictions)]
    return {
        "rouge1": sum([s['rouge1'].fmeasure for s in scores]) / len(scores),
        "rougeL": sum([s['rougeL'].fmeasure for s in scores]) / len(scores)
    }

def compute_bleu(predictions, references):
    refs = [[ref] for ref in references]
    return corpus_bleu(predictions, refs).score
