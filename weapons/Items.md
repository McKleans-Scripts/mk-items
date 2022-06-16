## Weapons
Add These To Your qb-core/Shared/Items.Lua

## Credit to Contributors
 - idrp
 - Jimathy
 - MrFurox
 - Techmanmurphy
 - KenanDK


----------  Weapons  ----------  Weapons  ----------  Weapons  ----------  Weapons  ----------
```lua
----------  Ammo  ----------

  ['beanbag_ammo'] = {    ['name'] = "beanbag_ammo",    ['label'] = "Beanbag Ammo",    ['weight'] = 100,    ['decay'] = "0.3",['type'] = "ammo",    ['image'] = "beanbag_ammo.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Non-lethal Beanbag Ammo",    ['combinable'] = nil  },
  ['beanbag_ammo2'] = {    ['name'] = "beanbag_ammo2",    ['label'] = "Beanbag Ammo 2",    ['weight'] = 100,    ['decay'] = "0.3",['type'] = "ammo",    ['image'] = "beanbag_ammo2.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Non-lethal Beanbag Ammo",    ['combinable'] = nil  },
  ['mg_ammo'] = {    ['name'] = "mg_ammo",    ['label'] = "Mg Ammo",    ['weight'] = 100,    ['decay'] = "0.3",['type'] = "ammo",    ['image'] = "mg_ammo.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "MG Ammo",    ['combinable'] = nil  },
  ['pistol_ammo'] = {    ['name'] = "pistol_ammo",    ['label'] = "Pistol Ammo",    ['weight'] = 100,    ['decay'] = "0.3",['type'] = "ammo",    ['image'] = "pistol_ammo.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Pistol Ammo",    ['combinable'] = nil  },
  ['rifle_ammo'] = {    ['name'] = "rifle_ammo",    ['label'] = "Rifle Ammo",    ['weight'] = 100,    ['decay'] = "0.3",['type'] = "ammo",    ['image'] = "rifle_ammo.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Rifle Ammo",    ['combinable'] = nil  },
  ['shotgun_ammo'] = {    ['name'] = "shotgun_ammo",    ['label'] = "Shotgun Ammo",    ['weight'] = 100,    ['decay'] = "0.3",['type'] = "ammo",    ['image'] = "shotgun_ammo.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Shotgun Ammo",    ['combinable'] = nil  },
  ['smg_ammo'] = {    ['name'] = "smg_ammo",    ['label'] = "SMG Ammo",    ['weight'] = 100,    ['decay'] = "0.3",['type'] = "ammo",    ['image'] = "smg_ammo.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "SMG Ammo",    ['combinable'] = nil  },
  ['taser_ammo'] = {    ['name'] = "taser_ammo",    ['label'] = "Taser Ammo",    ['weight'] = 100,    ['decay'] = "0.3",['type'] = "ammo",    ['image'] = "taserammo.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Taser Ammo",    ['combinable'] = nil  },

```
```lua
----------  Weapons AR ----------

  ['weapon_assaultrifle'] = {    ['name'] = "weapon_assaultrifle",    ['label'] = "Assault Rifle",    ['weight'] = 500,    ['decay'] = "0.0",['type'] = "weapon",    ['image'] = "weapon_assaultrifle.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Assault rifle",    ['combinable'] = nil  },
  ['weapon_assaultrifle_mk2'] = {    ['name'] = "weapon_assaultrifle_mk2",    ['label'] = "Assault Rifle MKll",    ['weight'] = 500,    ['decay'] = "0.0",['type'] = "weapon",    ['image'] = "weapon_assaultrifle_mk2.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Assault rifle MKII",    ['combinable'] = nil  },
  ```
  ```lua
----------  Weapons Lunchers ----------

  ['weapon_compactlauncher'] = {    ['name'] = "weapon_compactlauncher",    ['label'] = "Compact Launcher",    ['weight'] = 500,    ['decay'] = "0.0",['type'] = "weapon",    ['image'] = "weapon_compactlauncher.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Compact Launcher",    ['combinable'] = nil  },
  ['weapon_grenadelauncher'] = {    ['name'] = "weapon_grenadelauncher",    ['label'] = "Grenade Launcher",    ['weight'] = 500,    ['decay'] = "0.0",['type'] = "weapon",    ['image'] = "weapon_grenadelauncher.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Grenade Launcher",    ['combinable'] = nil  },
  ['weapon_hominglauncher'] = {    ['name'] = "weapon_hominglauncher",    ['label'] = "Homing Launcher",    ['weight'] = 500,    ['decay'] = "0.0",['type'] = "weapon",    ['image'] = "weapon_hominglauncher.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Homing Launcher",    ['combinable'] = nil  },
  ['weapon_rpg'] = {    ['name'] = "weapon_rpg",    ['label'] = "RPG Launcher",    ['weight'] = 500,    ['decay'] = "0.0",['type'] = "weapon",    ['image'] = "weapon_rpg.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "RPG Launcher",    ['combinable'] = nil  },
  ['weapon_firework'] = {    ['name'] = "weapon_firework",    ['label'] = "Firework Launcher",    ['weight'] = 500,    ['decay'] = "0.0",['type'] = "weapon",    ['image'] = "weapon_firework.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Fireworks Launcher",    ['combinable'] = nil  },
```
```lua
----------  Weapons Meele ----------
  ['weapon_ball'] = {    ['name'] = "weapon_ball",    ['label'] = "Baseball",    ['weight'] = 500,    ['decay'] = "0.0",['type'] = "weapon",    ['image'] = "weapon_ball.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Baseball",    ['combinable'] = nil  },
  ['weapon_bat'] = {    ['name'] = "weapon_bat",    ['label'] = "Baseball Bat",    ['weight'] = 500,    ['decay'] = "0.0",['type'] = "weapon",    ['image'] = "weapon_bat.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Baseball Bat",    ['combinable'] = nil  },
  ['weapon_battleaxe'] = {    ['name'] = "weapon_battleaxe",    ['label'] = "Battle Axe",    ['weight'] = 500,    ['decay'] = "0.0",['type'] = "weapon",    ['image'] = "weapon_battleaxe.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Battle Axe",    ['combinable'] = nil  },
  ['weapon_bottle'] = {    ['name'] = "weapon_bottle",    ['label'] = "Bottle",    ['weight'] = 500,    ['decay'] = "0.0",['type'] = "weapon",    ['image'] = "weapon_bottle.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Bottle",    ['combinable'] = nil  },
  ['weapon_crowbar'] = {    ['name'] = "weapon_crowbar",    ['label'] = "Crowbar",    ['weight'] = 500,    ['decay'] = "0.0",['type'] = "weapon",    ['image'] = "weapon_crowbar.png",    ['created'] = "nil",    ['unique'] = false,    ['usable'] = false,    ['shouldClose'] = false,    ['description'] = "Crowbar",    ['combinable'] = nil  },

```