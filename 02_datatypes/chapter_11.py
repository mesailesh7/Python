# import arrow
from collections import namedtuple

# brewing_time = arrow.utcnow()
# brewing_time.to("Europe/Rome")

# Collections
chai_profile = namedtuple("chaiProfile", ["flavor", "aroma"])
print(chai_profile)
