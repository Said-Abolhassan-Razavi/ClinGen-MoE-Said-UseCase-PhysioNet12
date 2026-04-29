# ClinGen-MoE — Use Cases: PhysioNet 2012

**Author:** Said Abolhassan Razavi  
**Project:** ClinGen-MoE · Université Paris-Saclay M1 AI  
**Dataset:** PhysioNet Computing in Cardiology Challenge 2012

## Overview

This repository contains 3 use cases demonstrating what can be done with AI-generated
synthetic ICU patient data from PhysioNet 2012. The key feature of this dataset is that
it combines two modalities: static descriptors (demographics) and time-series measurements.

## Use Cases

| # | Use Case | Key Feature |
|---|---|---|
| 1 | Demographically-Conditioned Subgroup Augmentation | Age · Gender · ICU Type → conditioned generation |
| 2 | ICU-Type Specific Alert Calibration | Different thresholds per ICU unit |
| 3 | Privacy-Safe Complete Profile Sharing | Static + time-series + DCR/NNDR verified |

## Generate the PDF

```bash
pip install reportlab
python generate_usecase.py
```

Output: `UseCase_PhysioNet12.pdf`

## Related Repository

SOTA code: [ClinGen-MoE-Said-StateOfArt-PhysioNet12](https://github.com/siad-Razavi/ClinGen-MoE-Said-StateOfArt-PhysioNet12)
