import requests
import csv
import json
import configuration


def upload_list(list_file):
    members = []
    with open('csvs/' + list_file + '.csv', mode='r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            members.append({
                "destination": row[0],
                "param1": row[1],
                "param2": row[2],
                "param3": row[3],
                "param4": row[4],
                "param5": row[5],
                "param6": row[6]
            })
        list_data = {
            "name": list_file,
            "members": members
        }

        list_id = requests.post(
            configuration.CM_lists,
            auth=(
                configuration.CM_user,
                configuration.CM_password),
            params={
                "name": configuration.CM_app
            },
            json=list_data
        )
        return json.loads(list_id.text)['id']


def get_lists():
    lists = requests.get(
        configuration.CM_lists,
        auth=(
            configuration.CM_user,
            configuration.CM_password),
        params={
            "name": configuration.CM_app
        }
    )
    return json.loads(lists.text)


def add_lists(managed_lists=configuration.CM_managed_lists):
    result = []
    for list_name in managed_lists:
        result.append(upload_list(list_name))
    return result


def delete_list(list_id):
    result = requests.delete(
        configuration.CM_lists + '/' + str(list_id),
        auth=(
            configuration.CM_user,
            configuration.CM_password),
        params={
            "name": configuration.CM_app
        }
    )
    return result


def replace_list_list(managed_lists=configuration.CM_managed_lists):
    all_lists = get_lists()
    to_delete = []
    for each_list in all_lists:
        if each_list['name'] in managed_lists:
            to_delete.append(each_list['id'])
    return to_delete


def process_lists(managed_lists=configuration.CM_managed_lists):
    to_delete = replace_list_list(managed_lists)
    add_lists(managed_lists)
    for each_list in to_delete:
        delete_list(each_list)
    return get_lists()


# print(process_lists())
