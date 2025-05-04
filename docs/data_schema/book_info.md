book.id                     // Unique identifier for the book
book.version_uri            // URI for the specific version of the book
book.date                   // Date of publication or creation
book.category.ar            // Category of the book (Arabic)
book.category.lat           // Category of the book (Latin script)
book.author.ar              // Author's name in Arabic
book.author.lat             // Author's name in Latin script
book.author.lat_shuhra      // Author's Latin short name (Shuhra)
book.author.lat_full_name   // Author's full name in Latin script
book.title.ar               // Title of the book in Arabic
book.title.lat              // Title of the book in Latin script
book.shortname              // Short name or abbreviation of the book
book.filename               // Filename of the book (e.g., PDF or TXT file)
book.language               // Language of the book (e.g., Arabic, English)
book.direction              // Text direction (e.g., RTL for Arabic, LTR for English)

book.structure.has_sections // Boolean indicating if the book has sections
book.structure.has_chapters // Boolean indicating if the book has chapters
book.structure.has_volumes  // Boolean indicating if the book has volumes
book.structure.has_pages    // Boolean indicating if the book has page-level data
book.structure.has_references // Boolean indicating if the book includes references or footnotes

book.edition                // Edition of the book (e.g., "1st Edition", "Revised Edition")
book.ed_info                // Additional edition information (e.g., publisher notes)

book.publisher.name         // Name of the publisher
book.publisher.place        // Place of publication (e.g., city, country)
book.publisher.date         // Date of publication
book.publisher.isbn         // ISBN number of the book

book.sources[].type         // Type of source (e.g., library, archive, website, other)
book.sources[].name         // Name of the source (e.g., library name, website name)
book.sources[].location     // Physical or digital location of the source (e.g., city, URL)
book.sources[].access_date  // Date the source was accessed
book.sources[].notes        // Additional notes about the source

book.status                 // Status of the book (e.g., published, draft)
book.page_count             // Total number of pages
book.volume_count           // Number of volumes
book.tok_length             // Tokenized length of the book
book.char_length            // Character length of the book

book.file_paths.pdf[]       // List of paths to PDF files
book.file_paths.txt[]       // List of paths to TXT files
book.file_paths.docx[]      // List of paths to DOCX files
book.local_path             // Local file path to the book

book.tags[]                 // List of tags associated with the book
book.genres[]               // List of genres (e.g., Fiction, History)
book.author_from_uri        // Author information extracted from the URI
book.source                 // General source information (e.g., origin or repository)
book.comments               // Comments or notes about the book
book.link                   // Link to the book (e.g., online resource or repository)
book.linkmin                // Minimal or shortened link to the book