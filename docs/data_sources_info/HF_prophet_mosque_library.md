---
license: mit
task_categories:
- image-to-text
language:
- ar
pretty_name: Prophet's Mosque Library
size_categories:
- 10K<n<100K
configs:
- config_name: index
  data_files:
  - split: index
    path: index.tsv
---

# Prophet's Mosque Library

## 📖 Overview
[Prophet’s Mosque Library](https://alharamain.gov.sa/public/?page=page_299500) is one of the primary resources for Islamic books. It hosts more than 48,000 PDF books across over 70 categories.

In this dataset, we processed the original PDF files using Google Document AI APIs and extracted their contents into two additional formats: TXT and DOCX.

## 📊 Dataset Contents
The dataset includes 70,884 PDF files (spanning 23,494,042 pages) representing 48,717 Islamic books. Each book is provided in three formats:
- PDF files are located in the `pdf` directory.
- TXT files are located in the `txt` directory.
- DOCX files are located in the `docx` directory.

All three directories (`pdf`, `txt`, and `docx`) share the same folder structure.

For example, a book located at `pdf/category/book/file.pdf` will have its corresponding TXT and DOCX versions at `txt/category/book/file.txt` and `docx/category/book/file.docx`, respectively.

The `index.tsv` file contains the following information about each book in the dataset:
- `category`: One of the 74 book categories available in the dataset.
- `author`: Book author.
- `title`: Book title.
- `pages`: Total number of book pages.
- `pdf_paths`: Array of PDF files paths as each book can be splitted into multiple files (e.g. Books with multiple volumes).
- `txt_paths`: Array of TXT files paths as each book can be splitted into multiple files (e.g. Books with multiple volumes).
- `docx_paths`: Array of DOCX files paths as each book can be splitted into multiple files (e.g. Books with multiple volumes).

The books are organized into 74 categories, as listed below:
| Category                       | Percentage | Number of Books |
| ------------------------------ | ---------- | --------------- |
| علوم القرآن                    | 2.07%      | 1010            |
| التجويد والقراءات              | 1.91%      | 931             |
| مباحث قرآنية عامة              | 2.00%      | 975             |
| أصول التفسير                   | 0.43%      | 208             |
| التفاسير القديمة               | 0.61%      | 298             |
| التفاسير الحديثة               | 0.81%      | 397             |
| فهارس الحديث                   | 0.24%      | 118             |
| مصطلح الحديث                   | 2.34%      | 1140            |
| الجرح والتعديل                 | 1.90%      | 926             |
| الحديث الستة                   | 1.06%      | 515             |
| مسانيد الأئمة الأربعة          | 0.33%      | 161             |
| المسانيد الأخرى والجوامع       | 1.20%      | 586             |
| باقي مجموعات الحديث            | 3.02%      | 1469            |
| التوحيد والعقيدة               | 6.26%      | 3048            |
| الفرق والأديان والردود         | 3.95%      | 1926            |
| أصول الفقه وقواعده             | 2.91%      | 1416            |
| الفرائض                        | 0.44%      | 212             |
| الأحوال الشخصية                | 0.14%      | 66              |
| السياسة الشرعية                | 1.24%      | 603             |
| الفقه العام                    | 6.48%      | 3157            |
| الفقه الحنفي                   | 0.39%      | 192             |
| الفقه المالكي                  | 0.69%      | 335             |
| الفقه الشافعي                  | 0.65%      | 318             |
| الفقه الحنبلي                  | 0.92%      | 447             |
| فقه المذاهب الأخرى             | 0.15%      | 74              |
| الفتاوى                        | 1.27%      | 618             |
| التزكية والأخلاق والآداب       | 5.91%      | 2881            |
| الأذكار والشعائر               | 0.94%      | 460             |
| اللغة العربية                  | 1.99%      | 970             |
| البلاغة                        | 0.48%      | 235             |
| النحو والصرف                   | 1.98%      | 964             |
| العروض                         | 0.06%      | 27              |
| الأدب                          | 5.75%      | 2803            |
| السيرة النبوية                 | 2.27%      | 1106            |
| الجغرافيا والرحلات             | 1.56%      | 758             |
| التراجم والأعلام               | 4.65%      | 2265            |
| الأنساب                        | 0.52%      | 254             |
| تاريخ أوربا                    | 0.09%      | 46              |
| تاريخ المملكة العربية السعودية | 0.68%      | 331             |
| التاريخ الإسلامي               | 3.37%      | 1643            |
| تاريخ مكة المكرمة              | 0.53%      | 256             |
| تاريخ المدينة المنورة          | 0.52%      | 255             |
| تاريخ أفريقيا                  | 0.19%      | 94              |
| المجاميع                       | 0.39%      | 190             |
| المجاميع العشر                 | 0.49%      | 240             |
| الأدلة والفهارس                | 0.83%      | 402             |
| المكتبات وطرق البحث            | 0.70%      | 343             |
| الدوريات                       | 0.02%      | 9               |
| الخطب والمساجد                 | 0.67%      | 327             |
| الثقافة الإسلامية العامة       | 2.93%      | 1425            |
| الدعوة والدفاع عن الإسلام      | 2.66%      | 1294            |
| قضايا الإصلاح الإجتماعي        | 1.83%      | 893             |
| الأمن الفكري                   | 0.10%      | 49              |
| علوم الحاسب الآلي              | 0.22%      | 108             |
| الإعلام ووسائل الإتصال         | 0.17%      | 84              |
| الموسوعات العامة               | 0.14%      | 67              |
| الإعلام والصحافة               | 0.12%      | 57              |
| المؤتمرات والندوات             | 0.77%      | 373             |
| علم النفس                      | 0.95%      | 462             |
| المنطق                         | 0.00%      | 1               |
| علم الإجتماع                   | 0.44%      | 215             |
| علم الإحصاء                    | 0.07%      | 36              |
| العلوم السياسية                | 1.27%      | 620             |
| الإقتصاد                       | 1.34%      | 653             |
| القانون                        | 0.41%      | 200             |
| الإدارة                        | 1.07%      | 520             |
| العلوم العسكرية                | 0.10%      | 49              |
| التربية والتعليم               | 4.15%      | 2023            |
| العلوم بحتة                    | 0.75%      | 365             |
| التكنولوجيا والعلوم التطبيقية  | 0.18%      | 89              |
| الطب                           | 1.56%      | 758             |
| الزراعة                        | 0.44%      | 215             |
| الفنون                         | 0.27%      | 130             |
| غير مصنف                       | 0.05%      | 26              |

### 📄 TXT Format
Each TXT file contains the raw text extracted by Google Document AI from the corresponding PDF. Pages are separated by the special marker: `\nPAGE_SEPARATOR\n`.

### 📝 DOCX Format
DOCX files also contain text extracted via Google Document AI. However, all consecutive whitespace characters have been replaced with a single space character (`' '`) to help maintain a consistent 1:1 alignment with the original PDF layout.
