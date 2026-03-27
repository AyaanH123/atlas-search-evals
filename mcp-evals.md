# MCP Atlas Search Evals

**134 evals** across **16 categories**

---

## Index Management — Text Search Index Creation

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `IDX_TEXT_DYNAMIC` | Dynamic Mapping Mode | Create index with dynamic: true to auto-index all fields | 2 |
| `IDX_TEXT_STATIC` | Explicit Field Definitions | Create index with dynamic: false and explicit field mappings | 1 |
| `IDX_TEXT_TYPESETS` | Configurable Dynamic TypeSets | Use typeSets to control which field types get auto-indexed | 1 |
| `IDX_TEXT_FIELD_TYPES` | Field Type Definitions | Define specific field types: string, number, date, objectId, boolean, geo, autocomplete, token, uuid, embeddedDocuments, document | 1 |
| `IDX_TEXT_ANALYZER_INDEX` | Index-Time Analyzer | Configure analyzer applied to string fields when indexing (default: lucene.standard) | 2 |
| `IDX_TEXT_ANALYZER_SEARCH` | Search-Time Analyzer | Configure a different analyzer for query text than index time | 1 |
| `IDX_TEXT_ANALYZER_BUILTIN` | Built-in Analyzers | Use built-in analyzers: lucene.standard, lucene.simple, lucene.whitespace, lucene.keyword, language-specific | 1 |
| `IDX_TEXT_ANALYZER_CUSTOM` | Custom Analyzer | Define custom analyzer with tokenizer + filters pipeline | 1 |
| `IDX_TEXT_MULTI_ANALYZER` | Multi Analyzer | Alternate analyzers on same field via multi for different query strategies | 1 |
| `IDX_TEXT_TOKEN_NORMALIZER` | Token Type Normalizer | Configure normalizers for token type: lowercase or none | 2 |
| `IDX_TEXT_SYNONYM_SOURCE` | Synonym Source Mappings | Configure synonym source mappings in index for synonym-aware search | 1 |
| `IDX_TEXT_FACET_MAPPING` | Facet-Type Field Mappings | Map fields with stringFacet / numberFacet to enable $searchMeta facet queries | 1 |
| `IDX_TEXT_MULTI_FIELD` | Multi-Field Definitions | Index multiple fields in one index definition | 1 |
| `IDX_TEXT_STORED_SOURCE` | Stored Source Configuration | Configure storedSource to store fields on mongot for returnStoredSource | 3 |
| `IDX_TEXT_NUM_PARTITIONS` | Index Partitioning | Set numPartitions for collections exceeding 2B documents | 1 |

### `IDX_TEXT_DYNAMIC` — Dynamic Mapping Mode

> Create index with dynamic: true to auto-index all fields

**Eval 1**: Create a text search index using dynamic mapping.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "mappings": {
       "dynamic": true
     }
   }
   ```

**Eval 2**: I want a full-text search index that automatically includes all existing and future fields.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "mappings": {
       "dynamic": true
     }
   }
   ```


### `IDX_TEXT_STATIC` — Explicit Field Definitions

> Create index with dynamic: false and explicit field mappings

**Prompt**: Create a search index for searching plot descriptions.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "mappings": {
       "dynamic": false,
       "fields": {
         "plot": {
           "type": "string"
         }
       }
     }
   }
   ```


### `IDX_TEXT_TYPESETS` — Configurable Dynamic TypeSets

> Use typeSets to control which field types get auto-indexed

**Prompt**: Create a dynamic search index but only auto-index string and number fields.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "typeSets": [
       {
         "name": "stringAndNumber",
         "types": [
           {
             "type": "string"
           },
           {
             "type": "number"
           }
         ]
       }
     ],
     "mappings": {
       "dynamic": {
         "typeSet": "stringAndNumber"
       }
     }
   }
   ```


### `IDX_TEXT_FIELD_TYPES` — Field Type Definitions

> Define specific field types: string, number, date, objectId, boolean, geo, autocomplete, token, uuid, embeddedDocuments, document

**Prompt**: Create a search index with title field as a string, year field as a number, released field as a date, genres field as a token type, title as autocomplete and netflix as boolean.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "mappings": {
       "dynamic": false,
       "fields": {
         "title": [
           {
             "type": "string"
           },
           {
             "type": "autocomplete"
           }
         ],
         "year": {
           "type": "number"
         },
         "released": {
           "type": "date"
         },
         "genres": {
           "type": "token"
         },
         "netflix": {
           "type": "boolean"
         }
       }
     }
   }
   ```


### `IDX_TEXT_ANALYZER_INDEX` — Index-Time Analyzer

> Configure analyzer applied to string fields when indexing (default: lucene.standard)

**Eval 1**: Create a search index with English stemming on the plot field.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "mappings": {
       "dynamic": false,
       "fields": {
         "plot": {
           "type": "string",
           "analyzer": "lucene.english"
         }
       }
     }
   }
   ```

**Eval 2**: Index the plot field for search using the English analyzer.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "mappings": {
       "dynamic": false,
       "fields": {
         "plot": {
           "type": "string",
           "analyzer": "lucene.english"
         }
       }
     }
   }
   ```


### `IDX_TEXT_ANALYZER_SEARCH` — Search-Time Analyzer

> Configure a different analyzer for query text than index time

**Prompt**: Index the plot field for search with the English analyzer but use the standard analyzer at search time.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "mappings": {
       "dynamic": false,
       "fields": {
         "plot": {
           "type": "string",
           "analyzer": "lucene.english",
           "searchAnalyzer": "lucene.standard"
         }
       }
     }
   }
   ```


### `IDX_TEXT_ANALYZER_BUILTIN` — Built-in Analyzers

> Use built-in analyzers: lucene.standard, lucene.simple, lucene.whitespace, lucene.keyword, language-specific

**Prompt**: Create a dynamic search index with the keyword analyzer.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "analyzer": "lucene.keyword",
     "mappings": {
       "dynamic": true
     }
   }
   ```


### `IDX_TEXT_ANALYZER_CUSTOM` — Custom Analyzer

> Define custom analyzer with tokenizer + filters pipeline

**Prompt**: Create a dynamic search index with a custom analyzer that uses a whitespace tokenizer and a lowercase filter.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "analyzers": [
       {
         "name": "myCustomAnalyzer",
         "tokenizer": {
           "type": "whitespace"
         },
         "tokenFilters": [
           {
             "type": "lowercase"
           }
         ]
       }
     ],
     "analyzer": "myCustomAnalyzer",
     "mappings": {
       "dynamic": true
     }
   }
   ```


### `IDX_TEXT_MULTI_ANALYZER` — Multi Analyzer

> Alternate analyzers on same field via multi for different query strategies

**Prompt**: Create a search index with the title field searchable with both the standard and keyword analyzers.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "mappings": {
       "dynamic": false,
       "fields": {
         "title": {
           "type": "string",
           "analyzer": "lucene.standard",
           "multi": {
             "keywordAnalyzer": {
               "type": "string",
               "analyzer": "lucene.keyword"
             }
           }
         }
       }
     }
   }
   ```


### `IDX_TEXT_TOKEN_NORMALIZER` — Token Type Normalizer

> Configure normalizers for token type: lowercase or none

**Eval 1**: Index the genres field as a token type with lowercase normalization.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "mappings": {
       "dynamic": false,
       "fields": {
         "genres": {
           "type": "token",
           "normalizer": "lowercase"
         }
       }
     }
   }
   ```

**Eval 2**: Index the rated field as a token type without normalization.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "mappings": {
       "dynamic": false,
       "fields": {
         "rated": {
           "type": "token",
           "normalizer": "none"
         }
       }
     }
   }
   ```


### `IDX_TEXT_SYNONYM_SOURCE` — Synonym Source Mappings

> Configure synonym source mappings in index for synonym-aware search

**Prompt**: Create an index with synonym support for movie genre terms like 'scary' and 'horror'.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "synonyms": [
       {
         "name": "genre_synonyms",
         "analyzer": "lucene.standard",
         "source": {
           "collection": "synonyms"
         }
       }
     ],
     "mappings": {
       "dynamic": true
     }
   }
   ```


### `IDX_TEXT_FACET_MAPPING` — Facet-Type Field Mappings

> Map fields with stringFacet / numberFacet to enable $searchMeta facet queries

**Prompt**: Create a search index that supports faceted search on genres and year.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "mappings": {
       "dynamic": false,
       "fields": {
         "genres": [
           {
             "type": "stringFacet"
           },
           {
             "type": "string"
           }
         ],
         "year": [
           {
             "type": "numberFacet"
           },
           {
             "type": "number"
           }
         ]
       }
     }
   }
   ```


### `IDX_TEXT_MULTI_FIELD` — Multi-Field Definitions

> Index multiple fields in one index definition

**Prompt**: Create an index covering the plot, fullplot, and title fields.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "mappings": {
       "dynamic": false,
       "fields": {
         "plot": {
           "type": "string"
         },
         "fullplot": {
           "type": "string"
         },
         "title": {
           "type": "string"
         }
       }
     }
   }
   ```


### `IDX_TEXT_STORED_SOURCE` — Stored Source Configuration

> Configure storedSource to store fields on mongot for returnStoredSource

**Eval 1**: Create a dynamic search index that stores the title and plot fields for faster retrieval.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "storedSource": {
       "include": [
         "title",
         "plot"
       ]
     },
     "mappings": {
       "dynamic": true
     }
   }
   ```

**Eval 2**: Create a dynamic search index that stores all fields.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "storedSource": true,
     "mappings": {
       "dynamic": true
     }
   }
   ```

**Eval 3**: Create a dynamic search index that stores everything except the fullplot field.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "storedSource": {
       "exclude": [
         "fullplot"
       ]
     },
     "mappings": {
       "dynamic": true
     }
   }
   ```


### `IDX_TEXT_NUM_PARTITIONS` — Index Partitioning

> Set numPartitions for collections exceeding 2B documents

**Prompt**: Create a dynamic search index with 4 partitions for a very large collection.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "numPartitions": 4,
     "mappings": {
       "dynamic": true
     }
   }
   ```


---

## Index Management — Vector Search Index Creation

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `IDX_VEC_SIMILARITY` | Similarity Functions | Specify similarity: euclidean, cosine, dotProduct | 3 |
| `IDX_VEC_QUANTIZATION` | Quantization | Scalar or binary quantization for reduced memory / maximum compression | 2 |
| `IDX_VEC_FILTER_FIELDS` | Filter Field Definitions | Define filter fields for pre-filtering in $vectorSearch | 1 |
| `IDX_VEC_AUTO_EMBED` | Auto-Embed Type | Automated embedding generation via Voyage AI at index/query time (Preview) | 1 |

### `IDX_VEC_SIMILARITY` — Similarity Functions

> Specify similarity: euclidean, cosine, dotProduct

**Eval 1**: Create a vector index on plot_embedding with 1024 dimensions using cosine similarity.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "fields": [
       {
         "type": "vector",
         "path": "plot_embedding",
         "numDimensions": 1024,
         "similarity": "cosine"
       }
     ]
   }
   ```

**Eval 2**: Create a vector index on plot_embedding with 1024 dimensions using Euclidean distance.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "fields": [
       {
         "type": "vector",
         "path": "plot_embedding",
         "numDimensions": 1024,
         "similarity": "euclidean"
       }
     ]
   }
   ```

**Eval 3**: Create a vector index on plot_embedding with 1024 dimensions using dot product similarity.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "fields": [
       {
         "type": "vector",
         "path": "plot_embedding",
         "numDimensions": 1024,
         "similarity": "dotProduct"
       }
     ]
   }
   ```


### `IDX_VEC_QUANTIZATION` — Quantization

> Scalar or binary quantization for reduced memory / maximum compression

**Eval 1**: Create a vector index on plot_embedding with 1024 dimensions and scalar quantization.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "fields": [
       {
         "type": "vector",
         "path": "plot_embedding",
         "numDimensions": 1024,
         "similarity": "cosine",
         "quantization": "scalar"
       }
     ]
   }
   ```

**Eval 2**: Create a vector index on plot_embedding with 1024 dimensions and binary quantization.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "fields": [
       {
         "type": "vector",
         "path": "plot_embedding",
         "numDimensions": 1024,
         "similarity": "euclidean",
         "quantization": "binary"
       }
     ]
   }
   ```


### `IDX_VEC_FILTER_FIELDS` — Filter Field Definitions

> Define filter fields for pre-filtering in $vectorSearch

**Prompt**: Create a vector index on plot_embedding with 1024 dimensions, cosine similarity, and genres and year as filter fields.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "fields": [
       {
         "type": "vector",
         "path": "plot_embedding",
         "numDimensions": 1024,
         "similarity": "cosine"
       },
       {
         "type": "filter",
         "path": "genres"
       },
       {
         "type": "filter",
         "path": "year"
       }
     ]
   }
   ```


### `IDX_VEC_AUTO_EMBED` — Auto-Embed Type

> Automated embedding generation via Voyage AI at index/query time (Preview)

**Prompt**: Create a vector index that auto-generates embeddings from the plot field.

**Expected tool calls:**

1. `create-index`
   ```json
   {
     "fields": [
       {
         "type": "autoEmbed",
         "path": "plot",
         "model": "voyage-4-large",
         "modality": "text",
         "numDimensions": 1024
       }
     ]
   }
   ```


---

## Index Management — Lifecycle

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `IDX_DELETE` | Index Deletion | Delete an existing search index | 1 |

### `IDX_DELETE` — Index Deletion

> Delete an existing search index

**Prompt**: Delete the index named 'old_index' from the movies collection.

**Expected tool calls:**

1. `drop-index`
   ```json
   {
     "indexName": "old_index"
   }
   ```


---

## Text Search ($search) — Operators

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `SEARCH_TEXT` | Basic Text Search | Keyword search via text operator. Multi-term, multi-path, array query (implicit OR) | 2 |
| `SEARCH_PHRASE` | Phrase Search | Exact phrase matching with optional slop for proximity | 2 |
| `SEARCH_FUZZY` | Fuzzy Search | Typo tolerance via fuzzy with maxEdits, prefixLength | 2 |
| `SEARCH_AUTOCOMPLETE` | Autocomplete / Typeahead | Prefix/typeahead matching | 1 |
| `SEARCH_WILDCARD` | Wildcard Search | Pattern matching with *, ? | 1 |
| `SEARCH_REGEX` | Regular Expression Search | Match via regex patterns | 1 |
| `SEARCH_EQUALS` | Exact Value Match | Exact match on boolean, date, objectId, number, token, uuid | 3 |
| `SEARCH_IN` | Match Any Value in Array | Match any from array of candidates | 2 |
| `SEARCH_RANGE` | Range Queries | Numeric/date/objectId/token ranges with gt, gte, lt, lte | 3 |
| `SEARCH_NEAR` | Proximity-Scored Search | Proximity-scored on number, date, or GeoJSON with pivot-based decay | 2 |
| `SEARCH_EXISTS` | Field Existence Check | Test for presence of indexed field | 2 |
| `SEARCH_MORE_LIKE_THIS` | Find Similar Documents | Find similar docs based on representative terms | 1 |
| `SEARCH_QUERY_STRING` | Lucene Query String | Lucene-style query syntax | 1 |
| `SEARCH_GEO_WITHIN` | Geospatial Filtering | Filter within circle, polygon, box, MultiPolygon | 1 |
| `SEARCH_GEO_SHAPE` | Spatial Relation Queries | Relations: contains, disjoint, intersects, within | 1 |
| `SEARCH_EMBEDDED_DOC` | Embedded Document Search | Query fields in arrays of embedded docs with per-doc scoring | 1 |
| `SEARCH_VECTOR_IN_SEARCH` | Vector Search within $search | vectorSearch operator inside $search for combined ANN/ENN + text pre-filters | 1 |

### `SEARCH_TEXT` — Basic Text Search

> Keyword search via text operator. Multi-term, multi-path, array query (implicit OR)

**Eval 1**: Search the plot field for movies about time travel.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "time travel",
           "path": "plot"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Find movies with 'robot' or 'AI' in the plot.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": [
             "robot",
             "AI"
           ],
           "path": "plot"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_PHRASE` — Phrase Search

> Exact phrase matching with optional slop for proximity

**Eval 1**: Find movies where 'save the world' appears within 2 words of each other in the plot.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "phrase": {
           "query": "save the world",
           "path": "plot",
           "slop": 2
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Find movies containing the exact phrase 'world war' in the plot.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "phrase": {
           "query": "world war",
           "path": "plot"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_FUZZY` — Fuzzy Search

> Typo tolerance via fuzzy with maxEdits, prefixLength

**Eval 1**: Search the plot for 'vampyres' with fuzzy matching to handle the typo.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "vampyres",
           "path": "plot",
           "fuzzy": {
             "maxEdits": 1
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Find horror movies mentioning 'vampyres' in the plot.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "compound": {
           "must": [
             {
               "text": {
                 "query": "vampyres",
                 "path": "plot",
                 "fuzzy": {
                   "maxEdits": 1
                 }
               }
             }
           ],
           "filter": [
             {
               "text": {
                 "query": "Horror",
                 "path": "genres"
               }
             }
           ]
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_AUTOCOMPLETE` — Autocomplete / Typeahead

> Prefix/typeahead matching

**Prompt**: Find movie titles starting with 'The Dark'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "autocomplete": {
           "query": "The Dark",
           "path": "title"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_WILDCARD` — Wildcard Search

> Pattern matching with *, ?

**Prompt**: Find titles matching the pattern 'Star*Wars'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "wildcard": {
           "query": "Star*Wars",
           "path": "title",
           "allowAnalyzedField": true
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_REGEX` — Regular Expression Search

> Match via regex patterns

**Prompt**: Find titles matching the regex pattern 'The.*Knight'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "regex": {
           "query": "The.*Knight",
           "path": "title",
           "allowAnalyzedField": true
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_EQUALS` — Exact Value Match

> Exact match on boolean, date, objectId, number, token, uuid

**Eval 1**: Find movies rated 'PG-13'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "equals": {
           "value": "PG-13",
           "path": "rated"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "rated": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Find movies from exactly the year 2020.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "equals": {
           "value": 2020,
           "path": "year"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "year": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```

**Eval 3**: Find documents where the type equals 'movie'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "equals": {
           "value": "movie",
           "path": "type"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "type": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_IN` — Match Any Value in Array

> Match any from array of candidates

**Eval 1**: Find movies rated either 'PG' or 'PG-13'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "in": {
           "value": [
             "PG",
             "PG-13"
           ],
           "path": "rated"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "rated": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Find movies from the years 2018, 2019, or 2020.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "in": {
           "value": [
             2018,
             2019,
             2020
           ],
           "path": "year"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "year": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_RANGE` — Range Queries

> Numeric/date/objectId/token ranges with gt, gte, lt, lte

**Eval 1**: Find movies from the 1990s with 'heist' in the plot.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "compound": {
           "must": [
             {
               "text": {
                 "query": "heist",
                 "path": "plot"
               }
             }
           ],
           "filter": [
             {
               "range": {
                 "path": "year",
                 "gte": 1990,
                 "lte": 1999
               }
             }
           ]
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "year": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Find movies with 'mystery' in the genres field from 2010 to 2020.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "compound": {
           "must": [
             {
               "text": {
                 "query": "mystery",
                 "path": "genres"
               }
             }
           ],
           "filter": [
             {
               "range": {
                 "path": "year",
                 "gte": 2010,
                 "lte": 2020
               }
             }
           ]
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "year": 1,
         "genres": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```

**Eval 3**: Find movies with 'world war' in the plot from the last 20 years.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "compound": {
           "must": [
             {
               "text": {
                 "query": "world war",
                 "path": "plot"
               }
             }
           ],
           "filter": [
             {
               "range": {
                 "path": "year",
                 "gte": 2006
               }
             }
           ]
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "year": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_NEAR` — Proximity-Scored Search

> Proximity-scored on number, date, or GeoJSON with pivot-based decay

**Eval 1**: Find movies closest to the year 2000, with relevance decaying over 5 years.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "near": {
           "path": "year",
           "origin": 2000,
           "pivot": 5
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "year": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Find movies released near January 2020.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "near": {
           "path": "released",
           "origin": {
             "$date": "2020-01-01T00:00:00Z"
           },
           "pivot": 7776000000
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "released": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_EXISTS` — Field Existence Check

> Test for presence of indexed field

**Eval 1**: Find movies where the fullplot field exists.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "exists": {
           "path": "fullplot"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Find movies that have an IMDB rating.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "exists": {
           "path": "imdb.rating"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "imdb": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_MORE_LIKE_THIS` — Find Similar Documents

> Find similar docs based on representative terms

**Prompt**: Find movies similar to The Matrix by matching on the title and plot fields.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "moreLikeThis": {
           "like": [
             {
               "title": "The Matrix",
               "plot": "A computer hacker learns about the true nature of reality and his role in the war against its controllers."
             }
           ]
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_QUERY_STRING` — Lucene Query String

> Lucene-style query syntax

**Prompt**: Find movies where title contains Batman and year is greater than 2000.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "queryString": {
           "defaultPath": "plot",
           "query": "title:Batman AND year:>2000"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "year": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_GEO_WITHIN` — Geospatial Filtering

> Filter within circle, polygon, box, MultiPolygon

**Prompt**: Find movies with 'New York' in the plot near the coordinates [40.7128, -74.0060] in the location field.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "compound": {
           "must": [
             {
               "text": {
                 "query": "New York",
                 "path": "plot"
               }
             }
           ],
           "filter": [
             {
               "geoWithin": {
                 "path": "location",
                 "circle": {
                   "center": {
                     "type": "Point",
                     "coordinates": [
                       -74.006,
                       40.7128
                     ]
                   },
                   "radius": 10000
                 }
               }
             }
           ]
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_GEO_SHAPE` — Spatial Relation Queries

> Relations: contains, disjoint, intersects, within

**Prompt**: Find locations that intersect with this polygon.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "geoShape": {
           "path": "location",
           "relation": "intersects",
           "geometry": {
             "type": "Polygon",
             "coordinates": [
               [
                 [
                   -73.98,
                   40.77
                 ],
                 [
                   -73.97,
                   40.76
                 ],
                 [
                   -73.99,
                   40.75
                 ],
                 [
                   -73.98,
                   40.77
                 ]
               ]
             ]
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "location": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_EMBEDDED_DOC` — Embedded Document Search

> Query fields in arrays of embedded docs with per-doc scoring

**Prompt**: Find movies where cast member 'Tom Hanks' is playing 'Forrest'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "embeddedDocument": {
           "path": "cast",
           "operator": {
             "compound": {
               "must": [
                 {
                   "text": {
                     "query": "Tom Hanks",
                     "path": "cast.name"
                   }
                 },
                 {
                   "text": {
                     "query": "Forrest",
                     "path": "cast.character"
                   }
                 }
               ]
             }
           },
           "score": {
             "embedded": {
               "aggregate": "maximum"
             }
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "cast": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SEARCH_VECTOR_IN_SEARCH` — Vector Search within $search

> vectorSearch operator inside $search for combined ANN/ENN + text pre-filters

**Prompt**: Find movies semantically similar to 'space exploration' using the plot_embedding field, where the title contains 'Star'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "compound": {
           "must": [
             {
               "vectorSearch": {
                 "path": "plot_embedding",
                 "queryVector": [
                   0.1,
                   -0.2,
                   0.3
                 ],
                 "numCandidates": 150
               }
             }
           ],
           "filter": [
             {
               "wildcard": {
                 "query": "Star*",
                 "path": "title",
                 "allowAnalyzedField": true
               }
             }
           ]
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


---

## Text Search ($search) — Compound Queries

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `COMPOUND_MUST` | Required Clauses | must — clauses that must match (affects score + filtering) | 1 |
| `COMPOUND_SHOULD` | Optional / Boosting Clauses | should — optional clauses that boost score, with minimumShouldMatch | 1 |
| `COMPOUND_FILTER` | Filter-Only Clauses | filter — required clauses, no score impact | 1 |
| `COMPOUND_MUST_NOT` | Exclusion Clauses | mustNot — exclude matching documents | 1 |

### `COMPOUND_MUST` — Required Clauses

> must — clauses that must match (affects score + filtering)

**Prompt**: Find movies with 'Comedy' in genres and 'robots' in the plot.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "compound": {
           "must": [
             {
               "text": {
                 "query": "robots",
                 "path": "plot"
               }
             },
             {
               "text": {
                 "query": "Comedy",
                 "path": "genres"
               }
             }
           ]
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "genres": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `COMPOUND_SHOULD` — Optional / Boosting Clauses

> should — optional clauses that boost score, with minimumShouldMatch

**Prompt**: Find movies with 'batman' in the title and 'batman' in the plot.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "compound": {
           "should": [
             {
               "text": {
                 "query": "batman",
                 "path": "title"
               }
             },
             {
               "text": {
                 "query": "batman",
                 "path": "plot"
               }
             }
           ],
           "minimumShouldMatch": 1
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `COMPOUND_FILTER` — Filter-Only Clauses

> filter — required clauses, no score impact

**Prompt**: Find movies with 'climate change' in the plot, filtered to 'Documentary' in genres, sorted by most recent.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "compound": {
           "must": [
             {
               "text": {
                 "query": "climate change",
                 "path": "plot"
               }
             }
           ],
           "filter": [
             {
               "text": {
                 "query": "Documentary",
                 "path": "genres"
               }
             }
           ]
         }
       }
     },
     {
       "$sort": {
         "released": -1
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "genres": 1,
         "released": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `COMPOUND_MUST_NOT` — Exclusion Clauses

> mustNot — exclude matching documents

**Prompt**: Find movies with 'action' in genres but exclude those with 'superhero' in the plot.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "compound": {
           "must": [
             {
               "text": {
                 "query": "action",
                 "path": "genres"
               }
             }
           ],
           "mustNot": [
             {
               "text": {
                 "query": "superhero",
                 "path": "plot"
               }
             }
           ]
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "genres": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


---

## Text Search ($search) — Scoring & Relevance

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `SCORE_BOOST_VALUE` | Static Score Boost | Boost field's score with static value | 2 |
| `SCORE_BOOST_PATH` | Dynamic Score Boost from Field | Boost dynamically using numeric field value | 1 |
| `SCORE_CONSTANT` | Constant Score | Replace score with fixed number | 1 |
| `SCORE_FUNCTION` | Computed Score Expression | Replace score with computed expression (arithmetic, log, path-based) | 1 |
| `SCORE_EMBEDDED` | Embedded Document Scoring | Scoring for embeddedDocument operator — aggregate across matches | 1 |
| `SCORE_DETAILS` | Score Breakdown | Enable scoreDetails for $meta: "searchScoreDetails" | 1 |

### `SCORE_BOOST_VALUE` — Static Score Boost

> Boost field's score with static value

**Eval 1**: Search for 'action' in the title and plot fields, with more weight on the title.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "compound": {
           "should": [
             {
               "text": {
                 "query": "action",
                 "path": "title",
                 "score": {
                   "boost": {
                     "value": 3
                   }
                 }
               }
             },
             {
               "text": {
                 "query": "action",
                 "path": "plot"
               }
             }
           ]
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Boost the title field score by 3x.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "compound": {
           "should": [
             {
               "text": {
                 "query": "action",
                 "path": "title",
                 "score": {
                   "boost": {
                     "value": 3
                   }
                 }
               }
             },
             {
               "text": {
                 "query": "action",
                 "path": "plot"
               }
             }
           ]
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SCORE_BOOST_PATH` — Dynamic Score Boost from Field

> Boost dynamically using numeric field value

**Prompt**: Search the plot for 'thriller' with results boosted by the imdb.rating field.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "thriller",
           "path": "plot",
           "score": {
             "boost": {
               "path": "imdb.rating",
               "undefined": 1
             }
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "imdb": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SCORE_CONSTANT` — Constant Score

> Replace score with fixed number

**Prompt**: Apply a genre filter with a constant score of 1.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "compound": {
           "filter": [
             {
               "text": {
                 "query": "Action",
                 "path": "genres",
                 "score": {
                   "constant": {
                     "value": 1
                   }
                 }
               }
             }
           ]
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "genres": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SCORE_FUNCTION` — Computed Score Expression

> Replace score with computed expression (arithmetic, log, path-based)

**Prompt**: Score results using the log of IMDB votes.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "thriller",
           "path": "plot",
           "score": {
             "function": {
               "log1p": {
                 "path": {
                   "value": "imdb.votes",
                   "undefined": 1
                 }
               }
             }
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "imdb": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SCORE_EMBEDDED` — Embedded Document Scoring

> Scoring for embeddedDocument operator — aggregate across matches

**Prompt**: Search embedded cast documents and use the maximum score.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "embeddedDocument": {
           "path": "cast",
           "operator": {
             "text": {
               "query": "Tom Hanks",
               "path": "cast.name"
             }
           },
           "score": {
             "embedded": {
               "aggregate": "maximum"
             }
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SCORE_DETAILS` — Score Breakdown

> Enable scoreDetails for $meta: "searchScoreDetails"

**Prompt**: Search the plot for 'romance' with a detailed score explanation.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "romance",
           "path": "plot"
         },
         "scoreDetails": true
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         },
         "scoreDetails": {
           "$meta": "searchScoreDetails"
         }
       }
     }
   ]
   ```


---

## Text Search ($search) — Highlighting & Synonyms

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `HIGHLIGHT` | Search Highlighting | Return highlighted matching text via highlight + $meta: "searchHighlights" | 1 |
| `SYNONYMS` | Synonym-Aware Search | Expand query terms via synonym mapping in index | 1 |

### `HIGHLIGHT` — Search Highlighting

> Return highlighted matching text via highlight + $meta: "searchHighlights"

**Prompt**: Search for 'space exploration' and highlight the matching text.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "space exploration",
           "path": "plot"
         },
         "highlight": {
           "path": "plot"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "searchScore"
         },
         "highlights": {
           "$meta": "searchHighlights"
         }
       }
     }
   ]
   ```


### `SYNONYMS` — Synonym-Aware Search

> Expand query terms via synonym mapping in index

**Prompt**: Search for 'scary' and also match 'horror' and 'frightening' as synonyms.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "scary",
           "path": "plot",
           "synonyms": "genre_synonyms"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


---

## Text Search ($search) — Faceted Search

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `FACET_STRING` | String Facets | Category counts via $searchMeta | 1 |
| `FACET_NUMBER` | Number Facets | Bucketed counts with boundaries | 2 |
| `FACET_DATE` | Date Facets | Time-based bucketed counts | 2 |

### `FACET_STRING` — String Facets

> Category counts via $searchMeta

**Prompt**: Count movies by genre that mention 'detective'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$searchMeta": {
         "facet": {
           "operator": {
             "text": {
               "query": "detective",
               "path": "plot"
             }
           },
           "facets": {
             "genreFacet": {
               "type": "string",
               "path": "genres"
             }
           }
         }
       }
     }
   ]
   ```


### `FACET_NUMBER` — Number Facets

> Bucketed counts with boundaries

**Eval 1**: Show a decade breakdown for movies about 'thriller'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$searchMeta": {
         "facet": {
           "operator": {
             "text": {
               "query": "thriller",
               "path": "plot"
             }
           },
           "facets": {
             "yearFacet": {
               "type": "number",
               "path": "year",
               "boundaries": [
                 1950,
                 1960,
                 1970,
                 1980,
                 1990,
                 2000,
                 2010,
                 2020,
                 2030
               ]
             }
           }
         }
       }
     }
   ]
   ```

**Eval 2**: Search for 'thriller' faceted by genre and year.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$searchMeta": {
         "facet": {
           "operator": {
             "text": {
               "query": "thriller",
               "path": "plot"
             }
           },
           "facets": {
             "genreFacet": {
               "type": "string",
               "path": "genres"
             },
             "yearFacet": {
               "type": "number",
               "path": "year",
               "boundaries": [
                 1980,
                 1990,
                 2000,
                 2010,
                 2020,
                 2030
               ]
             }
           }
         }
       }
     }
   ]
   ```


### `FACET_DATE` — Date Facets

> Time-based bucketed counts

**Eval 1**: Show the quarterly distribution of 'thriller' movies in 2020.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$searchMeta": {
         "facet": {
           "operator": {
             "text": {
               "query": "thriller",
               "path": "plot"
             }
           },
           "facets": {
             "releaseFacet": {
               "type": "date",
               "path": "released",
               "boundaries": [
                 {
                   "$date": "2020-01-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-04-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-07-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-10-01T00:00:00Z"
                 },
                 {
                   "$date": "2021-01-01T00:00:00Z"
                 }
               ]
             }
           }
         }
       }
     }
   ]
   ```

**Eval 2**: Show the monthly distribution of 'pandemic' movies in 2020.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$searchMeta": {
         "facet": {
           "operator": {
             "text": {
               "query": "pandemic",
               "path": "plot"
             }
           },
           "facets": {
             "releaseFacet": {
               "type": "date",
               "path": "released",
               "boundaries": [
                 {
                   "$date": "2020-01-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-02-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-03-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-04-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-05-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-06-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-07-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-08-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-09-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-10-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-11-01T00:00:00Z"
                 },
                 {
                   "$date": "2020-12-01T00:00:00Z"
                 },
                 {
                   "$date": "2021-01-01T00:00:00Z"
                 }
               ]
             }
           }
         }
       }
     }
   ]
   ```


---

## Text Search ($search) — Count Analytics

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `COUNT_TOTAL` | Exact Total Count | Exact count via $count stage or $searchMeta | 1 |
| `COUNT_LOWER_BOUND` | Fast Approximate Count | Fast approximate count with type: "lowerBound" | 1 |
| `COUNT_THRESHOLD` | Count Threshold | Configure count.threshold for lowerBound accuracy (default: 1000) | 1 |
| `COUNT_INLINE` | Inline Count via $$SEARCH_META | count option in $search + $$SEARCH_META variable | 1 |

### `COUNT_TOTAL` — Exact Total Count

> Exact count via $count stage or $searchMeta

**Prompt**: How many movies are about outer space?

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$searchMeta": {
         "facet": {
           "operator": {
             "text": {
               "query": "outer space",
               "path": "plot"
             }
           },
           "facets": {}
         },
         "count": {
           "type": "total"
         }
       }
     }
   ]
   ```


### `COUNT_LOWER_BOUND` — Fast Approximate Count

> Fast approximate count with type: "lowerBound"

**Prompt**: Give me a quick estimate of how many movies mention 'love'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$searchMeta": {
         "facet": {
           "operator": {
             "text": {
               "query": "love",
               "path": "plot"
             }
           },
           "facets": {}
         },
         "count": {
           "type": "lowerBound"
         }
       }
     }
   ]
   ```


### `COUNT_THRESHOLD` — Count Threshold

> Configure count.threshold for lowerBound accuracy (default: 1000)

**Prompt**: Count 'war' movies with a threshold of 5000.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$searchMeta": {
         "facet": {
           "operator": {
             "text": {
               "query": "war",
               "path": "plot"
             }
           },
           "facets": {}
         },
         "count": {
           "type": "lowerBound",
           "threshold": 5000
         }
       }
     }
   ]
   ```


### `COUNT_INLINE` — Inline Count via $$SEARCH_META

> count option in $search + $$SEARCH_META variable

**Prompt**: Search for 'comedy' and include the total count alongside the results.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "comedy",
           "path": "genres"
         },
         "count": {
           "type": "total"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         },
         "totalCount": "$$SEARCH_META.count"
       }
     }
   ]
   ```


---

## Text Search ($search) — Pagination

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `PAGE_OFFSET` | Offset-Based Pagination | Traditional $skip + $limit | 1 |
| `PAGE_CURSOR` | Token-Based Cursor Pagination | searchAfter / searchBefore with $meta: "searchSequenceToken" | 1 |

### `PAGE_OFFSET` — Offset-Based Pagination

> Traditional $skip + $limit

**Prompt**: Show page 2 of 'comedy' results with 10 per page.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "comedy",
           "path": "genres"
         }
       }
     },
     {
       "$skip": 10
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `PAGE_CURSOR` — Token-Based Cursor Pagination

> searchAfter / searchBefore with $meta: "searchSequenceToken"

**Prompt**: Show the next page after this token for 'comedy' results.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "comedy",
           "path": "genres"
         },
         "sort": {
           "released": -1,
           "_id": 1
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "paginationToken": {
           "$meta": "searchSequenceToken"
         }
       }
     }
   ]
   ```
2. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "comedy",
           "path": "genres"
         },
         "searchAfter": "<token-from-last-document>",
         "sort": {
           "released": -1,
           "_id": 1
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "paginationToken": {
           "$meta": "searchSequenceToken"
         }
       }
     }
   ]
   ```


---

## Text Search ($search) — Sorting

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `SORT_NATIVE` | Native Sort within $search | Sort within search engine via sort option. Supports boolean, date, number, objectId, uuid, token, score | 1 |
| `SORT_POST_SEARCH` | Post-Search Sort | Re-sort results by external fields via $sort after $search | 2 |

### `SORT_NATIVE` — Native Sort within $search

> Sort within search engine via sort option. Supports boolean, date, number, objectId, uuid, token, score

**Prompt**: Search for 'drama' sorted by year descending using native sort.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "drama",
           "path": "genres"
         },
         "sort": {
           "year": -1
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "year": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `SORT_POST_SEARCH` — Post-Search Sort

> Re-sort results by external fields via $sort after $search

**Eval 1**: Find the top 5 highest-rated movies about AI.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "AI",
           "path": "plot"
         }
       }
     },
     {
       "$limit": 100
     },
     {
       "$sort": {
         "imdb.rating": -1
       }
     },
     {
       "$limit": 5
     },
     {
       "$project": {
         "title": 1,
         "imdb": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Search for 'pandemic' movies sorted by viewer rating.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "pandemic",
           "path": "plot"
         }
       }
     },
     {
       "$limit": 100
     },
     {
       "$sort": {
         "imdb.rating": -1
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "imdb": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


---

## Text Search ($search) — $search Stage Options

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `OPT_CONCURRENT` | Concurrent Search | Parallelize search across segments on dedicated search nodes | 1 |
| `OPT_RETURN_STORED_SOURCE` | Return Stored Fields | Return stored fields from mongot instead of full doc lookup | 1 |
| `OPT_RETURN_SCOPE` | Return Scope for Embedded Docs | Set query context to embedded doc fields (requires returnStoredSource: true) | 1 |

### `OPT_CONCURRENT` — Concurrent Search

> Parallelize search across segments on dedicated search nodes

**Prompt**: Search for 'action' with concurrent execution enabled.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "action",
           "path": "genres"
         },
         "concurrent": true
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `OPT_RETURN_STORED_SOURCE` — Return Stored Fields

> Return stored fields from mongot instead of full doc lookup

**Prompt**: Search for 'thriller' using stored source for a faster response.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "thriller",
           "path": "genres"
         },
         "returnStoredSource": true
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `OPT_RETURN_SCOPE` — Return Scope for Embedded Docs

> Set query context to embedded doc fields (requires returnStoredSource: true)

**Prompt**: Search the embedded cast and return only the matching embedded documents.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "embeddedDocument": {
           "path": "cast",
           "operator": {
             "text": {
               "query": "Tom Hanks",
               "path": "cast.name"
             }
           }
         },
         "returnStoredSource": true,
         "returnScope": {
           "path": "cast"
         }
       }
     },
     {
       "$limit": 10
     }
   ]
   ```


---

## Text Search ($search) — Post-Search Aggregation

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `AGG_FACET` | Parallel Sub-Pipelines | $facet — multiple sub-pipelines over search results (stats + top-N) | 1 |
| `AGG_GROUP` | Aggregate Search Results | $group — aggregate with $avg, $sum, $push, $min/$max | 1 |
| `AGG_UNWIND` | Flatten Arrays | $unwind — flatten array fields for per-element grouping | 1 |
| `AGG_BUCKET` | Bucket into Ranges | $bucket / $bucketAuto — bin results into ranges | 2 |
| `AGG_SORT_BY_COUNT` | Shorthand Frequency Count | $sortByCount — shorthand for $unwind → $group → $sort | 1 |
| `AGG_LOOKUP` | Join with Other Collections | $lookup — join search results with other collections | 1 |
| `AGG_REPLACE_ROOT` | Promote Embedded Document | $replaceRoot / $replaceWith — promote embedded doc to top level | 1 |
| `AGG_OUT_MERGE` | Materialize Results | $out / $merge — write results to collection for caching | 2 |
| `AGG_SAMPLE` | Random Sample | $sample — random sample from search results | 1 |

### `AGG_FACET` — Parallel Sub-Pipelines

> $facet — multiple sub-pipelines over search results (stats + top-N)

**Prompt**: Search for 'superhero' and return the average rating, count, and top 3 genres.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "superhero",
           "path": "plot"
         }
       }
     },
     {
       "$facet": {
         "stats": [
           {
             "$group": {
               "_id": null,
               "avgRating": {
                 "$avg": "$imdb.rating"
               },
               "count": {
                 "$sum": 1
               }
             }
           }
         ],
         "topGenres": [
           {
             "$unwind": "$genres"
           },
           {
             "$group": {
               "_id": "$genres",
               "count": {
                 "$sum": 1
               }
             }
           },
           {
             "$sort": {
               "count": -1
             }
           },
           {
             "$limit": 3
           }
         ]
       }
     }
   ]
   ```


### `AGG_GROUP` — Aggregate Search Results

> $group — aggregate with $avg, $sum, $push, $min/$max

**Prompt**: Search for 'romance' and calculate the average IMDB rating per genre.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "romance",
           "path": "plot"
         }
       }
     },
     {
       "$limit": 100
     },
     {
       "$unwind": "$genres"
     },
     {
       "$group": {
         "_id": "$genres",
         "avgRating": {
           "$avg": "$imdb.rating"
         }
       }
     },
     {
       "$sort": {
         "avgRating": -1
       }
     }
   ]
   ```


### `AGG_UNWIND` — Flatten Arrays

> $unwind — flatten array fields for per-element grouping

**Prompt**: Search for 'comedy' and count the results per genre.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "comedy",
           "path": "plot"
         }
       }
     },
     {
       "$limit": 100
     },
     {
       "$unwind": "$genres"
     },
     {
       "$group": {
         "_id": "$genres",
         "count": {
           "$sum": 1
         }
       }
     },
     {
       "$sort": {
         "count": -1
       }
     }
   ]
   ```


### `AGG_BUCKET` — Bucket into Ranges

> $bucket / $bucketAuto — bin results into ranges

**Eval 1**: Search for 'drama' and bucket the results by IMDB rating.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "drama",
           "path": "genres"
         }
       }
     },
     {
       "$limit": 100
     },
     {
       "$bucket": {
         "groupBy": "$imdb.rating",
         "boundaries": [
           0,
           3,
           5,
           7,
           9,
           10
         ],
         "default": "Other"
       }
     }
   ]
   ```

**Eval 2**: Search for 'action' and auto-bucket the results by year.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "action",
           "path": "genres"
         }
       }
     },
     {
       "$limit": 100
     },
     {
       "$bucketAuto": {
         "groupBy": "$year",
         "buckets": 5
       }
     }
   ]
   ```


### `AGG_SORT_BY_COUNT` — Shorthand Frequency Count

> $sortByCount — shorthand for $unwind → $group → $sort

**Prompt**: Search for 'thriller' and show the most common genres.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "thriller",
           "path": "genres"
         }
       }
     },
     {
       "$limit": 100
     },
     {
       "$unwind": "$genres"
     },
     {
       "$sortByCount": "$genres"
     }
   ]
   ```


### `AGG_LOOKUP` — Join with Other Collections

> $lookup — join search results with other collections

**Prompt**: Find 'space' movies and include their comments from the comments collection.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "space",
           "path": "plot"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$lookup": {
         "from": "comments",
         "localField": "_id",
         "foreignField": "movie_id",
         "as": "comments"
       }
     },
     {
       "$project": {
         "title": 1,
         "comments": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `AGG_REPLACE_ROOT` — Promote Embedded Document

> $replaceRoot / $replaceWith — promote embedded doc to top level

**Prompt**: Return only the IMDB subdocument for each search result.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "drama",
           "path": "genres"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$replaceRoot": {
         "newRoot": "$imdb"
       }
     }
   ]
   ```


### `AGG_OUT_MERGE` — Materialize Results

> $out / $merge — write results to collection for caching

**Eval 1**: Save the 'horror' search results to a collection called 'horror_cache'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "horror",
           "path": "genres"
         }
       }
     },
     {
       "$limit": 100
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "year": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     },
     {
       "$out": "horror_cache"
     }
   ]
   ```

**Eval 2**: Merge the search results into the recommendations collection.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "drama",
           "path": "genres"
         }
       }
     },
     {
       "$limit": 100
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     },
     {
       "$merge": {
         "into": "recommendations",
         "whenMatched": "replace"
       }
     }
   ]
   ```


### `AGG_SAMPLE` — Random Sample

> $sample — random sample from search results

**Prompt**: Search for 'adventure' and give me 5 random picks.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "text": {
           "query": "adventure",
           "path": "genres"
         }
       }
     },
     {
       "$limit": 100
     },
     {
       "$sample": {
         "size": 5
       }
     }
   ]
   ```


---

## Vector Search ($vectorSearch)

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `VSEARCH_ANN` | Approximate Nearest Neighbor | ANN with numCandidates for recall/performance trade-off | 2 |
| `VSEARCH_ENN` | Exact Nearest Neighbor | ENN with exact: true (no numCandidates) | 1 |
| `VSEARCH_PRE_FILTER_EQ` | Pre-Filter Equality | Pre-filter on filter fields using $eq / short-form | 1 |
| `VSEARCH_PRE_FILTER_RANGE` | Pre-Filter Range | Pre-filter with $gt, $gte, $lt, $lte | 1 |
| `VSEARCH_PRE_FILTER_IN` | Pre-Filter Set Membership | Pre-filter with $in / $nin | 2 |
| `VSEARCH_PRE_FILTER_EXISTS` | Pre-Filter Field Existence | Pre-filter with $exists | 1 |
| `VSEARCH_PRE_FILTER_COMPOUND` | Compound Pre-Filters | Combine with $and, $or, $not, $nor | 2 |
| `VSEARCH_POST_FILTER` | Post-Filter via $match | Post-filter on fields NOT in vector index | 1 |
| `VSEARCH_SCORE` | Score Projection | Project similarity score via $meta: "vectorSearchScore" | 1 |
| `VSEARCH_SORT_EXTERNAL` | Sort by External Field | Sort by external field (inflated limit → $sort → $limit) | 1 |
| `VSEARCH_EXPLAIN` | Explain / Performance | Analyze query performance with .explain("executionStats") | 1 |
| `VSEARCH_EXPLAIN_TRACE` | Trace Document IDs | Trace specific doc IDs through pipeline via explainOptions.traceDocumentIds | 1 |

### `VSEARCH_ANN` — Approximate Nearest Neighbor

> ANN with numCandidates for recall/performance trade-off

**Eval 1**: Find plots that are semantically similar to this embedding.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$vectorSearch": {
         "index": "vector_index",
         "path": "plot_embedding",
         "queryVector": [
           "<1024-dim vector>"
         ],
         "numCandidates": 150,
         "limit": 10
       }
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "vectorSearchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Find movies similar to 'young heroes in epic struggles'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$vectorSearch": {
         "index": "vector_index",
         "path": "plot_embedding",
         "queryVector": "young heroes in epic struggles",
         "embeddingParameters": {
           "model": "voyage-3-large",
           "outputDimension": 1024
         },
         "numCandidates": 150,
         "limit": 10
       }
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "vectorSearchScore"
         }
       }
     }
   ]
   ```


### `VSEARCH_ENN` — Exact Nearest Neighbor

> ENN with exact: true (no numCandidates)

**Prompt**: Run an exact vector search for 'detective in a small town'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$vectorSearch": {
         "index": "vector_index",
         "path": "plot_embedding",
         "queryVector": "detective in a small town",
         "embeddingParameters": {
           "model": "voyage-3-large",
           "outputDimension": 1024
         },
         "exact": true,
         "limit": 10
       }
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "vectorSearchScore"
         }
       }
     }
   ]
   ```


### `VSEARCH_PRE_FILTER_EQ` — Pre-Filter Equality

> Pre-filter on filter fields using $eq / short-form

**Prompt**: Find sci-fi movies similar to 'space exploration'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$vectorSearch": {
         "index": "vector_index",
         "path": "plot_embedding",
         "queryVector": "space exploration",
         "embeddingParameters": {
           "model": "voyage-3-large",
           "outputDimension": 1024
         },
         "numCandidates": 150,
         "limit": 10,
         "filter": {
           "genres": "Sci-Fi"
         }
       }
     },
     {
       "$project": {
         "title": 1,
         "genres": 1,
         "score": {
           "$meta": "vectorSearchScore"
         }
       }
     }
   ]
   ```


### `VSEARCH_PRE_FILTER_RANGE` — Pre-Filter Range

> Pre-filter with $gt, $gte, $lt, $lte

**Prompt**: Find movies from 2000 to 2020 similar to 'romantic comedy in New York'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$vectorSearch": {
         "index": "vector_index",
         "path": "plot_embedding",
         "queryVector": "romantic comedy in New York",
         "embeddingParameters": {
           "model": "voyage-3-large",
           "outputDimension": 1024
         },
         "numCandidates": 150,
         "limit": 10,
         "filter": {
           "year": {
             "$gte": 2000,
             "$lte": 2020
           }
         }
       }
     },
     {
       "$project": {
         "title": 1,
         "year": 1,
         "score": {
           "$meta": "vectorSearchScore"
         }
       }
     }
   ]
   ```


### `VSEARCH_PRE_FILTER_IN` — Pre-Filter Set Membership

> Pre-filter with $in / $nin

**Eval 1**: Find Action or Adventure movies similar to 'car chases'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$vectorSearch": {
         "index": "vector_index",
         "path": "plot_embedding",
         "queryVector": "car chases",
         "embeddingParameters": {
           "model": "voyage-3-large",
           "outputDimension": 1024
         },
         "numCandidates": 150,
         "limit": 10,
         "filter": {
           "genres": {
             "$in": [
               "Action",
               "Adventure"
             ]
           }
         }
       }
     },
     {
       "$project": {
         "title": 1,
         "genres": 1,
         "score": {
           "$meta": "vectorSearchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Find movies similar to 'comedy' but not in the Romance genre.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$vectorSearch": {
         "index": "vector_index",
         "path": "plot_embedding",
         "queryVector": "comedy",
         "embeddingParameters": {
           "model": "voyage-3-large",
           "outputDimension": 1024
         },
         "numCandidates": 150,
         "limit": 10,
         "filter": {
           "genres": {
             "$nin": [
               "Romance"
             ]
           }
         }
       }
     },
     {
       "$project": {
         "title": 1,
         "genres": 1,
         "score": {
           "$meta": "vectorSearchScore"
         }
       }
     }
   ]
   ```


### `VSEARCH_PRE_FILTER_EXISTS` — Pre-Filter Field Existence

> Pre-filter with $exists

**Prompt**: Find movies similar to 'epic saga' that have a year field.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$vectorSearch": {
         "index": "vector_index",
         "path": "plot_embedding",
         "queryVector": "epic saga",
         "embeddingParameters": {
           "model": "voyage-3-large",
           "outputDimension": 1024
         },
         "numCandidates": 150,
         "limit": 10,
         "filter": {
           "year": {
             "$exists": true
           }
         }
       }
     },
     {
       "$project": {
         "title": 1,
         "year": 1,
         "score": {
           "$meta": "vectorSearchScore"
         }
       }
     }
   ]
   ```


### `VSEARCH_PRE_FILTER_COMPOUND` — Compound Pre-Filters

> Combine with $and, $or, $not, $nor

**Eval 1**: Find drama movies after 2010 similar to 'family struggles'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$vectorSearch": {
         "index": "vector_index",
         "path": "plot_embedding",
         "queryVector": "family struggles",
         "embeddingParameters": {
           "model": "voyage-3-large",
           "outputDimension": 1024
         },
         "numCandidates": 150,
         "limit": 10,
         "filter": {
           "$and": [
             {
               "genres": "Drama"
             },
             {
               "year": {
                 "$gt": 2010
               }
             }
           ]
         }
       }
     },
     {
       "$project": {
         "title": 1,
         "genres": 1,
         "year": 1,
         "score": {
           "$meta": "vectorSearchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Find Action or Thriller movies similar to 'heist'.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$vectorSearch": {
         "index": "vector_index",
         "path": "plot_embedding",
         "queryVector": "heist",
         "embeddingParameters": {
           "model": "voyage-3-large",
           "outputDimension": 1024
         },
         "numCandidates": 150,
         "limit": 10,
         "filter": {
           "$or": [
             {
               "genres": "Action"
             },
             {
               "genres": "Thriller"
             }
           ]
         }
       }
     },
     {
       "$project": {
         "title": 1,
         "genres": 1,
         "score": {
           "$meta": "vectorSearchScore"
         }
       }
     }
   ]
   ```


### `VSEARCH_POST_FILTER` — Post-Filter via $match

> Post-filter on fields NOT in vector index

**Prompt**: Find movies similar to 'epic battles' with an IMDB rating above 7.5.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$vectorSearch": {
         "index": "vector_index",
         "path": "plot_embedding",
         "queryVector": "epic battles",
         "embeddingParameters": {
           "model": "voyage-3-large",
           "outputDimension": 1024
         },
         "numCandidates": 500,
         "limit": 50
       }
     },
     {
       "$match": {
         "imdb.rating": {
           "$gt": 7.5
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "imdb": 1,
         "score": {
           "$meta": "vectorSearchScore"
         }
       }
     }
   ]
   ```


### `VSEARCH_SCORE` — Score Projection

> Project similarity score via $meta: "vectorSearchScore"

**Prompt**: Search for 'underwater exploration' and include the similarity scores.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$vectorSearch": {
         "index": "vector_index",
         "path": "plot_embedding",
         "queryVector": "underwater exploration",
         "embeddingParameters": {
           "model": "voyage-3-large",
           "outputDimension": 1024
         },
         "numCandidates": 150,
         "limit": 10
       }
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "vectorSearchScore"
         }
       }
     }
   ]
   ```


### `VSEARCH_SORT_EXTERNAL` — Sort by External Field

> Sort by external field (inflated limit → $sort → $limit)

**Prompt**: Find movies similar to 'coming of age' sorted by IMDB rating.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$vectorSearch": {
         "index": "vector_index",
         "path": "plot_embedding",
         "queryVector": "coming of age",
         "embeddingParameters": {
           "model": "voyage-3-large",
           "outputDimension": 1024
         },
         "numCandidates": 500,
         "limit": 50
       }
     },
     {
       "$sort": {
         "imdb.rating": -1
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "imdb": 1,
         "score": {
           "$meta": "vectorSearchScore"
         }
       }
     }
   ]
   ```


### `VSEARCH_EXPLAIN` — Explain / Performance

> Analyze query performance with .explain("executionStats")

**Prompt**: Analyze the vector search performance for 'space odyssey'.

**Expected tool calls:**

1. `explain`
   ```json
   {
     "pipeline": [
       {
         "$vectorSearch": {
           "index": "vector_index",
           "path": "plot_embedding",
           "queryVector": "space odyssey",
           "embeddingParameters": {
             "model": "voyage-3-large",
             "outputDimension": 1024
           },
           "numCandidates": 150,
           "limit": 10
         }
       }
     ],
     "verbosity": "executionStats"
   }
   ```


### `VSEARCH_EXPLAIN_TRACE` — Trace Document IDs

> Trace specific doc IDs through pipeline via explainOptions.traceDocumentIds

**Prompt**: Trace these document IDs through the vector search pipeline.

**Expected tool calls:**

1. `explain`
   ```json
   {
     "pipeline": [
       {
         "$vectorSearch": {
           "index": "vector_index",
           "path": "plot_embedding",
           "queryVector": "space odyssey",
           "embeddingParameters": {
             "model": "voyage-3-large",
             "outputDimension": 1024
           },
           "numCandidates": 150,
           "limit": 10,
           "explainOptions": {
             "traceDocumentIds": [
               "507f191e810c19729de860ea",
               "507f191e810c19729de860eb"
             ]
           }
         }
       }
     ],
     "verbosity": "executionStats"
   }
   ```


---

## Hybrid Search ($rankFusion / $scoreFusion)

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `HYBRID_RRF_BASIC` | Basic Reciprocal Rank Fusion | Combine vector + text via $rankFusion | 1 |
| `HYBRID_RRF_WEIGHTED` | RRF with Weighted Pipelines | Weight individual pipelines in $rankFusion | 2 |
| `HYBRID_RRF_SCORE_DETAILS` | RRF with Score Details | Enable scoreDetails in $rankFusion | 1 |
| `HYBRID_SCOREFUSION_SIGMOID` | Score Fusion — Sigmoid | Score-based fusion with sigmoid normalization | 1 |
| `HYBRID_SCOREFUSION_MINMAX` | Score Fusion — MinMax + Expression | Score fusion with minMaxScaler + custom combination expression | 1 |
| `HYBRID_SCOREFUSION_AVG` | Score Fusion — Average | Score fusion with default avg combination | 1 |
| `HYBRID_SCOREFUSION_NONE` | Score Fusion — No Normalization | Score fusion with none — raw scores | 1 |
| `HYBRID_MULTI_FIELD` | Hybrid — Multiple Text Pipelines | Rank fusion combining multiple lexical pipelines on different fields | 1 |
| `HYBRID_PRE_FILTER` | Hybrid — Pre-Filter via Lexical Prefilter Pattern | Use vectorSearch operator inside $search to apply an Atlas Search filter before vector scoring | 1 |
| `HYBRID_POST_FILTER` | Hybrid — Post-Filter with $match | Apply a $match stage after $rankFusion/$scoreFusion to further filter results | 1 |
| `HYBRID_SCOREFUSION_BOOST` | Score Fusion — Pipeline Weight Boost | Apply weight boost to one pipeline in $scoreFusion to increase its influence | 1 |
| `HYBRID_SUB_MATCH` | Hybrid Sub-pipeline — $match Filter | Use $match inside a hybrid sub-pipeline to narrow candidates before fusion | 1 |
| `HYBRID_SUB_SORT` | Hybrid Sub-pipeline — $sort Within Pipeline | Sort candidates within a sub-pipeline before fusion | 1 |
| `HYBRID_SUB_GEONEAR` | Hybrid Sub-pipeline — $geoNear | Use $geoNear inside a hybrid sub-pipeline for proximity ranking | 1 |
| `HYBRID_SUB_SAMPLE` | Hybrid Sub-pipeline — $sample | Use $sample inside a hybrid sub-pipeline to randomize one pipeline's candidates | 1 |
| `HYBRID_SUB_SCORE` | Hybrid Sub-pipeline — $addFields Score | Use $addFields to expose searchScore within a sub-pipeline for debugging or projection | 1 |

### `HYBRID_RRF_BASIC` — Basic Reciprocal Rank Fusion

> Combine vector + text via $rankFusion

**Prompt**: Search for 'star wars' using both semantic and keyword search combined.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$rankFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "star wars",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "star wars",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ]
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_RRF_WEIGHTED` — RRF with Weighted Pipelines

> Weight individual pipelines in $rankFusion

**Eval 1**: Search for 'AI' with more weight on the semantic pipeline.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$rankFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "artificial intelligence",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "AI",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ]
           }
         },
         "combination": {
           "weights": {
             "vector": 0.7,
             "text": 0.3
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```

**Eval 2**: Search with 70% weight on vector and 30% on text.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$rankFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "artificial intelligence",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "AI",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ]
           }
         },
         "combination": {
           "weights": {
             "vector": 0.7,
             "text": 0.3
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_RRF_SCORE_DETAILS` — RRF with Score Details

> Enable scoreDetails in $rankFusion

**Prompt**: Search for 'revenge thriller' and include a scoring breakdown.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$rankFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "revenge thriller",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "revenge thriller",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ]
           }
         },
         "scoreDetails": true
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "scoreDetails": {
           "$meta": "scoreDetails"
         }
       }
     }
   ]
   ```


### `HYBRID_SCOREFUSION_SIGMOID` — Score Fusion — Sigmoid

> Score-based fusion with sigmoid normalization

**Prompt**: Search for 'dystopian future' using sigmoid normalization.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$scoreFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "dystopian future",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "dystopian future",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ]
           },
           "normalization": "sigmoid"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_SCOREFUSION_MINMAX` — Score Fusion — MinMax + Expression

> Score fusion with minMaxScaler + custom combination expression

**Prompt**: Search for 'romantic comedy' with min-max normalization and custom scoring.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$scoreFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "romantic comedy",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "romantic comedy",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ]
           },
           "normalization": "minMaxScaler"
         },
         "combination": {
           "method": "expression",
           "expression": {
             "$sum": [
               {
                 "$multiply": [
                   "$vector",
                   0.6
                 ]
               },
               {
                 "$multiply": [
                   "$text",
                   0.4
                 ]
               }
             ]
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_SCOREFUSION_AVG` — Score Fusion — Average

> Score fusion with default avg combination

**Prompt**: Search for 'zombie apocalypse' with averaged scores.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$scoreFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "zombie apocalypse",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "zombie apocalypse",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ]
           },
           "normalization": "none"
         },
         "combination": {
           "method": "avg"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_SCOREFUSION_NONE` — Score Fusion — No Normalization

> Score fusion with none — raw scores

**Prompt**: Search for 'horror' using raw scores without normalization.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$scoreFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "horror",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "horror",
                     "path": "genres"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ]
           },
           "normalization": "none"
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_MULTI_FIELD` — Hybrid — Multiple Text Pipelines

> Rank fusion combining multiple lexical pipelines on different fields

**Prompt**: Search for 'adventure' across both the title and plot fields and combine the results.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$rankFusion": {
         "input": {
           "pipelines": {
             "titleSearch": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "adventure",
                     "path": "title"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ],
             "plotSearch": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "adventure",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ]
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "plot": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_PRE_FILTER` — Hybrid — Pre-Filter via Lexical Prefilter Pattern

> Use vectorSearch operator inside $search to apply an Atlas Search filter before vector scoring

**Prompt**: Find movies semantically similar to 'space exploration' but only among Action genre films.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$search": {
         "index": "default",
         "vectorSearch": {
           "index": "vector_index",
           "path": "plot_embedding",
           "queryVector": "space exploration",
           "embeddingParameters": {
             "model": "voyage-3-large",
             "outputDimension": 1024
           },
           "numCandidates": 150,
           "limit": 20,
           "filter": {
             "equals": {
               "path": "genres",
               "value": "Action"
             }
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "genres": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_POST_FILTER` — Hybrid — Post-Filter with $match

> Apply a $match stage after $rankFusion/$scoreFusion to further filter results

**Prompt**: Run a hybrid search for 'thriller' and then filter results to only movies released after 2000.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$rankFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "thriller",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "thriller",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ]
           }
         }
       }
     },
     {
       "$match": {
         "year": {
           "$gt": 2000
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "year": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_SCOREFUSION_BOOST` — Score Fusion — Pipeline Weight Boost

> Apply weight boost to one pipeline in $scoreFusion to increase its influence

**Prompt**: Do a hybrid search for 'romantic comedy' and weight the vector results three times higher than the text results.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$scoreFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "romantic comedy",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "romantic comedy",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ]
           },
           "normalization": "sigmoid",
           "combination": {
             "weights": {
               "vector": 3,
               "text": 1
             }
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_SUB_MATCH` — Hybrid Sub-pipeline — $match Filter

> Use $match inside a hybrid sub-pipeline to narrow candidates before fusion

**Prompt**: Find sci-fi movies similar to 'dystopian future', but in the vector pipeline only consider movies with an IMDB rating above 7.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$rankFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "dystopian future",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 50
                 }
               },
               {
                 "$match": {
                   "imdb.rating": {
                     "$gt": 7
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "dystopian future",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ]
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "imdb": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_SUB_SORT` — Hybrid Sub-pipeline — $sort Within Pipeline

> Sort candidates within a sub-pipeline before fusion

**Prompt**: Search for 'war epic' using hybrid search. In the text pipeline, sort by year descending before taking the top 20.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$rankFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "war epic",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "war epic",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$sort": {
                   "year": -1
                 }
               },
               {
                 "$limit": 20
               }
             ]
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "year": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_SUB_GEONEAR` — Hybrid Sub-pipeline — $geoNear

> Use $geoNear inside a hybrid sub-pipeline for proximity ranking

**Prompt**: Find restaurants semantically similar to 'cozy Italian dining' and also rank them by proximity to coordinates [-73.99, 40.74].

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$rankFusion": {
         "input": {
           "pipelines": {
             "semantic": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "description_embedding",
                   "queryVector": "cozy Italian dining",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               }
             ],
             "proximity": [
               {
                 "$geoNear": {
                   "near": {
                     "type": "Point",
                     "coordinates": [
                       -73.99,
                       40.74
                     ]
                   },
                   "distanceField": "dist",
                   "spherical": true
                 }
               },
               {
                 "$limit": 20
               }
             ]
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "name": 1,
         "dist": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_SUB_SAMPLE` — Hybrid Sub-pipeline — $sample

> Use $sample inside a hybrid sub-pipeline to randomize one pipeline's candidates

**Prompt**: Find movies similar to 'heist adventure' using hybrid search, but randomize the text pipeline candidates to add variety.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$rankFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "heist adventure",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "heist adventure",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$sample": {
                   "size": 20
                 }
               }
             ]
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "score": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


### `HYBRID_SUB_SCORE` — Hybrid Sub-pipeline — $addFields Score

> Use $addFields to expose searchScore within a sub-pipeline for debugging or projection

**Prompt**: Run a hybrid search for 'superhero origin story' and include the individual pipeline scores in the output.

**Expected tool calls:**

1. `aggregate`
   ```json
   [
     {
       "$rankFusion": {
         "input": {
           "pipelines": {
             "vector": [
               {
                 "$vectorSearch": {
                   "index": "vector_index",
                   "path": "plot_embedding",
                   "queryVector": "superhero origin story",
                   "embeddingParameters": {
                     "model": "voyage-3-large",
                     "outputDimension": 1024
                   },
                   "numCandidates": 150,
                   "limit": 20
                 }
               },
               {
                 "$addFields": {
                   "vectorScore": {
                     "$meta": "vectorSearchScore"
                   }
                 }
               }
             ],
             "text": [
               {
                 "$search": {
                   "index": "default",
                   "text": {
                     "query": "superhero origin story",
                     "path": "plot"
                   }
                 }
               },
               {
                 "$addFields": {
                   "textScore": {
                     "$meta": "searchScore"
                   }
                 }
               },
               {
                 "$limit": 20
               }
             ]
           }
         }
       }
     },
     {
       "$limit": 10
     },
     {
       "$project": {
         "title": 1,
         "vectorScore": 1,
         "textScore": 1,
         "fusedScore": {
           "$meta": "searchScore"
         }
       }
     }
   ]
   ```


---

## Data Operations

| Feature ID | Feature | Description | Evals |
|------------|---------|-------------|-------|
| `DATA_INSERT_SINGLE` | Insert Single Document | Insert a single document into a collection | 1 |
| `DATA_INSERT_BULK` | Insert Multiple Documents | Bulk insert an array of documents into a collection | 1 |
| `DATA_INSERT_FILTER_FIELDS` | Insert with Embedding Parameters | Insert documents specifying embeddingParameters for auto-embed on ingestion | 1 |
| `DATA_UPDATE` | Update Documents | Update matching documents using update-many | 1 |
| `DATA_DELETE` | Delete Documents | Delete matching documents using delete-many | 2 |

### `DATA_INSERT_SINGLE` — Insert Single Document

> Insert a single document into a collection

**Prompt**: Add a new movie called 'The Last Voyage' with year 2024 and genre 'Sci-Fi' to the movies collection.

**Expected tool calls:**

1. `insert-many`
   ```json
   {
     "documents": [
       {
         "title": "The Last Voyage",
         "year": 2024,
         "genres": [
           "Sci-Fi"
         ]
       }
     ]
   }
   ```


### `DATA_INSERT_BULK` — Insert Multiple Documents

> Bulk insert an array of documents into a collection

**Prompt**: Insert three new products — a 'Keyboard' at $99, a 'Mouse' at $49, and a 'Monitor' at $299 — into the products collection.

**Expected tool calls:**

1. `insert-many`
   ```json
   {
     "documents": [
       {
         "name": "Keyboard",
         "price": 99
       },
       {
         "name": "Mouse",
         "price": 49
       },
       {
         "name": "Monitor",
         "price": 299
       }
     ]
   }
   ```


### `DATA_INSERT_FILTER_FIELDS` — Insert with Embedding Parameters

> Insert documents specifying embeddingParameters for auto-embed on ingestion

**Prompt**: Insert a new article with title 'MongoDB Atlas Search Guide' and body text 'Atlas Search enables full-text search...' and auto-generate a vector embedding for the body field.

**Expected tool calls:**

1. `insert-many`
   ```json
   {
     "documents": [
       {
         "title": "MongoDB Atlas Search Guide",
         "body": "Atlas Search enables full-text search..."
       }
     ],
     "embeddingParameters": {
       "field": "body",
       "model": "voyage-3-large",
       "outputDimension": 1024
     }
   }
   ```


### `DATA_UPDATE` — Update Documents

> Update matching documents using update-many

**Prompt**: Set the 'status' field to 'archived' for all movies released before 1950.

**Expected tool calls:**

1. `update-many`
   ```json
   {
     "filter": {
       "year": {
         "$lt": 1950
       }
     },
     "update": {
       "$set": {
         "status": "archived"
       }
     }
   }
   ```


### `DATA_DELETE` — Delete Documents

> Delete matching documents using delete-many

**Eval 1**: Delete all documents in the reviews collection where the 'spam' field is true.

**Expected tool calls:**

1. `delete-many`
   ```json
   {
     "filter": {
       "spam": true
     }
   }
   ```

**Eval 2**: Remove all products with a price of 0 from the products collection.

**Expected tool calls:**

1. `delete-many`
   ```json
   {
     "filter": {
       "price": 0
     }
   }
   ```

