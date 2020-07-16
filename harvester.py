import os
import shutil
import json
import pprint
import tkinter as tk
from tkinter import filedialog

#Safely gets json code that might contain comments
#Credit: https://stackoverflow.com/questions/29959191/how-to-parse-json-file-with-c-style-comments
def get_json_from_file(fh):
    contents = ""
    for line in fh:
        cleanedLine = line.split("//", 1)[0]
        if len(cleanedLine) > 0 and line.endswith("\n") and "\n" not in cleanedLine:
            cleanedLine += "\n"
        contents += cleanedLine
    fh.close
    while "/*" in contents:
        preComment, postComment = contents.split("/*", 1)
        contents = preComment + postComment.split("*/", 1)[1]
    return json.loads(contents)

#Handle a single json file, return tuples of k/v pairs for stripped components

def strip_components(inpath, filename, ctype):
    with open(os.path.join(os.path.join(inpath, filename))) as json_file:
        data = get_json_from_file(json_file)

    print(filename)
    if ctype == "entities":
        return strip_entities(data, filename)
    elif ctype == "items":
        return strip_items(data, filename)
    elif ctype == "biomes":
        return strip_biomes(data, filename)
    elif ctype == "features":
        return strip_features(data, filename)
    elif ctype == "feature_rules":
        return strip_feature_rules(data, filename)
    elif ctype == "spawn_rules":
        return strip_spawn_rules(data, filename)

def strip_entities(data, filename):
    #Setup components list
    components = []

    #Gather raw components and groups
    components_raw = data.get("minecraft:entity", {}).get("components", {})
    component_groups = data.get("minecraft:entity", {}).get("component_groups", {})

    #Bring components into a list
    for component in components_raw.items():
        components.append(component)

    #Bring component groups into a list
    for group_name in component_groups:
        group = component_groups.get(group_name)
        for component in group.items():
            components.append(component)

    marked_components = []

    for component in components:
        marked_components.append(
            {
                "entity": filename,
                "id": component[0],
                "component": component[1]
            }
        )

    return marked_components 

#Handle a single json file, return tuples of k/v pairs for stripped components
def strip_items(data, filename):
    #Setup components list
    components = []

    #Gather raw components and groups
    components_raw = data.get("minecraft:item", {}).get("components", {})

    #Bring components into a list
    for component in components_raw.items():
        components.append(component)

    marked_components = []

    for component in components:
        marked_components.append(
            {
                "entity": filename,
                "id": component[0],
                "component": component[1]
            }
        )

    return marked_components 

def strip_biomes(data, filename):
    #Setup components list
    components = []

    #Gather raw components and groups
    components_raw = data.get("minecraft:biome", {}).get("components", {})

    #Bring components into a list
    for component in components_raw.items():
        components.append(component)

    marked_components = []

    for component in components:
        marked_components.append(
            {
                "entity": filename,
                "id": component[0],
                "component": component[1]
            }
        )

    return marked_components  

#Handle a single json file, return tuples of k/v pairs for stripped components
def strip_features(data, filename):
    #Setup components list
    components = []

    #Gather raw components and groups
    components_raw = data.get("minecraft:entity", {}).get("components", {})
    component_groups = data.get("minecraft:entity", {}).get("component_groups", {})

    #Bring components into a list
    for component in components_raw.items():
        components.append(component)

    #Bring component groups into a list
    for group_name in component_groups:
        group = component_groups.get(group_name)
        for component in group.items():
            components.append(component)

    marked_components = []

    for component in components:
        marked_components.append(
            {
                "entity": filename,
                "id": component[0],
                "component": component[1]
            }
        )

    return marked_components     

#Handle a single json file, return tuples of k/v pairs for stripped components
def strip_feature_rules(data, filename):
    #Setup components list
    components = []

    #Gather raw components and groups
    components_raw = data.get("minecraft:feature_rules", {}).get("conditions", {})

    #Bring components into a list
    for component in components_raw.items():
        components.append(component)

    marked_components = []

    for component in components:
        marked_components.append(
            {
                "entity": filename,
                "id": component[0],
                "component": component[1]
            }
        )

    return marked_components   

#Handle a single json file, return tuples of k/v pairs for stripped components
def strip_spawn_rules(data, filename):
    #Setup components list
    components = []

    #Bring components into a list
    for components_raw in data.get("minecraft:spawn_rules", {}).get("conditions", {}):
        for component in components_raw.items():
            components.append(component)

    marked_components = []

    for component in components:
        marked_components.append(
            {
                "entity": filename,
                "id": component[0],
                "component": component[1]
            }
        )

    return marked_components  

def print_to_file(inpath, outpath, outname, title, ctype):
    outfile = open(os.path.join(outpath,  outname), "w+")

    filenames = os.listdir(inpath)
    components = []

    #Loop over filename
    for filename in filenames:
        #We only care about json files.
        if(filename.endswith(".json")):
            components.extend(strip_components(inpath, filename, ctype))
    
    components = sorted(components, key = lambda i: i['id'])

    outfile.write("---\n")
    outfile.write("layout: page\n")
    outfile.write("title: {}\n".format(title))
    outfile.write("parent: Vanilla Usage\n")
    outfile.write("---\n\n")


    #Prep outfile:
    outfile.write("# {}\n".format(title))
    outfile.write(
        "This documentation is stripped from the vanilla files using an automated script. If there is an issue, please bring it to the authors attention by contacting him on discord: `SirLich#1658`\n\n"
    )
    
    outfile.write("# Table of contents\n")

    #Handle the table of contents:
    sections = set()

    #Gather non dupes
    for component in components:
        sections.add(component["id"])

    sections = sorted(sections)

    #Write out
    for section in sections:
        outfile.write(" - [{}](#{})\n".format(section, section.replace(":","").replace(".", "")))

    outfile.write("\n")

    #Handle components:
    current = ""
    current_entity = ""
    for component in components:
        #Reset current, so we can create headers:
        if(component["id"] != current):
            current = component["id"]
            outfile.write("# " + current + "\n")
        
        #Reset component for smaller headers.
        if(component["entity"] != current_entity):
            current_entity = component["entity"]
            outfile.write("### " + component["entity"].replace(".json", "") + "\n")

        outfile.write("```json\n\"" + component["id"] + "\": " + json.dumps(component["component"], indent=4) + "\n```\n\n")

def main():
    root = tk.Tk()
    root.withdraw()

    print("Entities!")
    infile = filedialog.askdirectory()
    print_to_file(infile, os.path.join(os.getcwd(), "output") , "components.md", "Components", "entities")

    print("Items!")
    infile = filedialog.askdirectory()
    print_to_file(infile, os.path.join(os.getcwd(), "output") , "items.md", "Items", "items")

    print("Biomes!")
    infile = filedialog.askdirectory()
    print_to_file(infile, os.path.join(os.getcwd(), "output") , "biomes.md", "Biomes", "biomes")

    print("Features!")
    infile = filedialog.askdirectory()
    print_to_file(infile, os.path.join(os.getcwd(), "output") , "features.md", "Features", "features")

    print("Feature Rules!")
    infile = filedialog.askdirectory()
    print_to_file(infile, os.path.join(os.getcwd(), "output") , "feature_rules.md", "Feature Rules", "feature_rules")

    print("Spawn Rules!")
    infile = filedialog.askdirectory()
    print_to_file(infile, os.path.join(os.getcwd(), "output") , "spawn_rules.md", "Spawn Rules", "spawn_rules")



main()