import pkg_resources

try:
    __version__ = pkg_resources.require("django-nocaptcha-recaptcha")[0].version
except pkg_resources.DistributionNotFound:
    __version__ = '0.0.18-via-buildout'

from .fields import NoReCaptchaField
from .widgets import NoReCaptchaWidget
