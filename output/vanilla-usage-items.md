---
title: Vanilla Usage Items
category: Documentation
---

This documentation is stripped from the vanilla files using an automated script. If there is an issue, you can tell us about it in [Bedrock OSS](https://discord.gg/XjV87YN) Discord server. Please not that examples are shown from not more than 8 files to keep the page fast to load.

## block

<Spoiler title="Show">

#### camera

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/camera.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:block": "minecraft:camera"
```

</Spoiler>

## camera

<Spoiler title="Show">

<CodeHeader></CodeHeader>

```json
"minecraft:camera": {
    "black_bars_duration": 0.2,
    "black_bars_screen_ratio": 0.08,
    "shutter_duration": 0.2,
    "picture_duration": 1.0,
    "slide_away_duration": 0.2
}
```

</Spoiler>

## foil

<Spoiler title="Show">

#### appleEnchanted

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/appleEnchanted.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:foil": true
```

#### golden_apple

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/golden_apple.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:foil": false
```

</Spoiler>

## food

<Spoiler title="Show">

#### apple

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/apple.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 4,
    "saturation_modifier": "low"
}
```

#### appleEnchanted

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/appleEnchanted.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 4,
    "saturation_modifier": "supernatural",
    "can_always_eat": true,
    "effects": [
        {
            "name": "regeneration",
            "chance": 1.0,
            "duration": 30,
            "amplifier": 4
        },
        {
            "name": "absorption",
            "chance": 1.0,
            "duration": 120,
            "amplifier": 3
        },
        {
            "name": "resistance",
            "chance": 1.0,
            "duration": 300,
            "amplifier": 0
        },
        {
            "name": "fire_resistance",
            "chance": 1.0,
            "duration": 300,
            "amplifier": 0
        }
    ]
}
```

#### baked_potato

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/baked_potato.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

#### beef

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/beef.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 3,
    "saturation_modifier": "low"
}
```

#### beetroot

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/beetroot.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 1,
    "saturation_modifier": "normal"
}
```

#### beetroot_soup

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/beetroot_soup.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 6,
    "saturation_modifier": "normal",
    "using_converts_to": "bowl"
}
```

#### bread

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/bread.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

#### carrot

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/carrot.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 3,
    "saturation_modifier": "normal"
}
```

</Spoiler>

## hand_equipped

<Spoiler title="Show">

#### appleEnchanted

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/appleEnchanted.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:hand_equipped": false
```

</Spoiler>

## max_damage

<Spoiler title="Show">

#### clownfish

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/clownfish.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:max_damage": 0
```

#### cooked_fish

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/cooked_fish.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:max_damage": 0
```

#### cooked_salmon

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/cooked_salmon.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:max_damage": 0
```

#### fish

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/fish.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:max_damage": 0
```

#### pufferfish

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/pufferfish.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:max_damage": 0
```

#### salmon

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/salmon.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:max_damage": 0
```

</Spoiler>

## max_stack_size

<Spoiler title="Show">

#### beetroot_soup

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/beetroot_soup.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:max_stack_size": 1
```

#### honey_bottle

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/honey_bottle.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:max_stack_size": 16
```

#### mushroom_stew

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/mushroom_stew.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:max_stack_size": 1
```

#### rabbit_stew

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/rabbit_stew.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:max_stack_size": 1
```

#### suspicious_stew

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/suspicious_stew.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:max_stack_size": 1
```

</Spoiler>

## seed

<Spoiler title="Show">

#### beetroot_seeds

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/beetroot_seeds.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "crop_result": "beetroot"
}
```

#### carrot

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/carrot.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "crop_result": "carrots"
}
```

#### glow_berries

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/glow_berries.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "crop_result": "cave_vines",
    "plant_at": [
        "cave_vines",
        "cave_vines_head_with_berries"
    ],
    "plant_at_any_solid_surface": true,
    "plant_at_face": "DOWN"
}
```

#### melon_seeds

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/melon_seeds.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "crop_result": "melon_stem"
}
```

#### nether_wart

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/nether_wart.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "plant_at": "soul_sand",
    "crop_result": "nether_wart"
}
```

#### potato

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/potato.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "crop_result": "potatoes"
}
```

#### pumpkin_seeds

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/pumpkin_seeds.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "crop_result": "pumpkin_stem"
}
```

#### sweet_berries

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/sweet_berries.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "crop_result": "sweet_berry_bush",
    "plant_at": [
        "grass",
        "dirt",
        "podzol",
        "moss_block",
        "mycelium"
    ]
}
```

</Spoiler>

## stacked_by_data

<Spoiler title="Show">

#### appleEnchanted

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/appleEnchanted.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

#### clownfish

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/clownfish.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

#### cooked_fish

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/cooked_fish.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

#### cooked_salmon

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/cooked_salmon.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

#### fish

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/fish.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

#### golden_apple

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/golden_apple.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

#### pufferfish

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/pufferfish.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

#### salmon

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/salmon.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

</Spoiler>

## use_duration

<Spoiler title="Show">

#### apple

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/apple.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

#### appleEnchanted

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/appleEnchanted.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

#### baked_potato

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/baked_potato.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

#### beef

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/beef.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

#### beetroot

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/beetroot.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

#### beetroot_soup

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/beetroot_soup.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

#### bread

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/bread.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

#### camera

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/items/camera.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 100000
```

</Spoiler>