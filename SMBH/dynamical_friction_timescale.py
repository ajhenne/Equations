import math

G = 6.67e-11
M_g = (10**11)*(1.988*10**30)
R_g = (10**3)*(3.086*10**16)
C = 10
t_universe_years = 13.77*10**9 #years
t_universe_seconds = t_universe_years * 3.154*10**7

rho = (3*M_g)/(4*math.pi*((R_g)**3))
v_0 = (G*M_g/R_g)**(1/2)

M = (v_0**3)/(12*math.pi*C*(G**2)*t_universe_seconds*rho)
# in kg

M_SolarUnits = M / (1.988e+30)

print(M)
print(M_SolarUnits)


M_2 = (M_g/(9*C*t_universe_seconds))*(((R_g**3)/(G*M_g))**(1/2))
M_2_SolarUnits = M_2 / (1.988e+30)
print(M_2_SolarUnits)
