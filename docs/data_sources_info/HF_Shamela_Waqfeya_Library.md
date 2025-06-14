---
license: mit
task_categories:
- image-to-text
language:
- ar
pretty_name: Shamela Waqfeya Library
size_categories:
- 1K<n<10K
configs:
- config_name: index
  data_files:
  - split: index
    path: index.tsv
---

# Shamela Waqfeya Library

## 📖 Overview
Shamela Waqfeya is one of the primary online resources for Islamic books, similar to [Shamela](https://shamela.ws). It hosts more than 4,500 PDF books across over 40 categories.

In this dataset, we processed the original PDF files using Google Document AI APIs and extracted their contents into two additional formats: TXT and DOCX.

## 📊 Dataset Contents
The dataset includes 12,877 PDF files (spanning 5,138,027 pages) representing 4,661 Islamic books. Each book is provided in three formats:
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
|Category                   |Percentage|Number of Books|
|---------------------------|----------|---------------|
|أصول الفقه والقواعد الفقهية|4.14%     |193            |
|الأجزاء الحديثية           |8.54%     |398            |
|الأدب والبلاغة             |4.72%     |220            |
|الأنساب                    |0.51%     |24             |
|البلدان والجغرافيا والرحلات|0.92%     |43             |
|التاريخ                    |3.22%     |150            |
|التجويد والقراءات          |0.51%     |24             |
|التراجم والطبقات           |8.28%     |386            |
|التفاسير                   |3.05%     |142            |
|الجوامع والمجلات ونحوها    |0.79%     |37             |
|الدعوة وأحوال المسلمين     |3.00%     |140            |
|الدواوين الشعرية           |0.09%     |4              |
|الرقاق والآداب والأذكار    |4.76%     |222            |
|السياسة الشرعية والقضاء    |1.20%     |56             |
|السيرة والشمائل            |2.32%     |108            |
|العقيدة                    |8.58%     |400            |
|العلل والسؤالات            |1.35%     |63             |
|الغريب والمعاجم ولغة الفقه |2.12%     |99             |
|الفتاوى                    |0.82%     |38             |
|الفرق والردود              |1.39%     |65             |
|النحو والصرف               |2.30%     |107            |
|بحوث ومسائل                |4.23%     |197            |
|شروح الحديث                |2.96%     |138            |
|علوم أخرى                  |0.26%     |12             |
|علوم الحديث                |3.82%     |178            |
|علوم القرآن                |4.78%     |223            |
|فقه حنبلي                  |1.74%     |81             |
|فقه حنفي                   |0.75%     |35             |
|فقه شافعي                  |1.01%     |47             |
|فقه عام                    |1.46%     |68             |
|فقه مالكي                  |1.27%     |59             |
|فهارس الكتب والأدلة        |1.46%     |68             |
|كتب إسلامية عامة           |0.06%     |3              |
|كتب ابن أبي الدنيا         |1.16%     |54             |
|كتب ابن القيم              |0.99%     |46             |
|كتب ابن تيمية              |1.54%     |72             |
|كتب الألباني               |1.57%     |73             |
|كتب التخريج والزوائد       |2.47%     |115            |
|كتب اللغة                  |0.84%     |39             |
|متون الحديث                |5.13%     |239            |
|محاضرات مفرغة              |0.02%     |1              |
|مخطوطات حديثية             |0.00%     |0              |

### 📄 TXT Format
Each TXT file contains the raw text extracted by Google Document AI from the corresponding PDF. Pages are separated by the special marker: `\nPAGE_SEPARATOR\n`.

### 📝 DOCX Format
DOCX files also contain text extracted via Google Document AI. However, all consecutive whitespace characters have been replaced with a single space character (`' '`) to help maintain a consistent 1:1 alignment with the original PDF layout.