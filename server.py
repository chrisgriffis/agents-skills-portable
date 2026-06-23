"""
Strategy Framework MCP Server

Exposes the four-skill stack (advisor, wartime, robertgreene, housekeeper),
reference documents, templates, and hygiene tools over the Model Context Protocol.
"""

from pathlib import Path
from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).parent

mcp = FastMCP(
    "strategy-framework",
    instructions=(
        "Strategy Framework server. Provides AI skills for strategic advisory work: "
        "peacetime advisor, wartime chief-of-staff, Robert Greene analytical lens, "
        "and housekeeper state-hygiene mixin. Also exposes reference documents, "
        "templates, and tools for maintaining multi-file strategic state systems."
    ),
)


# ─── Prompts: Skill definitions ─────────────────────────────────────────────


@mcp.prompt()
def advisor() -> str:
    """
    Peacetime advisor skill. Analytical strategic peer that maintains
    situational awareness, pushes back on bad moves, and keeps frames separate.
    Use for planning, sense-making, and document analysis.
    """
    return (ROOT / "peacetime" / "SKILL.md").read_text(encoding="utf-8")


@mcp.prompt()
def wartime() -> str:
    """
    Wartime chief-of-staff skill. Power-dynamics operator that makes moves land.
    Use for active maneuvering, sequencing, and crafting communications.
    Decorated by the Robert Greene lens.
    """
    skill = (ROOT / "wartime" / "SKILL.md").read_text(encoding="utf-8")
    greene = (ROOT / "robertgreene" / "SKILL.md").read_text(encoding="utf-8")
    return f"{skill}\n\n---\n\n# Decorator: Robert Greene Lens\n\n{greene}"


@mcp.prompt()
def robert_greene() -> str:
    """
    Robert Greene atomic skill. 48 Laws of Power + Art of Seduction as an
    analytical lens. Amoral power-dynamics pattern matching. Can be applied
    independently or as a decorator on other skills.
    """
    return (ROOT / "robertgreene" / "SKILL.md").read_text(encoding="utf-8")


@mcp.prompt()
def housekeeper() -> str:
    """
    Housekeeper mixin skill. State hygiene, global reconciliation, and
    spring cleaning for multi-file strategic state systems.
    """
    return (ROOT / "housekeeper" / "SKILL.md").read_text(encoding="utf-8")


# ─── Resources: Reference documents and templates ────────────────────────────


@mcp.resource("strategy://framework/readme")
def framework_readme() -> str:
    """The complete Strategy Workspace framework guide."""
    return (ROOT / "strategy-workspace" / "README.md").read_text(encoding="utf-8")


@mcp.resource("strategy://safety-net/readme")
def safety_net_readme() -> str:
    """Offline continuity cards template and guide."""
    return (ROOT / "safety-net" / "README.md").read_text(encoding="utf-8")


@mcp.resource("strategy://templates/reconciliation-report")
def reconciliation_template() -> str:
    """Global reconciliation report template for housekeeper springclean."""
    return (
        ROOT / "housekeeper" / "templates" / "reconciliation-report-template.md"
    ).read_text(encoding="utf-8")


@mcp.resource("strategy://templates/agent-peacetime")
def agent_template_peacetime() -> str:
    """Agent definition template for peacetime advisor."""
    return (
        ROOT / "strategy-workspace" / "templates" / "stamper.agent.md"
    ).read_text(encoding="utf-8")


@mcp.resource("strategy://templates/agent-wartime")
def agent_template_wartime() -> str:
    """Agent definition template for wartime chief-of-staff."""
    return (
        ROOT / "strategy-workspace" / "templates" / "real-doug-stamper.agent.md"
    ).read_text(encoding="utf-8")


# ─── Tools: Actions the AI can invoke ────────────────────────────────────────


@mcp.tool()
def get_reference(skill: str, document: str) -> str:
    """
    Retrieve a reference document for a given skill.

    Args:
        skill: One of 'peacetime', 'wartime', 'housekeeper', 'robertgreene'
        document: Filename (e.g. 'arc-tracking.md', 'power-framework.md')

    Available references:
        peacetime: arc-tracking.md, self-challenge.md, pushback-protocol.md, doc-ingestion.md
        wartime: persona.md, power-framework.md, real-doug-stamper.md
    """
    valid_skills = {"peacetime", "wartime", "housekeeper", "robertgreene"}
    if skill not in valid_skills:
        return f"Error: skill must be one of {valid_skills}"

    path = ROOT / skill / "references" / document
    if not path.exists():
        available = [
            f.name for f in (ROOT / skill / "references").iterdir()
            if f.is_file()
        ] if (ROOT / skill / "references").exists() else []
        return f"Error: '{document}' not found. Available: {available}"

    return path.read_text(encoding="utf-8")


@mcp.tool()
def list_references(skill: str) -> str:
    """
    List all available reference documents for a skill.

    Args:
        skill: One of 'peacetime', 'wartime', 'housekeeper', 'robertgreene'
    """
    valid_skills = {"peacetime", "wartime", "housekeeper", "robertgreene"}
    if skill not in valid_skills:
        return f"Error: skill must be one of {valid_skills}"

    refs_dir = ROOT / skill / "references"
    if not refs_dir.exists():
        return f"No references directory for '{skill}'"

    files = sorted(f.name for f in refs_dir.iterdir() if f.is_file())
    return "\n".join(files) if files else "No reference files found"


@mcp.tool()
def list_skills() -> str:
    """
    List all available skills with their descriptions and activation criteria.
    Returns a summary table of the four-skill stack.
    """
    skills = []
    for skill_dir in ["peacetime", "wartime", "robertgreene", "housekeeper"]:
        path = ROOT / skill_dir / "SKILL.md"
        if path.exists():
            content = path.read_text(encoding="utf-8")
            # Extract frontmatter name and description
            lines = content.split("\n")
            name = desc = ""
            for line in lines:
                if line.startswith("name:"):
                    name = line.split(":", 1)[1].strip()
                elif line.startswith("description:"):
                    desc = line.split(":", 1)[1].strip().strip('"')
            skills.append(f"## {name}\n{desc}\n")

    return "\n".join(skills)


@mcp.tool()
def get_framework_section(section: str) -> str:
    """
    Retrieve a specific section of the Strategy Workspace framework.

    Args:
        section: One of 'three-layer', 'merge-discipline', 'cast-schema',
                 'allup-protocol', 'harden', 'visual-layer', 'full'
    """
    content = (ROOT / "strategy-workspace" / "README.md").read_text(encoding="utf-8")

    if section == "full":
        return content

    # Section heading patterns
    section_map = {
        "three-layer": "Three-Layer Architecture",
        "merge-discipline": "Merge",
        "cast-schema": "Cast",
        "allup-protocol": "Allup",
        "harden": "Harden",
        "visual-layer": "Visual",
    }

    heading = section_map.get(section)
    if not heading:
        return f"Error: section must be one of {list(section_map.keys()) + ['full']}"

    # Extract section content
    lines = content.split("\n")
    start = None
    end = None
    for i, line in enumerate(lines):
        if heading.lower() in line.lower() and line.startswith("#"):
            start = i
            level = len(line) - len(line.lstrip("#"))
            # Find next heading at same or higher level
            for j in range(i + 1, len(lines)):
                if lines[j].startswith("#"):
                    next_level = len(lines[j]) - len(lines[j].lstrip("#"))
                    if next_level <= level:
                        end = j
                        break
            break

    if start is None:
        return f"Section '{section}' not found in framework document"

    return "\n".join(lines[start:end])


# ─── Entry point ─────────────────────────────────────────────────────────────


def main():
    mcp.run()


if __name__ == "__main__":
    main()
