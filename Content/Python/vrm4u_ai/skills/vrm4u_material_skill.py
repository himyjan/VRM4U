import unreal

from toolset_registry.agent_skill import agent_skill


_INSTRUCTIONS = (
    "Before changing a VRM4U material, inspect the source VRM metadata, VRM "
    "version, current import material type, skeletal-mesh material assignments, "
    "and the parents of the generated material instances.\n"
    "The material type can be selected during import. To change it afterward, "
    "change each generated material instance's parent to the corresponding "
    "VRM4U base material for the desired type. Before changing a parent, "
    "preserve intentional instance overrides and "
    "confirm that the new parent exposes compatible parameters; afterward, "
    "verify the skeletal-mesh material assignments.\n"
    "Primarily choose among MToon Unlit, MToon Lit, and Subsurface Profile. "
    "Use MToon Unlit when the material should not be affected by scene lighting, "
    "MToon Lit when it should receive a limited amount of lighting influence, "
    "and Subsurface Profile when the character should blend with Unreal "
    "Engine's PBR-rendered surfaces.\n"
    "Do not assume that parameter names are identical across material types or "
    "VRM4U versions. Inspect the currently assigned material instance and its "
    "parent, then change only parameters exposed by that material path.\n"
    "Tune the material in dependency order: establish base color and textures; "
    "fix opacity mode, cutoff, culling, and two-sided behavior; shape the shade "
    "and lighting response; then tune emission, rim, and outline. This keeps "
    "render-path problems from being mistaken for artistic parameter problems.\n"
    "ScreenBlend is available in VRM4U's basic materials and allows partial "
    "transparency by using render targets from a VrmSceneCaptureComponent2D. "
    "Both sides require configuration: assign the base-color, depth, and custom-"
    "stencil render targets to the scene-capture component, then assign those "
    "same textures to the corresponding screen-texture inputs in the material "
    "before enabling ScreenBlend. Confirm that the capture targets are updating "
    "and the material inputs reference them before diagnosing opacity settings.\n"
    "Treat the per-material MToon rim and VRM4U's screen-space rim-light filter "
    "as separate effects that may be layered. Keep the material rim as the "
    "always-on surface-local character shading, and add the screen-space filter "
    "for special moments or stencil-selected image-space emphasis. When both "
    "are active, judge and tune the combined result.\n"
    "Validate skin, hair, eyes, and translucent materials under the intended "
    "lighting and camera. Check outlines at both near and far distances, and "
    "verify that expression-driven material changes still work before saving.\n"
)


@agent_skill
class VRM4UMaterialSkill(unreal.AgentSkill):
    """Use when selecting or changing VRM4U material types or tuning generated
    MToon materials, including shading, ScreenBlend transparency, rim, outline,
    and emission."""

    instructions = _INSTRUCTIONS
