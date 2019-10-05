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

parseDAXFile("montage.xml")