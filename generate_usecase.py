"""
generate_usecase.py
-------------------
Generates the Use Case document for the PhysioNet 2012 synthetic dataset.

Use Cases:
  1. Demographically-Conditioned ICU Subgroup Augmentation
  2. ICU-Type Specific Vital Sign Baseline Calibration
  3. Privacy-Safe Multi-Centre Patient Profile Sharing with Demographics

Author: Said Abolhassan Razavi
Project: ClinGen-MoE · Université Paris-Saclay M1 AI
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# ── Colours ───────────────────────────────────────────────────────────────────
BLUE    = colors.HexColor("#2563EB")
PURPLE  = colors.HexColor("#7C3AED")
GREEN   = colors.HexColor("#16A34A")
ORANGE  = colors.HexColor("#D97706")
DARK    = colors.HexColor("#1E293B")
GRAY    = colors.HexColor("#6B7280")
LGRAY   = colors.HexColor("#F1F5F9")
LBLUE   = colors.HexColor("#EFF6FF")
LGREEN  = colors.HexColor("#F0FDF4")
WHITE   = colors.white

W, H = A4

# ── Styles ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def style(name, **kwargs):
    return ParagraphStyle(name, **kwargs)

title_style = style("Title",
    fontSize=22, textColor=BLUE, alignment=TA_CENTER,
    fontName="Helvetica-Bold", spaceAfter=4)

subtitle_style = style("Subtitle",
    fontSize=12, textColor=GRAY, alignment=TA_CENTER,
    fontName="Helvetica-Oblique", spaceAfter=2)

author_style = style("Author",
    fontSize=11, textColor=DARK, alignment=TA_CENTER,
    fontName="Helvetica", spaceAfter=12)

body_style = style("Body",
    fontSize=11, textColor=DARK, alignment=TA_JUSTIFY,
    fontName="Helvetica", spaceAfter=6, leading=16)

bullet_style = style("Bullet",
    fontSize=11, textColor=DARK, alignment=TA_LEFT,
    fontName="Helvetica", leftIndent=16, spaceAfter=4,
    bulletIndent=4, leading=15)

bold_style = style("Bold",
    fontSize=11, textColor=DARK, alignment=TA_LEFT,
    fontName="Helvetica-Bold", spaceAfter=4)

section_title_style = style("SectionTitle",
    fontSize=13, textColor=WHITE, alignment=TA_LEFT,
    fontName="Helvetica-Bold", spaceAfter=0, leading=18)

value_style = style("Value",
    fontSize=11, textColor=DARK, alignment=TA_JUSTIFY,
    fontName="Helvetica", spaceAfter=4, leading=15,
    leftIndent=8, rightIndent=8)

# ── Helpers ───────────────────────────────────────────────────────────────────
def section_header(text, color=BLUE):
    data = [[Paragraph(text, section_title_style)]]
    t = Table(data, colWidths=[16.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), color),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
    ]))
    return t

def real_world_box(text, color=BLUE):
    label = Paragraph("<b>Real-world value:</b>  " + text, value_style)
    data = [[label]]
    t = Table(data, colWidths=[16.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), LBLUE),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LINEWIDTH",     (0,0), (0,0), 3),
        ("LINEBEFORE",    (0,0), (0,-1), 3, color),
    ]))
    return t

def feature_table(headers, rows, col_widths, header_color=BLUE):
    data = [headers] + rows
    t = Table(data, colWidths=col_widths)
    style_cmds = [
        ("BACKGROUND",    (0,0), (-1,0), header_color),
        ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,-1), 10),
        ("FONTNAME",      (0,1), (-1,-1), "Helvetica"),
        ("TEXTCOLOR",     (0,1), (-1,-1), DARK),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [WHITE, LGRAY]),
        ("GRID",          (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
    ]
    t.setStyle(TableStyle(style_cmds))
    return t

def bullet(text):
    return Paragraph("•  " + text, bullet_style)

def sp(h=0.3):
    return Spacer(1, h*cm)

# ═════════════════════════════════════════════════════════════════════════════
# BUILD DOCUMENT
# ═════════════════════════════════════════════════════════════════════════════
doc = SimpleDocTemplate(
    "UseCase_PhysioNet12.pdf",
    pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm,
)

story = []

# ── Title page ────────────────────────────────────────────────────────────────
story.append(sp(1.5))
story.append(Paragraph(
    "Use Cases of the Synthetic PhysioNet 2012 Dataset", title_style))
story.append(Paragraph(
    "What can we do with AI-generated ICU patient data conditioned on demographics?",
    subtitle_style))
story.append(Paragraph("Said Abolhassan Razavi", author_style))
story.append(HRFlowable(width="100%", thickness=1, color=GRAY, spaceAfter=12))
story.append(sp(0.3))

story.append(Paragraph(
    "The ClinGen-MoE model applied to PhysioNet 2012 generates synthetic ICU patient data "
    "that combines two modalities: static descriptors (Age, Gender, ICU Type, Height, Weight) "
    "and time-series measurements (24 clinical features over 48 hours). "
    "Synthetic values are conditioned on patient demographics — a 75-year-old cardiac patient "
    "generates different vital sign trajectories than a 30-year-old surgical patient.",
    body_style))
story.append(sp(0.2))
story.append(Paragraph(
    "Below are 3 concrete use cases, each built around the unique combination of "
    "static and time-series modalities available in PhysioNet 2012.",
    body_style))
story.append(sp(0.5))

# ── Features table ────────────────────────────────────────────────────────────
story.append(Paragraph("The Dataset: Two Modalities", bold_style))
story.append(sp(0.2))

feat_data = [
    ["Modality", "Features", "Count"],
    ["Static Descriptors\n(time-invariant)",
     "Age · Gender · Height · Weight · ICU Type\n(Coronary, Cardiac Surgery, Medical, Surgical)",
     "5"],
    ["Vital Signs\n(time-series)",
     "Heart Rate · Systolic BP · Diastolic BP · Mean BP · Respiratory Rate\n"
     "O2 Saturation · GCS Verbal · GCS Eye · GCS Motor",
     "9"],
    ["Lab Tests\n(time-series)",
     "Glucose · Potassium · Sodium · Creatinine · Urea Nitrogen\n"
     "Bicarbonate · Hematocrit · White Blood Cells · Magnesium · and more",
     "15"],
    ["Total", "All measured over a 48-hour ICU window · conditioned on static descriptors", "24 + 5"],
]
story.append(feature_table(
    feat_data[0], feat_data[1:],
    [4*cm, 10*cm, 2.5*cm], DARK))
story.append(sp(0.8))

# ═══════════════════════════════════════════════════════
# USE CASE 1
# ═══════════════════════════════════════════════════════
story.append(KeepTogether([
    section_header("1   Demographically-Conditioned ICU Subgroup Augmentation", BLUE),
    sp(0.3),
]))

story.append(Paragraph("<b>What is this use case?</b>", bold_style))
story.append(Paragraph(
    "Some ICU patient subgroups are too rare for a hospital to train a reliable AI model. "
    "For example, a hospital may have very few elderly women admitted to the Coronary Care Unit. "
    "Because the Conditional GRU-VAE is conditioned on age, gender and ICU type, it can generate "
    "as many synthetic patients as needed for any specific demographic profile — "
    "without collecting additional real patient data.",
    body_style))
story.append(sp(0.3))

story.append(Paragraph("<b>Features used and why</b>", bold_style))
uc1_data = [
    ["Modality", "Feature", "Role in this use case"],
    ["Static", "Age",      "Conditions the generation — elderly patients have higher creatinine, lower HR variability"],
    ["Static", "Gender",   "Conditions the generation — female patients have different cardiac baselines"],
    ["Static", "ICU Type", "CCU, CSRU, MICU, SICU — each unit has distinct clinical profiles"],
    ["Static", "Height / Weight", "Body size affects drug dosing and physiological baselines"],
    ["Time-series", "Heart Rate · BP · O2 Sat", "Core vitals — generated to match the conditioned demographic"],
    ["Time-series", "Creatinine · Urea Nitrogen", "Kidney markers — naturally elevated in elderly patients"],
    ["Time-series", "GCS Verbal · Eye · Motor", "Neurological status — conditioned on age and ICU type"],
]
story.append(feature_table(
    uc1_data[0], uc1_data[1:],
    [2.5*cm, 4.5*cm, 9.5*cm], BLUE))
story.append(sp(0.3))

story.append(Paragraph("<b>Key results</b>", bold_style))
story.append(bullet("Input: Age=78, Gender=Female, ICU Type=CCU → model generates realistic coronary care vital trajectories for elderly women."))
story.append(bullet("Input: Age=35, Gender=Male, ICU Type=MICU → model generates young male medical ICU profiles with different baselines."))
story.append(bullet("Synthetic means for conditioned subgroups stay within physiological bounds (clinical plausibility check passed)."))
story.append(bullet("DCR & NNDR confirm: synthetic patients are not copies of real patients — privacy is preserved."))
story.append(sp(0.3))

story.append(real_world_box(
    "A hospital with only 40 elderly female CCU patients can generate 1,000 synthetic "
    "profiles for that exact subgroup. A mortality prediction model trained on this augmented "
    "dataset performs significantly better on the rare subgroup — at zero privacy cost.",
    BLUE))
story.append(sp(0.8))

# ═══════════════════════════════════════════════════════
# USE CASE 2
# ═══════════════════════════════════════════════════════
story.append(KeepTogether([
    section_header("2   ICU-Type Specific Vital Sign Baseline Calibration", GREEN),
    sp(0.3),
]))

story.append(Paragraph("<b>What is this use case?</b>", bold_style))
story.append(Paragraph(
    "Different ICU units treat very different patient populations. "
    "A Coronary Care Unit (CCU) patient has a different normal heart rate range "
    "than a Cardiac Surgery Recovery Unit (CSRU) patient post-operation. "
    "Clinical alert systems trained on mixed populations fire too many false alarms. "
    "Using demographically-conditioned synthetic data, each ICU type can calibrate its "
    "own alert thresholds independently.",
    body_style))
story.append(sp(0.3))

story.append(Paragraph("<b>ICU-type baselines in the dataset</b>", bold_style))
uc2_data = [
    ["Feature", "CCU\n(Coronary)", "CSRU\n(Cardiac Surgery)", "MICU\n(Medical)", "SICU\n(Surgical)"],
    ["Heart Rate (bpm)",    "Lower — stable cardiac rhythm",   "Higher — post-op stress",  "Variable — infection", "Variable — trauma"],
    ["Systolic BP (mmHg)",  "Controlled — hypertension common","Lower — post-op hypotension","Variable","Variable"],
    ["O2 Saturation (%)",   "High — closely monitored",        "May dip post-op",           "Often low — respiratory","Normal post-surgery"],
    ["Creatinine (mg/dL)",  "Elevated — cardiac output low",   "Elevated — post-op AKI risk","Variable","Variable"],
    ["GCS Score",           "Normal unless arrest",            "Normal unless complication", "Often reduced","Normal"],
]
story.append(feature_table(
    uc2_data[0], uc2_data[1:],
    [3.5*cm, 3.2*cm, 3.2*cm, 3.2*cm, 3.4*cm], GREEN))
story.append(sp(0.3))

story.append(Paragraph("<b>Key results</b>", bold_style))
story.append(bullet("Generate 500 synthetic CCU patients → compute 95th percentile HR → set CCU-specific tachycardia alert."))
story.append(bullet("Generate 500 synthetic CSRU patients → post-op BP thresholds are systematically lower → alerts calibrated accordingly."))
story.append(bullet("Each ICU type gets its own alert profile — without needing to collect more real patients from each unit."))
story.append(bullet("PhysioNet 2012 provides the ICU Type label directly — this use case is not possible without the static modality."))
story.append(sp(0.3))

story.append(real_world_box(
    "A newly opened Cardiac Surgery ICU with only 30 patients can use conditioned synthetic data "
    "to calibrate its monitoring system before it has collected enough real data. "
    "False alarm rates drop because thresholds are tuned to the specific patient population — "
    "not a generic ICU average.",
    GREEN))
story.append(sp(0.8))

# ═══════════════════════════════════════════════════════
# USE CASE 3
# ═══════════════════════════════════════════════════════
story.append(KeepTogether([
    section_header("3   Privacy-Safe Sharing of Complete Patient Profiles", PURPLE),
    sp(0.3),
]))

story.append(Paragraph("<b>What is this use case?</b>", bold_style))
story.append(Paragraph(
    "Real patient records cannot be shared across hospitals due to GDPR and HIPAA. "
    "Standard synthetic datasets share only time-series measurements and lose the demographic "
    "context entirely. Because PhysioNet 2012 includes both static descriptors and time-series, "
    "the generated synthetic records are complete patient profiles — "
    "demographics and measurements together — and can be shared freely.",
    body_style))
story.append(sp(0.3))

story.append(Paragraph("<b>What a complete synthetic profile contains</b>", bold_style))
uc3_data = [
    ["Component", "Fields included", "Why it matters for sharing"],
    ["Static descriptors",
     "Age · Gender · Height · Weight · ICU Type",
     "Demographic context needed for subgroup analysis and model stratification"],
    ["Vital signs (48h)",
     "HR · BP (Systolic, Diastolic, Mean) · RR · O2 Sat · GCS",
     "Core clinical trajectory — main input for mortality and deterioration models"],
    ["Lab results (48h)",
     "Creatinine · Glucose · Potassium · Sodium · WBC · Hematocrit · and more",
     "Organ function markers — essential for AKI, sepsis, and metabolic models"],
    ["Privacy guarantee",
     "DCR(synthetic) ≈ DCR(real held-out)",
     "Model generalised — no real patient was copied into the synthetic record"],
]
story.append(feature_table(
    uc3_data[0], uc3_data[1:],
    [3.5*cm, 6*cm, 7*cm], PURPLE))
story.append(sp(0.3))

story.append(Paragraph("<b>Key results</b>", bold_style))
story.append(bullet("All 5 static features + 24 time-series features generated together — one complete ICU patient record per row."))
story.append(bullet("Privacy verified: DCR and NNDR confirm synthetic patients are not memorised copies of real PhysioNet 2012 patients."))
story.append(bullet("GDPR Article 4(1) does not apply: no real person appears in the synthetic data."))
story.append(bullet("48-hour window matches the PhysioNet 2012 benchmark — synthetic data is directly comparable to the real dataset."))
story.append(sp(0.3))

story.append(real_world_box(
    "Hospital A in Paris generates a synthetic version of its PhysioNet-format ICU records "
    "and shares them with Hospital B in Lyon within hours — no legal agreements needed, "
    "no ethics board approval required. Hospital B trains an AKI early warning model "
    "on Paris demographics without ever seeing a single real Parisian patient record.",
    PURPLE))
story.append(sp(0.8))

# ── Summary table ─────────────────────────────────────────────────────────────
story.append(HRFlowable(width="100%", thickness=1, color=GRAY, spaceAfter=8))
story.append(Paragraph("Summary: 3 Use Cases and the Features They Use", bold_style))
story.append(sp(0.2))

sum_data = [
    ["#", "Use Case", "Key features used"],
    ["1", "Demographically-Conditioned Subgroup Augmentation",
     "Age · Gender · ICU Type · Height · Weight\n+ Heart Rate · BP · Creatinine · GCS"],
    ["2", "ICU-Type Specific Alert Calibration",
     "ICU Type · Heart Rate · Systolic BP · O2 Sat · Creatinine"],
    ["3", "Privacy-Safe Complete Profile Sharing",
     "All 5 static features + all 24 time-series features\n+ DCR & NNDR privacy verification"],
]
story.append(feature_table(
    sum_data[0], sum_data[1:],
    [0.8*cm, 6.5*cm, 9.2*cm], DARK))

doc.build(story)
print("Saved: UseCase_PhysioNet12.pdf")
