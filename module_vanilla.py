import dataclasses
from jaxtyping import Float, Array

@dataclasses.dataclass
class Dataclass:
    x: Float[Array, "h w c"]
