import unittest as ut
import main_func1 as mf
import settings
import random as rand


class Tests(ut.TestCase):

    def test_stuffing(self):  # testowanie funkcji przygotowującej do zakodowania
        data = "0111111110111111011011"
        self.assertEqual(
            "011111011101111101011011",
            mf.stuffing(data)
        )

    def test_de_stuffing(self):  # testowanie funkcji przygotowującej do zedekodowania
        data = "0111111110111111011011"
        self.assertEqual(
            data,
            mf.de_stuffing("011111011101111101011011")
        )

    def test_enc_frame(self):  # testowanie funkcji kodującej
        data = "0111111110111111011011"
        self.assertEqual(
            settings.START_MARKER +
            mf.stuffing(data + mf.count_crc(data))
            + settings.END_MARKER,
            mf.enc_frame(data)
        )

    def test_dec_frame(self):   # testowanie funkcji dekodującej
        data = "{0:b}".format((rand.randint(2 ^ 31, 2 ^ 32)))
        self.assertEqual(
            data,
            mf.dec_frame(mf.enc_frame(data))
        )


if __name__ == '__main__':
    ut.main()
