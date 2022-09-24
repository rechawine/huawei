#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : process_data.py
# @Desc    : KnowledgeSelection生成的result数据不能直接作为Generation的预测集合，因此需要本代码对其格式进行处理
import json


def main():
    input_file = open('../KnowledgeSelection/result.json', 'r', encoding='utf8')
    data = json.load(input_file)
    print(len(data))

    formatted_data = []
    for item in data.items():
        history = []
        speaker = "U"
        for sent in item[1]['context']:
            history.append({"speaker": f"{speaker}",
                            "text": sent})
            speaker = "S" if speaker == "U" else "U"

        formatted_data.append({"history": history,
                               "response": "",
                               "knowledge": item[1]['attrs'],
                               "dialog_id": eval(item[0])})

    output_file = open('data/test/data.json', 'w', encoding='utf8')
    json.dump(formatted_data, fp=output_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()