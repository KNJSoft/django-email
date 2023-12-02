from django.db import models

# Create your models here.
from django.core.mail import EmailMessage




class MonModeleEmail(EmailMessage):
    def __init__(self, sujet, corps, destinataires):
        super().__init__(sujet, corps, 'knjprod@gmail.com', destinataires)
        self.content_subtype = 'html'