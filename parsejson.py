from bottle import route, run
import json
import re

json_string = """
{
    "jobs": {
        "Build base AMI": {
            "Builds": [{
                "runtime_seconds": "1931",
                "build_date": "1506741166",
                "result": "SUCCESS",
                "output": "base-ami us-west-2 ami-9f0ae4e5 d1541c88258ccb3ee565fa1d2322e04cdc5a1fda"
            }, {
                "runtime_seconds": "1825",
                "build_date": "1506740166",
                "result": "SUCCESS",
                "output": "base-ami us-west-2 ami-d3b92a92 3dd2e093fc75f0e903a4fd25240c89dd17c75d66"
            }, {
                "runtime_seconds": "126",
                "build_date": "1506240166",
                "result": "FAILURE",
                "output": "base-ami us-west-2 ami-38a2b9c1 936c7725e69855f3c259c117173782f8c1e42d9a"
            }, {
                "runtime_seconds": "1842",
                "build_date": "1506240566",
                "result": "SUCCESS",
                "output": "base-ami us-west-2 ami-91a42ed5 936c7725e69855f3c259c117173782f8c1e42d9a"
            }, {
                "runtime_seconds": "5",
                "build_date": "1506250561",
            }, {
                "runtime_seconds": "215",
                "build_date": "1506250826",
                "result": "FAILURE",
                "output": "base-ami us-west-2 ami-34a42e15 936c7725e69855f3c259c117173782f8c1e42d9a"
            }]
        }
    }
}
"""
output = """
{
    "latest": {
        "build_date": "xxxxxxx",
        "ami_id": "ami-xxxxxx",
        "commit_hash": "xxxxxxxxxxxx"
    }
}
"""

@route('/build')
def hello():
    pattern = re.compile(r'\,(?!\s*?[\{\[\"\'\w])')
    json_string_fixed = pattern.sub("", json_string)
    data = json.loads(json_string_fixed) 
    jobs =data["jobs"]["Build base AMI"]["Builds"]
    jobs.sort(key=time_check, reverse=True)

    output_json = json.loads(output) 
    output_json["latest"]["build_date"] = jobs[0]["build_date"]
    output_json["latest"]["ami_id"] = jobs[0]["output"].split()[2]
    output_json["latest"]["commit_hash"] = jobs[0]["output"].split()[3]
    return output_json

def time_check(payload):
    try:
        return int(payload['build_date'])
    except KeyError:
        return 0



  
run(host='0.0.0.0', port=8080, debug=True)
