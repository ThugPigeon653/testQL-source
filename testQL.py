import argparse
import json
import os
import yaml

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
            print(f"\n{jobs}\n")
            print(f"\n{template_body}\n")
            template_body["jobs"] = jobs
            workflows_dir = os.path.join(os.getcwd(), ".github", "workflows")
            if not os.path.exists(workflows_dir):
                os.makedirs(workflows_dir)
                print("Created .github/workflows folder.")
            print(f"\n{template_body}\n")
            yaml_file_path = os.path.join(workflows_dir, f"testQL-{engine}.yaml")
            with open(yaml_file_path, "w") as yaml_file:
                yaml.dump(template_body, yaml_file, indent=2, default_flow_style=False, sort_keys=False, default_style='')

            # This is a hacky solution to 'on' key enfing up with quotation marks. It works for now, but should eventially
            # either move to yaml in the config file, or fix this issue at its root cause.
            # NOTE: before changing this, consider the complexity of managing yaml fragments, with consideration to the
            # whitespace formatting requirements. In JSON, it is much easier to spot formatting mistakes, so will make for
            # more agile development in future. 
            with open(yaml_file_path, 'r') as file:
                yaml_content = file.read()
            yaml_content = yaml_content.replace("'on'", "on")
            with open(yaml_file_path, 'w') as file:
                file.write(yaml_content)
            print(f"Workflow YAML file created at: {yaml_file_path}")

def create_unittest(engine:str):
    engine = engine.lower()
    config_path = os.path.join(script_dir, "config.json")
    with open(config_path, "r") as template_object:
        template = json.load(template_object)
        pyfile:list[str] = template["py-template"]
        pyfile_content:str=""
        try:
            for line in pyfile["imports"]:
                pyfile_content+=line+'\n'
            for line in template["engines"][engine]["deps"]:
                pyfile_content+=line+'\n'
            pyfile_content+=" \n"
            for line in pyfile["top"]:
                pyfile_content+=line+'\n'
            for line in template["engines"][engine]["db-config"]:
                pyfile_content+=line+'\n'
            pyfile_content+=" \n"
            for line in pyfile["bottom"]:
                pyfile_content+=line+'\n'
        except KeyError as e:
            print(f"The engine you have entered {engine} is not recognized.\n{e}")
        else:
            test_dir = os.path.join(os.getcwd(), "test")
            if not os.path.exists(test_dir):
                os.makedirs(test_dir)
                print("Created test folder.")
            
            if not os.path.exists("test/__init__.py"):
                with open("test/__init__.py", "w") as inifile:
                    inifile.write("")

            test_file_path = os.path.join(test_dir, f"test_testQL_{engine}.py")
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
