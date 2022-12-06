from performance_testing.time_to_load import page_load
from performance_testing.image_waterfall import create_waterfall
import pprint



url = "https://faroutsolutions.com/"
element = "div"

# print(page_load(url, element))

pprint.pprint(create_waterfall(url,10))