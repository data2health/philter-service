import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server import util

from philter_ucsf.philter import Philter
import nltk
nltk.download('averaged_perceptron_tagger')

import uuid
import os
import shutil


def deid(body):  # noqa: E501
    """Add a new pet to the store

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    note = body.decode("utf-8")
    print(note)

    note_uuid = str(uuid.uuid1())
    raw_note_filename = "data/tmp/" + note_uuid + "/raw_note.txt"
    deid_note_filename = raw_note_filename

    # Save received note to note_filename_in
    os.makedirs(os.path.dirname(raw_note_filename), exist_ok=True)
    with open(raw_note_filename, "w") as in_file:
        in_file.write(note)

    philter_config = {
        "verbose": True,
        "run_eval": False,
        "finpath": "data/tmp/" + note_uuid + "/",
        "foutpath": "data/tmp/" + note_uuid + "/",
        "outformat": "asterisk",
        "filters": "configs/philter_delta.json",
        "cachepos": None
    }

    filterer = Philter(philter_config)

    #map any sets, pos and regex groups we have in our config
    filterer.map_coordinates()

    #transform the data
    #Priority order is maintained in the pattern list
    filterer.transform()

    # Read the de-id note
    deid_note = ""
    with open(deid_note_filename, "r") as out_file:
        deid_note = out_file.read()

    shutil.rmtree("data/tmp/" + note_uuid)

    return deid_note

    # if connexion.request.is_json:
    #     body = Pet.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic2!'


def delete_pet(petId, api_key=None):  # noqa: E501
    """Deletes a pet

     # noqa: E501

    :param petId: Pet id to delete
    :type petId: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def find_pets_by_status(status):  # noqa: E501
    """Finds Pets by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: List[Pet]
    """
    return 'do some magic!'


def find_pets_by_tags(tags):  # noqa: E501
    """Finds Pets by tags

    Muliple tags can be provided with comma separated strings. Use         tag1, tag2, tag3 for testing. # noqa: E501

    :param tags: Tags to filter by
    :type tags: List[str]

    :rtype: List[Pet]
    """
    return 'do some magic!'


def get_pet_by_id(petId):  # noqa: E501
    """Find pet by ID

    Returns a single pet # noqa: E501

    :param petId: ID of pet to return
    :type petId: int

    :rtype: Pet
    """
    return 'do some magic!'


def update_pet(body):  # noqa: E501
    """Update an existing pet

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_pet_with_form(petId, name=None, status=None):  # noqa: E501
    """Updates a pet in the store with form data

     # noqa: E501

    :param petId: ID of pet that needs to be updated
    :type petId: int
    :param name: Updated name of the pet
    :type name: str
    :param status: Updated status of the pet
    :type status: str

    :rtype: None
    """
    return 'do some magic!'


def upload_file(petId, additionalMetadata=None, file=None):  # noqa: E501
    """uploads an image

     # noqa: E501

    :param petId: ID of pet to update
    :type petId: int
    :param additionalMetadata: Additional data to pass to server
    :type additionalMetadata: str
    :param file: file to upload
    :type file: werkzeug.datastructures.FileStorage

    :rtype: ApiResponse
    """
    return 'do some magic!'
