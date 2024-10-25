import pyLDAvis
import pyLDAvis.gensim_models
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaMulticore


def prepare_tokens(texts, nlp, removal_pos=['ADV','PRON','CCONJ','PUNCT','PART','DET','ADP','SPACE', 'NUM', 'SYM']):
    tokens = []
    for doc in nlp.pipe(texts):
        doc_tokens = [token.lemma_.lower() for token in doc 
                     if token.pos_ not in removal_pos 
                     and not token.is_stop 
                     and token.is_alpha]
        tokens.append(doc_tokens)
    return tokens



def create_lda_model(tokens, num_topics=10):
    dictionary = Dictionary(tokens)
    dictionary.filter_extremes(no_below=5, no_above=0.5, keep_n=1000)
    corpus = [dictionary.doc2bow(doc) for doc in tokens]
    
    model = LdaMulticore(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        workers=10,
        passes=10,
        iterations=50
    )
    
    return model, corpus, dictionary