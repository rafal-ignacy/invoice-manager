from dataclasses import dataclass
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import json

from app.settings import ROOT_DIR


@dataclass
class MailHandler:
    def get_credentials(self, path: str):
        with open(path, "r") as file:
            file_data_dict = json.loads(file.read())
        return file_data_dict["mail_address"], file_data_dict["mail_password"]

    def prepare_message(self, mail_address: str):
        message = MIMEMultipart()
        message['From'] = mail_address
        message['To'] = mail_address
        return message

    def attach_files(self, message: MIMEMultipart, invoice_binary_list):
        invoice_id = 1
        for invoice_binary in invoice_binary_list:
            attachment = MIMEApplication(invoice_binary)
            attachment['Content-Disposition'] = f'attachment; filename="invoice-{invoice_id}.pdf"'
            message.attach(attachment)
            invoice_id += 1

    def send_message(self, message: MIMEMultipart, mail_address: str, password: str):
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(mail_address, password)
        smtp_server.sendmail(mail_address, mail_address, message.as_string())
        smtp_server.quit()

    def send(self, invoice_binary_list):
        mail_address, mail_password = self.get_credentials(ROOT_DIR + r"/app/data/credentials.json")
        message = self.prepare_message(mail_address)
        self.attach_files(message, invoice_binary_list)
        self.send_message(message, mail_address, mail_password)
