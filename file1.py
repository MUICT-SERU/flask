def main():
    var l = {'a','b','c','d','e'}
    for i in range(len(l)):
        x = l[i]
        y = l[i+1]
    try:
        x = next(i for i, n in enumerate(l) if n > 0)
    except StopIteration:
        print('No positive numbers')
    else:
        print('The index of the first positive number is', x)

def i4():
        home = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
        home_triple = {x:y for (x,y) in home.items() if y>2 if y%2 == 0 if y%3 == 0}
        print(home_triple)

def i5():
    fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
    #Get the corresponding `celsius` values
    celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))
    #Create the `celsius` dictionary
    celsius_dict = dict(zip(fahrenheit.keys(), celsius))
    print(celsius_dict) 