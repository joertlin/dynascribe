# DynaScribe

This repository contains a system for transcribing audio files to Dynalist, by transcribing audio files using the Nemo library and sanitizing the transcription using OpenAI. The system is built using the following libraries:

1. Nemo: NVIDIA's audio processing library for video cards
2. OpenAI: A powerful AI library for sanitizing transcriptions
3. Dynalist API: To push changes to a Dynalist document

## Table of Contents

1. [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
2. [Usage](#usage)
    * [API Keys](#api-keys)
    * [Running the Application](#running-the-application)
3. [Testing](#testing)

## Getting Started

These instructions will help you set up the system on your local machine.

### Prerequisites

- Conda or miniconda
- see requirements.yml

### Installation

1. Clone the repository:
```bash
git clone https://github.com/joertlin/dynascribe.git
```
2. Navigate to the repository directory:
```bash
cd dynascribe
```
3. Set up a Conda environment:
```bash
conda env create -f requirements.yml
activate dynascribe
```
4. Set up the Nemo library  
This needs documentation!!!

## Usage

### API Keys

Before running the application, you need to set up the necessary API keys from Dynalist and OpenAI.

Use the `setup_template.py` file in the root directory of the project. Rename the file to `setup.py` and add your API keys as directed in the file.

### Running the Application

```bash
python listener.py <directory_to_listen_for_.wav_files>
```
## Testing  
Several Jupyter notebooks are included for testing different parts of the system. You can use JupyterLab to run these notebooks as mini tests.
