import os
from google.appengine.ext.webapp import template
import cgi
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail

class SendEmail(webapp.RequestHandler):
  def post(self):
    user_address = "helixhealth@gmail.com"
    sender_address = cgi.escape(self.request.get('txtEmailAddress'))
    name = cgi.escape(self.request.get('txtFirstName') + ' ' + self.request.get('txtLastName'))
    phone = cgi.escape(self.request.get('txtPhoneNumber1') + '-' + self.request.get('txtPhoneNumber2') + '-' + self.request.get('txtPhoneNumber3'))
    preferred_contact = cgi.escape(self.request.get('cbOKToLeaveMessage'))
    comments = cgi.escape(self.request.get('txtComments'))

    if not mail.is_email_valid(sender_address):
      sender_address = "unknown@helixhealth.org"

    subject = "Helix Health Contact Submission"

    body = """
name: %s
email: %s
phone: %s
contact: %s
comments: %s
""" % (name, sender_address, phone, preferred_contact, comments)


    mail.send_mail(sender_address, user_address, subject, body)

    title = "Message Sent"
    page_content = """
    <p>Your message has been successfully delivered, %s. A member of the Helix Health team will respond to your message shortly.</p>
    <p><a href="/" class="NormalLink">Return to Helix Health Home</a></p>
    """ % name
    template_values = {
      'page_title': title,
      'page_content': page_content
      }

    path = os.path.join(os.path.dirname(__file__), 'templates/template-aux.thtm')
    self.response.out.write(template.render(path, template_values))

  def get(self):
    self.redirect('/')
    

application = webapp.WSGIApplication(
                                     [('/send_form', SendEmail)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
