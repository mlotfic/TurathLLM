# 📦 Chunk Types Schema for Islamic Texts

A list of possible chunk types to assign when splitting and organizing Islamic texts.

---

## 📖 Core Religious Types

- **Hadith**  
  → Prophetic traditions (with chain of narration)

- **Quran Ayah**  
  → Direct Quran verses

- **Tafsir**  
  → Quranic commentary / explanation

- **Fatwa**  
  → Religious legal opinion

- **Fiqh Explanation**  
  → Jurisprudence reasoning

- **Aqeedah**  
  → Creed / belief explanation

- **Biography (Seerah / Tarikh)**  
  → Life stories of the Prophet ﷺ, companions, scholars

- **Khutbah / Sermon**  
  → Friday sermons, public talks

- **Du’a / Supplication**  
  → Prayers and invocations

- **Quranic Parable / Story**  
  → Quran-based narratives

- **Historical Event**  
  → Islamic historical narrative (battles, treaties, migrations)

---

## 💡 Scholarly / Intellectual Types

- **Commentary (Sharh)**  
  → Explanation of Hadith, poetry, or scholarly works

- **Glossary / Definition**  
  → Definition of Arabic or Islamic terms

- **Legal Ruling (Hukm)**  
  → Practical ruling on an issue

- **Debate / Polemic**  
  → Scholarly disagreements or arguments

- **Philosophical / Ethical Note**  
  → Reflections, ethics, wisdom

---

## 🛠️ Metadata / Utility Types

- **Introduction / Preface**  
  → Author’s introduction or purpose

- **Index / Table of Contents**  
  → Book navigation or section headings

- **Footnote / Editor Note**  
  → Modern editorial or scholarly notes

- **Manuscript Variant**  
  → Alternate readings, marginal notes, or scribal variants

---

## 🌍 Contextual Types (Advanced)

- **Tribal / Social Context**  
  → Tribal relationships, genealogies, social dynamics

- **Political Context**  
  → Caliphate, leadership, governance, political events

- **Scientific / Medical Reference**  
  → Scientific or medical references in historical texts

---

## ✅ Example JSON Label Schema

```json
{
  "chunk_id": "001",
  "text": "قال رسول الله ﷺ: إنما الأعمال بالنيات وإنما لكل امرئ ما نوى",
  "type": "Hadith",
  "source": "Bukhari 1"
}
