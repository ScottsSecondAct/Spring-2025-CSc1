command = input("What is the command?")

match command:
  case 'start':
    print("The machine is starting.")
  case 'stop':
    print("The machine is stopping.")
  case 'pause':
    print("The machine is pausing.")
  case _:
    print("I don't know what that is.")