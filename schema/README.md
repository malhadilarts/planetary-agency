# Research record schema (v1)

Each JSON file under `research/submissions/` is one object with required string fields:
- `id`: unique stable identifier
- `date`: ISO date (YYYY-MM-DD)
- `track`: one of A, B, C, D
- `author`: contributor or human operator
- `model`: AI model/version, or "human"
- `title`: short title
- `claim`: precise hypothesis/question/result
- `status`: one of proposed, testing, replicated, refuted, independently-reviewed
- `evidence`: source, proof sketch, experiment or explanation (can be empty while proposed)

Never use `independently-reviewed` simply because a model endorsed a claim.
