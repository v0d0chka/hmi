benzine_2_5_4x2 = {
    "price": 1263400,
    "has_dynamic_led_rear_lights": False,
    "exterior_design_elements": [
        "Roof rails",
        "Bumper protective trim",
        "Additional rear window tint",
        "18'' two-tone alloy wheels with diamond cut finish (tire size: 225/60 R18)"
    ],
    "panoramic_roof": {},
    "multimedia_system": "R-Link2 with 7'' touchscreen, no navigation, Apple CarPlay, Android Auto, 3D Sound Arkamys system",
    "leather_seat_upholstery": "Fabric/eco-leather black",
    "climate_control": "Dual-zone climate control",
    "heated_seats": True,
    "electric_side_mirrors": True,
    "front_and_rear_parking_sensors": True,
    "power_tailgate": True
}

benzine_2_5_4x4_intense = {
    "price": 1375700,
    "has_dynamic_led_rear_lights": True,
    "exterior_design_elements": [
        "Roof rails",
        "Bumper protective trim",
        "Additional rear window tint",
        "18'' two-tone alloy wheels with diamond cut finish (tire size: 225/60 R18)"
    ],
    "panoramic_roof": {
        "price": 30260
    },
    "multimedia_system": "R-Link2 with 8.7'' touchscreen, navigation, Apple CarPlay, Android Auto, 3D Sound Arkamys system, 12 speakers",
    "leather_seat_upholstery": "Leather Nappa black",
    "climate_control": "Dual-zone climate control",
    "heated_seats": True,
    "electric_side_mirrors": True,
    "front_and_rear_parking_sensors": True,
    "power_tailgate": True
}

for design_element in benzine_2_5_4x2["exterior_design_elements"]:
    print(design_element)

for design_element in benzine_2_5_4x4_intense["exterior_design_elements"]:
    print(design_element)