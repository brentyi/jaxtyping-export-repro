from jaxtyping import install_import_hook

with install_import_hook("module_equinox", ("typeguard", "typechecked")):
    import module_equinox
with install_import_hook("module_vanilla", ("typeguard", "typechecked")):
    import module_vanilla

from jax import numpy as jnp

# Fails successfully with equinox.
try:
    module_equinox.Dataclass(jnp.zeros((1,)))
except TypeError:
    print("Equinox OK")

# Should fail but doesn't.
module_vanilla.Dataclass(jnp.zeros((1,)))
