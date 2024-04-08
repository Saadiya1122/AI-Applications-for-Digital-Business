import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(job_description, resumes):
    vectorizer = TfidfVectorizer()
    resume_tfidf = vectorizer.fit_transform(resumes)
    job_description_tfidf = vectorizer.transform([job_description])
    similarity_scores = cosine_similarity(job_description_tfidf, resume_tfidf)
    return similarity_scores[0]


def rank_resumes(job_description, resumes):
    resumes_df = pd.DataFrame({'Resume': resumes})
    similarity_scores = calculate_similarity(
        job_description, resumes_df['Resume'])
    
    similarity_scores_formatted = ['{:.2f}%'.format(score * 100) for score in similarity_scores]

    results_df = pd.DataFrame({
        'Resume': resumes_df['Resume'],
        'Similarity Score': similarity_scores_formatted
    })

    results_df = results_df.drop_duplicates(subset=['Resume'])
    results_df = results_df.sort_values(by='Similarity Score', ascending=False)
    return results_df


