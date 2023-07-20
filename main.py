import subprocess
import sys
from kubernetes import client, config, watch

def handlePod(pod):
    print("///////////////////////////////////////////////////////////////")
    pod_name = pod.metadata.name
    pod_status = pod.status
    conditions = pod_status.conditions
    command = "mkdir ./tmp && touch ./tmp/ready" # change command to action to take



    if pod_status.phase == "Running" and any(
            condition.type == "Ready" and condition.status != "True" for condition in conditions):
            print(pod_name)
            exec_command = f"kubectl exec {pod_name} -- mkdir ./test" # can replace this line with code below
            # exec_command = f"kubectl exec {pod_name} -- {command}"
            subprocess.run(exec_command, shell=True, stdout=sys.stdout, stderr=sys.stderr)


def podWatcher():
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    watcher = watch.Watch()
    for event in watcher.stream(v1.list_namespaced_pod, "default"):
        handlePod(event["object"])


if __name__ == '__main__':
    podWatcher()