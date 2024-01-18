import re

string = "bababuba@wonderland.net"
small = "kjdafj lajfd laj f"
credit = "0987 8765 5674 6543"

# credit = credit.replace(" ", "")

# x = re.search('^[0-9]{4}', credit)
match = re.findall('[0-9]+', credit)

if match:
    print(', '.join(match))