def lunar_lander():
 
    restart_game = True

    print(''' Starting fuel: 1000 liters\n Starting altitude: 1000 meters
 Starting velocity: 0.0 m/s\n gravity: 1.6 m/s\n constant: 0.15 \n''')
    #add outer WHILE loop to restart the game
    while restart_game:
        remaining_fuel = 100.0 
        altitude = 100.0
    
        total_velocity = 0.0 #total over time
        altitude_post_fuel_burned = 0.0 #change this name to "altitude..."
        gravity = -1.6 #negative because going down
        change_in_velocity = 0.0 #can be zero; changes each turn
    
        seconds_elapsed = 0 
        fuel_constant = 0.15

        while altitude > 0:
            seconds_elapsed += 1
            fuel_burned = int(input("How much fuel do you want to burn? "))

            if remaining_fuel > 0:
                if fuel_burned > remaining_fuel: #if user burns more fuel than they have left
                    remaining_fuel = 0
                    altitude_post_fuel_burned = 0
                    fuel_burned = remaining_fuel
                    print("this thing works")
                elif fuel_burned > 0: 
                    altitude_post_fuel_burned = fuel_burned * fuel_constant 
                    remaining_fuel -= fuel_burned
                    print("remaining fuel:", remaining_fuel)
                elif fuel_burned == 0 or fuel_burned < 0: #
                    altitude_post_fuel_burned = 0
                    remaining_fuel -= fuel_burned
                    print("remaining fuel:", remaining_fuel)
            
            else:
                print("just so you know, you're out of fuel")
                altitude_post_fuel_burned = 0              
        
            total_velocity += gravity + altitude_post_fuel_burned 
            altitude += total_velocity 
            print("altitude", altitude)
            
            print("total velocity:", abs(total_velocity)) 
                
        if abs(total_velocity) < 10.0:
            print("Right on! You landed safely!\n", "Your final velocity was:", abs(total_velocity), "\nIt took you", seconds_elapsed, "seconds to land the ship\nYou still had", remaining_fuel, "liters left in the tank") 
        else:
            print("Sorry dude. You didn't land safely\n", "Your final velocity was:", abs(total_velocity), "\nIt took you", seconds_elapsed, "seconds to crash your ship\nYou still had", remaining_fuel, "liters left in the tank")

        ask_for_restart = input(("do you want to play again? y/n ").lower())
        if ask_for_restart.startswith('y'):
            restart_game = True
            print("Right on. Welcome back!")
        elif ask_for_restart.startswith('n'):
            restart_game = False
            print("Later.")
        else:
            print("That's not an appropriate response.")
            restart_game = False
            ask_for_restart = input(("do you want to play again? y/n ").lower())
            
lunar_lander()


     
