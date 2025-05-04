# 📦 Recommended Semantic Chunk Schema for Hadith

**Table name:** `hadith_chunks`

| 📌 Field         | 💬 Description                                                              | 🔑 Example                                        |
|------------------|---------------------------------------------------------------------------|--------------------------------------------------|
| `id`            | Unique chunk ID                                                         | `hadith-001-1`                                  |
| `source_id`     | Parent Hadith collection/document ID                                    | `hadith-001`                                    |
| `type`         | Type of chunk (`hadith`, `isnad`, `matn`, `commentary`)                 | `matn`                                          |
| `text`         | Raw chunk text                                                          | `قال رسول الله ﷺ: إنما الأعمال بالنيات ...`    |
| `start_line`    | Line or position where the chunk starts in the original document         | `12`                                           |
| `end_line`      | Line or position where the chunk ends                                   | `15`                                           |
| `main_entities` | Key extracted entities (people, places, concepts, narrators)             | `[“رسول الله ﷺ”, “نية”]`                      |
| `topics`        | Detected topics/themes (prayer, fasting, intention, sincerity, etc.)     | `[“النية”, “الأعمال”, “الإخلاص”]`             |
| `relations`     | Named relations or isnad chain (who narrated from whom)                 | `[("عمر بن الخطاب", "narrated from", "النبي ﷺ")]` |
| `language`      | Language code                                                          | `ar`                                           |
| `embedding`     | Precomputed embedding vector (optional, for vector DB)                 | `[0.121, -0.334, 0.998, ...]`                 |
| `metadata`      | Extra metadata (book, author, chapter, narrator, hadith number)         | `{“book”: “صحيح البخاري”, “narrator”: “عمر بن الخطاب”, “hadith_no”: 1}` |

---

## ✅ Key Tips for Hadith-specific Chunking

- **Split into subtypes:**
  - `isnad` → chain of narrators
  - `matn` → main text/content
  - `commentary` → explanations or notes (if present)

- **Add `source_collection` field if using mixed sources:**
  - Example values: `Bukhari`, `Muslim`, `Tirmidhi`, etc.

- **Optionally store additional fields:**
  - `grade` → e.g., `sahih`, `hasan`, `daif`
  - `narrator_reliability` → assessment of narrator trustworthiness
  - `book`, `chapter`, `page_number`

---

## ✅ Example JSON Record

```json
{
  "id": "hadith-001-1",
  "source_id": "hadith-001",
  "type": "matn",
  "text": "إنما الأعمال بالنيات وإنما لكل امرئ ما نوى",
  "start_line": 12,
  "end_line": 15,
  "main_entities": ["رسول الله ﷺ", "نية"],
  "topics": ["النية", "الإخلاص"],
  "relations": [["عمر بن الخطاب", "narrated from", "النبي ﷺ"]],
  "language": "ar",
  "embedding": [0.121, -0.334, 0.998],
  "metadata": {
    "book": "صحيح البخاري",
    "narrator": "عمر بن الخطاب",
    "hadith_no": 1,
    "grade": "sahih"
  }
}
