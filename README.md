# AnimateDiff for Win

## Introduction

This is Windows model of Magic Animate using Gradio.

Original: [Magic Animate](https://github.com/magic-research/magic-animate)

### Dependencies

- OS: Windows
- nvidia:
  - cuda: 11.7
- python 3.10.5 (using Pyenv)

## Install

## Clone from GitHub

Clone from GitHub, and move to the folder " AnimateDiff-for-Win".

```bash
git clone https://github.com/supplepentan/magic_animate_for_win_gradio
cd magic_animate_for_win_gradio
```

## Virtual environment

Virtual environment with Python-version 3.10.5 using Pyenv.

```bash
pyenv local 3.10.5
python -m venv venv
venv/scripts/activate
```

## Libraries

Install libraries using " reqruirements.txt "

```bash
python -m pip install -r requirements.txt
```

### Pytorch

Uninstall unnecessary installed Pytorch, and newly install Pytorch (CUDA11.7 compatible model).

```bash
python -m pip uninstall -y torch torchvision
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu117
```

### xFormers

```bash
python -m pip install xformers==0.0.20
```

### triton

```bash
python -m pip install triton-2.0.0-cp310-cp310-win_amd64.whl
```

## Run the Gradio

```bash
python app.py
```

Access to http://127.0.0.1:7860 .

## Acknowledgements

This code is built on [Magic Animate](https://github.com/magic-research/magic-animate), thank for the authors for sharing their codes.
