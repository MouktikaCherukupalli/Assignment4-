def main():
    T= 4/5  # Probability that A tells truth
    F= 1/5 # Probability that A tells false
    HC= 1/2  # Probability that head appears on coin
    TC = 1/2 # Probability that tails appears on coin

    #Output
    print(f"The probability that actually there was a head is {Prob(T,F,HC,TC)}")

         
def Prob(t,f,hc,tc) -> float:
        
        return t*hc/(t*hc + f*tc)

if __name__ == '__main__':
       main()