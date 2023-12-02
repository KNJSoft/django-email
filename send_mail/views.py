from django.shortcuts import render
from django.template.loader import render_to_string
from send_mail.models import MonModeleEmail


# Create your views here.
def send(request):
    if request.method == "POST":
        email = request.POST['email']
        destinataires = [email]
        sujet = 'Réunion de formation'
        corps = 'Contenu de l\'email'

        """email = MonModeleEmail(sujet, corps, destinataires)
        email.attach_file('send_mail/email.html')
        email.send()"""

        context={'nom':"knjsoft"}
        contenu_html = render_to_string('send_mail/email.html', context)
        #email.attach_file('/home/knjsoft/programme.zip')

        email = MonModeleEmail(sujet, contenu_html, destinataires)
        email.content_subtype = "html"
        #email.attach('email.html', contenu_html, 'text/html')
        email.send()

    return render(request, 'send_mail/index.html')
def mail(request):
    return render(request, 'send_mail/email.html')