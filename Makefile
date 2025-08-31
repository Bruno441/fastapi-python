run:
	@uvicorn fastapi_python.main:app --reload

create-migration:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m "${description}"

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head