"""
Generic filters that can wrap message handlers

Currently this module only contains one filter: reject_html_email
"""


from salmon.server import SMTPError


def reject_html_email(func, error_code=550):
    """Reject messages with HTML parts

    ``error_code`` is the error code that will be raised if HTML is found
    """

    def wrapped(message, *args, **kwargs):
        if "Content-Type" in message and message["Content-Type"].startswith("text/html"):
            raise SMTPError(error_code, "This server does not accept HTML mail")

        for part in message.walk():
            if "Content-Type" in part and part["Content-Type"].startswith("text/html"):
                raise SMTPError(error_code, "This server does not accept HTML mail")

        return func(message, *args, **kwargs)

    return wrapped


def reject_blocked_sender(func, spam_storage, error_code=550):
    """Reject mail from a list of known spammers

    ``spam_storage`` should implement ``__contains__``. Implementation details are
    up to you.
    """
    def wrapped(message, *args, **kwargs):
        sender = message.From
        if sender in spam_storage:
            raise SMTPError(error_code, "Email sender found in spammer list")

        return func(message, *args, **kwargs)

    return wrapped
