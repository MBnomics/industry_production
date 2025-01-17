# %%
import importlib
import sys
# %%
package_dir = importlib.resources.files("industrial_prod")

#%%
print(package_dir / "images/dbnomics.svg")

# %%
sys.path.append('/home/juliette/projets/industrial_prod/src/industrial_prod')

# %%
