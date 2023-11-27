import argparse
import json
import os

script_dir = os.path.dirname(__file__)

def create_workflow(engine: str):
    engine = engine.lower()
    config_path = os.path.join(script_dir, "config.json")
    with open(config_path, "r") as template_object:
        template = json.load(template_object)
        template_body = template["base-workflow"]
        print("opened json...")
        try:
            jobs = template["engines"][engine]["jobs"]
        except KeyError as e:
            print(f"The engine you have entered {engine} is not recognized.\n{e}")
        else:
            template_body["on"]["push"]["jobs"] = jobs
            workflows_dir = os.path.join(os.getcwd(), ".github", "workflows")
            if not os.path.exists(workflows_dir):
                os.makedirs(workflows_dir)
                print("Created .github/workflows folder.")

            json_file_path = os.path.join(workflows_dir, f"testQL-{engine}.json")
            with open(json_file_path, "w") as json_file:
                json.dump(template_body, json_file, indent=2)

            print(f"Workflow JSON file created at: {json_file_path}")

def create_unittest(engine:str):
    engine = engine.lower()
    config_path = os.path.join(script_dir, "config.json")
    with open(config_path, "r") as template_object:
        template = json.load(template_object)
        pyfile:list[str] = template["py-template"]
        pyfile_content:str=""
        try:
            for line in pyfile["top"]:
                pyfile_content+=line+'\n'
            for line in template["engines"][engine]["jobs"]:
                pyfile_content+=line+'\n'
            for line in pyfile["bottom"]:
                pyfile_content+=line+'\n'
        except KeyError as e:
            print(f"The engine you have entered {engine} is not recognized.\n{e}")
        else:
            test_dir = os.path.join(os.getcwd(), "test")
            if not os.path.exists(test_dir):
                os.makedirs(test_dir)
                print("Created test folder.")

            test_file_path = os.path.join(test_dir, "test_testQL.py")
            with open(test_file_path, "w") as test_file:
                test_file.write(pyfile_content)

            print(f"Test file created at: {test_file_path}")
            
def init(args)->str:
    engine:str=args.engine
    if engine in ["pg", "postgres", "postgresql"]:
        engine="postgres"
    elif engine in ["tsql", "microsoft", "microsoftsql"]:
        engine="tsql"
    create_workflow(engine)
    create_unittest(engine)
    return f"Executing the '{args.command}' command with engine: {engine}"

def help()->str:
    return "Help section to be formatted later..."

def main()->None:
    parser = argparse.ArgumentParser(description="testQL CLI Tool")
    parser.add_argument("command", choices=["init"], help="Choose a command to execute")
    parser.add_argument("--engine", default="postgres", help="Specify the engine parameter")
    args = parser.parse_args()
    if args.command == "init":
        result = init(args)
    print(result)

if __name__ == "__main__":
    main()
