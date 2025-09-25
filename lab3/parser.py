import imaplib
import email
import os
from dotenv import load_dotenv
from email.header import decode_header

load_dotenv()

sheck_email = os.getenv("SHECK_EMAIL")
sheck_password = os.getenv("SHECK_PASSWORD")

mail = imaplib.IMAP4_SSL("imap.mail.ru")
mail.login(sheck_email, sheck_password)

mail.select("inbox")
theme = os.getenv("THEME")
status, data = mail.search(None, '(SUBJECT "{}")'.format(theme))
mail_ids = data[0].split()

save_dir = os.getenv("SAVE_DIR")
os.makedirs(save_dir, exist_ok=True)

for num in mail_ids:
    _, msg_data = mail.fetch(num, "(RFC822)")
    msg = email.message_from_bytes(msg_data[0][1])

    for part in msg.walk():
        filename = part.get_filename()
        if filename:
            decoded, enc = decode_header(filename)[0]
            if isinstance(decoded, bytes):
                filename = decoded.decode(enc or "utf-8")

            file_path = os.path.join(save_dir, filename)
            with open(file_path, "wb") as f:
                f.write(part.get_payload(decode=True))
