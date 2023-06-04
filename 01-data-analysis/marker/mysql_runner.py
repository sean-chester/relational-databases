
import subprocess as sp

class MySQLRunner:
    def __init__(self, database = "counties", user = "root", timeout=25):
        self.database = database
        self.timeout = timeout
        self.user = user


    def run_query(self, query_file):
        try:
            with sp.Popen(['mysql', self.database, '-u', self.user], stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE) as process:
                output, errors = process.communicate(f"source {query_file}".encode(), self.timeout)
                output = [l.strip() for l in output.decode().strip().splitlines()]
                errors = errors.decode().strip()
                return (output, errors)

        except Exception as err:
            trace_err = traceback.format_exc()
            trace_err = trace_err.replace(folder, '')
            print(trace_err)

if __name__ == '__main__':
    sql_runner = MySQLRunner()
    print(sql_runner.run_query("../query01-solution.sql"))
