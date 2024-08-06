letx = {'color': 'red', 'opt' : True}
print(letx['opt'])

alien = {'position': 'mars', 'age' : 699}
alien['x_position'] = 25
alien['y_position'] = 56
alien['speed'] = 'fast'

print(alien)
print('adjusting x_position for alien')
alien['x_position'] = 69

x_increment = 0

if alien['speed'] == 'slow':
    x_increment += 1
elif alien['speed'] == 'medium':
    x_increment += 3
else:
    print('must be fast alien')
    x_increment += 5

print('delete position')
del alien['position']

print('get position')

print(alien.get('position', 'No value'))

print(alien)

val_alien = []
for alien_number in range(10):
    val_alien.append(alien)

print(val_alien)

mesx = input('siapa namamu : ? ')
print(mesx)

print('end me')
