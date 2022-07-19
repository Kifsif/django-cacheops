from ordered_enum import ValueOrderedEnum


class LANGUAGES(ValueOrderedEnum):
    ARABIC = 'ARABIC'
    CHINESE = 'CHINESE'
    ENGLISH = 'ENGLISH'
    FRENCH = 'FRENCH'
    RUSSIAN = 'RUSSIAN'
    SPANISH = 'SPANISH'


    def __lt__(self, other):
        if self.__class__ is other.__class__:
             return self.value < other.value


LANGUAGES_CHOICES = [
    (LANGUAGES.ARABIC.value, 'Арабский'),
    (LANGUAGES.CHINESE.value, 'Китайский'),
    (LANGUAGES.FRENCH.value, 'Французский'),
    (LANGUAGES.RUSSIAN.value, 'Русский'),
    (LANGUAGES.SPANISH.value, 'Испанский'),
    (LANGUAGES.ENGLISH.value, 'Английский'),
]

TABLE_PREFIX = 'nonverbis_treaties'
REMOTE_DB_NAME = 'wordpress'
DEFAULT_DB_NAME = 'default'
