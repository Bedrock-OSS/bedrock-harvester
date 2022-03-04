import os
import shutil
import json
import pprint
import tkinter as tk
from tkinter import filedialog
from unittest import skip
from jsonc_decoder import JSONCDecoder
import math


def strip_entities(data, filename, relative_path):
    # Setup components list
    components = []

    # Gather raw components and groups
    components_raw = data.get("minecraft:entity", {}).get("components", {})
    component_groups = data.get(
        "minecraft:entity", {}).get("component_groups", {})

    # Bring components into a list
    for component in components_raw.items():
        if component not in components:
            components.append(component)

    # Bring component groups into a list
    for group_name in component_groups:
        group = component_groups.get(group_name)
        for component in group.items():
            if component not in components:
                components.append(component)

    marked_components = []

    for component in components:
        marked_components.append(
            {
                "entity": filename,
                "path": relative_path,
                "id": component[0],
                "component": component[1]
            }
        )

    return marked_components

# Handle a single json file, return tuples of k/v pairs for stripped components


def strip_items(data, filename, relative_path):
    # Setup components list
    components = []

    # Gather raw components and groups
    components_raw = data.get("minecraft:item", {}).get("components", {})

    # Bring components into a list
    for component in components_raw.items():
        if component not in components:
            components.append(component)

    marked_components = []

    for component in components:
        marked_components.append(
            {
                "entity": filename,
                "path": relative_path,
                "id": component[0],
                "component": component[1]
            }
        )

    return marked_components


def strip_biomes(data, filename, relative_path):
    # Setup components list
    components = []

    # Gather raw components and groups
    components_raw = data.get("minecraft:biome", {}).get("components", {})

    # Bring components into a list
    for component in components_raw.items():
        if component not in components:
            components.append(component)

    marked_components = []

    for component in components:
        marked_components.append(
            {
                "entity": filename,
                "path": relative_path,
                "id": component[0],
                "component": component[1]
            }
        )

    return marked_components

# Handle a single json file, return tuples of k/v pairs for stripped components


def strip_features(data, filename, relative_path):
    # Setup components list
    components = []

    # Gather raw components and groups
    components_raw = data.get("minecraft:entity", {}).get("components", {})
    component_groups = data.get(
        "minecraft:entity", {}).get("component_groups", {})

    # Bring components into a list
    for component in components_raw.items():
        if component not in components:
            components.append(component)

    # Bring component groups into a list
    for group_name in component_groups:
        group = component_groups.get(group_name)
        for component in group.items():
            if component not in components:
                components.append(component)

    marked_components = []

    for component in components:
        marked_components.append(
            {
                "entity": filename,
                "path": relative_path,
                "id": component[0],
                "component": component[1]
            }
        )

    return marked_components

# Handle a single json file, return tuples of k/v pairs for stripped components


def strip_feature_rules(data, filename, relative_path):
    # Setup components list
    components = []

    # Gather raw components and groups
    components_raw = data.get(
        "minecraft:feature_rules", {}).get("conditions", {})

    # Bring components into a list
    for component in components_raw.items():
        if component not in components:
            components.append(component)

    marked_components = []

    for component in components:
        marked_components.append(
            {
                "entity": filename,
                "path": relative_path,
                "id": component[0],
                "component": component[1]
            }
        )

    return marked_components

# Handle a single json file, return tuples of k/v pairs for stripped components


def strip_spawn_rules(data, filename, relative_path):
    # Setup components list
    components = []

    # Bring components into a list
    for components_raw in data.get("minecraft:spawn_rules", {}).get("conditions", {}):
        for component in components_raw.items():
            if component not in components:
                components.append(component)

    marked_components = []

    for component in components:
        marked_components.append(
            {
                "entity": filename,
                "path": relative_path,
                "id": component[0],
                "component": component[1]
            }
        )

    return marked_components


def print_to_file(bp_path, folder, stable, outfile, title, strip_func):
    inpath = os.path.join(bp_path, folder)
    components = []
    # Defines maximum amount of files where examples are tooken from:
    counter_lim = 8
    # Maybe add it to function arguments?

    # Loop over filename
    if os.path.exists(inpath):
        filenames = os.listdir(inpath)
        for filename in filenames:
            # We only care about json files.
            if(filename.endswith(".json")):
                with open(os.path.join(inpath, filename)) as json_file:
                    data = json.load(json_file, cls=JSONCDecoder)
                relative_path = os.path.join(folder, filename)
                components.extend(strip_func(data, filename, relative_path))
    else:
        print(f'Warning! Input path {inpath} does not exist.')

    components = sorted(components, key=lambda i: i['id'])

    outfile.write("---\n")
    outfile.write("title: {}\n".format(title))
    outfile.write("category: Documentation\n")
    outfile.write("---\n\n")

    # Prep outfile:
    outfile.write(
        f"This documentation is stripped from the vanilla files using an [automated script](https://github.com/Bedrock-OSS/bedrock-harvester). If there is an issue, you can tell us about it in [Bedrock OSS](https://discord.gg/XjV87YN) Discord server. Please not that examples are shown from not more than {counter_lim} files to keep the page fast to load.\n\n"
    )

    # Handle components:
    counter = 0
    current = ""
    current_entity = ""
    for component in components:
        docs_url = get_docs_link(
            component["path"], True, stable).replace("\\", "/")

        # Reset current, so we can create headers:
        if(component["id"] != current):
            counter = 0
            if current != "":
                outfile.write("</Spoiler>" + "\n\n")
            current = component["id"]
            outfile.write("## " + current.split("minecraft:")
                          [1] + "\n\n")
            # Add links to bedrock.dev for entity components
            if "vanilla-usage-components" in str(outfile):
                dot_dev_link = "https://bedrock.dev/docs/stable/Entities#" + \
                    current.replace(":", "%3A")
                outfile.write(
                    "<small>[View docs](" + dot_dev_link + ")</small>\n\n")
            outfile.write('<Spoiler title="Show">\n\n')

        # Reset component for smaller headers.
        counter += 1
        if(component["entity"] != current_entity and counter <= counter_lim):
            current_entity = component["entity"]
            outfile.write("#### " + component["entity"].replace(
                ".json", "") + "\n\n" + "<small>[View file](" + docs_url + ")</small>\n\n")
        if counter <= counter_lim:
            outfile.write("<CodeHeader></CodeHeader>" + "\n\n" + "```json\n\"" +
                          component["id"] + "\": " + json.dumps(component["component"], indent=4) + "\n```\n\n")
    outfile.write("</Spoiler>")


def get_docs_link(f: str, bp: bool, stable: bool) -> str:
    url = "https://github.com/bedrock-dot-dev/packs/tree/master/"
    url = url + ("stable" if stable else "beta") + "/" + \
        ("behavior" if bp else "resource") + "/"
    return url + f


def harvest(bp_path: str, is_stable: bool):
    output_path = os.path.join(os.getcwd(), "output")

    print("Entities!")
    path = os.path.join(output_path, "vanilla-usage-components.md")
    with open(path, 'w') as output_file:
        print_to_file(bp_path, 'entities', is_stable,
                      output_file, "Vanilla Usage Components", strip_entities)

    print("Items!")
    with open(os.path.join(output_path, "vanilla-usage-items.md"), 'w') as output_file:
        print_to_file(bp_path, 'items', is_stable,
                      output_file, "Vanilla Usage Items", strip_items)

    print("Biomes!")
    with open(os.path.join(output_path, "biomes.md"), 'w') as output_file:
        print_to_file(bp_path, 'biomes', is_stable,
                      output_file, "Vanilla Usage Biomes", strip_biomes)

    print("Features!")
    with open(os.path.join(output_path, "features.md"), 'w') as output_file:
        print_to_file(bp_path, 'features', is_stable,
                      output_file, "Vanilla Usage Features", strip_features)

    print("Feature Rules!")
    with open(os.path.join(output_path, "feature_rules.md"), 'w') as output_file:
        print_to_file(bp_path, 'feature_rules', is_stable,
                      output_file, "Vanilla Usage Feature Rules", strip_feature_rules)

    print("Spawn Rules!")
    with open(os.path.join(output_path, "vanilla-usage-spawn-rules.md"), 'w') as output_file:
        print_to_file(bp_path, 'spawn_rules', is_stable,
                      output_file, "Vanilla Usage Spawn Rules", strip_spawn_rules)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    print("Please select behavior pack path.")
    bp_path = filedialog.askdirectory()
    harvest(bp_path)
