import io
from ntpath import join

from dsmr_parser import telegram_specifications
from dsmr_parser.parsers import TelegramParser

from obis_refs import obis_refs

# TODO: Read from tcp instead of file
file_contents = io.open('telegram.txt', 'r').read()

# Trick to fix line endings
telegram_str = '\r\n'.join(file_contents.splitlines())

# Parse telegram & validate checksum
parser = TelegramParser(telegram_specifications.V5, apply_checksum_validation = True)
telegram = parser.parse(telegram_str)

# Print for debugging
print('telegram: ')

for key, ref in obis_refs.items():
  if ref in telegram:
    print(key.ljust(40) + ':  ' + str(telegram[ref]))
  else:
    print(key.ljust(40) + ':  NOT FOUND')


# TODO: Get required values and send to sql-like database