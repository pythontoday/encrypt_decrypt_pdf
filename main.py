from PyPDF2 import PdfFileWriter, PdfFileReader
import sys


def encrypt_file():
    file_path = input("[+] Enter file path: ")
    password = input("[+] Enter password: ")
    encrypted_file_name = input("[+] Enter a name for the encrypted file: ")

    file_writer = PdfFileWriter()

    try:
        file_reader = PdfFileReader(file_path)
    except FileNotFoundError:
        print(f"[INFO] No file with path: {file_path}")
        sys.exit()

    for page in range(file_reader.numPages):
        file_writer.addPage(file_reader.getPage(page))

    file_writer.encrypt(password)

    with open(encrypted_file_name, "wb") as file:
        file_writer.write(file)

    print(f"[+] Created - {encrypted_file_name}")


def decrypt_file():
    file_path = input("[+] Enter file path: ")
    password = input("[+] Enter password: ")
    decrypted_file_name = input("[+] Enter a name for the decrypted file: ")

    file_writer = PdfFileWriter()

    try:
        file_reader = PdfFileReader(file_path)
    except FileNotFoundError:
        print(f"[INFO] No file with path: {file_path}")
        sys.exit()

    if file_reader.isEncrypted:
        file_reader.decrypt(password)

    for page in range(file_reader.numPages):
        file_writer.addPage(file_reader.getPage(page))

    with open(decrypted_file_name, "wb") as file:
        file_writer.write(file)

    print(f"[+] Created - {decrypted_file_name}")


def main():
    choose = input("[+] Enter 0 to encrypt the file, enter 1 to decrypt: ")
    encrypt_file() if choose == "0" else decrypt_file()


if __name__ == '__main__':
    main()
