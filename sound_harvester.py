import json 


"""
This file strips sounds from a custom format Katie stripped out of the sound files.
It should be replaced with a more robust system that pulls data from the actual files.
"""

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
    
with open("sounds.json") as json_file:
    data = json.load(json_file)
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

