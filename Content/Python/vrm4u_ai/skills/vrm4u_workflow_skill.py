import unreal

from toolset_registry.agent_skill import agent_skill


_INSTRUCTIONS = (
    "Inspect the imported VRM asset and its metadata before modifying generated assets.\n"
    "Preserve the source model and import settings so changes remain reproducible.\n"
    "Determine whether the asset follows VRM 0.x or VRM 1.0 conventions before "
    "changing humanoid mappings, expressions, or materials.\n"
    "The material type can be selected during import and changed afterward. "
    "Inspect the current type and preserve intentional material overrides before "
    "switching it.\n"
    "After a mutation, validate the affected assets and report warnings before saving.\n"
)


@agent_skill
class VRM4UWorkflowSkill(unreal.AgentSkill):
    """Use for VRM model imports, MToon material tuning, humanoid mappings,
    expressions, and animation retargeting with VRM4U."""

    instructions = _INSTRUCTIONS
