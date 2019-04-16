#! /usr/bin/env python
# coding=utf-8
import unittest

from collections import Counter


class TestCounter(unittest.TestCase):
    # setUp用于做测试前的准备工作，初始化，非必要
    def setUp(self):
        self.c = Counter('abcdaba')
        print('setUp starting ...')

    def test_basics(self):
        c = self.c
        self.assertEqual(c, Counter(a=3, b=2, c=1, d=1))
        self.assertIsInstance(c, dict)
        self.assertEqual(len(c), 4)
        self.assertIn('a', c)
        self.assertNotIn('f', c)
        self.assertRaises(TypeError, hash, c)

    def test_update(self):
        c = self.c
        c.update(f=1)
        self.assertEqual(c, Counter(a=3, b=2, c=1, d=1, f=1))
        c.update(a=10)
        self.assertEqual(c, Counter(a=13, b=2, c=1, d=1, f=1))  # 注意这是累加的
    # 做测试完成后的收尾工作，非必要
    def tearDown(self):
        print('tearDown starting...')


if __name__ == '__main__':
    unittest.main()