import json 

def strip_sounds(sound_definitions: str):
    '''
    This function assumes that the sounds definition file uses 1.14.0
    sounds_definitions.json file format. It doesn't work for older files
    and may not work in the future.
    '''
    print("Sound definitions!")
    with open(sound_definitions) as json_file:
        data = list(json.load(json_file)['sound_definitions'].keys())
    outfile = open("sound_out.md", "w+")

    #Collect sounds for the linker
    save = ""
    mob = ""
    for sound in data:
        current = sound.split(".")[0]
        mob_current = sound.split(".")[1]
        if(save != current):
            outfile.write(" - [{0}](#{0})\n".format(current))
            save = current
        if(current == "mob" and mob != mob_current):
            mob = mob_current
            outfile.write("   - [{0}](#{0})\n".format(mob_current))

    id = ""
    mob = ""

    for sound in data:
        current = sound.split(".")[0]
        mob_current = sound.split(".")[1]
        if(id != current):
            outfile.write("# " + current + "\n\n")
            id = current
        if(id == "mob" and mob != mob_current):
            mob = mob_current
            outfile.write("## " + mob_current + "\n\n")

        outfile.write("`" + sound + "`\n\n")
