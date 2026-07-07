class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        array=[""]*n
        for i in range(1,n+1):
            if i%15==0:
                array[i-1]="FizzBuzz"
            elif i%3==0:
                array[i-1]="Fizz"   
            elif i%5==0:
                array[i-1]="Buzz"   
            else:
                array[i-1]=str(i)   
        return array        
