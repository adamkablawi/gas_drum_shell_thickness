import math
type_choice = input("'shell' or 'head'?: ")

if type_choice == "shell":
            
    shell_choice = input("Enter A for Cylindrical or B for Conical: ")
    if shell_choice == "A":
        D = float(input("Enter the inner diameter in mm: ")) 
        P = float(input("Enter the internal design pressure in N/mm^2: ")) 
        S = float(input("Enter the allowable stress value in N/mm^2: ")) 
        E = float(input("Enter the efficiency (weld joint factor): ")) 
        CI = float(input("Enter the internal corrosion allowance in mm: ")) 
        CE = float(input("Enter the external corrosion allowance in mm: ")) 
        t = (D/2)*(math.exp(P/(S*E)) - 1) + CE + CI
        print("The optimal thickness is " + str(t) + " millimeters.")
    elif shell_choice == "B":
        D = float(input("Enter the inner diameter in mm: ")) 
        P = float(input("Enter the internal design pressure in N/mm^2: ")) 
        S = float(input("Enter the allowable stress value in N/mm^2: ")) 
        CI = float(input("Enter the internal corrosion allowance in mm: ")) 
        CE = float(input("Enter the external corrosion allowance in mm: ")) 
        E = float(input("Enter the efficiency (weld joint factor): "))    
        a = float(input("Enter the half apex angle of the cone (degrees): "))   
        t = (D/(2*math.cos(a)))*(math.exp(P/(S*E)) - 1) + CE + CI
        print("The optimal thickness is " + str(t) + " millimeters.")
    else:
        print("Error, enter either 'A' or 'B'.")

elif type_choice == "head":

    head_choice = input("Enter A for Spherical/Hemispherical, B for Topispherical, or C for Ellipsoidal: ")
    if head_choice == "A":
        D = float(input("Enter the inner diameter in mm: ")) 
        P = float(input("Enter the internal design pressure in N/mm^2: ")) 
        S = float(input("Enter the allowable stress value: ")) 
        E = float(input("Enter the efficiency (weld joint factor): ")) 
        CI = float(input("Enter the internal corrosion allowance in mm: ")) 
        CE = float(input("Enter the external corrosion allowance in mm: ")) 
        t = ((D+2*CI)/2)*(math.exp(P/(S*E)) - 1) + CE + CI
        print("The optimal thickness is " + str(t) + " millimeters.")
    elif head_choice == "B":
        same_different_choice = input("Are the Crown and knuckle the 'same' or 'different'?: ")
        D = float(input("Enter the inner diameter in mm: ")) 
        L = float(input("Enter the crown radius: ")) 
        R = float(input("Enter the knuckle radius: ")) 
        T = float(input("Enter the wall thickness: ")) 
        E = float(input("Enter the modulus of elasticity at maximum design temperature: ")) 
        P = float(input("Enter the internal design pressure in N/mm^2: ")) 
        Sy = float(input("Enter the yield strength: ")) 
        S = float(input("Enter the allowable stress value: ")) 
        if same_different_choice == "same":
            if 0.7<=(L/D)<=1.0 and (R/D)>=0.06 and 20<=(L/T)<=2000:
                b = math.acos(((0.5*D)-R)/(L-R))
                p = math.sqrt(L*T)/R
                if b > p:
                    z = (((0.5*D)-R)/(math.cos(b-p))) + R
                elif b <= p:  
                    z = 0.5*D  
                if (R/D) <= 0.08:
                    C1 = 9.31(R/D)-0.086
                    C2 = 1.25
                elif (R/D) > 0.08:
                    C1 = 0.692(R/D) + 0.605
                    C2 = 1.46 - 2.6(R/D)
                IntPresElaBuck = (C1*E*T*T)/(C2*z*((z/2)-R))
                allowable_stress = input("Enter A if the allowable stress at the design temperature is governed by time-independent properties, or B if the allowable stress at the design temperature is governed by time-dependent properties: ")
                if allowable_stress == "A":
                    C3 = Sy
                elif allowable_stress == "B":
                    criterion = input("Enter A if the allowable stress is on the 90% criterion, or B if on the 67% criterion: ")
                    if criterion == "A":
                        C3 = 1.1*S
                    elif criterion == "B":
                        C3 = 1.5*S
                IntPressMaxStress = (C3*T)/(C2*z*((z/(2*R))-1))
                G = IntPresElaBuck/IntPressMaxStress
                if G <= 1.0:
                    IntPresBuckFail=0.6*IntPresElaBuck
                elif G>1.0:
                    IntPresBuckFail=((0.77508*G - 0.20354*G*G + 0.019274*G*G*G)/(1 + 0.19014*G - 0.089534*G*G + 0.0093965*G*G*G))*IntPressMaxStress
                allowpresknuckle=IntPresBuckFail/1.5
                allowprescrown=(2*S*E)/((L/T)+0.5)
                maxallowintpres = min[allowprescrown,allowpresknuckle]
                if maxallowintpres>=P:
                    print("The design is complete.")
                elif maxallowintpres<P:
                    print("Increase head thickness and repeat.")
            else:
                print("Unfortunately, the values inputted do not meet the standards. This must be designed in accordance to Part 5 of ASME BPVC VIII-2.")
        elif same_different_choice == "different":
            minreqthicksphere = (D/2)*(math.exp(P/(S*E)) - 1)
            if 0.7<=(L/D)<=1.0 and (R/D)>=0.06 and 20<=(L/T)<=2000:
                b = math.acos(((0.5*D)-R)/(L-R))
                p = math.sqrt(L*T)/R
                if b > p:
                    z = (((0.5*D)-R)/(math.cos(b-p))) + R
                elif b <= p:  
                    z = 0.5*D  
                if (R/D) <= 0.08:
                    C1 = 9.31(R/D)-0.086
                    C2 = 1.25
                elif (R/D) > 0.08:
                    C1 = 0.692(R/D) + 0.605
                    C2 = 1.46 - 2.6(R/D)
                IntPresElaBuck = (C1*E*T*T)/(C2*z*((z/2)-R))
                allowable_stress = input("Enter A if the allowable stress at the design temperature is governed by time-independent properties, or B if the allowable stress at the design temperature is governed by time-dependent properties: ")
                if allowable_stress == "A":
                    C3 = Sy
                elif allowable_stress == "B":
                    criterion = input("Enter A if the allowable stress is on the 90% criterion, or B if on the 67% criterion: ")
                    if criterion == "A":
                        C3 = 1.1*S
                    elif criterion == "B":
                        C3 = 1.5*S
                IntPressMaxStress = (C3*T)/(C2*z*((z/(2*R))-1))
                G = IntPresElaBuck/IntPressMaxStress
                if G <= 1.0:
                    IntPresBuckFail=0.6*IntPresElaBuck
                elif G>1.0:
                    IntPresBuckFail=((0.77508*G - 0.20354*G*G + 0.019274*G*G*G)/(1 + 0.19014*G - 0.089534*G*G + 0.0093965*G*G*G))*IntPressMaxStress
                allowpresknuckle=IntPresBuckFail/1.5
                allowprescrown=(2*S*E)/((L/T)+0.5)
                maxallowintpres = min[allowprescrown,allowpresknuckle]
                if maxallowintpres>=P:
                    print("The design is complete.")
                elif maxallowintpres<P:
                    print("Increase head thickness and repeat.")
            else:
                print("Unfortunately, the values inputted do not meet the standards. This must be designed in accordance to Part 5 of ASME BPVC VIII-2.")
        else:
            print("You must choose 'same' or 'different'.")
    elif head_choice == "C":
        D = float(input("Enter the inner diameter in mm: ")) 
        L = float(input("Enter the crown radius: ")) 
        R = float(input("Enter the knuckle radius: ")) 
        T = float(input("Enter the wall thickness: ")) 
        E = float(input("Enter the modulus of elasticity at maximum design temperature: ")) 
        P = float(input("Enter the internal design pressure in N/mm^2: ")) 
        Sy = float(input("Enter the yield strength: ")) 
        S = float(input("Enter the allowable stress value: ")) 
        h = float(input("Enter the height of the ellipsoidal head: ")) 
        k = D/(2*h)
        R = D((0.5/k) - 0.08)
        L = D(0.44*k +0.02)
        if 1.7<= k <= 2.2:
            if 0.7<=(L/D)<=1.0 and (R/D)>=0.06 and 20<=(L/T)<=2000:
                b = math.acos(((0.5*D)-R)/(L-R))
                p = math.sqrt(L*T)/R
                if b > p:
                    z = (((0.5*D)-R)/(math.cos(b-p))) + R
                elif b <= p:  
                    z = 0.5*D  
                if (R/D) <= 0.08:
                    C1 = 9.31(R/D)-0.086
                    C2 = 1.25
                elif (R/D) > 0.08:
                    C1 = 0.692(R/D) + 0.605
                    C2 = 1.46 - 2.6(R/D)
                IntPresElaBuck = (C1*E*T*T)/(C2*z*((z/2)-R))
                allowable_stress = input("Enter A if the allowable stress at the design temperature is governed by time-independent properties, or B if the allowable stress at the design temperature is governed by time-dependent properties: ")
                if allowable_stress == "A":
                    C3 = Sy
                elif allowable_stress == "B":
                    criterion = input("Enter A if the allowable stress is on the 90% criterion, or B if on the 67% criterion: ")
                    if criterion == "A":
                        C3 = 1.1*S
                    elif criterion == "B":
                        C3 = 1.5*S
                IntPressMaxStress = (C3*T)/(C2*z*((z/(2*R))-1))
                G = IntPresElaBuck/IntPressMaxStress
                if G <= 1.0:
                    IntPresBuckFail=0.6*IntPresElaBuck
                elif G>1.0:
                    IntPresBuckFail=((0.77508*G - 0.20354*G*G + 0.019274*G*G*G)/(1 + 0.19014*G - 0.089534*G*G + 0.0093965*G*G*G))*IntPressMaxStress
                allowpresknuckle=IntPresBuckFail/1.5
                allowprescrown=(2*S*E)/((L/T)+0.5)
                maxallowintpres = min[allowprescrown,allowpresknuckle]
                if maxallowintpres>=P:
                    print("The design is complete.")
                elif maxallowintpres<P:
                    print("Increase head thickness and repeat.")
            else:
                print("Unfortunately, the values inputted do not meet the standards. This must be designed in accordance to Part 5 of ASME BPVC VIII-2.")
        else:
            print("Unfortunately, the values inputted do not meet the standards. This must be designed in accordance to Part 5 of ASME BPVC VIII-2.")
    else:
        print("Error, enter either 'A', 'B', or 'C'.")

else:
    print("Please input a 'Shell' or a 'Head'.")

