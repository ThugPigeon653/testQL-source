import argparse

def init(args):
    return f"Executing the '{args.command}' command"

def help():
    return "Help section to be formatted later..."

def main():
    parser = argparse.ArgumentParser(description="testQL CLI Tool")
    parser.add_argument("command", choices=["init", "command_one", "command_two"], help="Choose a command to execute")

    args = parser.parse_args()

    if args.command == "init":
        result = init(args)
        print(result)

if __name__ == "__main__":
    main()