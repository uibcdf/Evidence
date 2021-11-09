import yaml

def flatten(arg):

    output = []
    if type(arg) in [list, tuple]:

        for ii in arg:
            if type(ii) in [list, tuple]:
                output.extend(ii)
            else:
                output.append(ii)

    return output


with open('../requirements.yaml') as fff:
    all_requirements = yaml.load(fff, Loader=yaml.FullLoader)



# Production
env_dict={}
env_dict["channels"]=flatten(all_requirements["production"]["channels"])
env_dict["dependencies"]=flatten(all_requirements["production"]["dependencies"])
fff = open("production_env.yaml", "w")
yaml.dump(env_dict, fff, sort_keys=True)
fff.close()

# Development
env_dict={}
env_dict["channels"]=flatten(all_requirements["development"]["channels"])
env_dict["dependencies"]=flatten(all_requirements["development"]["dependencies"])
fff = open("development_env.yaml", "w")
yaml.dump(env_dict, fff, sort_keys=True)
fff.close()

# Test
env_dict={}
env_dict["channels"]=flatten(all_requirements["test"]["channels"])
env_dict["dependencies"]=flatten(all_requirements["test"]["dependencies"])
fff = open("test_env.yaml", "w")
yaml.dump(env_dict, fff, sort_keys=True)
fff.close()

# Docs
env_dict={}
env_dict["channels"]=flatten(all_requirements["docs"]["channels"])
env_dict["dependencies"]=flatten(all_requirements["docs"]["dependencies"])
fff = open("docs_env.yaml", "w")
yaml.dump(env_dict, fff, sort_keys=False)
fff.close()

# Setup
env_dict={}
env_dict["channels"]=flatten(all_requirements["setup"]["channels"])
env_dict["dependencies"]=flatten(all_requirements["setup"]["dependencies"])
fff = open("setup_env.yaml", "w")
yaml.dump(env_dict, fff, sort_keys=False)
fff.close()

# Build
env_dict={}
env_dict["channels"]=flatten(all_requirements["conda-build"]["channels"])
env_dict["dependencies"]=flatten(all_requirements["conda-build"]["dependencies"])
fff = open("build_env.yaml", "w")
yaml.dump(env_dict, fff, sort_keys=False)
fff.close()


