class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        suml = sumr = ql = qr = 0

        for i in range(n):
            if i < n//2:
                if num[i] == "?":
                    ql +=1
                else:
                    suml+=int(num[i])
            else:

                if num[i] == "?":
                    qr +=1
                else:
                    sumr += int(num[i])
        return 2*(suml-sumr) != 9*(qr-ql)



        

    