# Painy

## Features

- Painy is a simple tool which allows you to automatically generate commit messages via OpenAI API. It automatically check the changes in your repository and generate a commit message based on the changes.

## Installation

- Install the package via pip:

```bash
    pip install painy
```

- Set the environment variable `OPENAI_API_KEY` to your OpenAI API key.
- By default, model max content length is set to `4097` tokens (max length for `gpt-3.5-turbo`). If you want to use a different model with a different max length, set the environment variable `OPENAI_MODEL_MAX_LENGTH` to the max length of the model you want to use.

- By default, Painy will use the `gpt-3.5-turbo` (ChatGPT), if you want to use a different model, set the environment variable `OPENAI_MODEL_NAME` to the model you want to use. You must have access to the model you want to use.

## Usage

- (Recommended) Go to the folder with your repository and run the following command:

```bash
    painy
```

This will generate a commit message based on the staged changes in your repository.

- If you want to generate a commit message for all the changes in your repository, run the following command (this files must be registered in git before in order to have a diff to compare):

```bash
    painy --check-all
```
