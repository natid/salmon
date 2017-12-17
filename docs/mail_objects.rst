Mail Objects
============

``MailRequest`` and ``MailResponse`` objects are two ways that Salmon
represents emails. They provide a simplified interface to Python's own
``Email`` package.


MailRequest
-----------

``MailRequest`` objects are given to your message handlers when a new email comes in.

To/From properties
^^^^^^^^^^^^^^^^^^

``To`` and ``From`` are populated by the ``RCPT TO`` and ``MAIL FROM`` commands issued by the sender to Salmon. If you're using ``QueueReciever``, these properties will be ``None``


Headers
^^^^^^^

Headers are acceessed a dict-like interface::

    print(message["Subject"])  # prints the subject header


# body

# is bounce

# walking the mime tree

# accessing lower level API


MailResponse
------------

``MailResponse`` objects can be created to send responses via ``salmon.server.Relay``.

# creating via views or directly

# headers as above

# attach

# lower level api


MailBase
--------

# headers

# content encoding

# differences from Python email API

# Python email API-compatible interface on ``base.mime_part``
