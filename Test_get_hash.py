import get_hash
import unittest
import logging

# logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
# logging.getLogger('').setLevel(logging.INFO)

class Test_get_hash(unittest.TestCase):

    def test_get_hash(self):
        _filepath = "get_hash.py"
        _hash = get_hash.filehash(_filepath)
        self.assertTrue(_hash)
        logger.debug("filehash:%s", _hash)
        # self.assertEqual('3132333435363738393031323334353637383930', _key.hex())
    

if __name__ == "__main__":
    unittest.main(exit=False)

