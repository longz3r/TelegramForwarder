# Telegram Forwarder

This project forwards messages from specified Telegram channels to a specific chat or topic.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/longz3r/TelegramForwarder
    cd TelegramForwarder
    ```

2. Install the required dependencies using pip:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

### config.json

The `config.json` file is used to specify the source channels and the destination chat or topic.

- `forwardFrom`: List of channel IDs to forward messages from.
- `forwardTo`: List of objects containing `id` (destination chat ID) and `topicId` (optional, for specific topics).

Example:
```json
{
    "forwardFrom": [
        1234567890,
        1223424890
    ],
    "forwardTo": [
        {
            "id": 122534890,
            "topicId": 166
        }
    ]
}
```

### .env

The `.env` file contains the API credentials required to interact with the Telegram API.

- `API_ID`: Your Telegram API ID.
- `API_HASH`: Your Telegram API hash.

Example:
```properties
API_ID=6546875
API_HASH=a1b2c3d4
```

## Running the Project

After configuring the `config.json` and `.env` files, you can run the project using:
```sh
python main.py
```
