AIRFLOW_HOME=$(shell pwd)/airflow

all:
	@echo "see README.md"

.PHONY: start_airflow
start_airflow:
	@echo "Starting Airflow"
	NO_PROXY="*" AIRFLOW_HOME=$(AIRFLOW_HOME) airflow standalone
