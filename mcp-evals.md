# MCP Atlas Search Evals

**134 evals** across **16 categories**

## Index Management — Text Search Index Creation

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `IDX_TEXT_DYNAMIC` | Dynamic Mapping Mode | Create index with dynamic: true to auto-index all fields | Create a text search index using dynamic mapping. | `create-index` → `{"mappings":{"dynamic":true}}` |
| | | | I want a full-text search index that automatically includes all existing and future fields. | `create-index` → `{"mappings":{"dynamic":true}}` |
| `IDX_TEXT_STATIC` | Explicit Field Definitions | Create index with dynamic: false and explicit field mappings | Create a search index for searching plot descriptions. | `create-index` → `{"mappings":{"dynamic":false,"fields":{"plot":{"type":"string"}}}}` |
| `IDX_TEXT_TYPESETS` | Configurable Dynamic TypeSets | Use typeSets to control which field types get auto-indexed | Create a dynamic search index but only auto-index string and number fields. | `create-index` → `{"typeSets":[{"name":"stringAndNumber","types":[{"type":"string"},{"type":"number"}]}],"mappings"...` |
| `IDX_TEXT_FIELD_TYPES` | Field Type Definitions | Define specific field types: string, number, date, objectId, boolean, geo, autocomplete, token, uuid, embeddedDocuments, document | Create a search index with title field as a string, year field as a number, released field as a date, genres field as a token type, title as autocomplete and netflix as boolean. | `create-index` → `{"mappings":{"dynamic":false,"fields":{"title":[{"type":"string"},{"type":"autocomplete"}],"year"...` |
| `IDX_TEXT_ANALYZER_INDEX` | Index-Time Analyzer | Configure analyzer applied to string fields when indexing (default: lucene.standard) | Create a search index with English stemming on the plot field. | `create-index` → `{"mappings":{"dynamic":false,"fields":{"plot":{"type":"string","analyzer":"lucene.english"}}}}` |
| | | | Index the plot field for search using the English analyzer. | `create-index` → `{"mappings":{"dynamic":false,"fields":{"plot":{"type":"string","analyzer":"lucene.english"}}}}` |
| `IDX_TEXT_ANALYZER_SEARCH` | Search-Time Analyzer | Configure a different analyzer for query text than index time | Index the plot field for search with the English analyzer but use the standard analyzer at search time. | `create-index` → `{"mappings":{"dynamic":false,"fields":{"plot":{"type":"string","analyzer":"lucene.english","searc...` |
| `IDX_TEXT_ANALYZER_BUILTIN` | Built-in Analyzers | Use built-in analyzers: lucene.standard, lucene.simple, lucene.whitespace, lucene.keyword, language-specific | Create a dynamic search index with the keyword analyzer. | `create-index` → `{"analyzer":"lucene.keyword","mappings":{"dynamic":true}}` |
| `IDX_TEXT_ANALYZER_CUSTOM` | Custom Analyzer | Define custom analyzer with tokenizer + filters pipeline | Create a dynamic search index with a custom analyzer that uses a whitespace tokenizer and a lowercase filter. | `create-index` → `{"analyzers":[{"name":"myCustomAnalyzer","tokenizer":{"type":"whitespace"},"tokenFilters":[{"type...` |
| `IDX_TEXT_MULTI_ANALYZER` | Multi Analyzer | Alternate analyzers on same field via multi for different query strategies | Create a search index with the title field searchable with both the standard and keyword analyzers. | `create-index` → `{"mappings":{"dynamic":false,"fields":{"title":{"type":"string","analyzer":"lucene.standard","mul...` |
| `IDX_TEXT_TOKEN_NORMALIZER` | Token Type Normalizer | Configure normalizers for token type: lowercase or none | Index the genres field as a token type with lowercase normalization. | `create-index` → `{"mappings":{"dynamic":false,"fields":{"genres":{"type":"token","normalizer":"lowercase"}}}}` |
| | | | Index the rated field as a token type without normalization. | `create-index` → `{"mappings":{"dynamic":false,"fields":{"rated":{"type":"token","normalizer":"none"}}}}` |
| `IDX_TEXT_SYNONYM_SOURCE` | Synonym Source Mappings | Configure synonym source mappings in index for synonym-aware search | Create an index with synonym support for movie genre terms like 'scary' and 'horror'. | `create-index` → `{"synonyms":[{"name":"genre_synonyms","analyzer":"lucene.standard","source":{"collection":"synony...` |
| `IDX_TEXT_FACET_MAPPING` | Facet-Type Field Mappings | Map fields with stringFacet / numberFacet to enable $searchMeta facet queries | Create a search index that supports faceted search on genres and year. | `create-index` → `{"mappings":{"dynamic":false,"fields":{"genres":[{"type":"stringFacet"},{"type":"string"}],"year"...` |
| `IDX_TEXT_MULTI_FIELD` | Multi-Field Definitions | Index multiple fields in one index definition | Create an index covering the plot, fullplot, and title fields. | `create-index` → `{"mappings":{"dynamic":false,"fields":{"plot":{"type":"string"},"fullplot":{"type":"string"},"tit...` |
| `IDX_TEXT_STORED_SOURCE` | Stored Source Configuration | Configure storedSource to store fields on mongot for returnStoredSource | Create a dynamic search index that stores the title and plot fields for faster retrieval. | `create-index` → `{"storedSource":{"include":["title","plot"]},"mappings":{"dynamic":true}}` |
| | | | Create a dynamic search index that stores all fields. | `create-index` → `{"storedSource":true,"mappings":{"dynamic":true}}` |
| | | | Create a dynamic search index that stores everything except the fullplot field. | `create-index` → `{"storedSource":{"exclude":["fullplot"]},"mappings":{"dynamic":true}}` |
| `IDX_TEXT_NUM_PARTITIONS` | Index Partitioning | Set numPartitions for collections exceeding 2B documents | Create a dynamic search index with 4 partitions for a very large collection. | `create-index` → `{"numPartitions":4,"mappings":{"dynamic":true}}` |

## Index Management — Vector Search Index Creation

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `IDX_VEC_SIMILARITY` | Similarity Functions | Specify similarity: euclidean, cosine, dotProduct | Create a vector index on plot_embedding with 1024 dimensions using cosine similarity. | `create-index` → `{"fields":[{"type":"vector","path":"plot_embedding","numDimensions":1024,"similarity":"cosine"}]}` |
| | | | Create a vector index on plot_embedding with 1024 dimensions using Euclidean distance. | `create-index` → `{"fields":[{"type":"vector","path":"plot_embedding","numDimensions":1024,"similarity":"euclidean"}]}` |
| | | | Create a vector index on plot_embedding with 1024 dimensions using dot product similarity. | `create-index` → `{"fields":[{"type":"vector","path":"plot_embedding","numDimensions":1024,"similarity":"dotProduct...` |
| `IDX_VEC_QUANTIZATION` | Quantization | Scalar or binary quantization for reduced memory / maximum compression | Create a vector index on plot_embedding with 1024 dimensions and scalar quantization. | `create-index` → `{"fields":[{"type":"vector","path":"plot_embedding","numDimensions":1024,"similarity":"cosine","q...` |
| | | | Create a vector index on plot_embedding with 1024 dimensions and binary quantization. | `create-index` → `{"fields":[{"type":"vector","path":"plot_embedding","numDimensions":1024,"similarity":"euclidean"...` |
| `IDX_VEC_FILTER_FIELDS` | Filter Field Definitions | Define filter fields for pre-filtering in $vectorSearch | Create a vector index on plot_embedding with 1024 dimensions, cosine similarity, and genres and year as filter fields. | `create-index` → `{"fields":[{"type":"vector","path":"plot_embedding","numDimensions":1024,"similarity":"cosine"},{...` |
| `IDX_VEC_AUTO_EMBED` | Auto-Embed Type | Automated embedding generation via Voyage AI at index/query time (Preview) | Create a vector index that auto-generates embeddings from the plot field. | `create-index` → `{"fields":[{"type":"autoEmbed","path":"plot","model":"voyage-4-large","modality":"text","numDimen...` |

## Index Management — Lifecycle

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `IDX_DELETE` | Index Deletion | Delete an existing search index | Delete the index named 'old_index' from the movies collection. | `drop-index` → `{"indexName":"old_index"}` |

## Text Search ($search) — Operators

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `SEARCH_TEXT` | Basic Text Search | Keyword search via text operator. Multi-term, multi-path, array query (implicit OR) | Search the plot field for movies about time travel. | `aggregate` → `[{"$search":{"text":{"query":"time travel","path":"plot"}}},{"$limit":10},{"$project":{"title":1,...` |
| | | | Find movies with 'robot' or 'AI' in the plot. | `aggregate` → `[{"$search":{"text":{"query":["robot","AI"],"path":"plot"}}},{"$limit":10},{"$project":{"title":1...` |
| `SEARCH_PHRASE` | Phrase Search | Exact phrase matching with optional slop for proximity | Find movies where 'save the world' appears within 2 words of each other in the plot. | `aggregate` → `[{"$search":{"phrase":{"query":"save the world","path":"plot","slop":2}}},{"$limit":10},{"$projec...` |
| | | | Find movies containing the exact phrase 'world war' in the plot. | `aggregate` → `[{"$search":{"phrase":{"query":"world war","path":"plot"}}},{"$limit":10},{"$project":{"title":1,...` |
| `SEARCH_FUZZY` | Fuzzy Search | Typo tolerance via fuzzy with maxEdits, prefixLength | Search the plot for 'vampyres' with fuzzy matching to handle the typo. | `aggregate` → `[{"$search":{"text":{"query":"vampyres","path":"plot","fuzzy":{"maxEdits":1}}}},{"$limit":10},{"$...` |
| | | | Find horror movies mentioning 'vampyres' in the plot. | `aggregate` → `[{"$search":{"compound":{"must":[{"text":{"query":"vampyres","path":"plot","fuzzy":{"maxEdits":1}...` |
| `SEARCH_AUTOCOMPLETE` | Autocomplete / Typeahead | Prefix/typeahead matching | Find movie titles starting with 'The Dark'. | `aggregate` → `[{"$search":{"autocomplete":{"query":"The Dark","path":"title"}}},{"$limit":10},{"$project":{"tit...` |
| `SEARCH_WILDCARD` | Wildcard Search | Pattern matching with *, ? | Find titles matching the pattern 'Star*Wars'. | `aggregate` → `[{"$search":{"wildcard":{"query":"Star*Wars","path":"title","allowAnalyzedField":true}}},{"$limit...` |
| `SEARCH_REGEX` | Regular Expression Search | Match via regex patterns | Find titles matching the regex pattern 'The.*Knight'. | `aggregate` → `[{"$search":{"regex":{"query":"The.*Knight","path":"title","allowAnalyzedField":true}}},{"$limit"...` |
| `SEARCH_EQUALS` | Exact Value Match | Exact match on boolean, date, objectId, number, token, uuid | Find movies rated 'PG-13'. | `aggregate` → `[{"$search":{"equals":{"value":"PG-13","path":"rated"}}},{"$limit":10},{"$project":{"title":1,"ra...` |
| | | | Find movies from exactly the year 2020. | `aggregate` → `[{"$search":{"equals":{"value":2020,"path":"year"}}},{"$limit":10},{"$project":{"title":1,"year":...` |
| | | | Find documents where the type equals 'movie'. | `aggregate` → `[{"$search":{"equals":{"value":"movie","path":"type"}}},{"$limit":10},{"$project":{"title":1,"typ...` |
| `SEARCH_IN` | Match Any Value in Array | Match any from array of candidates | Find movies rated either 'PG' or 'PG-13'. | `aggregate` → `[{"$search":{"in":{"value":["PG","PG-13"],"path":"rated"}}},{"$limit":10},{"$project":{"title":1,...` |
| | | | Find movies from the years 2018, 2019, or 2020. | `aggregate` → `[{"$search":{"in":{"value":[2018,2019,2020],"path":"year"}}},{"$limit":10},{"$project":{"title":1...` |
| `SEARCH_RANGE` | Range Queries | Numeric/date/objectId/token ranges with gt, gte, lt, lte | Find movies from the 1990s with 'heist' in the plot. | `aggregate` → `[{"$search":{"compound":{"must":[{"text":{"query":"heist","path":"plot"}}],"filter":[{"range":{"p...` |
| | | | Find movies with 'mystery' in the genres field from 2010 to 2020. | `aggregate` → `[{"$search":{"compound":{"must":[{"text":{"query":"mystery","path":"genres"}}],"filter":[{"range"...` |
| | | | Find movies with 'world war' in the plot from the last 20 years. | `aggregate` → `[{"$search":{"compound":{"must":[{"text":{"query":"world war","path":"plot"}}],"filter":[{"range"...` |
| `SEARCH_NEAR` | Proximity-Scored Search | Proximity-scored on number, date, or GeoJSON with pivot-based decay | Find movies closest to the year 2000, with relevance decaying over 5 years. | `aggregate` → `[{"$search":{"near":{"path":"year","origin":2000,"pivot":5}}},{"$limit":10},{"$project":{"title":...` |
| | | | Find movies released near January 2020. | `aggregate` → `[{"$search":{"near":{"path":"released","origin":{"$date":"2020-01-01T00:00:00Z"},"pivot":77760000...` |
| `SEARCH_EXISTS` | Field Existence Check | Test for presence of indexed field | Find movies where the fullplot field exists. | `aggregate` → `[{"$search":{"exists":{"path":"fullplot"}}},{"$limit":10},{"$project":{"title":1,"score":{"$meta"...` |
| | | | Find movies that have an IMDB rating. | `aggregate` → `[{"$search":{"exists":{"path":"imdb.rating"}}},{"$limit":10},{"$project":{"title":1,"imdb":1,"sco...` |
| `SEARCH_MORE_LIKE_THIS` | Find Similar Documents | Find similar docs based on representative terms | Find movies similar to The Matrix by matching on the title and plot fields. | `aggregate` → `[{"$search":{"moreLikeThis":{"like":[{"title":"The Matrix","plot":"A computer hacker learns about...` |
| `SEARCH_QUERY_STRING` | Lucene Query String | Lucene-style query syntax | Find movies where title contains Batman and year is greater than 2000. | `aggregate` → `[{"$search":{"queryString":{"defaultPath":"plot","query":"title:Batman AND year:>2000"}}},{"$limi...` |
| `SEARCH_GEO_WITHIN` | Geospatial Filtering | Filter within circle, polygon, box, MultiPolygon | Find movies with 'New York' in the plot near the coordinates [40.7128, -74.0060] in the location field. | `aggregate` → `[{"$search":{"compound":{"must":[{"text":{"query":"New York","path":"plot"}}],"filter":[{"geoWith...` |
| `SEARCH_GEO_SHAPE` | Spatial Relation Queries | Relations: contains, disjoint, intersects, within | Find locations that intersect with this polygon. | `aggregate` → `[{"$search":{"geoShape":{"path":"location","relation":"intersects","geometry":{"type":"Polygon","...` |
| `SEARCH_EMBEDDED_DOC` | Embedded Document Search | Query fields in arrays of embedded docs with per-doc scoring | Find movies where cast member 'Tom Hanks' is playing 'Forrest'. | `aggregate` → `[{"$search":{"embeddedDocument":{"path":"cast","operator":{"compound":{"must":[{"text":{"query":"...` |
| `SEARCH_VECTOR_IN_SEARCH` | Vector Search within $search | vectorSearch operator inside $search for combined ANN/ENN + text pre-filters | Find movies semantically similar to 'space exploration' using the plot_embedding field, where the title contains 'Star'. | `aggregate` → `[{"$search":{"compound":{"must":[{"vectorSearch":{"path":"plot_embedding","queryVector":[0.1,-0.2...` |

## Text Search ($search) — Compound Queries

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `COMPOUND_MUST` | Required Clauses | must — clauses that must match (affects score + filtering) | Find movies with 'Comedy' in genres and 'robots' in the plot. | `aggregate` → `[{"$search":{"compound":{"must":[{"text":{"query":"robots","path":"plot"}},{"text":{"query":"Come...` |
| `COMPOUND_SHOULD` | Optional / Boosting Clauses | should — optional clauses that boost score, with minimumShouldMatch | Find movies with 'batman' in the title and 'batman' in the plot. | `aggregate` → `[{"$search":{"compound":{"should":[{"text":{"query":"batman","path":"title"}},{"text":{"query":"b...` |
| `COMPOUND_FILTER` | Filter-Only Clauses | filter — required clauses, no score impact | Find movies with 'climate change' in the plot, filtered to 'Documentary' in genres, sorted by most recent. | `aggregate` → `[{"$search":{"compound":{"must":[{"text":{"query":"climate change","path":"plot"}}],"filter":[{"t...` |
| `COMPOUND_MUST_NOT` | Exclusion Clauses | mustNot — exclude matching documents | Find movies with 'action' in genres but exclude those with 'superhero' in the plot. | `aggregate` → `[{"$search":{"compound":{"must":[{"text":{"query":"action","path":"genres"}}],"mustNot":[{"text":...` |

## Text Search ($search) — Scoring & Relevance

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `SCORE_BOOST_VALUE` | Static Score Boost | Boost field's score with static value | Search for 'action' in the title and plot fields, with more weight on the title. | `aggregate` → `[{"$search":{"compound":{"should":[{"text":{"query":"action","path":"title","score":{"boost":{"va...` |
| | | | Boost the title field score by 3x. | `aggregate` → `[{"$search":{"compound":{"should":[{"text":{"query":"action","path":"title","score":{"boost":{"va...` |
| `SCORE_BOOST_PATH` | Dynamic Score Boost from Field | Boost dynamically using numeric field value | Search the plot for 'thriller' with results boosted by the imdb.rating field. | `aggregate` → `[{"$search":{"text":{"query":"thriller","path":"plot","score":{"boost":{"path":"imdb.rating","und...` |
| `SCORE_CONSTANT` | Constant Score | Replace score with fixed number | Apply a genre filter with a constant score of 1. | `aggregate` → `[{"$search":{"compound":{"filter":[{"text":{"query":"Action","path":"genres","score":{"constant":...` |
| `SCORE_FUNCTION` | Computed Score Expression | Replace score with computed expression (arithmetic, log, path-based) | Score results using the log of IMDB votes. | `aggregate` → `[{"$search":{"text":{"query":"thriller","path":"plot","score":{"function":{"log1p":{"path":{"valu...` |
| `SCORE_EMBEDDED` | Embedded Document Scoring | Scoring for embeddedDocument operator — aggregate across matches | Search embedded cast documents and use the maximum score. | `aggregate` → `[{"$search":{"embeddedDocument":{"path":"cast","operator":{"text":{"query":"Tom Hanks","path":"ca...` |
| `SCORE_DETAILS` | Score Breakdown | Enable scoreDetails for $meta: "searchScoreDetails" | Search the plot for 'romance' with a detailed score explanation. | `aggregate` → `[{"$search":{"text":{"query":"romance","path":"plot"},"scoreDetails":true}},{"$limit":10},{"$proj...` |

## Text Search ($search) — Highlighting & Synonyms

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `HIGHLIGHT` | Search Highlighting | Return highlighted matching text via highlight + $meta: "searchHighlights" | Search for 'space exploration' and highlight the matching text. | `aggregate` → `[{"$search":{"text":{"query":"space exploration","path":"plot"},"highlight":{"path":"plot"}}},{"$...` |
| `SYNONYMS` | Synonym-Aware Search | Expand query terms via synonym mapping in index | Search for 'scary' and also match 'horror' and 'frightening' as synonyms. | `aggregate` → `[{"$search":{"text":{"query":"scary","path":"plot","synonyms":"genre_synonyms"}}},{"$limit":10},{...` |

## Text Search ($search) — Faceted Search

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `FACET_STRING` | String Facets | Category counts via $searchMeta | Count movies by genre that mention 'detective'. | `aggregate` → `[{"$searchMeta":{"facet":{"operator":{"text":{"query":"detective","path":"plot"}},"facets":{"genr...` |
| `FACET_NUMBER` | Number Facets | Bucketed counts with boundaries | Show a decade breakdown for movies about 'thriller'. | `aggregate` → `[{"$searchMeta":{"facet":{"operator":{"text":{"query":"thriller","path":"plot"}},"facets":{"yearF...` |
| | | | Search for 'thriller' faceted by genre and year. | `aggregate` → `[{"$searchMeta":{"facet":{"operator":{"text":{"query":"thriller","path":"plot"}},"facets":{"genre...` |
| `FACET_DATE` | Date Facets | Time-based bucketed counts | Show the quarterly distribution of 'thriller' movies in 2020. | `aggregate` → `[{"$searchMeta":{"facet":{"operator":{"text":{"query":"thriller","path":"plot"}},"facets":{"relea...` |
| | | | Show the monthly distribution of 'pandemic' movies in 2020. | `aggregate` → `[{"$searchMeta":{"facet":{"operator":{"text":{"query":"pandemic","path":"plot"}},"facets":{"relea...` |

## Text Search ($search) — Count Analytics

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `COUNT_TOTAL` | Exact Total Count | Exact count via $count stage or $searchMeta | How many movies are about outer space? | `aggregate` → `[{"$searchMeta":{"facet":{"operator":{"text":{"query":"outer space","path":"plot"}},"facets":{}},...` |
| `COUNT_LOWER_BOUND` | Fast Approximate Count | Fast approximate count with type: "lowerBound" | Give me a quick estimate of how many movies mention 'love'. | `aggregate` → `[{"$searchMeta":{"facet":{"operator":{"text":{"query":"love","path":"plot"}},"facets":{}},"count"...` |
| `COUNT_THRESHOLD` | Count Threshold | Configure count.threshold for lowerBound accuracy (default: 1000) | Count 'war' movies with a threshold of 5000. | `aggregate` → `[{"$searchMeta":{"facet":{"operator":{"text":{"query":"war","path":"plot"}},"facets":{}},"count":...` |
| `COUNT_INLINE` | Inline Count via $$SEARCH_META | count option in $search + $$SEARCH_META variable | Search for 'comedy' and include the total count alongside the results. | `aggregate` → `[{"$search":{"text":{"query":"comedy","path":"genres"},"count":{"type":"total"}}},{"$limit":10},{...` |

## Text Search ($search) — Pagination

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `PAGE_OFFSET` | Offset-Based Pagination | Traditional $skip + $limit | Show page 2 of 'comedy' results with 10 per page. | `aggregate` → `[{"$search":{"text":{"query":"comedy","path":"genres"}}},{"$skip":10},{"$limit":10},{"$project":{...` |
| `PAGE_CURSOR` | Token-Based Cursor Pagination | searchAfter / searchBefore with $meta: "searchSequenceToken" | Show the next page after this token for 'comedy' results. | `aggregate` → `[{"$search":{"text":{"query":"comedy","path":"genres"},"sort":{"released":-1,"_id":1}}},{"$limit"...`<br>`aggregate` → `[{"$search":{"text":{"query":"comedy","path":"genres"},"searchAfter":"<token-from-last-document>"...` |

## Text Search ($search) — Sorting

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `SORT_NATIVE` | Native Sort within $search | Sort within search engine via sort option. Supports boolean, date, number, objectId, uuid, token, score | Search for 'drama' sorted by year descending using native sort. | `aggregate` → `[{"$search":{"text":{"query":"drama","path":"genres"},"sort":{"year":-1}}},{"$limit":10},{"$proje...` |
| `SORT_POST_SEARCH` | Post-Search Sort | Re-sort results by external fields via $sort after $search | Find the top 5 highest-rated movies about AI. | `aggregate` → `[{"$search":{"text":{"query":"AI","path":"plot"}}},{"$limit":100},{"$sort":{"imdb.rating":-1}},{"...` |
| | | | Search for 'pandemic' movies sorted by viewer rating. | `aggregate` → `[{"$search":{"text":{"query":"pandemic","path":"plot"}}},{"$limit":100},{"$sort":{"imdb.rating":-...` |

## Text Search ($search) — $search Stage Options

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `OPT_CONCURRENT` | Concurrent Search | Parallelize search across segments on dedicated search nodes | Search for 'action' with concurrent execution enabled. | `aggregate` → `[{"$search":{"text":{"query":"action","path":"genres"},"concurrent":true}},{"$limit":10},{"$proje...` |
| `OPT_RETURN_STORED_SOURCE` | Return Stored Fields | Return stored fields from mongot instead of full doc lookup | Search for 'thriller' using stored source for a faster response. | `aggregate` → `[{"$search":{"text":{"query":"thriller","path":"genres"},"returnStoredSource":true}},{"$limit":10...` |
| `OPT_RETURN_SCOPE` | Return Scope for Embedded Docs | Set query context to embedded doc fields (requires returnStoredSource: true) | Search the embedded cast and return only the matching embedded documents. | `aggregate` → `[{"$search":{"embeddedDocument":{"path":"cast","operator":{"text":{"query":"Tom Hanks","path":"ca...` |

## Text Search ($search) — Post-Search Aggregation

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `AGG_FACET` | Parallel Sub-Pipelines | $facet — multiple sub-pipelines over search results (stats + top-N) | Search for 'superhero' and return the average rating, count, and top 3 genres. | `aggregate` → `[{"$search":{"text":{"query":"superhero","path":"plot"}}},{"$facet":{"stats":[{"$group":{"_id":nu...` |
| `AGG_GROUP` | Aggregate Search Results | $group — aggregate with $avg, $sum, $push, $min/$max | Search for 'romance' and calculate the average IMDB rating per genre. | `aggregate` → `[{"$search":{"text":{"query":"romance","path":"plot"}}},{"$limit":100},{"$unwind":"$genres"},{"$g...` |
| `AGG_UNWIND` | Flatten Arrays | $unwind — flatten array fields for per-element grouping | Search for 'comedy' and count the results per genre. | `aggregate` → `[{"$search":{"text":{"query":"comedy","path":"plot"}}},{"$limit":100},{"$unwind":"$genres"},{"$gr...` |
| `AGG_BUCKET` | Bucket into Ranges | $bucket / $bucketAuto — bin results into ranges | Search for 'drama' and bucket the results by IMDB rating. | `aggregate` → `[{"$search":{"text":{"query":"drama","path":"genres"}}},{"$limit":100},{"$bucket":{"groupBy":"$im...` |
| | | | Search for 'action' and auto-bucket the results by year. | `aggregate` → `[{"$search":{"text":{"query":"action","path":"genres"}}},{"$limit":100},{"$bucketAuto":{"groupBy"...` |
| `AGG_SORT_BY_COUNT` | Shorthand Frequency Count | $sortByCount — shorthand for $unwind → $group → $sort | Search for 'thriller' and show the most common genres. | `aggregate` → `[{"$search":{"text":{"query":"thriller","path":"genres"}}},{"$limit":100},{"$unwind":"$genres"},{...` |
| `AGG_LOOKUP` | Join with Other Collections | $lookup — join search results with other collections | Find 'space' movies and include their comments from the comments collection. | `aggregate` → `[{"$search":{"text":{"query":"space","path":"plot"}}},{"$limit":10},{"$lookup":{"from":"comments"...` |
| `AGG_REPLACE_ROOT` | Promote Embedded Document | $replaceRoot / $replaceWith — promote embedded doc to top level | Return only the IMDB subdocument for each search result. | `aggregate` → `[{"$search":{"text":{"query":"drama","path":"genres"}}},{"$limit":10},{"$replaceRoot":{"newRoot":...` |
| `AGG_OUT_MERGE` | Materialize Results | $out / $merge — write results to collection for caching | Save the 'horror' search results to a collection called 'horror_cache'. | `aggregate` → `[{"$search":{"text":{"query":"horror","path":"genres"}}},{"$limit":100},{"$project":{"title":1,"p...` |
| | | | Merge the search results into the recommendations collection. | `aggregate` → `[{"$search":{"text":{"query":"drama","path":"genres"}}},{"$limit":100},{"$project":{"title":1,"pl...` |
| `AGG_SAMPLE` | Random Sample | $sample — random sample from search results | Search for 'adventure' and give me 5 random picks. | `aggregate` → `[{"$search":{"text":{"query":"adventure","path":"genres"}}},{"$limit":100},{"$sample":{"size":5}}]` |

## Vector Search ($vectorSearch)

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `VSEARCH_ANN` | Approximate Nearest Neighbor | ANN with numCandidates for recall/performance trade-off | Find plots that are semantically similar to this embedding. | `aggregate` → `[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":["<1024-dim vecto...` |
| | | | Find movies similar to 'young heroes in epic struggles'. | `aggregate` → `[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"young heroes in ...` |
| `VSEARCH_ENN` | Exact Nearest Neighbor | ENN with exact: true (no numCandidates) | Run an exact vector search for 'detective in a small town'. | `aggregate` → `[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"detective in a s...` |
| `VSEARCH_PRE_FILTER_EQ` | Pre-Filter Equality | Pre-filter on filter fields using $eq / short-form | Find sci-fi movies similar to 'space exploration'. | `aggregate` → `[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"space exploratio...` |
| `VSEARCH_PRE_FILTER_RANGE` | Pre-Filter Range | Pre-filter with $gt, $gte, $lt, $lte | Find movies from 2000 to 2020 similar to 'romantic comedy in New York'. | `aggregate` → `[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"romantic comedy ...` |
| `VSEARCH_PRE_FILTER_IN` | Pre-Filter Set Membership | Pre-filter with $in / $nin | Find Action or Adventure movies similar to 'car chases'. | `aggregate` → `[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"car chases","emb...` |
| | | | Find movies similar to 'comedy' but not in the Romance genre. | `aggregate` → `[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"comedy","embeddi...` |
| `VSEARCH_PRE_FILTER_EXISTS` | Pre-Filter Field Existence | Pre-filter with $exists | Find movies similar to 'epic saga' that have a year field. | `aggregate` → `[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"epic saga","embe...` |
| `VSEARCH_PRE_FILTER_COMPOUND` | Compound Pre-Filters | Combine with $and, $or, $not, $nor | Find drama movies after 2010 similar to 'family struggles'. | `aggregate` → `[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"family struggles...` |
| | | | Find Action or Thriller movies similar to 'heist'. | `aggregate` → `[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"heist","embeddin...` |
| `VSEARCH_POST_FILTER` | Post-Filter via $match | Post-filter on fields NOT in vector index | Find movies similar to 'epic battles' with an IMDB rating above 7.5. | `aggregate` → `[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"epic battles","e...` |
| `VSEARCH_SCORE` | Score Projection | Project similarity score via $meta: "vectorSearchScore" | Search for 'underwater exploration' and include the similarity scores. | `aggregate` → `[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"underwater explo...` |
| `VSEARCH_SORT_EXTERNAL` | Sort by External Field | Sort by external field (inflated limit → $sort → $limit) | Find movies similar to 'coming of age' sorted by IMDB rating. | `aggregate` → `[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"coming of age","...` |
| `VSEARCH_EXPLAIN` | Explain / Performance | Analyze query performance with .explain("executionStats") | Analyze the vector search performance for 'space odyssey'. | `explain` → `{"pipeline":[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"spac...` |
| `VSEARCH_EXPLAIN_TRACE` | Trace Document IDs | Trace specific doc IDs through pipeline via explainOptions.traceDocumentIds | Trace these document IDs through the vector search pipeline. | `explain` → `{"pipeline":[{"$vectorSearch":{"index":"vector_index","path":"plot_embedding","queryVector":"spac...` |

## Hybrid Search ($rankFusion / $scoreFusion)

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `HYBRID_RRF_BASIC` | Basic Reciprocal Rank Fusion | Combine vector + text via $rankFusion | Search for 'star wars' using both semantic and keyword search combined. | `aggregate` → `[{"$rankFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path":...` |
| `HYBRID_RRF_WEIGHTED` | RRF with Weighted Pipelines | Weight individual pipelines in $rankFusion | Search for 'AI' with more weight on the semantic pipeline. | `aggregate` → `[{"$rankFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path":...` |
| | | | Search with 70% weight on vector and 30% on text. | `aggregate` → `[{"$rankFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path":...` |
| `HYBRID_RRF_SCORE_DETAILS` | RRF with Score Details | Enable scoreDetails in $rankFusion | Search for 'revenge thriller' and include a scoring breakdown. | `aggregate` → `[{"$rankFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path":...` |
| `HYBRID_SCOREFUSION_SIGMOID` | Score Fusion — Sigmoid | Score-based fusion with sigmoid normalization | Search for 'dystopian future' using sigmoid normalization. | `aggregate` → `[{"$scoreFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path"...` |
| `HYBRID_SCOREFUSION_MINMAX` | Score Fusion — MinMax + Expression | Score fusion with minMaxScaler + custom combination expression | Search for 'romantic comedy' with min-max normalization and custom scoring. | `aggregate` → `[{"$scoreFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path"...` |
| `HYBRID_SCOREFUSION_AVG` | Score Fusion — Average | Score fusion with default avg combination | Search for 'zombie apocalypse' with averaged scores. | `aggregate` → `[{"$scoreFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path"...` |
| `HYBRID_SCOREFUSION_NONE` | Score Fusion — No Normalization | Score fusion with none — raw scores | Search for 'horror' using raw scores without normalization. | `aggregate` → `[{"$scoreFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path"...` |
| `HYBRID_MULTI_FIELD` | Hybrid — Multiple Text Pipelines | Rank fusion combining multiple lexical pipelines on different fields | Search for 'adventure' across both the title and plot fields and combine the results. | `aggregate` → `[{"$rankFusion":{"input":{"pipelines":{"titleSearch":[{"$search":{"index":"default","text":{"quer...` |
| `HYBRID_PRE_FILTER` | Hybrid — Pre-Filter via Lexical Prefilter Pattern | Use vectorSearch operator inside $search to apply an Atlas Search filter before vector scoring | Find movies semantically similar to 'space exploration' but only among Action genre films. | `aggregate` → `[{"$search":{"index":"default","vectorSearch":{"index":"vector_index","path":"plot_embedding","qu...` |
| `HYBRID_POST_FILTER` | Hybrid — Post-Filter with $match | Apply a $match stage after $rankFusion/$scoreFusion to further filter results | Run a hybrid search for 'thriller' and then filter results to only movies released after 2000. | `aggregate` → `[{"$rankFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path":...` |
| `HYBRID_SCOREFUSION_BOOST` | Score Fusion — Pipeline Weight Boost | Apply weight boost to one pipeline in $scoreFusion to increase its influence | Do a hybrid search for 'romantic comedy' and weight the vector results three times higher than the text results. | `aggregate` → `[{"$scoreFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path"...` |
| `HYBRID_SUB_MATCH` | Hybrid Sub-pipeline — $match Filter | Use $match inside a hybrid sub-pipeline to narrow candidates before fusion | Find sci-fi movies similar to 'dystopian future', but in the vector pipeline only consider movies with an IMDB rating above 7. | `aggregate` → `[{"$rankFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path":...` |
| `HYBRID_SUB_SORT` | Hybrid Sub-pipeline — $sort Within Pipeline | Sort candidates within a sub-pipeline before fusion | Search for 'war epic' using hybrid search. In the text pipeline, sort by year descending before taking the top 20. | `aggregate` → `[{"$rankFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path":...` |
| `HYBRID_SUB_GEONEAR` | Hybrid Sub-pipeline — $geoNear | Use $geoNear inside a hybrid sub-pipeline for proximity ranking | Find restaurants semantically similar to 'cozy Italian dining' and also rank them by proximity to coordinates [-73.99, 40.74]. | `aggregate` → `[{"$rankFusion":{"input":{"pipelines":{"semantic":[{"$vectorSearch":{"index":"vector_index","path...` |
| `HYBRID_SUB_SAMPLE` | Hybrid Sub-pipeline — $sample | Use $sample inside a hybrid sub-pipeline to randomize one pipeline's candidates | Find movies similar to 'heist adventure' using hybrid search, but randomize the text pipeline candidates to add variety. | `aggregate` → `[{"$rankFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path":...` |
| `HYBRID_SUB_SCORE` | Hybrid Sub-pipeline — $addFields Score | Use $addFields to expose searchScore within a sub-pipeline for debugging or projection | Run a hybrid search for 'superhero origin story' and include the individual pipeline scores in the output. | `aggregate` → `[{"$rankFusion":{"input":{"pipelines":{"vector":[{"$vectorSearch":{"index":"vector_index","path":...` |

## Data Operations

| Feature ID | Feature | Description | Prompt | Expected Tool Calls |
|------------|---------|-------------|--------|---------------------|
| `DATA_INSERT_SINGLE` | Insert Single Document | Insert a single document into a collection | Add a new movie called 'The Last Voyage' with year 2024 and genre 'Sci-Fi' to the movies collection. | `insert-many` → `{"documents":[{"title":"The Last Voyage","year":2024,"genres":["Sci-Fi"]}]}` |
| `DATA_INSERT_BULK` | Insert Multiple Documents | Bulk insert an array of documents into a collection | Insert three new products — a 'Keyboard' at $99, a 'Mouse' at $49, and a 'Monitor' at $299 — into the products collection. | `insert-many` → `{"documents":[{"name":"Keyboard","price":99},{"name":"Mouse","price":49},{"name":"Monitor","price...` |
| `DATA_INSERT_FILTER_FIELDS` | Insert with Embedding Parameters | Insert documents specifying embeddingParameters for auto-embed on ingestion | Insert a new article with title 'MongoDB Atlas Search Guide' and body text 'Atlas Search enables full-text search...' and auto-generate a vector embedding for the body field. | `insert-many` → `{"documents":[{"title":"MongoDB Atlas Search Guide","body":"Atlas Search enables full-text search...` |
| `DATA_UPDATE` | Update Documents | Update matching documents using update-many | Set the 'status' field to 'archived' for all movies released before 1950. | `update-many` → `{"filter":{"year":{"$lt":1950}},"update":{"$set":{"status":"archived"}}}` |
| `DATA_DELETE` | Delete Documents | Delete matching documents using delete-many | Delete all documents in the reviews collection where the 'spam' field is true. | `delete-many` → `{"filter":{"spam":true}}` |
| | | | Remove all products with a price of 0 from the products collection. | `delete-many` → `{"filter":{"price":0}}` |
