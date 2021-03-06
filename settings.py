"""
Master default settings file. Do not change any of the values below directly.
Create a local_settings.py file, copy the variables, and change them there.
Anything in local_settings.py will override what is seen here.
"""
import os

# The path to the root directory of the project (has this settings.py 
# file in it) with trailing slash.
MAIN_PATH = os.path.abspath(os.path.split(__file__)[0])
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(MAIN_PATH, 'media')
# The number of decently rated (3+) songs in a random playlist.
# Name of the directory that contains music (not a full path).
MUSIC_DIR_NAME = 'music'
# The path to the music directory that contains all of the music files.
MUSIC_DIR = os.path.join(MEDIA_ROOT, MUSIC_DIR_NAME)

# Name as it should be displayed in the application header/title/etc...
PROGRAM_NAME = "django-jukebox"

RANDOM_REQ_GOOD_RATED_SONGS = 10
# Any song with a rating greater or equal to this value is considered 'good'.
RANDOM_REQ_GOOD_RATING = 3
# The number of songs with no rating in a random playlist.
RANDOM_REQ_UPCOMING = 6
# Songs that have more than this number of ratings can no longer be
# considered 'upcoming'.
RANDOM_REQ_UPCOMING_MAX_RATINGS = 4
# This is the number of seconds that the juke_daemon will sleep if it ever
# finds the SongRequest queue empty. This should never happen, but it's here
# as a fail-safe.
TIME_TO_SLEEP_WHEN_QUEUE_EMPTY = 10

# Number of previous songs to display in queue.
NUMBER_OF_PREVIOUS_SONGS_DISPLAY = 5
# Limit to number of songs in queue to be played.
LIMIT_UPCOMING_SONGS_DISPLAY = 15

# Maximum number of requests any user may have outstanding before they are refused further requests.
MAX_OUTSTANDING_REQUESTS_PER_USER = 5

# Maximum song length, in seconds.
MAX_SONG_LENGTH = 15. * 60.

# Minimum song length, in seconds.
MIN_SONG_LENGTH = 60.

# When True, allow anonymous users to request songs.
ALLOW_ANON_REQUESTS = False

# The command used to have your CLI player play an audio file.
# A list formatted for subprocess.call().
CLI_PLAYER_COMMAND_STR = ['mplayer', '-really-quiet', '-af', 'volume']

# Change this in production.
DEBUG = True
TEMPLATE_DEBUG = DEBUG
DJANGO_SERVE_MEDIA = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

# 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_ENGINE = 'sqlite3'
# Or path to database file if using sqlite3.
DATABASE_NAME = os.path.join(MAIN_PATH, 'djangojuke.db3')
# Not used with sqlite3.
DATABASE_USER = ''
# Not used with sqlite3.         
DATABASE_PASSWORD = ''
# Set to empty string for localhost. Not used with sqlite3.
DATABASE_HOST = ''
# Set to empty string for default. Not used with sqlite3.
DATABASE_PORT = ''

AUTHENTICATION_BACKENDS = (
    # Un-comment this in your local_settings.py if you want LDAP authentication.
    # Make -SURE- to set the LDAP settings below.
    #'auth_backends.auth_ldap.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# The LDAP connection string.
LDAP_HOST = 'ldap://some.ldaphost.com'
# The DN to authenticate users to for authentication.
LDAP_USER_BIND_DN = 'uid=%s,cn=users,dc=some,dc=ldaphost,dc=com'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(MAIN_PATH, 'staticfiles')
STATIC_URL = '/static/'

# URL to a YUI installation.
YUI_URL = 'http://yui.yahooapis.com/2.8.0r4/'

# Where to redirect to after logging in.
LOGIN_REDIRECT_URL = '/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=h#j0rha^hndrr$u6@8wc7=(08ntt_63d9-0q$*4hh$vyx-n0%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'includes.extra_context.common_urls',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(MAIN_PATH, 'templates'),
)

INSTALLED_APPS = (
	'django.contrib.admindocs',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.admin',
	'django.contrib.humanize',
	'django.contrib.staticfiles',
	'django_extensions',
	'apps.accounts',
	'apps.music_db',
	'apps.music_player',
	'apps.juke_daemon',
	'apps.juketunes_ui',
	'south',
)

"""
This makes any settings in local_settings.py take precedence over the ones
seen here. Make any local modifications to local_settings.py rather than
editing this file directly.
"""
try:
     from local_settings import *
except ImportError:
     pass
