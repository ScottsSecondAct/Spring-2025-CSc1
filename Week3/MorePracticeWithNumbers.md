# Practice with Number Systems

## Decimal Number System

The **Hindu-Arabic** or **decimal number system** is a **positional** base-10 system. This means:

1. **Digits:** The system has **ten** digits: **0, 1, 2, 3, 4, 5, 6, 7, 8, 9**.
2. **Place Value:** The position of a digit determines its value, based on powers of 10.  For example: 10<sup>6</sup>10<sup>5</sup>10<sup>4</sup>10<sup>3</sup>10<sup>2</sup>10<sup>1</sup>10<sup>0</sup>
3. **Numbers Greater Than 9:** Once you reach 9, the next number (10) requires two digits: **1** in the "tens" place and **0** in the "ones" place.

For example, in **base-10**:
\[
3045 = (3 \times 10^3) + (0 \times 10^2) + (4 \times 10^1) + (5 \times 10^0)
\]

Since any digit multiplied by 0 equals 0, we can omit that value from the calculation resulting in:
\[
3045 = (3 \times 10^3) + (4 \times 10^1) + (5 \times 10^0)
\]

## Binary Number System

The **binary number system** is a **positional** base-2 system. This means:

1. **Digits:** The system has **2** digits: **0, 1**.
2. **Place Value:** The position of a digit determines its value, based on powers of 2.  For example:   2<sup>7</sup> 2<sup>6</sup> 2<sup>5</sup> 2<sup>4</sup> 2<sup>3</sup> 2<sup>2</sup> 2<sup>1</sup> 2<sup>0</sup>.
3. **Numbers Greater Than 1:** Once you reach 1, the next number (2) requires two digits: **1** in the "twos" place and **0** in the "ones" place.




For example, in **base-2**:

1011 1110 0101

\[
3045 = (1 \times 2^{11})+(0 \times 2^{10})+(1 \times 2^9)+(1 \times 2^8)+(1 \times 2^7) + (1 \times 2^6) + (1 \times 2^5) + (0 \times 2^4) + (0 \times 2^3) +\ (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)
\]

Since any digit multiplied by 0 equals 0, we can omit that value from the calculation resulting in:

\[
3045 = (1 \times 2^{11})+(1 \times 2^9)+(1 \times 2^8)+(1 \times 2^7)+(1 \times 2^6)+(1 \times 2^5)+(1 \times 2^2) + (1 \times 2^0)
\]

## Hexadecimal Number System

The **hecadecimal number system** is a **positional** base-16 system. This means:

1. **Digits:** The system has **16** digits: **0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F**.
2. **Place Value:** The position of a digit determines its value, based on powers of 2.
3. **Numbers Greater Than 1:** Once you reach 1, the next number (2) requires two digits: **1** in the "twos" place and **0** in the "ones" place.




For example, in **base-16**:
\[
30A = (3 \times 16^2) + (0 \times 16^2) + (10 \times 16^1)
\]

Since any digit multiplied by 0 equals 0, we can omit that value from the calculation resulting in:

\[
30A = (3 \times 2^8)+(0 \times 2^7)+ (1 \times 2^6) + (0 \times 2^5) + (1 \times 2^4) + (1 \times 2^3) + (0 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)
\]

In general, in any **base-**\(b\) number system:

- The available digits range from **0** to \(b - 1\).
- A number is written using positional notation, where each digit represents a power of the base.

## Calculate the decimal value of a binary number

  _Remember the 1100 1111 is a more convenient way to write 11001111._



### Problem 1: Calculate the decimal value of the binary number: 0001 1100 1111<sub>2</sub>

\[
(0 \times 2048)+(0 \times 1024)+(0 \times 512)+(1 \times 256)+(1 \times 128)+(1 \times 64)+(0 \times 32) +(0 \times 16)+(1 \times 8)+(1 \times 4)+(1 \times 2)+(1 \times 1)
\]
1,2,4,8,16,32,64,128,256,512,1024,2048, 

234

1CF in binary 0001 1100 1111 <- Translate

1*256 + 12*16 + 15*1 = 463 <- Computation

## Calculate the decimal value of a hexadecimal number

### Problem 1: Calculate the decimal value of the hexadecimal value: 3FF<sub>16</sub>