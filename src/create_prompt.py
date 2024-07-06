from pathlib import Path

import json

def read_dataset():
    dataset_path = "./data/jmmlu_high_school_computer_science.json"
    with Path(dataset_path).open() as f:
        dataset = json.load(f)

    return dataset


def examples_to_alpaca(example: dict[str, str]) -> str:
    prompt = ""
    prompt += "### 問題\n" + example["input"] + "\n\n"
    prompt += "### 答え\n" + example["output"] + "\n\n"
    return prompt


def create_instruction():
    dataset = read_dataset()
    default_instruction: str = dataset["instruction"]
    examples: list[dict[str, str]] = dataset["samples"][:5]
    insruction = f"""\
次のテキストは問題の指示文・問題・答えです。指示文が適切でない場合、'A.認証'のように記号以外を含む回答が散見されます。
現在使用中の指示文は以下の通りです。

### 指示文
{default_instruction}

次の問題に最適な指示文を5つ考えてください。\n\n---\n\n"""
    insruction += "$問題の指示文\n\n"
    for example in examples:
        insruction += examples_to_alpaca(example=example)
    print(insruction)
    return