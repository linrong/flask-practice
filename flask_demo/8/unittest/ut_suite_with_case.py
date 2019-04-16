#! /usr/bin/env python 
# coding=utf-8
import unittest
from ut_case import TestCounter


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCounter('test_basics')) # 可以添加测试用例中的方法
    suite.addTest(TestCounter('test_update'))
    runner = unittest.TextTestRunner()
    runner.run(suite)