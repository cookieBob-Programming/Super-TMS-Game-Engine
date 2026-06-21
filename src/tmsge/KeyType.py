from enum import IntEnum
import pygame

KEY_TYPES = [kt[2:] for kt in pygame.__dict__ if kt.startswith("K_")]
KeyType = IntEnum("KeyType", [(kt, pygame.__dict__["K_"+kt]) for kt in KEY_TYPES])
