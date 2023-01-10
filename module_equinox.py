import equinox as eqx
from jaxtyping import Float, Array

class Dataclass(eqx.Module):
    x: Float[Array, "h w c"]
