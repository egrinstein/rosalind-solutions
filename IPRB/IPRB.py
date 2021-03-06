#!/usr/bin env python


def dominant_prob(Dominant,Heter,Recessive):
    
    total = Dominant + Heter + Recessive

    prob2Dom = (Dominant/float(total))*((Dominant-1)/float(total-1))

    probDomHeter = 2*(Dominant/float(total))*((Heter)/float(total-1))

    prob2Heter = (Heter/float(total))*((Heter-1)/float(total-1)) * 0.75

    probDomRecessive = 2*(Dominant/float(total))*((Recessive)/float(total-1))

    probHeterRecessive = 2*(Heter/float(total))*((Recessive)/float(total-1))*0.5

    return prob2Dom + probDomHeter + prob2Heter + probDomRecessive + probHeterRecessive



