def calculate_time():
    volume = float(input('Enter the volume of water in millilitres: '))
    temp = float(input('Enter the initial temperature of the water in '
                       'degrees celsius: '))
    power = float(input('Enter the power of the kettle in watts: '))
    energy_needed = 4.184 * volume * (100 - temp)
    time_needed = energy_needed / power
    print(f'The water should take around {int(time_needed // 60)} minutes and'
          f' {round(time_needed % 60)} seconds to boil.')


if __name__ == '__main__':
    calculate_time()
