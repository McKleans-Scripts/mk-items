## Drugs
Add These To Your qb-core/Shared/Items.Lua

## Credit to Contributors
 - KenanDK
 - MrFuRoX


----------  Drugs  ----------  Drugs  ----------  Drugs  ----------  Drugs  ----------

```lua
-- Joints
['joint1'] 			 	 		 = {['name'] = 'joint1', 						['label'] = 'Gelatti Joint', 			['weight'] = 100, 		['type'] = 'item', 		['image'] = 'joint1.png', 				['unique'] = false, 	['useable'] = true,  	['shouldClose'] = true,  	['combinable'] = nil, 	['description'] = 'Big Doinks!!'},
['joint2'] 			 			 = {['name'] = 'joint2', 						['label'] = 'Gary Payton Joint', 		['weight'] = 100, 		['type'] = 'item', 		['image'] = 'joint2.png', 				['unique'] = false, 	['useable'] = true,  	['shouldClose'] = true,  	['combinable'] = nil, 	['description'] = 'Big Doinks!!'},
['joint3'] 		 	 			 = {['name'] = 'joint3', 						['label'] = 'Cereal Milk Joint', 		['weight'] = 100, 		['type'] = 'item', 		['image'] = 'joint3.png', 				['unique'] = false, 	['useable'] = true,  	['shouldClose'] = true,  	['combinable'] = nil, 	['description'] = 'Big Doinks!!'},
['joint4'] 		 	 			 = {['name'] = 'joint4', 						['label'] = 'Cheetah Piss Joint', 		['weight'] = 100, 		['type'] = 'item', 		['image'] = 'joint4.png', 				['unique'] = false, 	['useable'] = true,  	['shouldClose'] = true,  	['combinable'] = nil, 	['description'] = 'Big Doinks!!'},
['joint5']			 	 		 = {['name'] = 'joint5', 						['label'] = 'Snow Man Joint', 			['weight'] = 100, 		['type'] = 'item', 		['image'] = 'joint5.png', 				['unique'] = false, 	['useable'] = true,  	['shouldClose'] = true,  	['combinable'] = nil, 	['description'] = 'Big Doinks!!'},
['joint6'] 		 	 			 = {['name'] = 'joint6', 						['label'] = 'Georgia Pie Joint', 		['weight'] = 100, 		['type'] = 'item', 		['image'] = 'joint6.png', 				['unique'] = false, 	['useable'] = true,  	['shouldClose'] = true,  	['combinable'] = nil, 	['description'] = 'Big Doinks!!'},
['joint7']				 	 	 = {['name'] = 'joint7', 						['label'] = 'El Jefe', 					['weight'] = 100, 		['type'] = 'item', 		['image'] = 'joint7.png', 				['unique'] = false, 	['useable'] = true,  	['shouldClose'] = true,  	['combinable'] = nil, 	['description'] = 'Big Doinks!!'},
```
```lua
-- Weed
["ground_weed"] 				 = {["name"] = "ground_weed", 			 		["label"] = "Ground Weed", 		        ["weight"] = 200, 		["type"] = "item", 		["image"] = "ground-weed.png", 			["unique"] = false, 	["useable"] = true, 	["shouldClose"] = false,   ["combinable"] = nil,   ["description"] = "Ground up Weed"},
["empty_weed_bag"] 				 = {["name"] = "empty_weed_bag", 			    ["label"] = "Empty Baggy", 			    ["weight"] = 10, 		["type"] = "item", 		["image"] = "weed-empty-bag.png", 		["unique"] = false, 	["useable"] = true, 	["shouldClose"] = true,	   ["combinable"] = nil,   ["description"] = "A empty baggy"},
["weed_nutrition"] 				 = {["name"] = "weed_nutrition", 			    ["label"] = "Plant Fertilizer", 		["weight"] = 2000, 		["type"] = "item", 		["image"] = "fertilizer.png", 			["unique"] = false, 	["useable"] = true, 	["shouldClose"] = true,	   ["combinable"] = nil,   ["description"] = "Plant nutrition"},
["weed_brick"] 		 			 = {["name"] = "weed_brick", 					["label"] = "Weed Brick", 				["weight"] = 1000, 		["type"] = "item", 		["image"] = "weed_brick.png", 			["unique"] = false, 	["useable"] = false, 	["shouldClose"] = true,	   ["combinable"] = nil,   ["description"] = "1KG Weed Brick to sell to large customers."},
```
```lua
-- Chems
["ironoxide"] 				 	 = {["name"] = "ironoxide", 			  		["label"] = "Iron Powder", 				["weight"] = 100, 		["type"] = "item", 		["image"] = "ironoxide.png", 			["unique"] = false, 	["useable"] = false, 	["shouldClose"] = false,   ["combinable"] = nil,   ["description"] = "Some powder to mix with"},
["aluminumoxide"] 				 = {["name"] = "aluminumoxide", 			  	["label"] = "Aluminium Powder", 		["weight"] = 100, 		["type"] = "item", 		["image"] = "aluminumoxide.png", 		["unique"] = false, 	["useable"] = false, 	["shouldClose"] = false,   ["combinable"] = nil,   ["description"] = "Some powder to mix with"},
["ephedrine"] 					 = {["name"] = "ephedrine", 					["label"] = "Ephedrine", 				["weight"] = 200, 		["type"] = "item", 		["image"] = "ephedrine.png", 			["unique"] = false, 	["useable"] = true, 	["shouldClose"] = false,   ["combinable"] = nil,   ["description"] = "make some meth"},
["hydrochloricacid"] 			 = {["name"] = "hydrochloricacid", 				["label"] = "Hydrochloricacid", 		["weight"] = 200, 		["type"] = "item", 		["image"] = "hydrochloricacid.png", 	["unique"] = false, 	["useable"] = true, 	["shouldClose"] = false,   ["combinable"] = nil,   ["description"] = "make some meth"},
["acetone"] 					 = {["name"] = "acetone", 						["label"] = "Acetone", 					["weight"] = 200, 		["type"] = "item", 		["image"] = "acetone.png", 			    ["unique"] = false, 	["useable"] = true, 	["shouldClose"] = false,   ["combinable"] = nil,   ["description"] = "make some meth"},
```
```lua
-- Coke
["cokebaggy"] 					 = {["name"] = "cokebaggy", 			  	  	["label"] = "Bag of Coke", 				["weight"] = 100, 		["type"] = "item", 		["image"] = "cocaine_baggy.png", 		["unique"] = false, 	["useable"] = true, 	["shouldClose"] = true,    ["combinable"] = nil,   ["description"] = "The devil's Drug"},
["crack_baggy"] 				 = {["name"] = "crack_baggy", 			  	  	["label"] = "Bag of Crack", 			["weight"] = 50, 		["type"] = "item", 		["image"] = "crack_baggy.png", 			["unique"] = false, 	["useable"] = true, 	["shouldClose"] = true,    ["combinable"] = nil,   ["description"] = "To get happy faster."},
```