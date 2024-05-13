import requests, json, time


HUB_ID = 25444850 
Extenstion_Name = ''
file_url = input_data.get('FILE')
deal_id = input_data.get('deal_id')
file_url_list = str(file_url).split(',')


def upload_file(file_name, file_url):
    file_id = ""
    url = f"https://api.hubapi.com/files/v3/files/import-from-url/async"
    headers = {'content-type': 'application/json','authorization': f"Bearer {auth_key}"}
    data = {
        "folderPath": "/",
        "access": "PUBLIC_INDEXABLE",
        "name": file_name,
        "url": file_url
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    # print(response.text)
    task_id = json.loads(response.text)['id']

    # ping until the upload is completed, then return the file ID
    while True:
        time.sleep(2)
        url = f"https://api.hubapi.com/files/v3/files/import-from-url/async/tasks/{task_id}/status"
        response = requests.get(url, headers=headers)
        print(response.status_code)
        response_json = json.loads(response.text)
        if response_json['status'] == "COMPLETE":
            file_id = response_json['result']['id']
            break
    return file_id


def associate_file_deal(fileId, dealId):
    # associate the file to a note & associate the note to a deal
    url = f"https://api.hubapi.com/crm/v3/objects/notes"
    headers = {'content-type': "application/json",'authorization': f"Bearer {auth_key}"}
    data = {
        "associations": [{
            "types": [{
                "associationCategory": "HUBSPOT_DEFINED",
                "associationTypeId": 214
            }],
            "to": {
                "id": dealId
            }
        }],
        "properties": {
            "hs_note_body": "",
            "hs_timestamp": int(time.time())*1000,  # current time in ms
            "hs_attachment_ids": fileId
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)


for count,url in enumerate(file_url_list,start=1):
    if url:
        if str(url).split('.')[-1]:
            Extenstion_Name = str(url).split('.')[-1]
        file_name = f"file{count}.{Extenstion_Name}"
        file_id = upload_file(file_name, url)
        rec = associate_file_deal(file_id, deal_id)
        output = {"rec":rec}