from sqlalchemy import Column, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import *
from sqlalchemy.databases.mysql import *

metadata = MetaData()
TableBase = declarative_base(metadata=metadata)

class Ability(TableBase):
    __tablename__ = 'abilities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(24), nullable=False)
    flavor_text = Column(Unicode(64), nullable=False)
    effect = Column(Unicode(255), nullable=False)

class ContestEffect(TableBase):
    __tablename__ = 'contest_effects'
    id = Column(Integer, primary_key=True, nullable=False)
    appeal = Column(SmallInteger, nullable=False)
    jam = Column(SmallInteger, nullable=False)
    flavor = Column(Unicode(255), nullable=False)
    effect = Column(Unicode(255), nullable=False)

class EggGroup(TableBase):
    __tablename__ = 'egg_groups'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(16), nullable=False)

class EvolutionChain(TableBase):
    __tablename__ = 'evolution_chains'
    id = Column(Integer, primary_key=True, nullable=False)
    growth_rate_id = Column(Integer, nullable=False)
    steps_to_hatch = Column(Integer, nullable=False)
    baby_trigger_item = Column(Unicode(12))

class EvolutionMethod(TableBase):
    __tablename__ = 'evolution_methods'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(64), nullable=False)
    description = Column(Unicode(255), nullable=False)

class Generation(TableBase):
    __tablename__ = 'generations'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(16), nullable=False)

class GrowthRate(TableBase):
    __tablename__ = 'growth_rates'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(16), nullable=False)
    formula = Column(Unicode(255), nullable=False)

class Language(TableBase):
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(16), nullable=False)

class MoveEffect(TableBase):
    __tablename__ = 'move_effects'
    id = Column(Integer, primary_key=True, nullable=False)
    priority = Column(SmallInteger, nullable=False)
    short_effect = Column(Unicode(128), nullable=False)
    effect = Column(Unicode(255), nullable=False)

class MoveTarget(TableBase):
    __tablename__ = 'move_targets'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(32), nullable=False)
    description = Column(Unicode(128), nullable=False)

class Move(TableBase):
    __tablename__ = 'moves'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(12), nullable=False)
    type_id = Column(Integer, nullable=False)
    power = Column(SmallInteger)
    pp = Column(SmallInteger, nullable=False)
    accuracy = Column(SmallInteger)
    target_id = Column(Integer, nullable=False)
    category = Column(Unicode(8), nullable=False)
    effect_id = Column(Integer, nullable=False)
    effect_chance = Column(Integer)
    contest_type = Column(Unicode(8), nullable=False)
    contest_effect_id = Column(Integer, nullable=False)
    super_contest_effect_id = Column(Integer, nullable=False)

class Pokemon(TableBase):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(20), nullable=False)
    forme_name = Column(Unicode(16))
    forme_base_pokemon_id = Column(Integer)
    evolution_chain_id = Column(Integer, nullable=False)
    evolution_parent_pokemon_id = Column(Integer)
    evolution_method_id = Column(Integer)
    evolution_parameter = Column(Unicode(32))
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    species = Column(Unicode(16), nullable=False)
    color = Column(Unicode(6), nullable=False)
    habitat = Column(Unicode(16), nullable=False)
    gender_rate = Column(Integer, nullable=False)
    capture_rate = Column(Integer, nullable=False)
    base_experience = Column(Integer, nullable=False)
    base_happiness = Column(Integer, nullable=False)
    gen1_internal_id = Column(Integer)
    is_baby = Column(Boolean, nullable=False)
    has_dp_fem_sprite = Column(Boolean, nullable=False)
    has_dp_fem_back_sprite = Column(Boolean, nullable=False)

class PokemonAbility(TableBase):
    __tablename__ = 'pokemon_abilities'
    pokemon_id = Column(Integer, primary_key=True, nullable=False)
    ability_id = Column(Integer, nullable=False)
    slot = Column(Integer, primary_key=True, nullable=False)

class PokemonDexNumber(TableBase):
    __tablename__ = 'pokemon_dex_numbers'
    pokemon_id = Column(Integer, primary_key=True, nullable=False)
    generation_id = Column(Integer, primary_key=True, nullable=False)
    pokedex_number = Column(Integer, nullable=False)

class PokemonEggGroup(TableBase):
    __tablename__ = 'pokemon_egg_groups'
    pokemon_id = Column(Integer, primary_key=True, nullable=False)
    egg_group_id = Column(Integer, primary_key=True, nullable=False)

class PokemonFlavorText(TableBase):
    __tablename__ = 'pokemon_flavor_text'
    pokemon_id = Column(Integer, primary_key=True, nullable=False)
    version_id = Column(Integer, primary_key=True, nullable=False)
    flavor = Column(Unicode(255), nullable=False)

class PokemonName(TableBase):
    __tablename__ = 'pokemon_names'
    pokemon_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(16), nullable=False)

class PokemonStat(TableBase):
    __tablename__ = 'pokemon_stats'
    pokemon_id = Column(Integer, primary_key=True, nullable=False)
    stat_id = Column(Integer, primary_key=True, nullable=False)
    base_stat = Column(Integer, nullable=False)
    effort = Column(Integer, nullable=False)

class PokemonType(TableBase):
    __tablename__ = 'pokemon_types'
    pokemon_id = Column(Integer, primary_key=True, nullable=False)
    type_id = Column(Integer, nullable=False)
    slot = Column(Integer, primary_key=True, nullable=False)

class Stat(TableBase):
    __tablename__ = 'stats'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(16), nullable=False)

class TypeEfficacy(TableBase):
    __tablename__ = 'type_efficacy'
    damage_type_id = Column(Integer, primary_key=True, nullable=False)
    target_type_id = Column(Integer, primary_key=True, nullable=False)
    damage_factor = Column(Integer, nullable=False)

class Type(TableBase):
    __tablename__ = 'types'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(8), nullable=False)
    abbreviation = Column(Unicode(3), nullable=False)

class VersionGroup(TableBase):
    __tablename__ = 'version_groups'
    id = Column(Integer, primary_key=True, nullable=False)
    generation_id = Column(Integer, nullable=False)

class Version(TableBase):
    __tablename__ = 'versions'
    id = Column(Integer, primary_key=True, nullable=False)
    version_group_id = Column(Integer, nullable=False)
    name = Column(Unicode(32), nullable=False)