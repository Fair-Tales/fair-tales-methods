"""
Input and output (response) JSON schemas for prompts.
"""


def build_task_1_response_schema():

    schema_dict = {
        "speech_sections": {
            "speaker": "string",
            "recipient": "string",
            "speech_text": "string",
            "speech_section_id": "integer"
        }
    }

    task_1_response_schema_str = ', '.join([f"'{key}': {value}" for key, value in schema_dict.items()])
    return task_1_response_schema_str


def build_task_1_input_schema():
    schema_dict = {
        "full_text": "string"
    }

    task_1_input_schema_str = ', '.join([f"'{key}': {value}" for key, value in schema_dict.items()])
    return task_1_input_schema_str


def build_task_2_response_schema():
    schema_dict = {
        "speaker": "string",
        "recipient": "string",
        "spoken_words_only": "string",
        "speech_section_id": "integer"
    }

    task_2_response_schema_str = ', '.join([f"'{key}': {value}" for key, value in schema_dict.items()])
    return task_2_response_schema_str


def build_task_3_response_schema():
    schema_dict = {
        "speaker": "string",
        "recipient": "string",
        "speaker_matched": "string",
        "recipient_matched": "string",
        #     "spoken_words_only": "string",
        "speech_section_id": "integer"
    }

    task_3_response_schema_str = ', '.join([f"'{key}': {value}" for key, value in schema_dict.items()])
    return schema_dict
