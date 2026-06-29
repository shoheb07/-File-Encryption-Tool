# -File-Encryption-Tool
A File Encryption Tool is a strong beginner-to-intermediate Python project that demonstrates cryptography, file handling, and GUI development. It’s compact enough for GitHub while showcasing practical skills.

File Encryption Tool

A simple and secure Python application to encrypt and decrypt files using strong symmetric encryption. This project helps protect sensitive files such as documents, images, PDFs, videos, and archives from unauthorized access.

Features

- Encrypt any file using AES-based Fernet encryption
- Decrypt encrypted files
- Secure key generation and storage
- Simple command-line interface
- Fast and lightweight
- Cross-platform support
- Easy to extend with a GUI

Tech Stack

- Python 3
- cryptography

Project Structure

```
File-Encryption-Tool/
│
├── main.py
├── encrypt.py
├── decrypt.py
├── key_manager.py
├── requirements.txt
├── README.md
├── LICENSE
├── keys/
│   └── secret.key
└── sample_files/
```

Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/File-Encryption-Tool.git
```

2. Navigate to the project directory

```bash
cd File-Encryption-Tool
```

3. Install the required package

```bash
pip install -r requirements.txt
```

Usage

Generate the encryption key (only required the first time)

```bash
python key_manager.py
```

Run the application

```bash
python main.py
```

Menu

```
1. Encrypt File
2. Decrypt File
3. Exit
```

Example

Encrypt

```
Enter file path:
sample_files/report.pdf
```

Output

```
report.pdf.enc
```

Decrypt

```
Enter encrypted file path:
sample_files/report.pdf.enc
```

Output

```
report.pdf
```

Requirements

- Python 3.9 or later
- cryptography

Install dependency

```bash
pip install cryptography
```

Future Improvements

- Graphical User Interface (Tkinter)
- Password-based encryption
- Folder encryption
- Batch encryption
- Drag-and-drop support
- File integrity verification
- Progress bar
- Dark mode
- Secure key rotation
- Cloud storage integration

Learning Outcomes

- File handling in Python
- Symmetric encryption
- Modular programming
- Secure key management
- Error handling
- Command-line application development

Contributing

Contributions are welcome. Feel free to fork the repository, improve the project, and submit a pull request.

License

This project is licensed under the MIT License.

Author

Shoheb Mulla
If you found this project useful, consider giving it a star.
