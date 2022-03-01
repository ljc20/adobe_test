from Adobetest import roman_numeral

class Solution(object): # this is a class and function I got from online in order to get the inverse Roman numeral so I can test my function
   def romanToInt(self, s):
      """
      :type s: str
      :rtype: int
      """
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      num = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            #print(i)
            num+=roman[s[i]]
            i+=1
      return num
ob1 = Solution()

i = 1
#x = roman_numeral(2)
#print(ob1.romanToInt(x))
while (i < 256): # I check for all numbers in the range if they are correct
    if (i != ob1.romanToInt(roman_numeral(i))): # it takes the integer converts it to a roman numeral and back to an integer and compares it to the original one
        print("error at number ", i) # only prints if there is an error
    i +=1

# if there is no output means that the function is correct