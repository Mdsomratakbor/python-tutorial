command_list = {
    'start': 'Car started... Ready to go!',
    'stop': 'Car stopped... Taking a break!',
    'exit': 'Exiting the driving simulator. Goodbye!',
    'help': """
Available Commands:
  start      - Start the car
  stop       - Stop the car
  reverse    - Reverse the car
  accelerate - Speed up the car
  brake      - Apply brakes
  status     - Show current car status
  help       - Show this help message
  exit       - Exit the game
"""
}

# Track car state
car_running = False

def run():
    global car_running

    print("🚗 Welcome to the Driving Simulator Game!")
    print("Type 'help' to see available commands.\n")

    while True:
        command = input("👉 Enter command: ").strip().lower()

        if command == 'start':
            if not car_running:
                car_running = True
                print("✅ " + command_list[command])
            else:
                print("ℹ️  Car is already running.")
        
        elif command == 'stop':
            if car_running:
                car_running = False
                print("🛑 " + command_list[command])
            else:
                print("ℹ️  Car is already stopped.")
        
        elif command == 'status':
            print(f"📊 Car is currently {'running' if car_running else 'stopped'}.")

        elif command == 'reverse':
            if car_running:
                print("🔁 Reversing the car...")
            else:
                print("❌ You need to start the car first.")
        
        elif command == 'accelerate':
            if car_running:
                print("🏎️  Accelerating...")
            else:
                print("❌ Start the car before accelerating.")
        
        elif command == 'brake':
            if car_running:
                print("🛑 Brakes applied.")
            else:
                print("ℹ️  Car is already stopped.")

        elif command == 'help':
            print(command_list['help'])

        elif command == 'exit':
            print("👋 " + command_list[command])
            break

        else:
            print("❌ Invalid command. Type 'help' to see the list of valid commands.\n")

# Run the game
run()
