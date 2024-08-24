from .schemas import *
from .examples import example_data

def get_task_1_prompt_string(data):
    example_input_1 = example_data['task_1']['example_input_1']
    example_output_1 = example_data['task_1']['example_output_1']

    task_1_input_schema_str = build_task_1_input_schema()

    return f"""
        I will provide you below with the following data in JSON format: {task_1_input_schema_str}

        The full_text is text of a children's book as a single string. 

        Using the full_text, please identify any sections of direct speech, and for each one tell me who is the speaker and who is the recipient.
        Remember that a section of direct speech can be broken up by information about who is speaking and that this break could even span 
        multiple lines in some cases. In these cases, please treat this as a single section of speech.

        For example, the input: {example_input_1}
        Should produce the following output: {example_output_1}

        Use '\n' as the newline character and reproduce these as they occur.
        Reproduce all punctuation as it is written.    

        Provide the results in JSON format with the following fields: speaker, recipient, speech_text, speech_section_id
        (where speech_section_id counts the number of sections of speech in this book)

        Data: {data}
    """


def get_task_1_system_prompt():
    input_schema = build_task_1_input_schema()
    output_schema = build_task_1_response_schema()
    return f"""
            You are a data analysis assistant, capable of accurate and precise natural language processing. 
            You will recieve data in JSON format with the following schema: {input_schema}
            Output your response in JSON format using the following schema: {output_schema}.
            Please start all indexing of lists and arrays at 0 rather than 1.
        """


def get_task_2_prompt_string(task_1_response):
    example_input_1 = example_data['task_2']['example_input_1']
    example_output_1 = example_data['task_2']['example_output_1']

    return f"""
        Here are the speech sections that you just found: {task_1_response}. 

        Look at the speech_text fields.
        Extract only the words that are direct speech, omitting any words that are not actually spoken.
        Add these spoken words as a field in the JSON output called 'spoken_words_only'.
        Ensure that there is a one-to-one mapping between speech sections in the input and output. 

        For example, these speech sections: {example_input_1}
        Should produce the following output: {example_output_1}

        Remove all speech marks and add full stops where needed, otherwise produce all punctuation as it is written. Replace each newline character '\n' with a sinlge space.   
        Provide your response in JSON.
    """

def get_task_2_system_prompt():

    input_schema= build_task_1_response_schema()
    response_schema = build_task_2_response_schema()
    return f"""
        You are a data analysis assistant, capable of accurate and precise natural language processing. 
        You will recieve data in JSON format with the following schema: {input_schema}
        Use the following schema for your JSON response: {response_schema}.
        Please start all indexing of lists and arrays at 0 rather than 1.
    """


def get_task_3_prompt_string(task_2_response, characters, aliases, meta_characters):
    example_input_1 = example_data['task_3']['example_input_1']
    example_characters_1 = example_data['task_3']['example_characters_1']
    example_aliases_1 = example_data['task_3']['example_aliases_1']
    example_output_1 = example_data['task_3']['example_output_1']

    if not isinstance(characters, list):
        character_list = list(characters.name)
    else:
        character_list = characters
    if not isinstance(aliases, str):
        alias_csv = aliases[['alias', 'character']].to_csv()
    else:
        alias_csv = aliases

    character_list.append(meta_characters)
    return f"""
        Here are the speech sections that you just found: {task_2_response}. 

        Look at the speakers and recipients. I want you to match these to pre-defined character names,
        and to store the matched name as new fileds called speaker_matched and recipient_matched in the JSON ouput.

        Here is a list of character names: {character_list}
        If you find the speaker or recipient in this list (or a close enough match case-insensitive, including typos), 
        please use the found name as the match value.
        If there is no match in the list, look for the name in the 'alias' column of the following
        csv lookup table: {alias_csv}
        If you find the name in the 'alias' column, take the corresponding value from the 'character' column
        as the match.
        If you cannot find a name in either the characters or aliases, record the match value as 'Unknown'.
        If the recipient appears to be the reader or general audience, record the match value as 'The Reader'.
        If the speaker is talking to themself, record the match value as 'Self'.

        For example, these speech sections: {example_input_1}
        with this character list: {example_characters_1}
        and this alias lookup table: {example_aliases_1}
        Should produce the following output: {example_output_1}

        Provide your response in JSON.
        Do not change the value of the speaker, recipient fields. Do not include the spoken_words_only field.   
    """

def get_task_3_system_prompt():
    _task_3_input_schema = build_task_2_response_schema()
    _task_3_response_schema = build_task_3_response_schema()
    return f"""
        You are a data analysis assistant, capable of accurate and precise natural language processing. 
        You will recieve data in JSON format with the following schema: {_task_3_input_schema}
        Use the following schema for your JSON response: {_task_3_response_schema}.
        Please start all indexing of lists and arrays at 0 rather than 1.
    """