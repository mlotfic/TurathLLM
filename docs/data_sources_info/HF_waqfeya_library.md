---
license: mit
task_categories:
- image-to-text
language:
- ar
pretty_name: Waqfeya Library
size_categories:
- 10K<n<100K
configs:
- config_name: index
  data_files:
  - split: index
    path: index.tsv
---

# Waqfeya Library

## 📖 Overview
[Waqfeya](https://waqfeya.net) is one of the primary online resources for Islamic books, similar to [Shamela](https://shamela.ws). It hosts more than 10,000 PDF books across over 80 categories.

In this dataset, we processed the original PDF files using Google Document AI APIs and extracted their contents into two additional formats: TXT and DOCX.

## 📊 Dataset Contents
The dataset includes 22,443 PDF files (spanning 8,978,634 pages) representing 10,150 Islamic books. Each book is provided in three formats:
- PDF files are located in the `pdf` directory.
- TXT files are located in the `txt` directory.
- DOCX files are located in the `docx` directory.

All three directories (`pdf`, `txt`, and `docx`) share the same folder structure.

For example, a book located at `pdf/category/book/file.pdf` will have its corresponding TXT and DOCX versions at `txt/category/book/file.txt` and `docx/category/book/file.docx`, respectively.

The `index.tsv` file contains the following information about each book in the dataset:
- `category`: One of the 83 book categories available in the dataset.
- `author`: Book author.
- `title`: Book title.
- `pages`: Total number of book pages.
- `volumes`: Number of book volumes.
- `pdf_paths`: Array of PDF files paths as each book can be splitted into multiple files (e.g. Books with multiple volumes).
- `txt_paths`: Array of TXT files paths as each book can be splitted into multiple files (e.g. Books with multiple volumes).
- `docx_paths`: Array of DOCX files paths as each book can be splitted into multiple files (e.g. Books with multiple volumes).

The books are organized into 83 categories, as listed below:
|Category                      |Percentage|Number of Books|
|------------------------------|----------|---------------|
|علوم القرآن                   |2.63%     |267            |
|التجويد والقراءات             |1.39%     |141            |
|مباحث قرآنية عامة             |1.26%     |128            |
|التفاسير                      |2.24%     |227            |
|أصول التفسير                  |0.45%     |46             |
|فهارس الحديث                  |0.3%      |30             |
|مصطلح الحديث                  |3.51%     |356            |
|الجرح والتعديل                |2.33%     |236            |
|الحديث الستة                  |2.29%     |232            |
|مسانيد الأئمة الأربعة         |0.69%     |70             |
|المسانيد الأخرى والجوامع      |2.27%     |230            |
|باقي مجموعات الحديث           |5.68%     |577            |
|التوحيد والعقيدة              |5.53%     |561            |
|الرد الصهيونية والماسونية     |0.15%     |15             |
|الرد الأشاعرة والماتريدية     |0.17%     |17             |
|الرد الشيوعية والإلحاد        |0.35%     |36             |
|الرد الصوفية والطرقية         |0.53%     |54             |
|الرد العلمانية والليبرالية    |0.59%     |60             |
|الرد اليهود والنصارى          |1.47%     |149            |
|الرد الشيعة والرافضة          |1.78%     |181            |
|الفرق والأديان والردود        |2.8%      |284            |
|أصول الفقه وقواعده            |3.95%     |401            |
|الفرائض                       |0.18%     |18             |
|الأحوال الشخصية               |0.19%     |19             |
|السياسة الشرعية               |2.09%     |212            |
|الفقه العام                   |6.76%     |686            |
|الفقه الحنفي                  |0.62%     |63             |
|الفقه المالكي                 |1.23%     |125            |
|الفقه الشافعي                 |1.25%     |127            |
|الفقه الحنبلي                 |1.9%      |193            |
|فقه المذاهب الأخرى            |0.07%     |7              |
|الفتاوى                       |1.4%      |142            |
|التزكية والأخلاق والآداب      |4.15%     |421            |
|الأذكار والشعائر              |1.59%     |161            |
|اللغة                         |1.37%     |139            |
|المعاجم والقواميس الأجنبية    |0.23%     |23             |
|المعاجم والقواميس العربية     |1.06%     |108            |
|البلاغة                       |0.41%     |42             |
|النحو والصرف                  |2.0%      |203            |
|العروض                        |0.2%      |20             |
|دواوين الشعر                  |1.51%     |153            |
|الأدب                         |2.79%     |283            |
|السيرة النبوية                |2.04%     |207            |
|الجغرافيا والرحلات            |1.66%     |168            |
|التراجم والأعلام              |5.92%     |601            |
|الأنساب                       |0.18%     |18             |
|تاريخ أوربا                   |0.1%      |10             |
|تاريخ المملكة العربية السعودية|0.07%     |7              |
|التاريخ الإسلامي              |2.56%     |260            |
|تاريخ مكة المكرمة             |0.28%     |28             |
|تاريخ المدينة المنورة         |0.21%     |21             |
|تاريخ أفريقيا                 |0.13%     |13             |
|المجاميع المكررة              |0.39%     |40             |
|المجاميع                      |0.67%     |68             |
|فهارس المخطوطات               |0.5%      |51             |
|الأدلة والفهارس               |0.61%     |62             |
|المكتبات وطرق البحث           |0.4%      |41             |
|الدوريات                      |0.18%     |18             |
|الخطب والمساجد                |0.47%     |48             |
|الثقافة الإسلامية العامة      |1.93%     |196            |
|الدعوة والدفاع عن الإسلام     |3.0%      |304            |
|قضايا الإصلاح الإجتماعي       |1.0%      |101            |
|علوم الحاسب الآلي             |0.08%     |8              |
|الإعلام ووسائل الإتصال        |0.18%     |18             |
|الموسوعات العامة              |0.17%     |17             |
|الإعلام والصحافة              |0.09%     |9              |
|المؤتمرات والندوات            |0.35%     |36             |
|الرؤى والأحلام                |0.23%     |23             |
|علم النفس                     |0.28%     |28             |
|المنطق                        |0.05%     |5              |
|علم الإجتماع                  |0.09%     |9              |
|علم الإحصاء                   |0.03%     |3              |
|العلوم السياسية               |0.38%     |39             |
|الإقتصاد                      |0.38%     |39             |
|القانون                       |0.1%      |10             |
|الإدارة                       |0.26%     |26             |
|العلوم العسكرية               |0.06%     |6              |
|التربية والتعليم              |0.87%     |88             |
|العلوم بحتة                   |0.15%     |15             |
|التكنولوجيا والعلوم التطبيقية |0.01%     |1              |
|الطب                          |0.53%     |54             |
|الزراعة                       |0.05%     |5              |
|الفنون                        |0.06%     |6              |

### 📄 TXT Format
Each TXT file contains the raw text extracted by Google Document AI from the corresponding PDF. Pages are separated by the special marker: `\nPAGE_SEPARATOR\n`.

### 📝 DOCX Format
DOCX files also contain text extracted via Google Document AI. However, all consecutive whitespace characters have been replaced with a single space character (`' '`) to help maintain a consistent 1:1 alignment with the original PDF layout.
