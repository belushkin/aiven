# Creating initial table

# health_checker
"""
"id" SERIAL NOT NULL,
"http_response_time" INTEGER NOT NULL,
"status_code" SMALLINT NOT NULL,
"page_content_exists" BOOLEAN NOT NULL,
"created_at" TIMESTAMP(6) NOT NULL DEFAULT now()
"""
# ALTER TABLE health_checker ALTER COLUMN http_response_time TYPE NUMERIC(5,2)
