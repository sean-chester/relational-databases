
import subprocess as sp
import traceback

class MySQLRunner:
    def __init__(self, database = "counties", user = "root", timeout=25):
        self.database = database
        self.timeout = timeout
        self.user = user


    def run_query(self, query_file):
        try:
            with sp.Popen(['mysql', self.database, '-u', self.user], stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE) as process:
                output, errors = process.communicate(f"source {query_file}".encode(), self.timeout)
                if output:
                    output = [l.strip() for l in output.decode().strip().splitlines()]
                if errors:
                    errors = errors.decode().strip()
                return (output, errors)

        except Exception as err:
            trace_err = traceback.format_exc()
            return('', trace_err)

if __name__ == '__main__':
    sql_runner = MySQLRunner()
    print(sql_runner.run_query("../query01-solution.sql"))
