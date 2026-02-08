def gcd(a: int, b: int) -> int:
      """
      Calculate the greatest common divisor (GCD) of two integers a and b
      using the Euclidean algorithm.
      """
      # Implement your solution here
      
      if a ==0 and b==0:
            return None
      a= abs(a)
      b= abs(b)
      
      if b == 0:
            return a
      return gcd(b, a % b)
