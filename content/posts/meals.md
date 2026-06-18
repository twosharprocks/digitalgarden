---
title: Meals - Dashboard
created: 2026-04-16
updated: 2026-04-16
status: seed
draft: false
tags:
  - dashboard
  - dataview
Related: "[[Meals]]"
---
# Well Known & Easy
- Vege Pad Thai - Tofu, Carrot, Broccolli, Noodles
- Parmie - Schnitzel, Tomato Paste, Cheese, + Chips
- Burgers - Buns, Mince/Pattie, Lettuce
- Enchiladas - Wraps, Beans, Cheese
- Nachos - Corn Chips, Mince, Beans, Cheese
- Pork Strips - Crunchy fried noodles

- Meal - High Protein Chicken Katsu Fried Rice 
- Meal - Smokey Bacon Gnocchi 
- Meal - Chicken & Chorizo One Pan Rice 
- Meal - High Protein Mexican Bowl 
- Meal - Giant Chicken Poppers 
- Meal - Chicken Alfredo Tortellini
## Quick Meals
```dataview
LIST
FROM ""
WHERE contains(tags, "meal") AND contains(tags, "quick")
SORT file.name ASC
```
# To Try
- Meal - Chipotle Beef & Crispy Chorizo Gnocchi
- Meal - Honey Garlic Chicken Fried Rice

- Meal - Honey BBQ Chicken Mac & Cheese
- Meal - Cheeseburger Bowls
- Meal - Air Fryer Nachos 
#### Taco Wraps
- [Bolognese Tacos](https://www.instagram.com/reel/C2SI84uoBoc/) - Mini wraps, Mince, Onion, Grated Carrot, Italian Herbs, Garlic, Sweet Paprika, Tomato Puree
- [Smash Dumpling Tacos](https://www.instagram.com/p/C5RTQ11IhB5/) - Mince, wraps, soy sauce, sesame seeds, chilli sauce
- [Arayes](https://www.instagram.com/p/C86hGxVKpzA/) - mince, garlic, onion, jalapeno, 
- [Nacho beef folded wrap](https://www.instagram.com/p/C8MZZsno-rw/) - Mince, wraps, corn chips, burger sauce, lettuce
- [Cheesy Bacon Jalapeño Popper wrap](https://www.instagram.com/p/C4Q2y9YPWNv/) - mozzarella, cheddar, crumbled bacon, grilled jalapeños, cream cheese, tortilla
- [Garlic honey BBQ pulled chicken tacos](https://www.instagram.com/reel/C9zmtXKIEzV/?igsh=MTRudm5yZTN6ZmxiZg==)
#### Burritos
- [Pepper Jack Chicken Burrito](https://www.instagram.com/p/C3C9joqLri5/) - Chicken breast, cheddar, mozzarella, bacon, tortillas, Taco spice, green chilli
- [Beef Bulgogi Burrito (Freezable)](https://www.instagram.com/p/C8SA1OVp6Hp/) - Beef, sushi rice (Account has many other freezable burritos)
- [Chicken Bacon Ranch Burrito](https://www.instagram.com/reel/C-CxvcxSodf/?igsh=ODBlNXBzbDRwNGp2) - Chicken breast, cottage cheese, mozzarella, bacon, tortilla wraps
- [CHICKEN PARM BAKED WRAPS](https://www.instagram.com/reel/C-YNCyitW-P/?igsh=cTFybjN3Nm1tZ21l)
- [Grilled Cheese Burrito](https://www.instagram.com/reel/C-S7lLrR8xd/?igsh=MXBiMTMza3cwcXM0eA==)
- [Chicken Bacon Ranch Burritos](https://www.instagram.com/reel/C-CxvcxSodf/?igsh=ODBlNXBzbDRwNGp2)
- [Nacho Cheese Beef Burritos](https://www.instagram.com/reel/C-Z9YjWS0-j/?igsh=MWMwZXY2b2V4NGt6OA==)
- [Lasagne Burritos](https://www.instagram.com/reel/C_LWkDcxIQM/?igsh=Yjd5em10NGFndWdq)
- [High Protein Grilled Cheese Burritos](https://www.instagram.com/reel/C_u8HVwSlMc/?igsh=MTZwcWg1aHVuM2Ny)
- [Spicy Steak & Cheese Burritos](https://www.instagram.com/reel/C_wcOk8R6SV/?igsh=MXh5a2h4ZGUzdHVwOQ==)

# Breakfast
- Meal - High Protein Breakfast Bagel
- Meal - Big Mac Toastie
- Meal - Feta Fried Egg Tortilla
- Meal - Chorizo Smash Breakfast Tacos
- Meal - Loaded Breakfast Wrap
- Meal - High Protein Breakfast Burritos 
- Meal - High Protein Chicken Sausage Breakfast Burritos
- Meal - Hash Brown, Halloumi & Chorizo Hash 
# Snacks
- Meal - Healthy Chicken Nuggets 
- Meal - Hash Brown Feta Bites
- Meal - High Protein KFC Chicken Bowl
- Meal - High Protein Hot Honey Popcorn Chicken
- Meal - Cheese Pull Apart Bread
- Meal - Pizza Cupcakes
- Meal - Garlic Butter Jalapeño Popper Croissants
- Meal - Pizza Cupcakes
- Meal - No-Bake Chocolate Chip Cookie Dough Bars 
# Misc
- ["Poached" Eggs in a strainer over boiling water](https://www.facebook.com/watch/?ref=saved&v=981608874289839) 

```dataview
TABLE
  calories_per_serving AS Calories,
  protein_g AS Protein,
  carbs_g AS Carbs,
  fat_g AS Fat,
  meal_type AS Type,
  cook_method AS Method
FROM ""
WHERE contains(tags, "meal")
SORT file.name ASC
```

## High Protein Meals
```dataview
TABLE
  calories_per_serving AS Calories,
  protein_g AS Protein,
  carbs_g AS Carbs,
  fat_g AS Fat
FROM ""
WHERE contains(tags, "meal") AND contains(tags, "high-protein")
SORT protein_g DESC
```

## Meal Prep Friendly
```dataview
LIST
FROM ""
WHERE contains(tags, "meal") AND contains(tags, "meal-prep")
SORT file.name ASC
```

## By Main Ingredient
```dataview
TABLE tags
FROM ""
WHERE contains(tags, "meal")
SORT file.name ASC
```

