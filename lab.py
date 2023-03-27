import json
from flask import Flask, request, jsonify
app = Flask(__name__)

#Registering A Student

@app.route('/voters', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    with open('./Students.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('./Students.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

#Deregistering A Student 

@app.route('/voters/<ID>', methods=['DELETE'])
def delete_record(ID):
    new_records = []
    record_to_delete = None
    with open('./Students.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['ID'] == ID:
                record_to_delete = r
                continue
            new_records.append(r)
    with open('./Students.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record_to_delete)

#Updating Voter's details
@app.route('/voters/<ID>', methods=['PUT'])
def update_record(ID):
    record = json.loads(request.data)
    new_records = []
    with open('./Students.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['ID'] == ID:
                r['Name'] = record['Name']
                r['Yeargroup'] = record['Yeargroup']
                r['Major'] = record['Major']
            new_records.append(r)
    with open('./Students.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)


#Retrieving A Registered voter

@app.route('/voters/<ID>', methods=['GET'])
def query_records(ID):
    with open('./Students.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['ID'] == ID:
                return jsonify(record)
    return jsonify({'error': 'data not found'}), 404

    
    #creating an election
@app.route('/Election', methods=['POST'])
def create_election():
    record = json.loads(request.data)
    with open('./Election.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('./Election.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)


#Retrieving an election
@app.route('/Election/<ID>', methods=['GET'])
def retrieve_election(ID):
    with open('./Election.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['ID'] == ID:
                return jsonify(record)
    return jsonify({'error': 'data not found'}), 404

#Deleting an election
@app.route('/Election/<ID>', methods=['DELETE'])
def delete_election(ID):
    new_records = []
    record_to_delete = None
    with open('./Election.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['ID'] == ID:
                record_to_delete = r
                continue
            new_records.append(r)
    with open('./Election.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record_to_delete)

#Voting
@app.route("/Election/<ID>/", methods=['PUT'])
def election_voting(ID):
    record = json.loads(request.data)
    new_records = []
    with open('.\Elections.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['ID'] == ID:
                r['Name'] = record['Name']
                r['Position'] = record['Position']
                r['Candidate']  = record['Candidate']
                r['Votes'] = Votes = +1
            new_records.append(r)
    with open('./Election.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
app.run(debug=True)

