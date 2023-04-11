# CHAPTER2:Representing and Manipulating Infomation

## 2.1 Information Storage

### Practice Problem 2.1

Perform the following number conversions:

A. 0x25B9D2 to binary

* 0010 0101 1010 1001 1101 0010

B. binary 1010 1110 0100 1001 to hexadecimal

* 0xAE49

C. 0xA8B3D to binary

* 1010 1000 1011 0011 1101

D. binary 11 0010 0010 1101 1001 0110 to hexadecimal

* 0x322D96



### Practice Problem 2.2

Fill in the blank entries in the following table, giving the decimal and hexadecimal representations of different powers of 2:

| n    | 2^n^ (decimal) | 2^n^(hex)          |
| ---- | -------------- | ------------------ |
| 5    | 32             | 0x20               |
| 23   | 4294967296     | 0x800000 (3 + 5*4) |
| 15   | 32,768         | 0x8000 (3 + 3*4)   |
| 13   | 8,192          | 0x2000 (1 + 3*4)   |
| 12   | 4,096          | 0x1000 (0 + 3*4)   |
| 6    | 64             | 0x40 (2 + 1*4)     |
| 9    | 512            | 0x100 (1+2*4)      |



### Practice Problem 2.3

A single byte can be represented by 2 hexadecimal digits. Fill in the missing entries in the following table, giving the decimal, binary, and hexadecimal values of different byte patterns:

| Decimal | Binary    | Hexadecimal |
| ------- | --------- | ----------- |
| 0       | 0000 0000 | 0x00        |
| 158     | 1001 1110 | 0x9E        |
| 76      | 0100 1100 | 0x4C        |
| 145     | 1001 0001 | 0x91        |
| 175     | 1010 1110 | 0xAE        |
| 60      | 0011 1100 | 0x3C        |
| 241     | 1111 0001 | 0xF1        |
| 117     | 0111 0101 | 0x75        |
| 189     | 1011 1101 | 0xBD        |
| 251     | 1111 0101 | 0xF5        |



### Practice Problem 2.4

Without converting the numbers to decimal or binary, try to solve the following arithmetic problems, giving the answers in hexadecimal. *Hint:* Just modify the methods you use for performing decimal addition and subtraction to use base 16.

1. 0x605c+0x5=0x6061
2. 0x605c − 0x20 =0x603c
3. 0x605c+32=0x605c + 0x0020 = 0x607c
4. 0x60fa−0x605c= 0x00ad



### Practice Problem 2.5

Consider the following three calls to show_bytes:

```c
 int a = 0x12345678;
 byte_pointer ap = (byte_pointer) &a;
 show_bytes(ap, 1); /* A. */
 show_bytes(ap, 2); /* B. */
 show_bytes(ap, 3); /* C. */
```

Indicate the values that will be printed by each call on a little-endian machine and on a big-endian machine:

| Little endian | Big endian |
| ------------- | ---------- |
| 78            | 78         |
| 78 56         | 56 78      |
| 78 56 34      | 34 56 78   |



### Practice Problem 2.6

Using show_int and show_float, we determine that the integer 2607352 has hexa- decimal representation 0x0027C8F8, while the floating-point number 3510593.0 has hexadecimal representation 0x4A1F23E0.

1. Write the binary representations of these two hexadecimal values.

    0000 0000 0010 0111 1100 1000 1111 1000

    0100 1010 0001 1111 0010 0011 1110 0000

2. Shift these two strings relative to one another to maximize the number of matching bits. How many bits match?

    11 0010 0011 1110 00 match

3. What parts of the strings do not match?



### Practice Problem 2.7

What would be printed as a result of the following call to show_bytes? const char *m = "mnopqr";

show_bytes((byte_pointer) m, strlen(m));

Note that letters ‘a’ through ‘z’ have ASCII codes 0x61 through 0x7A.



0x6d6e6f707172



### Pratice Problem 2.8

Fill in the following table showing the results of evaluating Boolean operations on bit vectors.

| Operation | Result     |
| --------- | ---------- |
| a         | [01001110] |
| b         | [11100001] |
| ~a        | [10110001] |
| ~b        | [00011110] |
| a&b       | [01000000] |
| a\|b      | [11101111] |
| a^b       | [10101111] |



### Practice Problem 2.9

