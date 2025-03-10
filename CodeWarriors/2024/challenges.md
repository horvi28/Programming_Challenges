# Challenges

## Challenge 1

Write a function based on the following examples:

* task01("abcd") -> "A-Bb-Ccc-Dddd"
* task01("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
* task01("cwAt") -> "C-Ww-Aaa-Tttt"
* "ZpglnRxqenU" -> "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
* "EquhxOswchE" -> "E-Qq-Uuu-Hhhh-Xxxxx-Oooooo-Sssssss-Wwwwwwww-Ccccccccc-Hhhhhhhhhh-Eeeeeeeeeee"

input: Randomly generated strings (as above) in the range 1-100.

## Challenge 2

Greed is a dice game played with give six-sided dice. Your task is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

* Three 1's => 1000 points
* Three 6's =>  600 points
* Three 5's =>  500 points
* Three 4's =>  400 points
* Three 3's =>  300 points
* Three 2's =>  200 points
* One 1     =>  100 points
* One 5     =>   50 points

## Challenge 3

## Challenge 3.5

Create a function that calculates the count of n-digit strings with the same sum for the first half and second half of their digits. These digits are referred to as "lucky" digits.

Examples

* Input: 2 ➞ Output: 10 # "00", "11", "22", "33", "44", "55", "66", "77", "88", "99"
* Input: 4 ➞ Output: 670
* Input: 6 ➞ Output: 55252 # "000000", "001010", "112220", ..., "999999"

Rules

* The value of n will always be even.
* 2 <= n <= 150
* To avoid hard-coding, your code limit should be <= 250 characters

Form

```python
def tickets(n):
      #your code here
```
