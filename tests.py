#!/usr/bin/env python3

import asyncio
import unittest

import sixtynine


class TestSixtynine(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.get_event_loop()

    def tearDown(self):
        self.loop.close()

    def test_mouthful(self):
        self.assertEqual(self.loop.run_until_complete(sixtynine.mouthful()), 69)
