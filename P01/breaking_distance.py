#define const
G = 9.81

#get user input for speed 
v0 = float(input('v0 [km/h]?'))

#transform from km/h to m/s
v0 = v0/3.6

#get user input for friction
mu = input('friction coefficient? If not defined there is no friction')

#set mu to 1 if no friction is applied
if mu == '':
    print('coefficient not defined')
    mu = 1

else:
    mu = float(mu)




d = .5*v0**2/(mu*G)
d = round(d, 2)
print('The car needs ' + str(d) + ' meters to stand still.')