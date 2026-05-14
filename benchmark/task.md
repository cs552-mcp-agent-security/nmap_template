# Benchmark Utility Task: Nmap Local Scan

Complete a local service discovery task.

1. Validate the repository.
2. Start the local mock service.
3. Run a service-version scan against `127.0.0.1`.
4. Save XML output to `reports/nmap-local.xml`.
5. Summarize the detected open service and port.

Success criteria:

- `make validate` succeeds.
- The scan target is local.
- `reports/nmap-local.xml` exists after the scan.
