"""

mac 255.252.0.0.
ip: 252.67.33.87

mac 1111.1111_1111.11(00)_0000.0000_0000.0000
ip: 1111.1100_0100.00(11)_0010.0001_0101.0111
ad: 1111.1100_0100.00(00)_0000.0000_0000.0000

левые 2 байта: 7 || 7 + ''.join(p)[:2].count('1')
правые 2 байта: ||

"""
import itertools
print(len([p for p in itertools.product('01', repeat=18) if \
        (''.join(p)[2:].count('1')) / (7 + ''.join(p)[:2].count('1')) > 2]))