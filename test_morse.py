#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from morse import decodeMorse, decodeBits


class TestMorse(unittest.TestCase):

    def test_hey_jude(self):
        """Basic HEY JUDE"""
        self.assertEqual(decodeMorse(decodeBits(
            '1100110011001100000011000000111111001100111111001111110000000000'
            '0000110011111100111111001111110000001100110011111100000011111100'
            '11001100000011')),
            'HEY JUDE')

    def test_basic_bits(self):
        """Basic bits decoding"""
        self.assertEqual(decodeMorse(decodeBits('1')), 'E')
        self.assertEqual(decodeMorse(decodeBits('101')), 'I')
        self.assertEqual(decodeMorse(decodeBits('10001')), 'EE')
        self.assertEqual(decodeMorse(decodeBits('10111')), 'A')
        self.assertEqual(decodeMorse(decodeBits('1110111')), 'M')

    def test_multiple_bits_per_dot(self):
        """Multiple bits per dot handling"""
        self.assertEqual(decodeMorse(decodeBits('111')), 'E')
        self.assertEqual(decodeMorse(decodeBits('1111111')), 'E')
        self.assertEqual(decodeMorse(decodeBits('110011')), 'I')
        self.assertEqual(decodeMorse(decodeBits('111000111')), 'I')
        self.assertEqual(decodeMorse(decodeBits('111110000011111')), 'I')
        self.assertEqual(decodeMorse(decodeBits('111000000000111')), 'EE')
        self.assertEqual(decodeMorse(decodeBits('11111100111111')), 'M')
        self.assertEqual(decodeMorse(decodeBits('111000111000111')), 'S')
        self.assertEqual(decodeMorse(decodeBits(
            '1111110000001111110000001111'
            '11000000111111000000000000000000111111000000000000000000111111111111'
            '11111100000011111100000011111111111111111100000011111111111111111100'
            '00000000000000000000000000000000000000001111110000001111111111111111'
            '110000001111111111111111110000001111111111111111110000000000000000001'
            '111110000001111110000001111111111111111110000000000000000001111111111'
            '11111111000000111111000000111111000000000000000000111111')),
            'HEY JUDE')

    def test_extra_zeroes(self):
        """Extra zeros handling"""
        self.assertEqual(decodeMorse(decodeBits('01110')), 'E')
        self.assertEqual(decodeMorse(decodeBits('000000011100000')), 'E')

    def test_long_messages(self):
        """Long messages handling"""
        self.assertEqual(decodeMorse(decodeBits(
            '0001110001010101000100000001110111010111000101011100010100011101'
            '0111010001110101110000000111010101000101110100011101110111000101'
            '1101110001110100000001010111010001110111011100011101010111000000'
            '01011101110111000101011100011101110001011101110100010101000000011'
            '10111011100010101011100010001011101000000011100010101010001000000'
            '01011101010001011100011101110101000111010111011100000001110101000'
            '11101110111000111011101000101110101110101110')),
            'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')
        self.assertEqual(decodeMorse(decodeBits(
            '1111111111111110000000000000001111100000111110000011111000001111'
            '1000000000000000111110000000000000000000000000000000000011111111'
            '1111111000001111111111111110000011111000001111111111111110000000'
            '0000000011111000001111100000111111111111111000000000000000111110'
            '0000111110000000000000001111111111111110000011111000001111111111'
            '1111100000111110000000000000001111111111111110000011111000001111'
            '1111111111100000000000000000000000000000000000111111111111111000'
            '00111110000011111000001111100000000000000011111000001111111111111'
            '11000001111100000000000000011111111111111100000111111111111111000'
            '00111111111111111000000000000000111110000011111111111111100000111'
            '11111111111100000000000000011111111111111100000111110000000000000'
            '00000000000000000000001111100000111110000011111111111111100000111'
            '11000000000000000111111111111111000001111111111111110000011111111'
            '111111100000000000000011111111111111100000111110000011111000001111'
            '11111111111000000000000000000000000000000000001111100000111111111'
            '11111100000111111111111111000001111111111111110000000000000001111'
            '10000011111000001111111111111110000000000000001111111111111110000'
            '0111111111111111000000000000000111110000011111111111111100000111111111111111000001111100000000000000011111000001111100000111110000000000000000000000000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111000001111111111111110000000000000001111100000000000000011111000001111111111111110000011111000000000000000000000000000000000001111111111111110000000000000001111100000111110000011111000001111100000000000000011111000000000000000000000000000000000001111100000111111111111111000001111100000111110000000000000001111100000111111111111111000000000000000111111111111111000001111111111111110000011111000001111100000000000000011111111111111100000111110000011111111111111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111111111111110000011111111111111100000111110000000000000001111100000111111111111111000001111100000111111111111111000001111100000111111111111111')), 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')


if __name__ == '__main__':
    unittest.main(verbosity=2)
