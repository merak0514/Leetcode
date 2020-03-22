# Time: O()     ms
# Memory: O()   MB
from typing import *
from unittest import TestCase
from unittest import skip
import brute_force_2
import brute_force_1
import brute_force_3


class TestSolution(TestCase):
    def setUp(self) -> None:
        bf1 = brute_force_1.Solution()
        bf2 = brute_force_2.Solution()
        bf3 = brute_force_3.Solution()
        self.t = bf1

    def test_longestPalindrome(self):
        s = 'asfsa'
        ans = 'asfsa'
        print('\n')
        print('\n', self.t.longestPalindrome(s))
        self.assertEqual(ans, self.t.longestPalindrome(s))

    def test_1(self):
        s = 'aaabbb'
        ans = 'aaa'
        self.assertEqual(ans, self.t.longestPalindrome(s))

    def test_2(self):
        s = 'atabab'
        ans = 'ata'
        self.assertEqual(ans, self.t.longestPalindrome(s))

    def test_3(self):
        s = 'ahkhagg'
        ans = 'ahkha'
        self.assertEqual(ans, self.t.longestPalindrome(s))

    def test_4(self):
        s = 'ahabhhb'
        ans = 'bhhb'
        self.assertEqual(ans, self.t.longestPalindrome(s))

    def test_5(self):
        s = 'abcdbbfcba'
        ans = 'bb'
        self.assertEqual(ans, self.t.longestPalindrome(s))

    # @skip
    def test_6(self):
        # bf1: 7.84s
        # bf2: 17.4s
        # bf3: 14s

        s = "esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq"
        s = s+s
        s = s+s


        self.t.longestPalindrome(s)
