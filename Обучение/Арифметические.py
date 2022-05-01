#pow(num, n) степень
#sqrt() корень
#ceil() наибольшее целое
#floor() наименьшее целое
#factorial()
#deegrees(rad)
#radians(grad)
import math
print(math.pow(2,3))
print(math.e)
print(math.pi)

print("\n********************\n")
print(0.1+0.1+0.1)
from decimal import Decimal
n = Decimal ("0.1")
n2 = Decimal ("0.010")
print(n + n + n2 + 2)
print()

#округление
n = Decimal ("0.446")
n = n.quantize(Decimal("1.00"))
print (n)
