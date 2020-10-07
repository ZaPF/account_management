import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    FLASK_COVERAGE = 0
    MOCKSERVER = False
    LDAP_HOST = 'localhost'
    LDAP_PORT = 8369
    LDAP_BASE_DN = 'dc=my-domain,dc=com'
    LDAP_USER_DN = 'ou=users'
    LDAP_GROUP_DN = 'ou=groups'
    LDAP_OAUTH2_CLIENT_DN = 'ou=oauth2'
    LDAP_BIND_USER_DN = 'uid=bind,dc=my-domain,dc=com'
    LDAP_BIND_USER_PASSWORD = 'bind123'
    LDAP_USER_RDN_ATTR = 'uid'
    LDAP_USER_LOGIN_ATTR = 'uid'
    LDAP_GROUP_OBJECT_FILTER = '(objectClass=groupOfNames)'
    LDAP_GROUP_MEMBERS_ATTR = 'member'
    LDAP_READONLY = False

    DEFAULT_USER_UID = "admin"
    DEFAULT_USER_GIVENNAME = "Auth"
    DEFAULT_USER_SN = "Administrator"
    DEFAULT_USER_PASSWORD = "changeme"
    DEFAULT_USER_MAIL = "admin@example.com"

    DEFAULT_GROUPS = ['all']

    DELETED_USER_GIVENNAME = "Deleted"
    DELETED_USER_SN = "User"
    DELETED_USER_MAIL = "deleted@example.com"

    BABEL_TRANSLATION_DIRECTORIES='translations/'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///anmeldung.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOGOUT_ALLOWED_NEXT = [ "https://anmeldung.zapf.in/oauth/loggedout" ]

    ZAPF_GUARANTEED_GROUPS = ['StAPF', 'TOPF', 'KommGrem', 'ZaPF e.V. Kassenpruefer', 'ZaPF e.V. Vorstand']

    MAIL_USE_TLS = True
    MAIL_DEFAULT_SENDER = 'auth@example.com'
    MAIL_NEXT_ZAPF_ORGA = 'orga@example.com'

    RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}
    import ldap3
    PASSWORD_HASHING_FUNC = ldap3.HASHED_SALTED_SHA384

    CACHE_TYPE = "simple" # Flask-Caching related configs
    CACHE_DEFAULT_TIMEOUT = 3600

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SECRET_KEY = 'secrets'
    DEBUG=True
    RECAPTCHA_PUBLIC_KEY="6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
    RECAPTCHA_PRIVATE_KEY="6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
    RECAPTCHA_USE_SSL=False
    #MOCKSERVER = True

class ProductionConfig(Config):
    LOGPATH='logs'

class TestingConfig(Config):
    DEBUG=True
    TESTING=True
    MOCKSERVER=True
    FLASK_COVERAGE = 1
    SECRET_KEY = 'secrets'
    WTF_CSRF_ENABLED = False
    RECAPTCHA_PUBLIC_KEY="6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
    RECAPTCHA_PRIVATE_KEY="6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
    RECAPTCHA_USE_SSL=False


config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig,
        'default': DevelopmentConfig
        }

