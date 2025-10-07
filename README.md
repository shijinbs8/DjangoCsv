

***

# CSV Upload API with Serializer Validation

This Django REST Framework APIView allows uploading a CSV file containing user profile data. It validates each row using a Django serializer before saving valid records to the database.

## Features

- Accepts multipart form data with CSV file upload.
- Validates required fields: `name`, `email`, and `age`.
- Ensures email is unique and properly formatted.
- Validates age is an integer between 0 and 120.
- Skips invalid entries and reports detailed errors.
- Returns a summary of saved records and rejected entries.

## Installation

1. Clone this repository.
2. Install dependencies:


3. Configure your Django settings and database.
4. Apply migrations:

```bash
python manage.py migrate
```

## Usage

Send a POST request with a CSV file containing columns: `name`, `email`, `age`.

Example using `curl`:

```bash
curl -X POST -F "file=@/path/to/yourfile.csv" http://localhost:8000/api/upload-csv/
```

### CSV format example

```csv
name,email,age
John Doe,john@example.com,30
Jane Smith,jane@example.com,25
```

## Response

The response JSON provides:

- `records_saved`: Number of valid records saved.
- `records_rejected`: Number of invalid records skipped.
- `errors`: List of row numbers and related validation errors.

Example response:

```json
{
  "records_saved": 2,
  "records_rejected": 1,
  "errors": [
    {"row": 3, "error": {"email": ["This email already exists."]}}
  ]
}
```

## Serializer Details

`UserProfileSerializer` handles validation:

- `validate_name`: Ensures name is not empty.
- `validate_email`: Checks uniqueness and valid format.
- `validate_age`: Confirms age is an int from 0 to 120.

## Customization

Modify the serializer and view code to suit your data model or validation rules.

## License

