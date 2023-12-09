def ist_primzahl(p):
    if p > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(p/2)+1):
            # If p is divisible by any number between
            # 2 and n / 2, it is not prime
            if (p % i) == 0:
                return False
        else:
            return True
    else:
        return False


#========== nur dieser Code-Abschnitt ist gefragt ==========

def naechst_groessere_primzahl(m):
    while ist_primzahl(m) != True:
        m += 1

    return m

#========== nur dieser Code-Abschnitt ist gefragt ==========

print(naechst_groessere_primzahl(234))

    