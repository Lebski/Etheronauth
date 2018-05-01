import json
from etheronauth import tools
from etheronauth import log

log.out.info("### Testing on module > tools <")
log.out.info("# Checking on global Datadir")
log.out.info(tools.get_dir())
log.out.info("# Standard File write")
log.out.info(tools.write_file("../tests/results/res_filewrite.txt", "Test payload"))
log.out.info("# Standard File read")
log.out.info(tools.get_file("../tests/results/res_filewrite.txt"))
log.out.info("# JSON File write")
log.out.info(tools.write_json("../tests/results/res_filewrite_json.txt", json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')))
log.out.info("# JSON File read")
log.out.info(tools.get_json("../tests/results/res_filewrite_json.txt"))
log.out.info("### End of Test")
