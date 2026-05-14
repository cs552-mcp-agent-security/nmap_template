.PHONY: validate mock-service scan-local clean

validate:
	python3 -m py_compile mock/mock_service.py scripts/validate_target.py
	python3 scripts/validate_target.py 127.0.0.1
	bash -n scripts/run_scan.sh
	python3 tests/test_template.py

mock-service:
	python3 mock/mock_service.py

scan-local:
	./scripts/run_scan.sh 127.0.0.1 reports/nmap-local.xml

clean:
	rm -f reports/*.xml reports/*.txt
