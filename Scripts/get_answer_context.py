from nltk.tokenize import sent_tokenize

def get_answer_context(df):
    length_context = 0
    answer = ""

    for sentence in sent_tokenize(df.context):
        length_context += len(sentence) + 1
        if df.answer_start <= length_context:
            if len(sentence) >= len(str(df.answer)):
                if answer == "":
                    return sentence
                else:
                    return answer + " " + sentence
            else:
                answer += sentence

df['entire_answer_text'] = df.apply(lambda row: get_answer_context(row), axis = 1)