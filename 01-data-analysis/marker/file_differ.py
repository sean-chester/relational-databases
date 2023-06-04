
import difflib

def compare_outputs(expected_output, actual_output):
    diffs = []
    if(len(actual_output) == 0):
        return len(expected_output)

    diffs = [line+'\n' for line in difflib.unified_diff(actual_output, expected_output, fromfile='YourOutput', tofile='ExpectedOutput', lineterm='', n=0)]
    diffs = [line for line in diffs if not line.startswith(('---', '+++', '@@'))]

    return diffs

if __name__ == '__main__':
    actual_result = ['name', 'glasscock county', 'union county']
    expected_result = ['name', 'glasscock county', 'midland county', 'shackelford county', 'union county']
    assert len(compare_outputs(expected_result, actual_result)) == 2
#    print(compare_outputs(expected_result, actual_result))
