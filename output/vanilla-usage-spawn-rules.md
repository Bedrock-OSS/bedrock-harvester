---
title: Vanilla Usage Spawn Rules
category: Documentation
---

This documentation is stripped from the vanilla files using an automated script. If there is an issue, you can tell us about it in [Bedrock OSS](https://discord.gg/XjV87YN) Discord server. Please not that examples are shown from not more than 8 files to keep the page fast to load.

## biome_filter

<Spoiler title="Show">

#### axolotl

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/axolotl.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "lush_caves"
}
```

#### bat

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/bat.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

#### bee

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/bee.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "plains"
    },
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "sunflower_plains"
    },
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "flower_forest"
    }
]
```

#### chicken

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/chicken.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

#### cod

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cod.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "ocean"
    },
    {
        "test": "has_biome_tag",
        "operator": "!=",
        "value": "warm"
    }
]
```

#### cow

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cow.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

#### creeper

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/creeper.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

#### dolphin

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/dolphin.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "ocean"
    },
    {
        "test": "has_biome_tag",
        "operator": "!=",
        "value": "frozen"
    }
]
```

</Spoiler>

## brightness_filter

<Spoiler title="Show">

#### bat

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/bat.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 0,
    "max": 4,
    "adjust_for_weather": true
}
```

#### bee

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/bee.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

#### chicken

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/chicken.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

#### cow

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cow.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

#### creeper

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/creeper.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

#### donkey

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/donkey.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

#### drowned

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/drowned.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

#### enderman

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/enderman.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

</Spoiler>

## delay_filter

<Spoiler title="Show">

#### pillager_patrol

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/pillager_patrol.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:delay_filter": {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_easy",
    "spawn_chance": 20
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:delay_filter": {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_normal",
    "spawn_chance": 20
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:delay_filter": {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_hard",
    "spawn_chance": 20
}
```

</Spoiler>

## density_limit

<Spoiler title="Show">

#### axolotl

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/axolotl.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "underground": 5
}
```

#### bat

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/bat.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 5
}
```

#### cod

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cod.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 20
}
```

#### creeper

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/creeper.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 5
}
```

#### dolphin

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/dolphin.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 5,
    "underground": 0
}
```

#### drowned

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/drowned.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 5
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 2
}
```

#### ghast

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/ghast.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 0,
    "underground": 2
}
```

</Spoiler>

## difficulty_filter

<Spoiler title="Show">

#### creeper

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/creeper.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

#### drowned

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/drowned.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

#### enderman

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/enderman.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

#### ghast

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/ghast.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

#### hoglin

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/hoglin.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "peaceful",
    "max": "hard"
}
```

#### husk

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/husk.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

#### magma_cube

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/magma_cube.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

#### phantom

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/phantom.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

</Spoiler>

## disallow_spawns_in_bubble

<Spoiler title="Show">

#### axolotl

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/axolotl.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:disallow_spawns_in_bubble": {}
```

</Spoiler>

## distance_filter

<Spoiler title="Show">

#### cod

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cod.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

#### pillager_patrol

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/pillager_patrol.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:distance_filter": {
    "min": 24,
    "max": 48
}
```

#### pufferfish

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/pufferfish.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

#### salmon

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/salmon.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

#### tropicalfish

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/tropicalfish.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

</Spoiler>

## height_filter

<Spoiler title="Show">

#### bat

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/bat.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": -63,
    "max": 63
}
```

#### cod

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cod.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": 50,
    "max": 64
}
```

#### dolphin

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/dolphin.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": 50,
    "max": 64
}
```

#### glow_squid

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/glow_squid.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": -64,
    "max": 30
}
```

#### pufferfish

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/pufferfish.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": 50,
    "max": 64
}
```

#### salmon

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/salmon.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": 50,
    "max": 64
}
```

#### stray

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/stray.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": 60,
    "max": 66
}
```

#### tropicalfish

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/tropicalfish.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": 50,
    "max": 64
}
```

</Spoiler>

## herd

<Spoiler title="Show">

#### axolotl

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/axolotl.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 4,
    "max_size": 6,
    "event": "minecraft:entity_born",
    "event_skip_count": 2
}
```

#### bat

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/bat.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 2,
    "max_size": 2
}
```

#### bee

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/bee.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 1,
    "max_size": 1
}
```

#### chicken

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/chicken.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 2,
    "max_size": 4
}
```

#### cod

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cod.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 4,
    "max_size": 7
}
```

#### cow

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cow.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 2,
    "max_size": 3
}
```

#### dolphin

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/dolphin.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 3,
    "max_size": 5
}
```

#### donkey

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/donkey.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 2,
    "max_size": 6
}
```

</Spoiler>

## mob_event_filter

<Spoiler title="Show">

#### pillager_patrol

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/pillager_patrol.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:mob_event_filter": {
    "event": "minecraft:pillager_patrols_event"
}
```

</Spoiler>

## permute_type

<Spoiler title="Show">

<CodeHeader></CodeHeader>

```json
"minecraft:permute_type": [
    {
        "weight": 100,
        "entity_type": "minecraft:pillager<minecraft:spawn_as_patrol_follower>"
    }
]
```

#### zombie

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/zombie.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:permute_type": [
    {
        "weight": 95
    },
    {
        "weight": 5,
        "entity_type": "minecraft:zombie_villager_v2"
    }
]
```

</Spoiler>

## player_in_village_filter

<Spoiler title="Show">

#### pillager_patrol

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/pillager_patrol.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:player_in_village_filter": {
    "distance": 48,
    "village_border_tolerance": 32
}
```

</Spoiler>

## spawn_event

<Spoiler title="Show">

#### stray

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/stray.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawn_event": {
    "event": "change_to_skeleton"
}
```

</Spoiler>

## spawns_lava

<Spoiler title="Show">

#### strider

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/strider.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_lava": {}
```

</Spoiler>

## spawns_on_block_filter

<Spoiler title="Show">

#### axolotl

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/axolotl.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": "minecraft:clay"
```

#### chicken

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/chicken.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

#### cow

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cow.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

#### donkey

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/donkey.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

#### goat

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/goat.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": [
    "minecraft:stone",
    "minecraft:snow",
    "minecraft:powder_snow",
    "minecraft:snow_layer",
    "minecraft:packed_ice",
    "minecraft:gravel"
]
```

#### horse

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/horse.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

#### llama

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/llama.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

#### ocelot

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/ocelot.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

</Spoiler>

## spawns_on_block_prevented_filter

<Spoiler title="Show">

#### hoglin

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/hoglin.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

#### magma_cube

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/magma_cube.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

#### piglin

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/piglin.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

#### skeleton

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/skeleton.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

#### zombie_pigman

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/zombie_pigman.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

</Spoiler>

## spawns_on_surface

<Spoiler title="Show">

#### bee

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/bee.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

#### chicken

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/chicken.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

#### cod

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cod.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

#### cow

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cow.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

#### creeper

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/creeper.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

#### dolphin

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/dolphin.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

#### donkey

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/donkey.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

#### drowned

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/drowned.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

</Spoiler>

## spawns_underground

<Spoiler title="Show">

#### axolotl

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/axolotl.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

#### bat

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/bat.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

#### creeper

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/creeper.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

#### enderman

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/enderman.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

#### ghast

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/ghast.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

#### glow_squid

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/glow_squid.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

#### hoglin

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/hoglin.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

#### magma_cube

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/magma_cube.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

</Spoiler>

## spawns_underwater

<Spoiler title="Show">

#### axolotl

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/axolotl.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

#### cod

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cod.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

#### dolphin

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/dolphin.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

#### drowned

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/drowned.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

#### glow_squid

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/glow_squid.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

#### guardian

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/guardian.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

#### pufferfish

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/pufferfish.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

#### salmon

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/salmon.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

</Spoiler>

## weight

<Spoiler title="Show">

#### axolotl

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/axolotl.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 10
}
```

#### bat

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/bat.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 10
}
```

#### bee

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/bee.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 10
}
```

#### chicken

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/chicken.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 10
}
```

#### cod

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cod.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 75
}
```

#### cow

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/cow.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 8
}
```

#### creeper

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/creeper.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 100
}
```

#### dolphin

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/dolphin.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 7
}
```

</Spoiler>

## world_age_filter

<Spoiler title="Show">

#### pillager_patrol

<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/spawn_rules/pillager_patrol.json)</small>

<CodeHeader></CodeHeader>

```json
"minecraft:world_age_filter": {
    "min": 6000
}
```

</Spoiler>