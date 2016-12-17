Email
=============

Our current email system consists of a postfix email server configured in the machine located in our office.
This allows us to both send and receive (and forward) emails. The hostname for this machine is mail-upe.cs.berkeley.edu.
Inside the directory for postfix, the `virtual` file defines our current mailing lists. The receiving addresses are first, followed by
a newline delimited list of email addresses to forward emails sent to the receiving address.

We plan on migrating this system to the [OCF](https://www.ocf.berkeley.edu/docs/services/vhost/mail/), which provides email forwarding 
and also an SMTP server we need for sending out emails. Email sending is currently used for the process of approving accounts, and will 
later be used for scheduling mock interviews. This should be easy to configure within `settings.py` 
