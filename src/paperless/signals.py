import logging

logger = logging.getLogger("paperless.auth")


# https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.signals.user_login_failed
def handle_failed_login(sender, credentials, request, **kwargs):
    logger.info(
        f"Login for {credentials['username']} failed: {request}",
    )
