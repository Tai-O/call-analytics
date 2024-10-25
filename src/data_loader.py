import os
import spacy


def read_transcripts(directory):
    transcripts = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            try:
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    content = file.read()
                    transcripts.append(content)
            except Exception as e:
                print(f"Error reading {filename}: {str(e)}")
    return transcripts




def extract_member_lines(transcripts):
    return [line for transcript in transcripts for line in transcript.split('\n') 
            if 'Member:' in line]



def dynamic_document_chunking(text, max_chunk_size=500, nlp=None):
    if nlp is None:
        nlp = spacy.load('en_core_web_sm')
    
    doc = nlp(text)
    chunks = []
    current_chunk = []
    current_size = 0

    for sent in doc.sents:
        if current_size + len(sent.text) > max_chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sent.text]
            current_size = len(sent.text)
        else:
            current_chunk.append(sent.text)
            current_size += len(sent.text)
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks
