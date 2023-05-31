import math

def effective(r,m):
    sub = r/m
    res = (1 - sub)**m
    ressy = res - 1
    return ressy

def nominal(eff, m):
    x = eff + 1
    y = x**(1/m)
    w = y - 1
    res = w*m
    return res

def continuous(original, nom, t):
    exponent = math.exp(nom*t)
    return (original*exponent)

def cont_current(future, nom, t):
    exponent = math.exp(nom*t)
    return (future/exponent)

def cont_nominal(eff):
    x = 1 + eff
    y = math.log(x)
    return y

def cont_eff(nom):
    x = math.exp(nom) - 1
    return x
    

def perpetuity(a, i):
    return (a/i)

def p_given_a(a, i, N):
    res1 = (1 + i)**N
    res2 = a*(((res1)-1)/(i*res1))
    return res2

def a_given_p(p, i, N):
    res1 = (1 + i)**N
    res2 = (i*res1)/(res1 - 1)
    res3 = p*res2
    return res3

def f_given_p(p, i, N):
    res1 = (1 + i)**N
    res2 = p*res1
    return res2

def p_given_f(f, i, N):
    res1 = (1 + i)**(-N)
    res2 = f*res1
    return res2

def f_given_a(a, i, N):
    res1 = (1 + i)**N
    res2 = a*((res1 - 1)/i)
    return res2

def a_given_f(f, i, N):
    res1 = (1 + i)**N
    res2 = f*(i/(res1 - 1))
    return res2

def p_given_g(g, i, N):
    res1 = (1 + i)**N
    res2 = (1/(i**2))*(1 - ((1+(i*N))/res1))
    res3 = g*res2
    return res3

def p_given_geom(geom, i, g, N):
    res1 = ((1+g)/(1 + i))**N
    res2 = (1 - res1)/(i -g)
    res3 = geom*(res2)
    return res3

def bond_maturing(face_val, i, comp_length, mature_time):
    res1 = (1 + (i)/(12/comp_length))
    res2 = res1**(mature_time/comp_length)
    pres_val = face_val/res2
    return pres_val

def coupon_value(face_val, i, freq):
    return ((face_val*i)/freq)

def coupon_bond(face_val, i, mature_time, coup_i, coup_freq):
    coup_val = coupon_value(face_val, coup_i, coup_freq)
    coup = p_given_a(coup_val, (i/coup_freq), (mature_time*coup_freq))
    not_da_coup = p_given_f(face_val, (i/coup_freq), (mature_time*coup_freq))
    total = coup + not_da_coup
    return total

def monthly_mortgage(principal, i, num_years):
    res = a_given_p(principal, (i/12), (num_years*12))
    return res

def left_mortgage(principle, i, term, num_years):
    principle_future = f_given_p(principle, (i/12), (term*12))
    month = monthly_mortgage(principle, i, num_years)
    pay_in_future = f_given_a(month, (i/12), (term*12))
    return (principle_future - pay_in_future)

def new_monthly_payments(principle, original_i, term, num_years, new_i):
    left = left_mortgage(principle, original_i, term, num_years)
    new = a_given_p(left, (new_i/12), ((num_years - term)*12))
    return new
    

#def yield_rate(face_val, pres_val, coup_i, coup_freq, mature_time):
    #coup_val = coupon_value(face_val, coup_i, coup_freq)
    #coup = coup_val
