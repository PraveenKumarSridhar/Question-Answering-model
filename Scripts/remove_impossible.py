from tkinter import W
import pandas as pd
import numpy as  np 
import json

def clean_impossible(json_file):
    for data in json_file['data']:
        for paragraph in data['paragraphs']:
            answerable_dicts = []
            for index,question_dict in enumerate(paragraph['qas']):
                if question_dict['is_impossible'] == False:
                    answerable_dicts.append(question_dict)
            paragraph['qas'] = answerable_dicts
    return json_file

if __name__ == '__main__':

    init_path = r'C:\Users\prasr\Documents\Northeastern\Sem2\Stanford Question Answering Dataset - PROJECT\Question-Answering-model'
    raw_train_data_path =  init_path + r'\data\raw\train-v2.0.json'
    raw_dev_data_path =  init_path + r'\data\raw\dev-v2.0.json'

    interim_path = init_path + r'\data\interim'
    with open(raw_dev_data_path) as f:
        data = json.load(f)
    data = clean_impossible(data)
    with open(interim_path+'\dev_impossible_removed.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4) 




