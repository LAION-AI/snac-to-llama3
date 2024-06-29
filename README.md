# Emo-2-SNAC to LLaMA 3 Audio Token Conversion

This repository contains scripts and documentation for converting audio samples from the [0xd4t4/Emo-2-SNAC](https://huggingface.co/0xd4t4/Emo-2-SNAC) dataset into tokens compatible with the LLaMA 3 language model. This project is part of a collaboration with LAION to develop advanced audio processing capabilities for [AI assistants](https://laion.ai/notes/open-gpt-4-o/).

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

The goal of this project is to enhance the audio processing capabilities of the LLaMA 3 language model by converting audio samples into discrete tokens. These tokens will then be used to train the model to understand and generate audio, similar to how it processes text.

## Dataset

The dataset used in this project is the [0xd4t4/Emo-2-SNAC](https://huggingface.co/0xd4t4/Emo-2-SNAC) dataset, available on Hugging Face. This dataset contains audio samples labeled with emotional content, which will be converted into SNAC (Multi-Scale Neural Audio Codec) tokens.

## Requirements

- Python 3.8 or higher
- hugging face

## Installation

(Optional) Create your own enviroment

## Usage

1. Clone the repository:
   
``` bash
git clone https://github.com/LAION-AI/snac-to-llama3.git
cd snac-to-llama3
```

2. Install the requirments

``` bash
pip install -r requirements.txt
```

3. Download The hugging face dataset

``` bash
huggingface-cli download 0xd4t4/Emo-2-SNAC --local-dir ./dataset --revision refs/convert/parquet --repo-type dataset
```

4. Integrate SNAC codec with LLaMA 3 model:

```bash
python codec-to-token.py
```

5. Byte pair encoder

## Project Structure

- `codec-to-token.py`: Script for converting audio samples to SNAC tokens.
- `byte-pair-encoding.py`: Script for integrating SNAC tokens with the LLaMA 3 model.
- `requirements.txt`: List of dependencies required for the project.
- `README.md`: This file.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project is a collaboration with [LAION](https://laion.ai/). Special thanks to the Hugging Face team for providing the [0xd4t4/Emo-2-SNAC](https://huggingface.co/0xd4t4/Emo-2-SNAC) dataset.
