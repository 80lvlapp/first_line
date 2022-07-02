from .categories import categories
from .coach import coaches
from .sportsman import sportsman
from .school import schools
from .type_of_tournaments import type_of_tournaments
from .tournament import tournament
from .base import metadata, engine

metadata.create_all(bind=engine)
