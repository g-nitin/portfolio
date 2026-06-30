#!/usr/bin/env python3
from __future__ import annotations

import copy
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


TEMPLATE = Path("/Users/nitingupta/Desktop/Sogetic/Sogeti Resume Template - Blank 2026 - College Hire.docx")
OUT = Path("artifacts/sogeti_resume/Nitin_Gupta_Sogeti_Resume_2026.docx")

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W_NS}

ET.register_namespace("w", W_NS)
for prefix, uri in {
    "wpc": "http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas",
    "cx": "http://schemas.microsoft.com/office/drawing/2014/chartex",
    "cx1": "http://schemas.microsoft.com/office/drawing/2015/9/8/chartex",
    "cx2": "http://schemas.microsoft.com/office/drawing/2015/10/21/chartex",
    "cx3": "http://schemas.microsoft.com/office/drawing/2016/5/9/8/chartex",
    "cx4": "http://schemas.microsoft.com/office/drawing/2016/5/10/21/chartex",
    "cx5": "http://schemas.microsoft.com/office/drawing/2016/5/11/9/chartex",
    "cx6": "http://schemas.microsoft.com/office/drawing/2016/5/12/9/chartex",
    "cx7": "http://schemas.microsoft.com/office/drawing/2016/5/13/9/chartex",
    "cx8": "http://schemas.microsoft.com/office/drawing/2016/5/14/9/chartex",
    "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "v": "urn:schemas-microsoft-com:vml",
    "wp14": "http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "w14": "http://schemas.microsoft.com/office/word/2010/wordml",
    "w15": "http://schemas.microsoft.com/office/word/2012/wordml",
    "w16cex": "http://schemas.microsoft.com/office/word/2018/wordml/cex",
    "w16cid": "http://schemas.microsoft.com/office/word/2016/wordml/cid",
    "w16": "http://schemas.microsoft.com/office/word/2018/wordml",
    "w16du": "http://schemas.microsoft.com/office/word/2023/wordml/word16du",
    "w16sdtdh": "http://schemas.microsoft.com/office/word/2020/wordml/sdtdatahash",
    "w16sdtfl": "http://schemas.microsoft.com/office/word/2024/wordml/sdtformatlock",
    "w16se": "http://schemas.microsoft.com/office/word/2015/wordml/symex",
}.items():
    try:
        ET.register_namespace(prefix, uri)
    except ValueError:
        pass


def qn(tag: str) -> str:
    prefix, local = tag.split(":")
    if prefix == "w":
        return f"{{{W_NS}}}{local}"
    raise ValueError(tag)


def el(tag: str, attrs: dict[str, str] | None = None, text: str | None = None) -> ET.Element:
    node = ET.Element(qn(tag), attrs or {})
    if text is not None:
        node.text = text
    return node


def w_attr(name: str) -> str:
    return f"{{{W_NS}}}{name}"


def ppr(
    style: str | None = None,
    *,
    keep_next: bool = False,
    right_tab: bool = False,
    align: str | None = None,
) -> ET.Element:
    ppr_node = el("w:pPr")
    if style:
        ppr_node.append(el("w:pStyle", {w_attr("val"): style}))
    if keep_next:
        ppr_node.append(el("w:keepNext"))
    if right_tab:
        tabs = el("w:tabs")
        tabs.append(el("w:tab", {w_attr("val"): "right", w_attr("pos"): "9360"}))
        ppr_node.append(tabs)
    if align:
        ppr_node.append(el("w:jc", {w_attr("val"): align}))
    return ppr_node


def run(text: str, *, bold: bool = False, italic: bool = False) -> ET.Element:
    r = el("w:r")
    if bold or italic:
        rpr = el("w:rPr")
        if bold:
            rpr.append(el("w:b"))
        if italic:
            rpr.append(el("w:i"))
        r.append(rpr)
    t = el("w:t")
    if text.startswith(" ") or text.endswith(" ") or "  " in text:
        t.set(f"{{{XML_NS}}}space", "preserve")
    t.text = text
    r.append(t)
    return r


def paragraph(
    parts: str | list[tuple[str, dict[str, bool]]] | list[str],
    style: str | None = None,
    *,
    keep_next: bool = False,
    right_tab: bool = False,
    align: str | None = None,
) -> ET.Element:
    p = el("w:p")
    p.append(ppr(style, keep_next=keep_next, right_tab=right_tab, align=align))
    if isinstance(parts, str):
        p.append(run(parts))
    else:
        for part in parts:
            if isinstance(part, str):
                p.append(run(part))
            else:
                text, opts = part
                p.append(run(text, **opts))
    return p


def date_row(left: str, right: str, style: str = "ProfessionalExperienceCompanyName") -> ET.Element:
    gap = max(3, 105 - len(left) - len(right))
    return paragraph(f"{left}{' ' * gap}{right}", style, keep_next=True)


def bullet(text: str) -> ET.Element:
    return paragraph(text, "Accomplishmentsbullet")


def section(title: str) -> ET.Element:
    return paragraph(title, "Heading1", keep_next=True)


def subheading(text: str) -> ET.Element:
    return paragraph(text, "Heading3", keep_next=True)


def skills_table(rows: list[tuple[str, str]]) -> ET.Element:
    tbl = el("w:tbl")
    tbl_pr = el("w:tblPr")
    tbl_pr.append(el("w:tblW", {w_attr("w"): "0", w_attr("type"): "auto"}))
    tbl_pr.append(el("w:tblInd", {w_attr("w"): "0", w_attr("type"): "dxa"}))
    borders = el("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        borders.append(el(f"w:{side}", {w_attr("val"): "nil"}))
    tbl_pr.append(borders)
    tbl_look = el("w:tblLook", {
        w_attr("val"): "04A0",
        w_attr("firstRow"): "1",
        w_attr("lastRow"): "0",
        w_attr("firstColumn"): "1",
        w_attr("lastColumn"): "0",
        w_attr("noHBand"): "0",
        w_attr("noVBand"): "1",
    })
    tbl_pr.append(tbl_look)
    tbl.append(tbl_pr)
    grid = el("w:tblGrid")
    grid.append(el("w:gridCol", {w_attr("w"): "2300"}))
    grid.append(el("w:gridCol", {w_attr("w"): "7060"}))
    tbl.append(grid)
    for label, value in rows:
        tr = el("w:tr")
        for idx, content in enumerate((label, value)):
            tc = el("w:tc")
            tc_pr = el("w:tcPr")
            tc_pr.append(el("w:tcW", {w_attr("w"): "2300" if idx == 0 else "7060", w_attr("type"): "dxa"}))
            tc.append(tc_pr)
            style = "SkillHeads" if idx == 0 else "ProfileText"
            tc.append(paragraph(content, style))
            tr.append(tc)
        tbl.append(tr)
    return tbl


def add_experience(body: list[ET.Element], company: str, date: str, role: str, bullets: list[str]) -> None:
    body.append(date_row(company, date))
    body.append(paragraph(role, "ProfessionalExperienceEmploymentSubheaders", keep_next=True))
    body.append(subheading("Accomplishments and Responsibilities"))
    for item in bullets:
        body.append(bullet(item))


def build_body(sect_pr: ET.Element) -> list[ET.Element]:
    body: list[ET.Element] = []

    body.append(section("Summary"))
    body.append(paragraph(
        "AI engineer and computer science researcher with 3+ years of experience designing, building, and evaluating machine learning workflows, LLM applications, and data-driven systems. Skilled in neuro-symbolic AI, natural language processing, explainable AI planning, knowledge graphs, RAG pipelines, multimodal GenAI evaluation, Python, and responsible AI practices. Experienced translating research and stakeholder needs into deployed tools, evaluation frameworks, dashboards, and technical recommendations. Strong communicator with peer-reviewed AI publications, event leadership experience, and a track record of collaborating with academic, government, and cross-functional teams.",
        "ProfileText",
    ))

    body.append(section("Education"))
    body.append(date_row("University of South Carolina, M.S. Computer Science", "May 2026", "ProfileText"))
    body.append(paragraph("Concentration: Artificial Intelligence | GPA: 3.8/4.0", "ProfileText"))
    body.append(date_row("University of South Carolina, B.S. Computer Science", "May 2025", "ProfileText"))
    body.append(paragraph("Minors: Data Science and Mathematics | GPA: 4.0/4.0", "ProfileText"))

    body.append(section("Skills"))
    body.append(skills_table([
        ("AI and ML", "LLMs, RAG, PEFT, LoRA, GenAI, NLP, computer vision, topic modeling, dimensionality reduction, MLOps, PyTorch, TensorFlow, Hugging Face"),
        ("Languages", "Python, C++, Java, SQL, NoSQL, R, JavaScript, REST APIs"),
        ("Data and Cloud", "AWS, GCP, Docker, CI/CD, Git, Linux, Apache Hadoop, Pandas, NumPy, scikit-learn"),
        ("Methods", "Knowledge graphs, explainable AI, evaluation frameworks, Agile/Scrum, statistical analysis, data visualization"),
        ("Spoken Languages", "English, Hindi, Punjabi, Spanish"),
    ]))

    body.append(section("Selected Publications and Awards"))
    for item in [
        "On Sample-Efficient Generalized Planning via Learned Transition Models, ICAPS 2026, in press",
        "GAICo: A Deployed and Extensible Framework for Evaluating Diverse and Multimodal Generative AI Outputs, IAAI/AAAI 2026, in press",
        "Building a Plan Ontology to Represent and Exploit Planning Knowledge and Its Applications, Discover Data, November 2025",
        "AAAI Student Scholar and NSF Research Fellowship recipient, February 2025",
        "McNAIR Junior Fellowship for undergraduate computer science research excellence, May 2024",
    ]:
        body.append(bullet(item))

    body.append(section("Professional Experience Details"))
    body.append(date_row("Sogeti USA", "July 2026 to Present"))
    body.append(paragraph("Associate Consultant", "ProfessionalExperienceEmploymentSubheaders", keep_next=True))
    body.append(subheading("In-House Sogeti Training"))
    for item in [
        "Attended Sogeti New Hire Training Academy learning about each of Sogeti technology practices including Applications and Cloud, Quality Engineering and Customer First",
        "Reviewed essential services and architectures of AWS and Azure cloud systems",
        "Completed creative design thinking labs and client challenge exercises",
    ]:
        body.append(bullet(item))

    add_experience(body, "AI Institute of SC, University of South Carolina", "August 2024 to Present", "AI Researcher", [
        "Lead research in neuro-symbolic AI and NLP across AI planning, knowledge graphs, and multimodal systems under Dr. Biplav Srivastava.",
        "Designed a scalable evaluation architecture to benchmark multimodal AI outputs across text, image, and audio for responsible deployment in high-stakes enterprise settings.",
        "Architected and deployed multi-agent AI workflows to automate NLP tasks and reduce manual processing overhead.",
        "Organized Safe AI for Seniors, a full-day hybrid AAAI-sponsored event with 80+ attendees and 8+ expert speakers.",
        "Contributed to 4+ peer-reviewed publications, including ICAPS 2026 transition-model planning work, IAAI/AAAI 2026 GAICo work, and the Discover Data planning ontology paper.",
        "Mentored students and peer-reviewed 10+ research papers for top-tier AI conferences.",
    ])

    add_experience(body, "Trew Friends, University of South Carolina", "August 2021 to December 2024", "Volunteering Ambassador", [
        "Promoted organ, eye, and tissue donation through community outreach, helping persuade 300+ individuals to register as donors.",
    ])

    add_experience(body, "AI Institute of SC, University of South Carolina", "May 2024 to August 2024", "Explainable AI Research Intern", [
        "Developed a planning ontology and LLM framework for transparent plan explanations and explainable AI workflows.",
        "Built Python data analysis workflows for large-scale traffic datasets from SCDHEC, SCDPS, and NSCSC, identifying collision patterns to inform safety policy.",
        "Presented research at the 2024 Summer Research Symposium and translated complex data insights into actionable recommendations.",
    ])

    add_experience(body, "Digital Research Services, University of South Carolina", "January 2022 to April 2024", "Machine Learning and Data Visualization Researcher", [
        "Built data ingestion pipelines to parse, normalize, and mine trends from 10,000+ historical documents using NLP and clustering-based pattern detection.",
        "Applied Latent Dirichlet Allocation and unsupervised clustering to surface topical structure in unstructured text corpora, achieving 85%+ classification accuracy.",
        "Designed interactive web-based data visualizations that improved stakeholder access to analytical outputs for the Digital Research Services department.",
    ])

    body.append(section("Academic Projects"))
    body.append(subheading("ArtEdge: Real-Time Neural Style Transfer for Mobile Devices | Swift, Core ML, PyTorch"))
    body.append(bullet("Developed a mobile-first iOS app for on-device neural style transfer, converting/adapting PyTorch NST models into Core ML packages for Neural Engine acceleration."))
    body.append(bullet("Implemented and evaluated four NST architectures - custom MobileNet AdaIN, Fast Style Transfer, StyTr2, and AesFA - across latency, quality, and privacy tradeoffs."))

    body.append(subheading("RoostAI: University-Centered RAG Chatbot | Python, Streamlit, Vector Databases, RAG"))
    body.append(bullet("Built a USC-focused chatbot using retrieval-augmented generation to deliver accurate, context-aware responses to university-related queries."))
    body.append(bullet("Implemented web scraping, text chunking, data ingestion, vector database management, backend query processing, reranking, Streamlit UI, and RAG evaluation workflows."))

    body.append(subheading("Beacon of Hope: Context-Aware Meal Recommendation System | React/TypeScript, Django, Ontologies"))
    body.append(bullet("Built a full-stack meal recommendation system focused on diabetes and African-American dietary contexts, using preferences, restrictions, health goals, and ontologies for personalization."))
    body.append(bullet("Delivered interactive meal exploration, categorization, health-condition-aware filtering, and nutritional comparison views for healthier decision support."))

    body.append(subheading("Segify: Semantic Segmentation for Localized Artistic Effects | Python, PyTorch, Streamlit, SAM"))
    body.append(bullet("Built an interactive Streamlit app that lets users upload images, define masks, choose artistic styles, and control styling parameters for region-specific neural style transfer."))
    body.append(bullet("Combined AdaIN-based style transfer with Meta's Segment Anything model for accurate user-guided segmentation and localized artistic effects."))

    body.append(copy.deepcopy(sect_pr))
    return body


def replace_doc_text(xml_bytes: bytes, replacements: dict[str, str]) -> bytes:
    root = ET.fromstring(xml_bytes)
    for text_node in root.findall(".//w:t", NS):
        if text_node.text in replacements:
            text_node.text = replacements[text_node.text]
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def update_core_props(xml_bytes: bytes) -> bytes:
    root = ET.fromstring(xml_bytes)
    for node in root.iter():
        local = node.tag.rsplit("}", 1)[-1]
        if local == "title":
            node.text = "Nitin Gupta - Sogeti Resume 2026"
        elif local == "creator":
            node.text = "Nitin Gupta"
        elif local == "lastModifiedBy":
            node.text = "OpenAI Codex"
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(TEMPLATE) as zin:
        document_xml = zin.read("word/document.xml")
        document_root = ET.fromstring(document_xml)
        body_node = document_root.find("w:body", NS)
        if body_node is None:
            raise RuntimeError("Template document.xml has no body")
        sect_pr = body_node.find("w:sectPr", NS)
        if sect_pr is None:
            raise RuntimeError("Template document.xml has no sectPr")
        body_node.clear()
        for child in build_body(sect_pr):
            body_node.append(child)
        new_document_xml = ET.tostring(document_root, encoding="utf-8", xml_declaration=True)

        with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == "word/document.xml":
                    data = new_document_xml
                elif item.filename in {"word/header1.xml", "word/header2.xml"}:
                    data = replace_doc_text(data, {"Name": "Nitin Gupta"})
                elif item.filename == "docProps/core.xml":
                    data = update_core_props(data)
                zout.writestr(item, data)

    print(OUT)


if __name__ == "__main__":
    main()
