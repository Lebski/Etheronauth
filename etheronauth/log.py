import logging

# create out
out = logging.getLogger('etheronauth')
out.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)
ch.setLevel(logging.INFO)
#ch.setLevel(logging.WARN)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to out
out.addHandler(ch)
