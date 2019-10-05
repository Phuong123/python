import json

ROOT_NODE_ID = "IDR"
EXIT_NODE_ID = "EDR"
FEEDFORWARD_ORDER = {"IDR": 1,
                     "mProject": 2,
                     "mDiffFit": 3,
                     "mConcatFit": 4,
                     "mBgModel": 5,
                     "mBackground": 6,
                     "mImgtbl": 7,
                     "mAdd": 8,
                     "mJPEG": 9,
                     "EDR": 10}

S3_BUCKET_PREFIX = ""
LAMBDA_ANS_ADDRESS = ""

P_CLUSTER_STATE_NAME = "parallelCluster"
P_CLUSTER_WAIT_STATE_NAME = "waitParallelCluster"
PARAMETER_PREFIX = "para"

# XML Parser
import xml.etree.ElementTree as ET
from pprint import pprint

DAX_PEGASUS_PREFIX = "{http://pegasus.isi.edu/schema/DAX}"
JOB_ID = "job"
STRUCTURE_ID = "child"
ARGUMENT_ID = "argument"
FILE_USAGE_ID = "uses"


def getElementList(root, elementAttrib):
    l = []
    for k in root:
        if (k.tag == elementAttrib):
            l.append(k)
    return l


def extract_argument_list(arg):
    argument_list = []
    argument_list.append(arg.text)
    for argument in arg:
        argument_list.append(argument.attrib.get('name'))
    return argument_list


def extract_argument_list_mjpeg(arg):
    argument_list_files = []
    for argument in arg:
        argument_list_files.append(argument.attrib.get('name'))
    argument_list_mods = []
    for k in arg.itertext():
        argument_list_mods.append(k)
    combine_arg = []
    for i in range(0,len(argument_list_files)):
        combine_arg.append(argument_list_mods[i])
        combine_arg.append(argument_list_files[i])
    pprint(combine_arg)
    return combine_arg

def extract_arguments(raw_job):
    usage_list_input = []
    usage_list_output = []
    for arg in raw_job:  # type: ET.Element
        if (arg.tag == DAX_PEGASUS_PREFIX + ARGUMENT_ID):
            if(raw_job.get('name') == 'mJPEG'):
                arg_list = extract_argument_list_mjpeg(arg)
            else:
                arg_list = extract_argument_list(arg)
        if (len(arg.attrib) != 0):
            file_name = arg.attrib.get('name')
            if (arg.attrib.get('link') == 'input'):
                usage_list_input.append(file_name)
            else:
                usage_list_output.append(file_name)
    return arg_list, usage_list_input, usage_list_output


def create_job_dict(id, prog, ordered_argument_list, usage_list_in, usage_list_out):
    job_dict = {}
    job_dict['id'] = id
    job_dict['name'] = prog
    job_dict['arg_list'] = ordered_argument_list
    job_dict['in_files'] = usage_list_in
    job_dict['out_files'] = usage_list_out
    return job_dict


def transformRawJobListToJobDict(raw_job_list):
    job_list = []
    for raw_job in raw_job_list:  # type: ET.Element
        ordered_argument_list, usage_list_in, usage_list_out = extract_arguments(raw_job)
        job_list.append(create_job_dict(raw_job.get('id'),
                                        raw_job.get('name'),
                                        ordered_argument_list,
                                        usage_list_in,
                                        usage_list_out))

    return job_list


def extract_parents(raw_struct):
    parent_list = []
    for entry in raw_struct:
        parent_list.append(entry.attrib.get('ref'))
    return parent_list


def create_struct_dict(child_id, parent_list):
    struct_dict = {}
    struct_dict['child_id'] = child_id
    struct_dict['parent_list'] = parent_list
    return struct_dict


def transformRawStructureListToStructureDict(raw_structure_list):
    structure_list = []
    for raw_struct in raw_structure_list:
        parent_list = extract_parents(raw_struct)
        structure_list.append(create_struct_dict(raw_struct.attrib.get('ref'), parent_list))
    return structure_list


def parseDAXFile(filepath):
    e = ET.parse(filepath)
    root = e.getroot()
    raw_job_list = getElementList(root, DAX_PEGASUS_PREFIX + JOB_ID)
    raw_structure_list = getElementList(root, DAX_PEGASUS_PREFIX + STRUCTURE_ID)
    job_list = transformRawJobListToJobDict(raw_job_list)
    structure_list = transformRawStructureListToStructureDict(raw_structure_list)
    pprint(job_list)
    pprint(structure_list)
    return job_list, structure_list


########################### dag to ASL-json #########################


#mImgTbl == mImgtbl ?????
def isInFeedforwardOrder(dag, id, current_id):
    pos_down = FEEDFORWARD_ORDER[dag[id]['name']]
    pos_up = FEEDFORWARD_ORDER[dag[current_id]['name']]
    if ((pos_down - pos_up) == 1):
        return True
    return False


# extremly inefficent too lazy to change now
def lookup_job(job_list, param):
    for j in job_list:
        if (j['id'] == param):
            return j


def add_job_to_dag(job, dag):
    id = job['id']
    dag[id] = job


def add_root_to_dag(dag):
    no_prev_nodes_id = []
    for id in dag:
        if (len(dag[id]['prev_list']) == 0):
            no_prev_nodes_id.append(id)
            (dag[id]['prev_list']).append(ROOT_NODE_ID)
    root_node = {}
    root_node['id'] = ROOT_NODE_ID
    root_node['name'] = ROOT_NODE_ID
    root_node['next_list'] = no_prev_nodes_id
    root_node['prev_list'] = []
    dag[ROOT_NODE_ID] = root_node


def add_exit_to_dag(dag):
    no_next_nodes_id = []
    for id in dag:
        if (len(dag[id]['next_list']) == 0):
            no_next_nodes_id.append(id)
            (dag[id]['next_list']).append(EXIT_NODE_ID)
    exit_node = {}
    exit_node['id'] = EXIT_NODE_ID
    exit_node['name'] = EXIT_NODE_ID
    exit_node['prev_list'] = no_next_nodes_id
    exit_node['next_list'] = []
    dag[EXIT_NODE_ID] = exit_node


def recursive_level_builder(level_dict, level, dag, current_node_id):
    if (level not in level_dict):
        level_dict[level] = []
    if (current_node_id not in level_dict[level]):
        (level_dict[level]).append(current_node_id)
    next_list_l = dag[current_node_id]['next_list']
    for i in next_list_l:
        if (isInFeedforwardOrder(dag, i, current_node_id)):
            recursive_level_builder(level_dict, level + 1, dag, i)


def convert_dag_to_level_dict(dag):
    level_dict = {}
    level = 0
    recursive_level_builder(level_dict, level, dag, ROOT_NODE_ID)
    return level_dict


def set_up_state_machine():
    state_machine = {
        "Comment": "Test",
        "StartAt": ROOT_NODE_ID,
        "States": {
        }
    }
    return state_machine


def setup_start(state_machine, cluster_count):
    start_state = {
        "Type": "Pass",
        "Next": P_CLUSTER_STATE_NAME+str(cluster_count)
    }
    state_machine['States'][ROOT_NODE_ID] = start_state


def parallel_branch_insertion(state_machine, cluster_count):
    parallel_branch_state = {
        "Type": "Parallel",
        "Branches": [],
        "Next":  P_CLUSTER_WAIT_STATE_NAME+str(cluster_count)
    }
    state_machine['States'][P_CLUSTER_STATE_NAME+str(cluster_count)] = parallel_branch_state


def prepare_download_upload_list(list):
    down_up = []
    for i in list:
        down_up.append(i)
    return down_up

def insert_job_into_parallel_state(job_info, state_machine, cluster_count):
    job_state = {
        "StartAt": job_info['id'],
        "States": {
            job_info['id']: {
                "Type": "Task",
                "Resource": LAMBDA_ANS_ADDRESS,
                "Parameters":{
                },
                "End": True
            }
        }
    }
    # (job_state['States'][job_info['id']])
    job_state['States'][job_info['id']]['Parameters']['ordered_arg_list'] = job_info['arg_list']
    job_state['States'][job_info['id']]['Parameters']['progName_path'] = job_info['name']
    # I added a separate bucket parameter so we can join strings later if we need to
    job_state['States'][job_info['id']]['Parameters']['bucket_name'] = S3_BUCKET_PREFIX
    job_state['States'][job_info['id']]['Parameters']['progName'] = job_info['name']
    download_list = prepare_download_upload_list(job_info['in_files'])
    upload_list = prepare_download_upload_list(job_info['out_files'])
    job_state['States'][job_info['id']]['Parameters']['download_list'] = download_list
    job_state['States'][job_info['id']]['Parameters']['upload_list'] = upload_list
    state_machine['States'][P_CLUSTER_STATE_NAME+str(cluster_count)]['Branches'].append(job_state)


def setup_parallel_level_execution(state_machine, dag, job_list, cluster_count):
    parallel_branch_insertion(state_machine, cluster_count)
    for job in job_list:
        job_info = dag[job]
        insert_job_into_parallel_state(job_info, state_machine, cluster_count)


def setup_wait_state(state_machine, cluster_count):
    parallel_branch_state = {
        "Type": "Pass",
        "Next": P_CLUSTER_STATE_NAME + str(cluster_count+1)
    }
    state_machine['States'][P_CLUSTER_WAIT_STATE_NAME + str(cluster_count)] = parallel_branch_state


def setup_end(state_machine, cluster_count):
    end_state = {
        "Type": "Pass",
        "End": True
    }
    state_machine['States'][EXIT_NODE_ID] = end_state
    #reset previous wait state
    state_machine['States'][P_CLUSTER_WAIT_STATE_NAME+str(cluster_count-1)]['Next'] = EXIT_NODE_ID


def convert_level_dict_to_step_function(level_dict, dag):
    state_machine = set_up_state_machine()
    cluster_count = 0
    for level in level_dict:
        if (ROOT_NODE_ID in level_dict[level]):
            setup_start(state_machine, cluster_count)
            continue
        if (EXIT_NODE_ID in level_dict[level]):
            setup_end(state_machine, cluster_count)
            continue
        setup_parallel_level_execution(state_machine, dag, level_dict[level], cluster_count)
        setup_wait_state(state_machine, cluster_count)
        cluster_count += 1
    return state_machine


def dump_to_json(step_function, filepath):
    with open(filepath, 'w') as fp:
        json.dump(step_function, fp, indent=4)


def add_struct_info_to_job(j, structure_list):
    j['prev_list'] = []
    j['next_list'] = []
    for s in structure_list:
        if (s['child_id'] == j['id']):
            (j['prev_list']).extend(s['parent_list'])
        if (j['id'] in s['parent_list']):
            (j['next_list']).append(s['child_id'])


def dag_to_step_function(dag_filepath, json_filepath, s3_bucket_prefix, ans_lambda_address):
    job_list, structure_list = parseDAXFile(dag_filepath)
    global LAMBDA_ANS_ADDRESS, S3_BUCKET_PREFIX
    LAMBDA_ANS_ADDRESS = ans_lambda_address
    S3_BUCKET_PREFIX = s3_bucket_prefix
    dag = {}
    for j in job_list:
        add_struct_info_to_job(j, structure_list)
        add_job_to_dag(j, dag)
    add_root_to_dag(dag)
    add_exit_to_dag(dag)
    level_dict = convert_dag_to_level_dict(dag)
    step_function = convert_level_dict_to_step_function(level_dict, dag)
    # pprint(step_function)
    dump_to_json(step_function, json_filepath)