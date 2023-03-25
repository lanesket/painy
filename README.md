# Painy

    Comments for this repository commits are written with Painy itself.

## Features

- Painy is a simple tool which allows you to automatically generate commit messages via OpenAI API. It automatically check the changes in your repository and generate a commit message based on the changes.

- Works well with Jupyter Notebooks (`.ipynb` files) by using `nbdime` for diffing.

- Interactive mode

## Prerequisites

- OpenAI API key. You can get one [here](https://platform.openai.com).

- Python 3.7.1 or higher and `pip` package manager.

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

  - Add something to stage:

    ```bash
        git add <files>
    ```

  - Then use Painy:

    ```bash
        painy comment
    ```

  - Or with the environment variable `OPENAI_API_KEY` set inplace:

    ```bash
        OPENAI_API_KEY=<your-openai-api-key> painy comment
    ```

    This will generate a commit message based on the staged changes in your repository.

- Commit staged changes with a generated commit message:

```bash
    painy commit
```

- Interactive mode:

```bash
    painy <comment|commit> -i
```

This will generate a commit message based on the staged changes in your repository and will ask you if you want to regenerate the commit message.

- If you want to generate a commit message for all the changes in your repository, run the following command (this files must be registered in git before in order to have a diff to compare):

```bash
    painy <comment|commit> --check-all
```
