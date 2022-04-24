from tkinter import W
import pandas as pd
import numpy as  np 
import json

def json_to_df(json_file):
    array_for_df = []
    for data in json_file['data']:
        title = data['title']
        for paragraph in data['paragraphs']:
            context = paragraph['context']
            for question_dict in paragraph['qas']:
                question = question_dict['question']
                if(len(question)<2):
                    continue
                id = question_dict['id']
                is_impossible = question_dict['is_impossible']
                for answer_dict in question_dict['answers']:
                    answer = answer_dict['text']
                    answer_start = answer_dict['answer_start']
                    record = {
                        "id":id,
                        "title": title,
                        "context": context,
                        "question": question,
                        "answer": answer,
                        "answer_start": answer_start,
                        "is_impossible": is_impossible
                    }
                    array_for_df.append(record)
    df = pd.DataFrame(array_for_df)
    return df

if __name__ == '__main__':

    init_path = r'C:\Users\prasr\Documents\Northeastern\Sem2\Stanford Question Answering Dataset - PROJECT\Question-Answering-model'
    raw_train_data_path =  init_path + r'\data\raw\train-v2.0.json'
    raw_dev_data_path =  init_path + r'\data\raw\dev-v2.0.json'

    interim_path = init_path + r'\data\interim'

    with open(raw_train_data_path) as f:
        data = json.load(f)
    train_df = json_to_df(data)
    # train_df.to_csv(interim_path+r'\train_data.csv')
    print('Finished with train')

    with open(raw_dev_data_path) as f:
        data = json.load(f) 
    val_df = json_to_df(data) 
    val_df.to_csv(interim_path+r'\val_data.csv')
    print('Finished with Val data')



