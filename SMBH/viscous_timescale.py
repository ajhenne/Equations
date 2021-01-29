# calculation of viscous timescale

k = (1.38064852*10**-23)
T = 10**7
G = 6.67*10**(-11)
M = (10**8) * 1.998*10**30
c = 2.998*10**8
mu = 0.5
m_h = 1.66*10**(-24)
R = 7.405*10**(15)

alpha = 0.3
print(alpha)

omega = (G*M/(R**3))**(1/2)
print(omega)
inv_omega = omega**(-1)
print(inv_omega)


R_s = 2*G*M/(c**2)
print(R_s)

HoverR = (((k*R_s*T)/(G*M*mu*m_h))**(1/2))*((R/R_s)**(-3/16))
print(HoverR)
HoverRsquared = HoverR**2
RoverHsquared = HoverRsquared**(-1)
print(RoverHsquared)

timescale = (1/alpha) * RoverHsquared * inv_omega
print(timescale) # seconds

seconds_year = 60*60*24*365
print(seconds_year)

print(timescale/seconds_year)
