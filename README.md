# Autopuller

## Description
Autopuller is a Python program designed to search through your files for GitHub repositories and save their directories in a text file. This allows you to push all the repositories simultaneously with ease.

## Usage
1. Install Python on your system (if not already installed).
2. Clone or download the Autopuller repository from GitHub.
3. Navigate to the project directory.

## Setup
Before running the program, you need to perform the following steps:

1. Install the required dependencies by running the following command:
``pip install -r requirements.txt``
2. Open the `config.json` file and provide your GitHub access token. This token is necessary for the program to interact with the GitHub API. Ensure that you have appropriate permissions to access the repositories you want to push.

## Running the Program
To run the program, use the following command:
``python autopuller.py

``

The program will search through your files and identify any GitHub repositories. It will then save their directories in a text file called `repo_list.txt`.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

