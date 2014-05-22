import math

class ErrorCheck:
    def _init_(self):
        pass
    def biti_red(self, bynaryCode):
        bynaryCodeLength = len(bynaryCode)
        nNumber = int(math.log(len(bynaryCode),2))
        
        while int(math.log(nNumber+bynaryCodeLength,2)) > nNumber:
            nNumber=int(math.log(nNumber+bynaryCodeLength,2))
        return nNumber
    
    def encode(self,bynaryCode):
        
        bynaryCodeLengthEncoded = len(bynaryCode) + self.biti_red(bynaryCode)+1
        bynaryEncoded = [0]*bynaryCodeLengthEncoded
        
        i1=1
        i2=0
        while i1<=bynaryCodeLengthEncoded:
            if not(i1 & (i1-1)):
                bynaryEncoded[i1-1] = 'X'
            else:
                bynaryEncoded[i1-1] = bynaryCode[i2]
                i2+=1
            i1+=1
        i1=1
        while i1<bynaryCodeLengthEncoded:
            sum = 0
            i2=i1
            while i2<bynaryCodeLengthEncoded:
                i3=i2
                while i3<(i2+i1) and i3<bynaryCodeLengthEncoded:
                    if bynaryEncoded[i3] != 'X':
                        sum+=ord(bynaryEncoded[i3])-48
                    
                    i3+=1
                i2+=(i1+1)
            bynaryEncoded[i1-1]=str(sum%2)
            i1<<=1
        return bynaryEncoded

    def decode(self, binaryToDecode):
        nFlag = 0
        bynaryCodeLengthEncoded=len(binaryToDecode)
        i1=1
        while i1<bynaryCodeLengthEncoded:
            sum = 0
            i2=i1
            while i2<bynaryCodeLengthEncoded:
                i3=i2
                while i3<(i2+i1) and i3<bynaryCodeLengthEncoded:
                    if i3 & (i3-1):
                        sum+=ord(binaryToDecode[i3])
                    
                    i3+=1
                i2+=(i1+1)
            if str(sum%2) != binaryToDecode[i1-1]:
                nFlag+=(i1-1)
            i1<<=1
        return nFlag
                

error = ErrorCheck()

print("Codul initial : 1001 ")
print(error.encode("1001"))

print("Codul primit : 0111001")

print(error.decode("0111001"))   
