
# Flow Transcriptor Real-Time Speech-to-Text App

This repository contains a Python application for real-time speech-to-text conversion using IBM Watson's Speech to Text service. It's designed to capture audio from a microphone primarly, send it to the IBM Watson service via WebSocket, and receive the transcribed text in real time.

## Features

- Real-time audio streaming to IBM Watson Speech to Text service.
- WebSocket communication for efficient real-time processing.
- Support for various audio configurations.
- Easy configuration through environment variables.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- IBM Cloud account with Speech to Text service credentials

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/degarzonm/flow-transcriptor.git
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to a new file named `.env` and fill in your IBM Watson Speech to Text service credentials.

### Usage

Run the application using:
```
python src/main.py
```
The application will start recording audio from your default microphone and stream it to IBM Watson for real-time job, you will get a string stream with the transcription.

## Configuration

The application can be configured using the following environment variables in the `.env` file:

- `IBM_API_KEY`
- `IBM_SPEECH_SERVICE_INSTANCE_ID` 
- `IBM_SPEECH_SERVICE_REGION` 
- `IBM_LANG_MODEL`

## Contributing

Contributions to this project are welcome. Please ensure to follow the usual contribution guidelines

## License

This project is licensed under the [GNU LESSER GENERAL PUBLIC LICENSE](LICENSE).

## Support

For support or any queries, please contact us at degarzonm@unal.edu.co
