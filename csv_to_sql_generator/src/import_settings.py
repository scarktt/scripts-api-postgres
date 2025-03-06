database_mappings = [
    {
        "database_name": "candidate-tracker-db",
        "tables": [
            {
                "table_name": "candidates",
                "columns": ["id", "title", "location", "hire_flag"],
                "data_files": ["candidates.csv"],
                "ignore_first_row": True,
                "skip": False,
            },
            {
                "table_name": "jobs",
                "columns": [
                    "id",
                    "ocupation",
                    "dateRange",
                    "skills",
                    "current_job",
                    "occupation_title",
                    "start_date",
                    "end_date",
                    "candidate_id",
                ],
                "data_files": ["jobs.csv"],
                "ignore_first_row": True,
                "skip": False,
            },
            {
                "table_name": "education",
                "columns": ["education_id", "title", "description", "dateRange", "candidate_id"],
                "data_files": ["education.csv"],
                "ignore_first_row": True,
                "skip": False,
            },
        ],
        "input_files_path": "files/candidate-tracker-db/cleaned/",
        "output_files_path": "files/candidate-tracker-db/queries/",
    }
]
