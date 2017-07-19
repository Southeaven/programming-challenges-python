def is_scale_valid(option):
    try:
        int(option)
        return True
    except:
        return False

def is_temperature_valid(temperature):
    try:
        float(temperature)
        return True
    except:
        return False

def c_to_f(temperature):
    return temperature * 1.8 + 32

def f_to_c(temperature):
    return (temperature - 32) / 1.8

def c_to_k(temperature):
    return temperature + 273.15

def k_to_c(temperature):
    return temperature - 273.15

def convert(temperature, scale_from, scale_to):
    if scale_from == scale_to:
        return temperature
    if scale_from == 1:
        if scale_to == 2:
            return c_to_f(temperature)
        else:
            return c_to_k(temperature)
    elif scale_from == 3:
        if scale_to == 1:
            return k_to_c(temperature)
        else:
            return c_to_f(k_to_c(temperature))
    else:
        if scale_to == 1:
            return f_to_c(temperature)
        else:
            return c_to_k(f_to_c(temperature))

if __name__ == '__main__':
    print('What is the scale you want to convert from?\n[1] Celsius\n[2] Fahrenheit\n[3] Kelvin')
    while True:
        scale_from = input()
        if is_scale_valid(scale_from):
            scale_from = int(scale_from)
            if 1 <= scale_from <= 3:
                break
            else:
                print('Wrong input, try again!')
        else:
            print('Wrong input, try again!')
    print('What is the scale you want to convert to?\n[1] Celsius\n[2] Fahrenheit\n[3] Kelvin')
    while True:
        scale_to = input()
        if is_scale_valid(scale_to):
            scale_to = int(scale_to)
            if 1 <= scale_to <= 3:
                break
            else:
                print('Wrong input, try again!')
        else:
            print('Wrong input, try again!')
    print('Input the temperature you want to convert')
    while True:
        temperature = input()
        if is_temperature_valid(temperature):
            temperature = float(temperature)
            break
        else:
            print('Wrong input, try again!')
    print(convert(temperature, scale_from, scale_to))
