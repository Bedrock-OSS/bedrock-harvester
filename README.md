# bedrock-harvester
Documentation scraper for Bedrock Minecraft documentation.

This tool can be run on minecraft base-game files, including the hosted Vanilla Behavior Pack files, or those pulled from the APK.

## Running:
`python ./create.py`

For each type (item, feature rule, etc) a file dialogue will open. Select the folder containing the json files. For example for `entities`, you should select `resource_pack/entities`.

## Output:
Output will go into the `output` folder. The output is in markdown, and can be rendered on a site like Jekyll, or using a previewer.

# Contributing

PRs and contributions are welcome. Its a hacky little tool for use on the wiki. If you want to make it less terrible, by my guest :)
