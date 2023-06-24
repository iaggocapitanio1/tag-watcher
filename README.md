# TAG WATCHER

Tagger Watcher is a Python application that monitors a directory for changes and performs certain actions based on the changes detected. It is designed to be configurable through environment variables and provides logging functionality.


## Requirements

- Python 3.10 or later.

## Getting Started

Before using the WoodWorkProjectWatcher, ensure that you have Python 3.9 or later installed on your system. You can check your Python version by running:

```sh
python --version
```

If you have an older version of Python, you can download the latest version from the [official Python website](https://www.python.org/downloads/).
## Features

- Monitors a specified directory for changes in Excel files.
- Performs delayed scanning of directories to avoid redundant processing.
- Logs activity to both the console and a file.
- Configuration through environment variables.

### Clone the Repository

Clone this repository to your local machine:

```sh
git clone git@github.com:iaggocapitanio1/WoodWorkProjectWatcher.git
cd WoodWorkProjectWatcher
```


### Set Up a Virtual Environment (optional)

It is a good practice to create a virtual environment for your Python projects. You can create a virtual environment by running:

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
## Configuration

The application can be configured using environment variables. You can place these variables in a `.dev.env` file for local development or set them in your environment for production use.

Here is the list of environment variables:



| Environment Variable  | Description                                                  | Default Value                    |
|-----------------------|--------------------------------------------------------------|----------------------------------|
| `PRODUCTION`          | Set to `True` if running in a production environment         | `True`                           |
| `DELAY_FOR_SCAN`      | Delay (in seconds) between directory scans                    | `5`                              |
| `MAPPING_FILE`        | Path to the mapping file                                      | `"MAPPING.xlsx"`                 |
| `SLEEP_DURATION`      | Duration (in seconds) to sleep between scans                  | `1`                              |
| `NUM_WORKER_THREADS`  | Number of worker threads to use for processing                | `4`                              |
| `PATH_REFERENCE`      | Reference path                                               | `"mofreitas/clientes/"`          |
| `WATCHING_DIR`        | Directory to monitor for changes                              | `BASE_DIR / '/home/app/media/public/mofreitas'` |
| `CUT_LIST_DIR`        | Name of the directory for cut lists and labels                | `"Listas de Corte e Etiquetas"`   |
| `KEYWORD`             | Keyword to search for in the directory                        | `"clientes"`                     |

You can copy the above table and use it in your README file. Feel free to customize the formatting or add any additional information as needed.
### Install Dependencies

Install the required dependencies:

```sh
pip install -r requirements.txt
```

### Running the Application

Run the main script:

```sh
python main.py
```

## Usage

Provide a brief description of how to use the application, including any command-line arguments and options, configuration files, etc.

## Contributing

Explain how others can contribute to your project. For example, how to submit bugs, feature requests, and how to contribute code.

## License

Specify the license under which your project is distributed.

## Contact

Iaggo Capitanio - iaggo.capitanio@gmail.com

Project Link: [https://github.com/iaggocapitanio1/tag-watcher](https://github.com/iaggocapitanio1/tag-watcher)
