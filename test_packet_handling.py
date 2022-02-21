import unittest
import json
from main import decode_packets


class TestPacketFuncs(unittest.TestCase):

    def test_decode_packets(self):
        sep = json.dumps("*")
        incoming_packet = sep+json.dumps([9999, "Error"])+sep+json.dumps("heartbeat")+sep+sep+json.dumps({"sensor1": [0, 23.7, 29.7, 13.7]})+sep  # noqa

        incoming_packet = bytes(incoming_packet, "utf-8")

        self.assertEqual(decode_packets(""), [])
        self.assertEqual(decode_packets(True), [])
        self.assertEqual(decode_packets(incoming_packet), [[9999, "Error"], {"sensor1": [0, 23.7, 29.7, 13.7]}])  # noqa
