import json
import pandas as pd

example_data = {
        'task_1': {
            'example_input_1': {
                'full_text': '\nBob saw an animal just like a horse. “That’s a\ndonkey,” said Alice.\n“Horses have got longer legs.” \n The donkey realy was quite short and said it definitely wasn\'t a horse. \n“Cool! I\'ve never seen a donkey before.” shouted Bob.'
            },
            'example_output_1': json.dumps(
                {
                    'speech_sections': [
                        {
                            "speaker": "Alice",
                            "recipient": "Bob",
                            "speech_text": 'That’s a\ndonkey,” said Alice.\n“Horses have got longer legs.”',
                            "speech_section_id": 0
                        },
                        {
                            "speaker": "Bob",
                            "recipient": "Alice",
                            "speech_text": '\n“Cool! I\'ve never seen a donkey before.” shouted Bob.',
                            "speech_section_id": 1
                        }
                    ]
                }
            ),
            'example_input_2': {
                'full_text': '"What a strange day!" Alice said to herself. \n"What do you think of that everyone? She is talking to herself!" asked Bob.'
            },
            'example_output_2': json.dumps(
                {
                    'speech_sections': [
                        {
                            "speaker": "Alice",
                            "recipient": "self",
                            "speech_text": '"What a strange day!" Alice said to herself.',
                            "speech_section_id": 0
                        },
                        {
                            "speaker": "Bob",
                            "recipient": "reader",
                            "speech_text": '\n"What do you think of that? She is talking to herself!"',
                            "speech_section_id": 1
                        }
                    ]
                }
            )
        },
        'task_2': {
            'example_input_1': json.dumps(
                {
                    'speech_sections': [
                        {
                            "speaker": "Alice",
                            "recipient": "Bob",
                            "speech_text": 'That’s a\ndonkey,” said Alice.\n“Horses have got longer legs.”',
                            "speech_section_id": 0
                        },
                        {
                            "speaker": "Bob",
                            "recipient": "Alice",
                            "speech_text": '\n“Cool! I\'ve never seen a donkey before.” shouted Bob.',
                            "speech_section_id": 1
                        },
                        {
                            "speaker": "Alice",
                            "recipient": "Bob",
                            "speech_text": '\n“You can\'t be serious Bob!”\nShe said he must have seen a donkey before.',
                            "speech_section_id": 2
                        },

                    ]
                }
            ),
            'example_output_1': json.dumps(
                {
                    'speech_sections': [
                        {
                            "spe                                                                                                                                                                                                                                                                                    aker": "Alice",
                            "recipient": "Bob",
                            "spoken_words_only": 'That’s a donkey. Horses have got longer legs.',
                            "speech_section_id": 0
                        },
                        {
                            "speaker": "Bob",
                            "recipient": "Alice",
                            "speech_text": 'Cool! I\'ve never seen a donkey before.',
                            "speech_section_id": 1
                        },
                        {
                            "speaker": "Alice",
                            "recipient": "Bob",
                            "speech_text": 'You can\'t be serious Bob!',
                            "speech_section_id": 2
                        },
                    ]
                }
            )
        },
        'task_3': {
            'example_input_1': json.dumps(
                {
                    'speech_sections': [
                        {
                            "speaker": "Alace",
                            "recipient": "Bobby",
                            "spoken_words_only": 'That’s a donkey. Horses have got longer legs.',
                            "speech_section_id": 0
                        },
                        {
                            "speaker": "Bob",
                            "recipient": "The Queen",
                            "speech_text": 'Cool! I\'ve never seen a donkey before.',
                            "speech_section_id": 1
                        },
                        {
                            "speaker": "Alice",
                            "recipient": "Robert",
                            "speech_text": 'You can\'t be serious Bob!',
                            "speech_section_id": 2
                        },
                        {
                            "speaker": "Bob",
                            "recipient": "everyone",
                            "speech_text": 'What do you think, everyone?',
                            "speech_section_id": 2
                        },
                    ]
                }
            ),
            'example_characters_1': ['Alice', 'Bob', 'Charlie'],
            'example_aliases_1': pd.DataFrame({
                'alias': ['The Queen', 'Bobby'],
                'character': ['Alice', 'Bob']
            }).to_csv(),
            'example_output_1': json.dumps(
                {
                    'speech_sections': [
                        {
                            "speaker": "Alace",
                            "recipient": "Bobby",
                            "speaker_matched": "Alice",
                            "recipient_matched": "Bob",
                            #                         "spoken_words_only": 'That’s a donkey. Horses have got longer legs.',
                            "speech_section_id": 0
                        },
                        {
                            "speaker": "Bob",
                            "recipient": "The Queen",
                            "speaker_matched": "Bob",
                            "recipient_matched": "Alice",
                            #                         "speech_text": 'Cool! I\'ve never seen a donkey before.',
                            "speech_section_id": 1
                        },
                        {
                            "speaker": "Alice",
                            "recipient": "Robert",
                            "speaker_matched": "Alice",
                            "recipient_matched": "Unknown",
                            #                         "speech_text": 'You can\'t be serious Bob!',
                            "speech_section_id": 2
                        },
                        {
                            "speaker": "Bob",
                            "recipient": "everyone",
                            "speaker_matched": "Bob",
                            "recipient_matched": "The Reader",
                            #                         "speech_text": 'What do you think, everyone?',
                            "speech_section_id": 2
                        },
                    ]
                }
            )
        }
    }