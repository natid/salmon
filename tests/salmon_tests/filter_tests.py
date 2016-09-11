from nose.tools import assert_equal, assert_raises

from salmon import mail, filters, server


PLAIN = """To: me@example.com
From: you@example.com
Subject: Email testing

Hello,

This is a test!
"""

PLAIN_MIME = """To: me@example.com
From: you@example.com
Subject: Email testing
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="salmon"


--salmon
Content-Type: text/plain"

Hello,

This is a test!


--salmon--
"""

HTML_MIME = """To: me@example.com
From: you@example.com
Subject: Email testing
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="salmon"


--salmon
Content-Type: text/plain"

Hello,

This is a test!


--salmon
Content-Type: text/html; charset=UTF-8

<html><body>
<p>Hello</p><p>This is a test!</p>
</body></html>

--salmon--
"""

HTML_BADBADBAD = """To: me@example.com
From: you@example.com
Subject: Email testing
Content-Type: text/html; charset=UTF-8

<html><body>
<p>Hello</p><p>This is a test!</p>
</body></html>
"""


def test_html_rejection():
    msg = mail.MailRequest("localhost", "you@example.com", "me@example.com", PLAIN)
    func = filters.reject_html_email(lambda message: None)
    assert_equal(func(msg), None)

    msg = mail.MailRequest("localhost", "you@example.com", "me@example.com", PLAIN_MIME)
    func = filters.reject_html_email(lambda message: None)
    assert_equal(func(msg), None)

    msg = mail.MailRequest("localhost", "you@example.com", "me@example.com", HTML_MIME)
    with assert_raises(server.SMTPError):
        func = filters.reject_html_email(lambda message: None)
        func(msg)

    msg = mail.MailRequest("localhost", "you@example.com", "me@example.com", HTML_BADBADBAD)
    with assert_raises(server.SMTPError):
        func = filters.reject_html_email(lambda message: None)
        func(msg)
